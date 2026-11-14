#!/usr/bin/env python3
"""Build-22 native module removal contract. Only disposable synthetic files.

--expect-fixed returns 1 if an invariant fails. Default mode records the
baseline failure without treating the experiment itself as a failed run.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import tempfile


def command(binary, root, *args):
    env = dict(os.environ, PCPOS_ROOT=str(root), PCPOS_REGISTER='.pcp/register.jsonl')
    return subprocess.run([str(binary), *map(str, args)], cwd=root, env=env,
                          capture_output=True, text=True, timeout=15)


def setup(binary, parent, name):
    root = parent / name
    root.mkdir()
    reg = root / '.pcp/register.jsonl'
    reg.parent.mkdir()
    assert command(binary, root, 'init', reg, '--principal', 'principal').returncode == 0
    return root, reg


def removals(reg):
    return [json.loads(line) for line in reg.read_text().splitlines()
            if json.loads(line).get('body', {}).get('event') == 'MODULE_REMOVED']


def test_nonmodule(binary, parent, kind):
    root, reg = setup(binary, parent, kind)
    folder = reg.parent / 'modules' / kind
    folder.mkdir(parents=True)
    note = folder / 'synthetic-note.txt'
    note.write_bytes(b'NOT A PCP MODULE\n')
    if kind == 'malformed':
        spec = folder / 'SOURCE/Specification.md'
        spec.parent.mkdir()
        spec.write_text('invalid module header\n')
    before = reg.read_bytes()
    result = command(binary, root, 'module', 'remove', reg, kind, '--by', 'principal')
    preserved = note.is_file() and note.read_bytes() == b'NOT A PCP MODULE\n'
    stable = reg.read_bytes() == before
    valid = command(binary, root, 'verify', reg).returncode == 0
    accurate = not removals(reg)
    return {'pass': bool(result.returncode and preserved and stable and valid and accurate),
            'remove_exit': result.returncode, 'note_preserved': preserved,
            'register_unchanged': stable, 'chain_valid': valid, 'no_fictitious_event': accurate}


def test_normal(binary, method, parent):
    root, reg = setup(binary, parent, 'normal')
    src = root / 'source'
    src.mkdir()
    (src / 'Specification.md').write_text('**Component:** `local.normal`, Version 1.0\n\n## 1. Scope\n\nSynthetic.\n')
    add = command(binary, root, 'module', 'add', reg, src, '--by', 'principal', '--method', method)
    installed = (reg.parent / 'modules/normal/SOURCE/Specification.md').is_file()
    remove = command(binary, root, 'module', 'remove', reg, 'normal', '--by', 'principal')
    valid = command(binary, root, 'verify', reg).returncode == 0
    return {'pass': bool(add.returncode == 0 and installed and remove.returncode == 0
                         and not (reg.parent / 'modules/normal').exists() and valid and len(removals(reg)) == 1),
            'add_exit': add.returncode, 'remove_exit': remove.returncode, 'chain_valid': valid}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--pcpos', type=Path, required=True)
    p.add_argument('--method', type=Path, required=True)
    p.add_argument('--expect-fixed', action='store_true')
    p.add_argument('--json', type=Path)
    a = p.parse_args()
    binary, method = a.pcpos.resolve(), a.method.resolve()
    if not binary.is_file() or not (method / 'KERNEL.md').is_file():
        p.error('need a native host executable and a method directory')
    with tempfile.TemporaryDirectory(prefix='pcpos-nonmodule-contract-') as t:
        parent = Path(t)
        cases = {'normal': test_normal(binary, method, parent),
                 'unrelated': test_nonmodule(binary, parent, 'unrelated'),
                 'malformed': test_nonmodule(binary, parent, 'malformed')}
    data = {'binary_sha256': hashlib.sha256(binary.read_bytes()).hexdigest(), 'cases': cases}
    if a.json:
        a.json.write_text(json.dumps(data, indent=2) + '\n')
    for name, value in cases.items():
        print(name + ': ' + ('PASS' if value['pass'] else 'FAIL'))
    errors = [name for name, value in cases.items() if not value['pass']]
    if a.expect_fixed and errors:
        print('REGRESSION_FAIL:', ', '.join(errors))
        return 1
    print('EVIDENCE_ONLY' if errors else 'REGRESSION_PASS')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
