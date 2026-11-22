#!/usr/bin/env python3
"""Build-22 PCP OS native host: exact module identity and no unintended removal.

Only synthetic module data under automatically deleted temporary directories.
This is a negative control and regression contract, not a source patch.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import tempfile


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(binary, *args):
    env = {k:v for k,v in os.environ.items() if not k.startswith('PCPOS_') and not k.startswith('CLAUDE_PLUGIN_OPTION_')}
    completed = subprocess.run([str(binary), *(str(x) for x in args)], text=True,
                               capture_output=True, timeout=20, env=env)
    return {'exit': completed.returncode,
            'stdout': completed.stdout.strip()[:500],
            'stderr': completed.stderr.strip()[:500]}


def prepare(binary, root, names, method):
    workspace = root / 'workspace'
    (workspace / '.pcp').mkdir(parents=True)
    register = workspace / '.pcp/register.jsonl'
    init = run(binary, 'init', register, '--principal', 'principal')
    if init['exit']:
        raise RuntimeError('register init failed: ' + repr(init))
    sources = {}
    for name in names:
        incoming = root / ('source_' + name)
        incoming.mkdir()
        content = (f'**Component:** `local.{name}`, Version 1.0\n\n'
                   f'## 1. Synthetic {name}\n\nControlled test data.\n')
        (incoming / 'Specification.md').write_text(content, encoding='utf8')
        added = run(binary, 'module', 'add', register, incoming,
                    '--by', 'principal', '--method', method)
        if added['exit']:
            raise RuntimeError('valid module add failed: ' + repr(added))
        sources[name] = (incoming / 'Specification.md').read_bytes()
    return register, sources


def removals(reg):
    return [line['body']['module'] for line in (json.loads(row) for row in reg.read_text().splitlines())
            if line.get('body', {}).get('event') == 'MODULE_REMOVED']


def one_case(binary, method, base, case, modules, requested, intended, should_refuse=False):
    root = base / case
    root.mkdir()
    register, original = prepare(binary, root, modules, method)
    before = register.read_bytes()
    response = run(binary, 'module', 'remove', register, requested,
                   '--by', 'principal', '--method', method)
    moddir = register.parent / 'modules'
    existing = {name: (moddir / name / 'SOURCE/Specification.md').read_bytes()
                for name in modules if (moddir / name / 'SOURCE/Specification.md').is_file()}
    published = removals(register)
    verified = run(binary, 'verify', register)['exit'] == 0
    if should_refuse:
        correct = response['exit'] != 0 and existing == original and register.read_bytes() == before and not published
    else:
        correct = (response['exit'] == 0 and intended not in existing
                   and existing == {name: data for name, data in original.items() if name != intended}
                   and len(published) == 1 and published[0].get('id') == f'local.{intended}')
    return {'pass_control': bool(correct and verified),
            'request': requested, 'expected_removed': None if should_refuse else intended,
            'response_exit': response['exit'], 'modules_remaining': sorted(existing),
            'recorded_removed_ids': [item.get('id') for item in published],
            'register_verified': verified,
            'record_unchanged': register.read_bytes() == before}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--pcpos', type=Path, required=True)
    ap.add_argument('--method', type=Path, required=True)
    ap.add_argument('--json', type=Path)
    ap.add_argument('--expect-fixed', action='store_true')
    args = ap.parse_args()
    binary, method = args.pcpos.resolve(), args.method.resolve()
    if not binary.is_file() or not (method / 'MANIFEST.json').is_file():
        ap.error('provide the actual binary and a method folder containing MANIFEST.json')
    report = {'host_sha256': sha(binary), 'method_manifest_sha256': sha(method / 'MANIFEST.json'),
              'scope': 'hosted native Linux PCP OS program; temporary modules only', 'cases': {}}
    cases = [
        ('normal', ['plain'], 'plain', 'plain', False),
        ('hyphen_underscore', ['alpha-beta', 'alpha_beta'], 'alpha-beta', 'alpha-beta', False),
        ('uppercase', ['Upper'], 'Upper', 'Upper', False),
        ('mixed_case_collision', ['Alpha', 'alpha'], 'Alpha', 'Alpha', False),
        ('literal_local_prefix', ['Mixed'], 'local.Mixed', 'Mixed', False),
        ('reserved_acr_prefix', ['marker'], 'acr.marker', None, True),
    ]
    with tempfile.TemporaryDirectory(prefix='pcp-native-identity-regression-') as temp:
        for key, names, request, intended, refuse in cases:
            report['cases'][key] = one_case(binary, method, Path(temp), key, names, request, intended, refuse)
            print(f'{key}: {"PASS" if report["cases"][key]["pass_control"] else "FAIL"}', flush=True)
    report['all_passed'] = all(c['pass_control'] for c in report['cases'].values())
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(json.dumps(report, indent=2, sort_keys=True) + '\n', encoding='utf8')
    print('RESULT', 'ALL_PASS' if report['all_passed'] else 'REGRESSION_RED',
          sum(x['pass_control'] for x in report['cases'].values()), '/', len(report['cases']))
    return 1 if args.expect_fixed and not report['all_passed'] else 0


if __name__ == '__main__':
    raise SystemExit(main())
