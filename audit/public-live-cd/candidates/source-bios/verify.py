"""Verify this tester package. Optionally write its verified ISO to a new file."""
import argparse
import hashlib
import json
from pathlib import Path
import zipfile

HERE = Path(__file__).resolve().parent
ZIP_SHA256 = "7f5eb3d4c8057da6e16eaaf593a6181c989b129c72ff5edff00958a55b691c30"
ISO_SHA256 = "7c1cd0d0ef7959f7dd095588106ad10bb5a87db2c3a9a0b09535f1debb6e10eb"
MEASUREMENT = "82b96a61b5e949caa63abb9e262f0c7e135de443c8a8576344687aa84f2d6cde"


def verified_iso():
    package = HERE / "source-bios-tester.zip"
    if hashlib.sha256(package.read_bytes()).hexdigest() != ZIP_SHA256:
        raise ValueError("Unexpected tester ZIP digest")
    with zipfile.ZipFile(package) as archive:
        if sorted(archive.namelist()) != ["Third-party-notices.txt", "pcp-os-tester.iso", "receipt.json"]:
            raise ValueError("Unexpected tester ZIP contents")
        receipt = json.loads(archive.read("receipt.json"))
        iso = archive.read("pcp-os-tester.iso")
    if (len(iso) != receipt["iso_bytes"] or hashlib.sha256(iso).hexdigest() != ISO_SHA256
            or receipt["iso_sha256"] != ISO_SHA256 or receipt["kernel_measurement"] != MEASUREMENT):
        raise ValueError("ISO or build receipt does not match the tested image")
    return iso


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("destination", nargs="?", type=Path, help="optional new file for the verified ISO")
    args = parser.parse_args()
    data = verified_iso()
    if args.destination is not None:
        with args.destination.open("xb") as stream:
            stream.write(data)
    print(f"Verified {len(data)} ISO bytes. SHA-256 {ISO_SHA256}")
