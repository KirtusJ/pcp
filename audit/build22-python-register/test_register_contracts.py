#!/usr/bin/env python3
"""Build-22 Python PCP OS register-path and repair negative controls.

Uses only new temporary directories and synthetic events. No live register is read.
Run: python test_register_contracts.py --python-os /path/to/PCP_OS_Python
"""
import argparse
import os
from pathlib import Path
import sys
import tempfile
import threading
import unittest
from unittest.mock import patch

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--python-os', type=Path, required=True)
args, rest = parser.parse_known_args()
src = args.python_os.resolve()
if not (src / 'pcpos/store.py').is_file():
    parser.error('supply the exact intended Python source folder')
sys.path.insert(0, str(src))
from pcpos import base, store  # noqa: E402
from pcpos.store import Workspace  # noqa: E402


class RegisterContracts(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory(prefix='pcp-register-contract-')
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name)

    def test_regular_register_append(self):
        ws = Workspace.create(self.root / 'workspace')
        event, _ = ws.append('NOTE', {'text': 'control'}, 'P')
        self.assertEqual(event['seq'], 0)
        self.assertEqual(len(ws.events()[0]), 1)
        self.assertFalse(ws.register_path.is_symlink())
        self.assertEqual(ws.register_path.stat().st_nlink, 1)

    def test_symlink_or_hardlink_register_is_refused_without_exterior_effect(self):
        for alias in ('symlink', 'hardlink'):
            with self.subTest(alias=alias):
                base_path = self.root / alias
                ws = Workspace.create(base_path / 'workspace')
                exterior = base_path / 'outside.jsonl'
                exterior.write_bytes(ws.register_path.read_bytes())
                ws.register_path.unlink()
                if alias == 'symlink':
                    ws.register_path.symlink_to(exterior)
                else:
                    os.link(exterior, ws.register_path)
                original = exterior.read_bytes()
                with self.assertRaises(base.PcposError) as cm:
                    ws.append('NOTE', {'text': 'must not escape'}, 'P')
                self.assertEqual(cm.exception.code, base.INTEGRITY)
                self.assertEqual(exterior.read_bytes(), original)

    def test_repair_does_not_erase_event_completed_by_locked_writer(self):
        ws = Workspace.create(self.root / 'workspace')
        _, head = ws.events()
        event = {'seq': 0, 'prev': head, 'ts': base.now_utc(),
                 'actor': 'P', 'auth': 'DECLARED', 'kind': 'NOTE',
                 'body': {'text': 'completed and synced'}}
        line = base.canon(event) + b'\n'
        half = len(line) // 2
        lock = ws._lock()
        attempted_replace = threading.Event()
        permit_replace = threading.Event()
        outcome = {}
        real_write = store.atomic_write

        def gated_write(path, data):
            attempted_replace.set()
            if not permit_replace.wait(5):
                raise RuntimeError('test write gate timed out')
            return real_write(path, data)

        def do_repair():
            try:
                outcome['removed'] = ws.repair()
            except Exception as error:
                outcome['error'] = repr(error)

        try:
            with ws.register_path.open('ab') as f:
                f.write(line[:half]); f.flush(); os.fsync(f.fileno())
            with patch.dict(os.environ, {'PCPOS_LOCK_WAIT': '3'}):
                with patch.object(store, 'atomic_write', side_effect=gated_write):
                    thread = threading.Thread(target=do_repair)
                    thread.start()
                    # An unlocked repair reaches atomic_write with the writer's
                    # lock still held. A correct repair must wait for that lock.
                    attempted_replace.wait(0.35)
                    with ws.register_path.open('ab') as f:
                        f.write(line[half:]); f.flush(); os.fsync(f.fileno())
                    self.assertEqual(len(ws.events()[0]), 1)
                    lock.unlink()
                    permit_replace.set()
                    thread.join(timeout=5)
            self.assertFalse(thread.is_alive(), 'repair must complete')
            self.assertNotIn('error', outcome)
            self.assertFalse(attempted_replace.is_set(), 'repair reached replacement while writer lock was held')
            self.assertEqual(outcome.get('removed'), 0)
            self.assertEqual(len(ws.events()[0]), 1)
        finally:
            lock.unlink(missing_ok=True)
            permit_replace.set()


if __name__ == '__main__':
    unittest.main(argv=[sys.argv[0], *rest], verbosity=2)
