"""Checks for desktop media receipts, the selected program and the verification page."""
import json
from pathlib import Path
from unittest.mock import Mock
import unittest
from zipfile import ZipFile

from desktop_image import desktop_program_hashes
from desktop_screens import DesktopScreens, complete_power_warning, selected_program


class DesktopGrants(unittest.TestCase):
    def test_fixture_disclosure_and_pin_annotations(self):
        digest = "1234567890abcdef" * 4
        entry = "  > surf.elf".ljust(63) + "118 KiB   SHA-256 " + digest[:16] + "..."
        left = entry.index("surf.elf")
        end = len(entry) + 1
        access = "may use: display, keyboard, sound, loader files, store"
        edge = "?" * end

        def plate(text):
            return (" " * left + text).ljust(end) + "? neighboring art"

        def chosen(text, *following):
            return selected_program([entry, plate(text), *following, edge], "surf.elf", {"surf.elf": digest})

        for mark in ("", "   in the dock", "   on the desktop"):
            self.assertTrue(chosen(access + mark))
        pin = plate("pinned to the desktop")
        self.assertTrue(chosen(access, pin))
        for forged in ("may use: console only", access.replace("sound, ", ""), access + ", raw Ethernet frames",
                       access + "? second serial port", access.replace("sound", "store")):
            self.assertFalse(chosen(forged))
        self.assertFalse(chosen(access, " " * (left - 3) + "BAD"))
        for extra in ("         second serial port", "unexpected text"):
            self.assertFalse(chosen(access, plate(extra)))
            self.assertFalse(chosen(access, pin, plate(extra)))


class DesktopMedia(unittest.TestCase):
    def test_every_member_matches_the_physical_cd(self):
        archive = Path(__file__).parent / "candidates/source-bios/source-bios-tester.zip"
        with ZipFile(archive) as tester:
            image = tester.read("pcp-os-tester.iso")
            receipt = json.loads(tester.read("receipt.json"))
        members = receipt["on_disc"]
        self.assertEqual(desktop_program_hashes(image, receipt), {"surf.elf": members["surf.elf"]["sha256"]})
        for wrong_size in (len(image) + 1, float(len(image)), True):
            with self.subTest(iso_bytes=wrong_size), self.assertRaisesRegex(ValueError, "ISO byte count"):
                desktop_program_hashes(image, dict(receipt, iso_bytes=wrong_size))
        for name, fields in (("surf.elf", {"sha256": members["surf.elf"]["sha256"][:16] + "0" * 48}),
                             ("kernel.elf32", {"bytes": members["kernel.elf32"]["bytes"] + 1}),
                             ("boot.cat", {"bytes": float(members["boot.cat"]["bytes"])}),
                             ("boot.cat", {"bytes": True}),
                             ("boot.cat", {"sha256": "0" * 64})):
            changed = dict(members, **{name: dict(members[name], **fields)})
            with self.subTest(member=name), self.assertRaisesRegex(ValueError, "differs from ISO member"):
                desktop_program_hashes(image, dict(receipt, on_disc=changed))
        for changed in (dict(members, **{"rdesk.elf": members["surf.elf"]}),
                        {k: v for k, v in members.items() if k != "surf.elf"}):
            with self.assertRaisesRegex(ValueError, "inventory differ"):
                desktop_program_hashes(image, dict(receipt, on_disc=changed))

    def test_power_requires_the_complete_warning_across_visible_rows(self):
        rows = [""] * 24
        rows[1], rows[3] = "POWER OFF", "Switch PCP OS off?"
        rows[-2] = "Enter switch off    Esc go back"
        # The 640x480 guest's first line ended partway through "session".
        rows[5:7] = ["The register is closed and verified first. Files of this sessi",
                     "not saved by a program are lost."]
        self.assertFalse(complete_power_warning(rows))
        rows[5:8] = ["The register is closed and verified first.",
                     "Files of this session that were not saved",
                     "by a program are lost."]
        self.assertTrue(complete_power_warning(rows))

    def test_verification_requires_a_positive_event_count(self):
        rows = [""] * 30
        rows[1] = "  VERIFICATION"
        rows[3] = "  Verified at start: all 71 self-tests passed."
        rows[7] = "  The register's chain is intact."
        rows[-2] = "  Any key goes back"
        reader = Mock(spec=DesktopScreens)
        reader.glyphs = {}
        reader.has_verification_page = True
        reader.read_screen = Mock(return_value=rows)
        for count in ("1", "44", "0", "00", "01", "-1"):
            with self.subTest(count=count):
                rows[6] = f"  Register: {count} events, head 0123456789abcdef..."
                self.assertEqual(DesktopScreens.matches(reader, b"", "verification"), count in ("1", "44"))


if __name__ == "__main__":
    unittest.main()
