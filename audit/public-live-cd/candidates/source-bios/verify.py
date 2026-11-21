"""Verify this tester package. Optionally write its verified ISO to a new file."""
import argparse
import hashlib
import json
from pathlib import Path
import zipfile

HERE = Path(__file__).resolve().parent
ZIP_SHA256 = "936f8366a714cb5d57b129f801d29caf1679f171860744ebf82cb3feb9b4e71b"
ISO_SHA256 = "f904f393c9332c32ea5de8d73c5d81762717c6c31166708d6ce9ffdaa63e6f96"
MEASUREMENT = "4732843ca93272f5b553a0ba7a6fb89a96f4672044edc686d4518567651e5bf4"


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
