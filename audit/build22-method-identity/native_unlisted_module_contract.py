#!/usr/bin/env python3
"""Check that unlisted acr.* text cannot claim a released method identity.

Uses a disposable copy of the selected method folder and a temporary register.
Evidence mode reports existing behavior. --expect-fixed fails on any identity leak.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile


def command(binary, root, *args):
    env = dict(os.environ, PCPOS_ROOT=str(root), PCPOS_REGISTER='.pcp/register.jsonl')
    return subprocess.run([str(binary), *map(str, args)], cwd=root, env=env,
                          capture_output=True, text=True, timeout=15)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--pcpos', type=Path, required=True)
    parser.add_argument('--method', type=Path, required=True)
    parser.add_argument('--expect-fixed', action='store_true')
    parser.add_argument('--json', type=Path)
    args = parser.parse_args()
    binary, method = args.pcpos.resolve(), args.method.resolve()
    if not binary.is_file() or not (method / 'MANIFEST.json').is_file():
        parser.error('select the intended native host and pinned method folder')
    fingerprint = hashlib.sha256((method / 'MANIFEST.json').read_bytes()).hexdigest()
    with tempfile.TemporaryDirectory(prefix='pcpos-method-identity-') as temp:
        root = Path(temp)
        copy = root / 'method'
        shutil.copytree(method, copy)
        intact = command(binary, root, 'method', copy)
        expected_modules = command(binary, root, 'modules', copy)
        extra = copy / 'MODULES/08_Synthetic/SOURCE/Specification.md'
        extra.parent.mkdir(parents=True)
        extra.write_text('**Component:** `acr.synthetic`, Version 1.0\n\n## 1. Scope\n\nUNLISTED TEST ONLY\n')
        altered = command(binary, root, 'method', copy)
        modules = command(binary, root, 'modules', copy)
        clause = command(binary, root, 'clause', copy, 'synthetic', '1')
        register = root / '.pcp/register.jsonl'
        register.parent.mkdir()
        begin = command(binary, root, 'init', register, '--principal', 'principal')
        select = command(binary, root, 'workspace', register, '--by', 'principal',
                         '--method', copy, 'synthetic')
        verify = command(binary, root, 'verify', register)
        module_rows = [x for x in modules.stdout.splitlines() if 'acr.synthetic' in x]
        recorded = '"id":"acr.synthetic"' in register.read_text()
        status_unchanged = (intact.returncode == altered.returncode == 0 and
                            intact.stdout == altered.stdout)
        result = {
            'unmodified_method_ok': intact.returncode == 0,
            'unmodified_absent': 'acr.synthetic' not in expected_modules.stdout,
            'unlisted_file_sha256': hashlib.sha256(extra.read_bytes()).hexdigest(),
            'method_report_unchanged': status_unchanged,
            'unlisted_classified_specialist': any('SPECIALIST' in x for x in module_rows),
            'unlisted_clause_served': clause.returncode == 0 and 'UNLISTED TEST ONLY' in clause.stdout,
            'unlisted_workspace_selected': select.returncode == 0 and recorded,
            'record_chain_verified': verify.returncode == 0,
            'manifest_fingerprint_unchanged': hashlib.sha256((copy / 'MANIFEST.json').read_bytes()).hexdigest() == fingerprint,
        }
    leaks = [k for k in ('method_report_unchanged', 'unlisted_classified_specialist',
                         'unlisted_clause_served', 'unlisted_workspace_selected') if result[k]]
    result['pass_control'] = bool(result['unmodified_method_ok'] and result['unmodified_absent'] and
                                  result['manifest_fingerprint_unchanged'] and not leaks)
    report = {'binary_sha256': hashlib.sha256(binary.read_bytes()).hexdigest(),
              'release_manifest_fingerprint': fingerprint, 'checks': result}
    if args.json:
        args.json.write_text(json.dumps(report, indent=2) + '\n')
    for key, value in result.items():
        print(f'{key}: {value}')
    if args.expect_fixed and not result['pass_control']:
        print('REGRESSION_FAIL:', ', '.join(leaks))
        return 1
    print('REGRESSION_PASS' if result['pass_control'] else 'EVIDENCE_ONLY')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
