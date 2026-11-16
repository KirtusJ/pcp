"""Run three paired cold starts of the unchanged public CD with no guest input."""
import argparse
import json
from pathlib import Path
import subprocess

from check import check, GuestSafe, IMAGE_SHA, ISO_SHA


def observe(iso, directory, mode, *, expected_iso=ISO_SHA, expected_image=IMAGE_SHA):
    row = {}
    try:
        check(iso, directory, clock=mode, startup_only=True,
              expected_iso=expected_iso, expected_image=expected_image)
        row["outcome"] = "launcher"
    except GuestSafe:
        row["outcome"] = "SAFE"
    except Exception as error:
        row.update(outcome="incomplete", error=repr(error))
    serial = directory / "serial.txt"
    log = serial.read_text(errors="replace") if serial.exists() else ""
    lines = log.splitlines()
    measurement = (f"running image (code and read-only data), SHA-256: {expected_image} "
                   "(measured; equal to the value the loader named)")
    row["running_image_matched"] = lines.count(measurement) == 1
    row["sleep_stop_observations"] = [line.strip() for line in lines
                                      if line.startswith("  note stop key while asleep:")]
    row["keyboard_observations"] = [
        line.strip() for line in log.splitlines()
        if "note key while waiting:" in line or "note stop key while waiting for a key:" in line
    ]
    row["failed_checks"] = [line.strip() for line in log.splitlines() if line.startswith("  FAIL ")]
    return row


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
            row.update(observe(args.iso.resolve(), directory, mode))
            report["runs"].append(row)
            summary.write_text(json.dumps(report, indent=2) + "\n")
            print(json.dumps(row), flush=True)

    if any(not row["running_image_matched"] or row["outcome"] == "incomplete" or
           len(row["keyboard_observations"]) != 2 for row in report["runs"]):
        raise SystemExit("Incomplete comparison. Inspect every recorded outcome.")


if __name__ == "__main__":
    main()
