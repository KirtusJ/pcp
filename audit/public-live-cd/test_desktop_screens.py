"""Negative controls for the selected card on the AC'97 desktop CD and VM fixtures."""
import unittest

from desktop_screens import selected_program


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


if __name__ == "__main__":
    unittest.main()
