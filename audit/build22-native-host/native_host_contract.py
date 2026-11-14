#!/usr/bin/env python3
"""Reproduce build-22 native PCP OS filesystem defects, entirely in temporary roots.

Run with --expect-fixed to turn unexpected red controls into an exit-1 regression
result. A collision-free race trial is evidence for that one trial, not proof of
race-freedom. No network access, kernel boot, or Rust compiler is needed.
"""
import argparse
import concurrent.futures
import hashlib
import json
import os
from pathlib import Path
import signal
import subprocess
import tempfile


def digest(data):
    return hashlib.sha256(data).hexdigest()


def run(bin_path, *args, root=None, input_text=None, preexec_fn=None):
    env = dict(os.environ)
    if root is not None:
        env.update(PCPOS_ROOT=str(root), PCPOS_REGISTER='.pcp/register.jsonl')
    p = subprocess.run([str(bin_path), *map(str, args)], cwd=root, env=env,
                       input=input_text, text=True, capture_output=True,
                       preexec_fn=preexec_fn, timeout=20)
    return dict(exit=p.returncode, stdout=p.stdout, stderr=p.stderr)


def initialize(binary, root):
    root.mkdir()
    reg = root / '.pcp/register.jsonl'
    reg.parent.mkdir()
    out = run(binary, 'init', reg, '--principal', 'principal')
    if out['exit']:
        raise RuntimeError('fresh register init failed: ' + repr(out))
    return reg


def source(root, name, tag):
    path = root / ('input_' + str(tag))
    path.mkdir()
    (path / 'Specification.md').write_text(
        '**Component:** \x60local.%s\x60, Version 1.0\n\n## 1. Purpose\n\nSynthetic %s\n' % (name, tag), encoding='utf-8')
    return path


def additions(reg):
    return [e for e in map(json.loads, reg.read_text().splitlines())
            if e.get('body', {}).get('event') == 'MODULE_ADDED']


def add(binary, method, reg, src):
    return run(binary, 'module', 'add', reg, src, '--by', 'principal', '--method', method)


def mcp(binary, root, calls):
    requests = [
        {'jsonrpc': '2.0', 'id': 0, 'method': 'initialize', 'params': {
            'protocolVersion': '2025-06-18', 'capabilities': {},
            'clientInfo': {'name': 'native-regression', 'version': '1'}}},
        {'jsonrpc': '2.0', 'method': 'notifications/initialized'}]
    requests.extend({'jsonrpc': '2.0', 'id': i, 'method': 'tools/call', 'params': item}
                    for i, item in enumerate(calls, 1))
    result = run(binary, 'mcp', root=root,
                 input_text='\n'.join(json.dumps(x) for x in requests) + '\n')
    if result['exit']:
        raise RuntimeError('MCP process failed: ' + repr(result))
    replies = [json.loads(line) for line in result['stdout'].splitlines() if line.strip()]
    return replies[1:]


def text_of(reply):
    return '\n'.join(p.get('text', '') for p in reply.get('result', {}).get('content', []))


def normal_control(binary, method, base):
    root = base / 'normal'; reg = initialize(binary, root)
    src = source(root, 'normal', 'normal')
    first = add(binary, method, reg, src)
    before = reg.read_bytes()
    second = add(binary, method, reg, src)
    installed = reg.parent / 'modules/normal/SOURCE/Specification.md'
    ok = first['exit'] == 0 and second['exit'] != 0 and len(additions(reg)) == 1
    ok = ok and reg.read_bytes() == before and run(binary, 'verify', reg)['exit'] == 0
    ok = ok and installed.is_file() and installed.read_bytes() == (src / 'Specification.md').read_bytes()
    return dict(pass_control=ok, first_exit=first['exit'], duplicate_exit=second['exit'])


def concurrent_add(binary, method, base, rounds):
    trials = []
    for r in range(rounds):
        root = base / ('race_' + str(r)); reg = initialize(binary, root)
        sources = [source(root, 'race', f'{r}_{i}') for i in range(8)]
        with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
            replies = list(pool.map(lambda p: add(binary, method, reg, p), sources))
        written = additions(reg)
        accepted = sum(p['exit'] == 0 for p in replies)
        trials.append(dict(accepted=accepted, recorded=len(written),
                           distinct_hashes=len({e['body']['module']['sha256'] for e in written}),
                           register_verified=(run(binary, 'verify', reg)['exit'] == 0)))
    bad = any(t['recorded'] > 1 or t['accepted'] > 1 for t in trials)
    healthy = all(t['accepted'] == 1 and t['recorded'] == 1 and t['register_verified'] for t in trials)
    return dict(pass_control=healthy and not bad, violation_seen=bad, trials=trials,
                note='No collision in finite trials does not prove absence of a race')


def linked_module(binary, method, base):
    root = base / 'linked_module'; reg = initialize(binary, root)
    outside = base / 'external_module'; outside.mkdir()
    module_dir = reg.parent / 'modules'; module_dir.mkdir()
    (module_dir / 'linked').symlink_to(outside, target_is_directory=True)
    result = add(binary, method, reg, source(root, 'linked', 'linked'))
    escaped = (outside / 'SOURCE/Specification.md').exists()
    return dict(pass_control=not escaped and run(binary, 'verify', reg)['exit'] == 0,
                violation_seen=escaped, module_exit=result['exit'], outside_written=escaped)


def failed_remove(binary, method, base):
    if os.name != 'posix':
        return dict(skipped='POSIX RLIMIT_FSIZE required')
    import resource
    root = base / 'remove_failure'; reg = initialize(binary, root)
    added = add(binary, method, reg, source(root, 'removeme', 'removeme'))
    if added['exit']:
        raise RuntimeError('positive module installation failed: ' + repr(added))
    previous = reg.read_bytes()
    def no_file_growth():
        signal.signal(signal.SIGXFSZ, signal.SIG_IGN)
        resource.setrlimit(resource.RLIMIT_FSIZE, (0, 0))
    result = run(binary, 'module', 'remove', reg, 'removeme', '--by', 'principal', preexec_fn=no_file_growth)
    installed = (reg.parent / 'modules/removeme/SOURCE/Specification.md').is_file()
    same = reg.read_bytes() == previous
    return dict(pass_control=result['exit'] != 0 and same and installed and run(binary, 'verify', reg)['exit'] == 0,
                violation_seen=not installed and same,
                remove_exit=result['exit'], preserved_file=installed, register_unchanged=same)


def repair_symlink(binary, base):
    root = base / 'repair'; reg = initialize(binary, root)
    fragment = b'{"seq":999,"unfinished":true'
    with reg.open('ab') as out: out.write(fragment)
    aside = reg.with_suffix('.fragment-' + digest(fragment)[:12])
    sentinel = base / 'external_repair'; sentinel.write_bytes(b'UNMODIFIED EXTERNAL SENTINEL')
    aside.symlink_to(sentinel)
    result = run(binary, 'repair', reg)
    outside_mutated = sentinel.read_bytes() != b'UNMODIFIED EXTERNAL SENTINEL'
    return dict(pass_control=not outside_mutated,
                violation_seen=outside_mutated, repair_exit=result['exit'], outside_changed=outside_mutated)


def artifact_hardlink(binary, base):
    root = base / 'hardlink_artifact'; reg = initialize(binary, root)
    payload = b'HOST_TEXT_EXACT'
    dest = reg.parent / 'artifacts' / digest(payload)
    dest.parent.mkdir()
    sentinel = base / 'external_hardlink'; sentinel.write_bytes(b'UNMODIFIED EXTERNAL SENTINEL')
    os.link(sentinel, dest)
    replies = mcp(binary, root, [
        {'name': 'acr_begin', 'arguments': {}},
        {'name': 'acr_artifact', 'arguments': {'text': payload.decode(), 'origin': 'PRODUCED', 'name': 'synthetic'}}])
    changed = sentinel.read_bytes() != b'UNMODIFIED EXTERNAL SENTINEL'
    return dict(pass_control=not changed and run(binary, 'verify', reg)['exit'] == 0,
                violation_seen=changed, outside_changed=changed,
                recorded_success=text_of(replies[-1]).startswith('WRITTEN as event'))


def artifact_read_control(binary, base):
    root = base / 'artifact_read'; root.mkdir()
    ext = base / 'external_read'; ext.write_bytes(b'outside')
    (root / 'inside').write_bytes(b'inside')
    (root / 'link').symlink_to(ext)
    (root / 'linkdir').symlink_to(base, target_is_directory=True)
    paths = ['inside', 'link', 'linkdir/external_read', '../external_read', str(ext)]
    replies = mcp(binary, root, [{'name': 'acr_artifact', 'arguments': {'path': p, 'record': False}}
                                 for p in paths])
    allowed = [not x.get('result', {}).get('isError', False) for x in replies]
    return dict(pass_control=(allowed == [True, False, False, False, False] and not (root / '.pcp').exists()),
                allowed=dict(zip(paths, allowed)))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--pcpos', type=Path, required=True)
    ap.add_argument('--method', type=Path, required=True)
    ap.add_argument('--rounds', type=int, default=3)
    ap.add_argument('--json', type=Path)
    ap.add_argument('--expect-fixed', action='store_true')
    options = ap.parse_args()
    binary, method = options.pcpos.resolve(), options.method.resolve()
    if not binary.is_file() or not (method / 'KERNEL.md').is_file() or options.rounds < 1:
        ap.error('valid native binary, method tree and positive --rounds required')
    report = dict(binary_sha256=digest(binary.read_bytes()),
                  method_manifest_sha256=digest((method / 'MANIFEST.json').read_bytes()),
                  cases={}, note='Temporary synthetic paths only; no claim about live registers or hardware kernel')
    with tempfile.TemporaryDirectory(prefix='pcp22-native-contract-') as folder:
        base = Path(folder)
        checks = [('normal', lambda: normal_control(binary, method, base)),
                  ('race', lambda: concurrent_add(binary, method, base, options.rounds)),
                  ('module_symlink', lambda: linked_module(binary, method, base)),
                  ('failed_remove', lambda: failed_remove(binary, method, base)),
                  ('repair_symlink', lambda: repair_symlink(binary, base)),
                  ('artifact_hardlink', lambda: artifact_hardlink(binary, base)),
                  ('artifact_read', lambda: artifact_read_control(binary, base))]
        for name, fn in checks:
            try: report['cases'][name] = fn()
            except Exception as error: report['cases'][name] = {'probe_error': repr(error)}
            print(f"{name}: {report['cases'][name]}", flush=True)
    if options.json:
        options.json.parent.mkdir(parents=True, exist_ok=True)
        options.json.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    failure = [name for name, result in report['cases'].items() if result.get('pass_control') is False or result.get('probe_error')]
    if options.expect_fixed and failure:
        print('REGRESSION_FAIL: ' + ', '.join(failure))
        return 1
    print('EVIDENCE_ONLY' if not options.expect_fixed else 'REGRESSION_PASS')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
