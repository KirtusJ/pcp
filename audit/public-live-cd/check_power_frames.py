"""Replay the F10 screens captured for pcp-os#314 through the distribution checker.

The 640x480 and 800x600 originals came from native guests at pcp-os 8979270.
The two reflows use those same pixels. Their source records are at
pcp-os d6b7f85 (evidence/compact-desktop) and pcp 5983154 (audit/desktop-power-check).
"""
import argparse
import hashlib
from pathlib import Path
from zipfile import ZipFile

from desktop_screens import DesktopScreens


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("kernel_source", type=Path)
    args = parser.parse_args()
    reader = DesktopScreens(args.kernel_source, {})
    expected = {
        "guest-640x480-clipped.ppm": False,
        "guest-800x600-complete.ppm": True,
        "reflow-640x480-complete.ppm": True,
        "reflow-640x480-missing-not.ppm": False,
    }
    failures = []
    with ZipFile(Path(__file__).with_name("power-warning-frames.zip")) as frames:
        for name, should_accept in expected.items():
            frame = frames.read(name)
            accepted = reader.matches(frame, "power")
            print(f"{name}: {'accepted' if accepted else 'rejected'}  sha256={hashlib.sha256(frame).hexdigest()}")
            if accepted != should_accept:
                failures.append(name)
    if failures:
        raise SystemExit("Unexpected warning verdict for " + ", ".join(failures))


if __name__ == "__main__":
    main()
