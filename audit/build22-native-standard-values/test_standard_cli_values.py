#!/usr/bin/env python3
"""PCP OS 1.0.22: CLI standard inputs must be parsed without silent coercion.

No live workspaces: every command acts on a disposable, synthetic register.
--expect-fixed returns nonzero when the implementation violates an oracle.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import tempfile

STRICT = dict(method='NATIVE_ONLY', model_findings='MECHANICAL_ONLY',
              human_adoption=True, dual_authorization=True,
              static_tasks=True, offline_only=True)


def run(binary, *args):
    env = {k: v for k, v in os.environ.items()
           if not k.startswith('PCPOS_') and not k.startswith('CLAUDE_PLUGIN_OPTION_')}
    p = subprocess.run([str(binary), *(str(x) for x in args)],
                       text=True, capture_output=True, env=env, timeout=20)
    return p.returncode, p.stdout.strip(), p.stderr.strip()


def examine(binary, root, label, overrides, expected=None):
    reg = root / label / '.pcp' / 'register.jsonl'
    reg.parent.mkdir(parents=True)
    code, _, detail = run(binary, 'init', reg, '--principal', 'principal')
    if code:
        raise RuntimeError(f'init for {label} failed: {detail}')
    before = reg.read_bytes()
    code, out, err = run(binary, 'standard', reg, '--by', 'principal', 'CRITICAL', *overrides)
    events = [json.loads(row) for row in reg.read_text().splitlines()]
    standards = [event['body'] for event in events if event.get('kind') == 'STANDARD_SET']
    verify = run(binary, 'verify', reg)[0] == 0
    recorded = {key: standards[-1][key] for key in STRICT} if standards else None
    if expected is None:
        good = code != 0 and reg.read_bytes() == before and not standards and verify
    else:
        good = code == 0 and len(standards) == 1 and recorded == expected and verify
    return dict(pass_control=bool(good), exit=code,
                register_unchanged=reg.read_bytes() == before,
                recorded=recorded, standard_events=len(standards),
                register_verified=verify,
                error=(err or out)[:180] if code else None)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--pcpos', required=True, type=Path)
    p.add_argument('--json', type=Path)
    p.add_argument('--expect-fixed', action='store_true')
    args = p.parse_args()
    binary = args.pcpos.resolve()
    if not binary.is_file():
        p.error('provide a real pcpos executable')
    specs = [
        ('critical_exact', [], STRICT),
        ('critical_explicit_false_human', ['human_adoption=false'], dict(STRICT, human_adoption=False)),
        ('critical_explicit_false_offline', ['offline_only=false'], dict(STRICT, offline_only=False)),
        ('critical_explicit_false_dual', ['dual_authorization=false'], dict(STRICT, dual_authorization=False)),
        ('critical_explicit_false_tasks', ['static_tasks=false'], dict(STRICT, static_tasks=False)),
        ('critical_explicit_native_or_pinned', ['method=NATIVE_OR_PINNED'], dict(STRICT, method='NATIVE_OR_PINNED')),
        ('critical_explicit_human_closes', ['model_findings=HUMAN_CLOSES'], dict(STRICT, model_findings='HUMAN_CLOSES')),
        ('reject_human_typo', ['human_adoption=tru'], None),
        ('reject_dual_typo', ['dual_authorization=treu'], None),
        ('reject_static_typo', ['static_tasks=tru'], None),
        ('reject_offline_typo', ['offline_only=TRUE'], None),
        ('reject_method_typo', ['method=NATIVE-ONLy'], None),
        ('reject_findings_typo', ['model_findings=MECHANICAL-ONLY'], None),
    ]
    report = {'host_sha256': hashlib.sha256(binary.read_bytes()).hexdigest(), 'cases': {},
              'scope': 'native host CLI only; fresh temporary registers, no system administration'}
    with tempfile.TemporaryDirectory(prefix='pcp-standard-values-') as tmp:
        for name, tokens, expectation in specs:
            report['cases'][name] = examine(binary, Path(tmp), name, tokens, expectation)
            print(name, 'PASS' if report['cases'][name]['pass_control'] else 'FAIL', flush=True)
    passing = sum(c['pass_control'] for c in report['cases'].values())
    report['summary'] = dict(passed=passing, total=len(specs), all_passed=passing == len(specs))
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(json.dumps(report, indent=2, sort_keys=True) + '\n', encoding='utf8')
    print('SUMMARY', report['summary'])
    return 1 if args.expect_fixed and passing != len(specs) else 0


if __name__ == '__main__':
    raise SystemExit(main())
