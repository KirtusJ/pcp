#!/usr/bin/env python3
"""Native PCP OS 1.0.22: positional operands must survive flag-value collisions.

Uses only self-deleting synthetic registers; --expect-fixed exits 1 on failures.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import tempfile


def execute(binary, *args):
    env = {k: v for k, v in os.environ.items() if not k.startswith('PCPOS_')
           and not k.startswith('CLAUDE_PLUGIN_OPTION_')}
    p = subprocess.run([str(binary), *(str(x) for x in args)], text=True,
                       capture_output=True, timeout=20, env=env)
    return p.returncode, p.stdout.strip(), p.stderr.strip()


def case(binary, method, base, label, principal, action, wanted):
    root = base / label
    register = root / '.pcp/register.jsonl'
    register.parent.mkdir(parents=True)
    code, _, err = execute(binary, 'init', register, '--principal', principal)
    if code:
        raise RuntimeError('failed to create synthetic register: ' + err)
    if action == 'standard':
        command = ('standard', register, '--by', principal, wanted)
    else:
        command = ('workspace', register, '--by', principal,
                   '--method', method, wanted)
    code, out, err = execute(binary, *command)
    events = [json.loads(line) for line in register.read_text().splitlines()]
    if action == 'standard':
        values = [event['body'] for event in events if event.get('kind') == 'STANDARD_SET']
        expected = dict(method='NATIVE_ONLY', model_findings='MECHANICAL_ONLY',
                        human_adoption=True, dual_authorization=True,
                        static_tasks=True, offline_only=True)
        selected = {k: values[-1].get(k) for k in expected} if values else None
        good = code == 0 and len(values) == 1 and selected == expected
    else:
        values = [event['body'] for event in events if event.get('kind') == 'HOST_EVENT'
                  and event.get('body', {}).get('event') == 'WORKSPACE_PROFILE']
        selected = [module.get('id') for module in values[-1].get('modules', [])] if values else None
        good = code == 0 and len(values) == 1 and selected == ['acr.' + wanted]
    verified = execute(binary, 'verify', register)[0] == 0
    return dict(pass_control=bool(good and verified), principal=principal,
                action=action, requested=wanted, exit=code, recorded=selected,
                event_count=len(values), register_verified=verified,
                error=(err or out)[:200] if code else None)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--pcpos', type=Path, required=True)
    p.add_argument('--method', type=Path, required=True)
    p.add_argument('--json', type=Path)
    p.add_argument('--expect-fixed', action='store_true')
    args = p.parse_args()
    binary, method = args.pcpos.resolve(), args.method.resolve()
    if not binary.is_file() or not (method / 'MANIFEST.json').is_file():
        p.error('required: native binary and method tree')
    specs = [
        ('standard_normal', 'principal', 'standard', 'CRITICAL'),
        ('standard_actor_collision', 'CRITICAL', 'standard', 'CRITICAL'),
        ('standard_unrelated_baseline_label', 'BASELINE', 'standard', 'CRITICAL'),
        ('workspace_normal', 'principal', 'workspace', 'science'),
        ('workspace_actor_collision_science', 'science', 'workspace', 'science'),
        ('workspace_actor_collision_mathematics', 'mathematics', 'workspace', 'mathematics'),
    ]
    result = {'host_sha256': hashlib.sha256(binary.read_bytes()).hexdigest(),
              'method_manifest_sha256': hashlib.sha256((method / 'MANIFEST.json').read_bytes()).hexdigest(),
              'cases': {}, 'scope': 'hosted native CLI with temporary workspaces only'}
    with tempfile.TemporaryDirectory(prefix='pcp-flag-operand-collision-') as tmp:
        for label, principal, action, wanted in specs:
            data = case(binary, method, Path(tmp), label, principal, action, wanted)
            result['cases'][label] = data
            print(label, 'PASS' if data['pass_control'] else 'FAIL', flush=True)
    n = sum(c['pass_control'] for c in result['cases'].values())
    result['summary'] = dict(passed=n, total=len(specs), all_passed=n == len(specs))
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(json.dumps(result, indent=2, sort_keys=True) + '\n', encoding='utf8')
    print('SUMMARY', result['summary'])
    return 1 if args.expect_fixed and n < len(specs) else 0


if __name__ == '__main__':
    raise SystemExit(main())
