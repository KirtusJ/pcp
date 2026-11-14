#!/usr/bin/env python3
"""Test build-22 Python PCP OS filesystem contracts on disposable files only."""
import argparse
import hashlib
import os
from pathlib import Path
import sys
import tempfile
import unittest

argp = argparse.ArgumentParser(description=__doc__)
argp.add_argument("--python-os", type=Path, required=True)
argp.add_argument("--method-zip", type=Path, required=True)
args, remaining = argp.parse_known_args()
source = args.python_os.resolve()
packet = args.method_zip.resolve()
if not (source / "pcpos/store.py").is_file() or not packet.is_file():
    argp.error("supply the exact trusted Python source and ACR packet paths")
sys.path.insert(0, str(source))

from pcpos.base import atomic_write, PcposError
from pcpos.method import install_from_zip
from pcpos.store import Workspace


class FilesystemContract(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory(prefix="pcpos-contract-")
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)

    def workspace(self):
        return Workspace.create(self.root / "ws")

    def test_normal_method_install(self):
        parent = self.root / "install"
        parent.mkdir()
        dest, ident = install_from_zip(packet, parent)
        self.assertTrue(ident["matches_required"])
        self.assertTrue((dest / "MODULES/01_Core/SOURCE/Specification.md").is_file())

    def test_method_install_rejects_prelinked_modules(self):
        parent = self.root / "install"
        target = parent / "ACR_1.0_Implementation"
        target.mkdir(parents=True)
        outside = self.root / "outside"
        outside.mkdir()
        (target / "MODULES").symlink_to(outside, target_is_directory=True)
        with self.assertRaises(PcposError):
            install_from_zip(packet, parent)
        self.assertFalse(list(outside.rglob("*")))
        self.assertFalse((target / "MANIFEST.json").exists())

    def test_normal_atomic_replace(self):
        target = self.root / "out"
        atomic_write(target, b"ONE")
        atomic_write(target, b"TWO")
        self.assertEqual(target.read_bytes(), b"TWO")
        self.assertFalse(target.is_symlink())

    def test_preplaced_temp_symlink_is_not_followed(self):
        target = self.root / "out"
        outside = self.root / "outside"
        outside.write_bytes(b"SENTINEL")
        old_temp = target.with_name(target.name + ".tmp%d" % os.getpid())
        old_temp.symlink_to(outside)
        atomic_write(target, b"NEW")
        self.assertEqual(outside.read_bytes(), b"SENTINEL")
        self.assertEqual(target.read_bytes(), b"NEW")
        self.assertFalse(target.is_symlink())

    def test_normal_object_write_and_reuse(self):
        ws = self.workspace()
        data = b"normal object"
        digest = hashlib.sha256(data).hexdigest()
        self.assertEqual(ws.put_bytes(data), digest)
        self.assertEqual(ws.put_bytes(data), digest)
        input_path = self.root / "input"
        input_path.write_bytes(data)
        self.assertEqual(ws.put_file(input_path), (digest, len(data)))
        self.assertEqual(ws.get(digest), data)

    def test_object_store_refuses_linked_objects_folder(self):
        ws = self.workspace()
        outside = self.root / "external-store"
        outside.mkdir()
        ws.objects.rmdir()
        ws.objects.symlink_to(outside, target_is_directory=True)
        with self.assertRaises(PcposError):
            ws.put_bytes(b"synthetic test")
        self.assertFalse(list(outside.rglob("*")))

    def test_put_bytes_rejects_existing_corruption(self):
        ws = self.workspace()
        data = b"correct bytes"
        digest = hashlib.sha256(data).hexdigest()
        target = ws.object_path(digest)
        target.parent.mkdir()
        target.write_bytes(b"wrong")
        with self.assertRaises(PcposError):
            ws.put_bytes(data)
        self.assertEqual(target.read_bytes(), b"wrong")

    def test_put_file_rejects_existing_corruption(self):
        ws = self.workspace()
        data = b"input contents"
        source_file = self.root / "input"
        source_file.write_bytes(data)
        digest = hashlib.sha256(data).hexdigest()
        target = ws.object_path(digest)
        target.parent.mkdir()
        target.write_bytes(b"wrong")
        with self.assertRaises(PcposError):
            ws.put_file(source_file)
        self.assertEqual(target.read_bytes(), b"wrong")


if __name__ == "__main__":
    unittest.main(argv=[sys.argv[0], *remaining])
