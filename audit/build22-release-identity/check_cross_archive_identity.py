#!/usr/bin/env python3
"""Audit a PCP outer release ZIP against each nested edition/plugin identity.

Read-only, standard-library-only. Local digests establish byte identity relative
 to a supplied manifest, not publisher identity or semantic fitness.
"""
from __future__ import annotations
import argparse
from hashlib import sha256
from io import BytesIO
import json
from pathlib import Path
from zipfile import ZipFile, BadZipFile


def hex256(raw: bytes) -> str:
    return sha256(raw).hexdigest()


def json_member(z: ZipFile, path: str) -> dict:
    value = json.loads(z.read(path))
    if not isinstance(value, dict):
        raise ValueError(f'{path} must be a JSON object')
    return value


def check(path: Path) -> dict:
    out = {'release_zip_sha256': hex256(path.read_bytes()),
           'source': str(path), 'hash_checks': [], 'build_labels': [],
           'problems': [], 'summary': {}}
    with ZipFile(path) as outer:
        indexes = [n for n in outer.namelist() if n.endswith('/RELEASE.json') and n.count('/') == 1]
        if len(indexes) != 1:
            raise ValueError(f'exactly one top-level RELEASE.json required, got {indexes}')
        prefix = indexes[0].removesuffix('RELEASE.json')
        index = json_member(outer, indexes[0])
        build = index.get('build')
        if type(build) is not int or build < 1:
            raise ValueError(f'outer build is not a positive integer: {build!r}')
        out['outer_build'] = build
        out['outer_plugin_version'] = index.get('plugins', {}).get('version')
        expected_plugin_version = '1.0.' + str(build)
        if out['outer_plugin_version'] != expected_plugin_version:
            out['problems'].append(f'outer plugin version != {expected_plugin_version}')
        for kind, row in [('source', index.get('source')), ('record', index.get('record'))]:
            if not isinstance(row, dict):
                raise ValueError(f'missing outer {kind} record')
            nested = row['file']
            raw = outer.read(prefix + nested)
            matches = hex256(raw) == row['sha256']
            out['hash_checks'].append({'scope': kind, 'file': nested, 'matches': matches})
            if not matches: out['problems'].append(f'{kind} archive hash mismatch')
        editions = index.get('editions', {})
        if sorted(editions) != ['COMMERCIAL', 'ENTERPRISE', 'PERSONAL']:
            raise ValueError('expected PERSONAL/COMMERCIAL/ENTERPRISE editions')
        for edition, rec in sorted(editions.items()):
            for label, data in [('edition', rec), ('plugin_only', rec['plugins_archive'])]:
                name = data['file']
                raw = outer.read(prefix + name)
                matches = hex256(raw) == data['sha256']
                out['hash_checks'].append({'scope': edition + '/' + label,
                                           'file': name, 'matches': matches})
                if not matches:
                    out['problems'].append(f'{edition} {label} hash mismatch')
                with ZipFile(BytesIO(raw)) as inner:
                    subroot = name.removesuffix('.zip') + '/'
                    if label == 'edition':
                        manifests = ['EDITION.json', 'MANIFEST.json']
                    else:
                        manifests = ['PLUGINS.json', 'MANIFEST.json']
                    for manifest in manifests:
                        info = json_member(inner, subroot + manifest)
                        actual = info.get('build')
                        same = type(actual) is int and actual == build
                        out['build_labels'].append({'scope': edition + '/' + label,
                                                    'file': manifest, 'actual': actual,
                                                    'outer': build, 'matches': same})
                        if not same:
                            out['problems'].append(f'{edition}/{label}/{manifest}: '
                                                   f'build {actual!r} != outer {build}')
                    plugins_prefix = ('PCP_1.0_Plugins/plugins/' if label == 'edition'
                                      else 'PCP_1.0_Plugins/plugins/')
                    for plugin in ('pcp', 'pcp-os'):
                        info = json_member(inner, subroot + plugins_prefix
                                           + plugin + '/.claude-plugin/plugin.json')
                        version = info.get('version')
                        same = version == out['outer_plugin_version']
                        out['build_labels'].append({'scope': edition + '/' + label,
                                                    'file': plugin + '/plugin.json',
                                                    'actual': version,
                                                    'outer': out['outer_plugin_version'],
                                                    'matches': same})
                        if not same:
                            out['problems'].append(f'{edition}/{label}/{plugin}: '
                                                   f'version {version!r} != outer plugin version')
    out['summary'] = {'checked_archives': len(out['hash_checks']),
                      'hashes_passed': sum(x['matches'] for x in out['hash_checks']),
                      'build_labels_checked': len(out['build_labels']),
                      'build_labels_matched': sum(x['matches'] for x in out['build_labels']),
                      'problems': len(out['problems'])}
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('release_zip', type=Path)
    ap.add_argument('--json', type=Path)
    args = ap.parse_args()
    try:
        result = check(args.release_zip)
    except (OSError, ValueError, KeyError, BadZipFile) as error:
        print('BLOCKED:', type(error).__name__, str(error))
        return 2
    for label in result['build_labels']:
        if not label['matches']:
            print('IDENTITY_MISMATCH:', label['scope'], label['file'],
                  'actual=', label['actual'], 'outer=', label['outer'])
    print('SUMMARY:', json.dumps(result['summary'], sort_keys=True))
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(json.dumps(result, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    return 1 if result['problems'] else 0


if __name__ == '__main__':
    raise SystemExit(main())
