"""Compare wall-clock CD startup with and without a single competing CPU task."""
import argparse
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import time

from check import IMAGE_SHA, ISO_SHA
from compare_clocks import observe


def trial(iso, directory, cpu, loaded, expected_iso=ISO_SHA, expected_image=IMAGE_SHA):
    row = {"cpu": cpu, "loaded": loaded}
    worker = None
    start = time.monotonic()
    try:
        if loaded:
            # The worker inherits the same CPU affinity as the QEMU process.
            # Its own deadline also bounds it if the invoking process disappears.
            worker = subprocess.Popen(
                [sys.executable, "-c",
                 "import signal; signal.alarm(200); print('ready', flush=True)\nwhile True: pass"],
                stdout=subprocess.PIPE, text=True,
            )
            if worker.stdout.readline().strip() != "ready" or os.sched_getaffinity(worker.pid) != {cpu}:
                raise RuntimeError("Competing task did not start on the pinned CPU")
        row.update(observe(iso, directory, "wall", expected_iso=expected_iso,
                           expected_image=expected_image))
    finally:
        if worker is not None:
            worker.terminate()
            pid, status, usage = os.wait4(worker.pid, 0)
            worker.returncode = os.waitstatus_to_exitcode(status)
            worker.stdout.close()
            row["competitor_cpu_seconds"] = usage.ru_utime + usage.ru_stime
            row["competitor_terminated_by_test"] = worker.returncode == -signal.SIGTERM
        row["elapsed_seconds"] = time.monotonic() - start
    return row


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("iso", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--candidate", type=Path, help="compare keyboard-01 with the public CD under the same load")
    args = parser.parse_args()
    root = args.output.resolve()
    root.mkdir(parents=True, exist_ok=False)
    allowed = os.sched_getaffinity(0)
    cpu = min(allowed)
    runs = []
    report = {"cpu": cpu, "clock": "wall", "iso_sha256": ISO_SHA, "runs": runs,
              "qemu": subprocess.check_output(["qemu-system-x86_64", "--version"], text=True).splitlines()[0]}
    released = (args.iso.resolve(), ISO_SHA, IMAGE_SHA)
    if args.candidate:
        inventory = Path(__file__).parent / "candidates/keyboard-01/identity.json"
        identity = json.loads(inventory.read_text())
        candidate = (args.candidate.resolve(), identity["candidate_iso"], identity["candidate_image"])
        members = [("released", True, released), ("keyboard-01", True, candidate)]
        report["candidate_iso_sha256"] = identity["candidate_iso"]
    else:
        members = [("control", False, released), ("loaded", True, released)]
    try:
        os.sched_setaffinity(0, {cpu})
        for pair, order in enumerate([members, members[::-1]] * 2, 1):
            for label, loaded, (iso, iso_sha, image_sha) in order:
                row = trial(iso, root / f"{pair}-{label}", cpu, loaded, iso_sha, image_sha)
                row.update(label=label, iso_sha256=iso_sha, expected_image=image_sha)
                row["pair"] = pair
                runs.append(row)
                (root / "summary.json").write_text(json.dumps(report, indent=2) + "\n")
                print(json.dumps(row), flush=True)
    finally:
        os.sched_setaffinity(0, allowed)
    if any(row["outcome"] == "incomplete" or not row["running_image_matched"] or
           len(row["keyboard_observations"]) != 2 or
           (row["loaded"] and (not row["competitor_terminated_by_test"] or
                               row["competitor_cpu_seconds"] <= 0)) for row in runs):
        raise SystemExit("Incomplete comparison. Inspect individual trials.")
    if args.candidate and any(len(row["sleep_stop_observations"]) != 1 for row in runs):
        raise SystemExit("Missing longest-sleep Stop observation. Inspect individual trials.")
    if any(row["label"] == "keyboard-01" and row["outcome"] != "launcher" for row in runs):
        raise SystemExit("The candidate did not reach the launcher in every loaded trial.")


if __name__ == "__main__":
    main()
