"""Run three paired cold starts of the unchanged public CD with no guest input."""
import argparse
import json
from pathlib import Path
import subprocess

from check import check, GuestSafe, IMAGE_SHA, ISO_SHA


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("iso", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    root = args.output.resolve()
    root.mkdir(parents=True, exist_ok=False)
    report = {
        "iso_sha256": ISO_SHA,
        "qemu": subprocess.check_output(["qemu-system-x86_64", "--version"], text=True).splitlines()[0],
        "runs": [],
    }
    summary = root / "summary.json"
    for pair, order in enumerate([("wall", "instructions"), ("instructions", "wall"),
                                  ("wall", "instructions")], 1):
        for mode in order:
            directory = root / f"{pair}-{mode}"
            row = {"pair": pair, "clock": mode}
            try:
                check(args.iso.resolve(), directory, clock=mode, startup_only=True)
                row["outcome"] = "launcher"
            except GuestSafe:
                row["outcome"] = "SAFE"
            except Exception as error:
                row.update(outcome="incomplete", error=repr(error))
            serial = directory / "serial.txt"
            log = serial.read_text(errors="replace") if serial.exists() else ""
            row["running_image_matched"] = IMAGE_SHA + " (measured; equal" in log
            row["keyboard_observations"] = [
                line.strip() for line in log.splitlines()
                if "note key while waiting:" in line or "note stop key while waiting for a key:" in line
            ]
            row["failed_checks"] = [line.strip() for line in log.splitlines() if line.startswith("  FAIL ")]
            report["runs"].append(row)
            summary.write_text(json.dumps(report, indent=2) + "\n")
            print(json.dumps(row), flush=True)

    if any(not row["running_image_matched"] or row["outcome"] == "incomplete" or
           len(row["keyboard_observations"]) != 2 for row in report["runs"]):
        raise SystemExit("Incomplete comparison. Inspect every recorded outcome.")


if __name__ == "__main__":
    main()
