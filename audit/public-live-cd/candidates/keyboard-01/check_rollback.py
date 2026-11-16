"""Exercise the public download links and boot both media from separate empty directories."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import zipfile

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from check import check, GuestSafe, ISO_SHA, IMAGE_SHA


def download(guide, name, directory):
    # Read the user-facing link and checksum from the guide. The independent pins below and
    # the candidate inventory anchor the fetched bytes to the original distribution.
    url, = re.findall(r"\[" + re.escape(name) + r"\]\((https://raw\.githubusercontent\.com/[^)]+)\)", guide)
    directory.mkdir()
    target = directory / name
    subprocess.run(["curl", "--fail", "--location", "--silent", "--show-error", "--retry", "2",
                    "--output", target, url], check=True)
    digest = verify_download(guide, target)
    return {"filename": name, "url": url, "bytes": target.stat().st_size, "sha256": digest}


def verify_download(guide, path):
    expected, = re.findall(r"echo '([0-9a-f]{64})  " + re.escape(path.name) + r"' \| sha256sum -c -", guide)
    actual = hashlib.sha256(path.read_bytes()).hexdigest()
    if actual != expected:
        raise ValueError(f"{path.name} differs from the documented SHA-256")
    return actual


def main(output):
    here = Path(__file__).resolve().parent
    guide = (here / "restore.md").read_text()
    identity = json.loads((here / "identity.json").read_text())
    output.mkdir(parents=True, exist_ok=False)
    trial, recovery = output / "trial", output / "recovery"
    package = download(guide, "keyboard-01.zip", trial)
    if package["sha256"] != "995b4cb4af06163c92cf82150d61598e577dafbe70500b263718478b846c8de4":
        raise ValueError("Expected the keyboard-01 archive published in PCP #37")
    with zipfile.ZipFile(trial / package["filename"]) as archive:
        if archive.testzip() or sorted(archive.namelist()) != ["candidate.iso", "kernel.elf32"]:
            raise ValueError("Unexpected candidate archive contents")
        candidate = trial / "candidate.iso"
        candidate.write_bytes(archive.read("candidate.iso"))
    if verify_download(guide, candidate) != identity["candidate_iso"]:
        raise ValueError("Downloaded candidate differs from its distribution inventory")
    check(candidate, output / "candidate-wall", clock="wall",
          expected_iso=identity["candidate_iso"], expected_image=identity["candidate_image"])

    previous = download(guide, "PCP-OS.iso", recovery)
    if previous["sha256"] != ISO_SHA or identity["released_iso"] != ISO_SHA:
        raise ValueError("Recovery did not obtain the preceding public CD")
    iso = recovery / previous["filename"]
    check(iso, output / "previous-instructions", clock="instructions")
    try:
        check(iso, output / "previous-wall", clock="wall")
        wall = "launcher, playback, Stop, return and power-off"
    except GuestSafe:
        wall = "SAFE during startup"
    receipt = {"candidate_download": package, "candidate_iso_sha256": identity["candidate_iso"],
               "candidate_measured_image": identity["candidate_image"], "previous_download": previous,
               "previous_measured_image": IMAGE_SHA, "previous_ordinary_clock": wall}
    (output / "rollback.json").write_text(json.dumps(receipt, indent=2) + "\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path, help="a new directory")
    main(parser.parse_args().output.resolve())
