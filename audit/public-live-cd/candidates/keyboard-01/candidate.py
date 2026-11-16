"""Build or inspect the keyboard-01 BIOS CD and exercise one QEMU clock per run."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import struct
import subprocess
import sys
import tempfile
import time
import zipfile

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from check import check, ISO_SHA, IMAGE_SHA
from check_audio import check_audio
from check_video import check_video

OS_COMMIT = "946ef854d908c9beb37436cf3f37284a2ad86610"
ORIGINAL_KERNEL = "d2fae4ef3df316ff4fa0c1a88744e66cc17bd794856979fa55188b8402f7222f"
BUNDLE = "keyboard-01.zip"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition, message):
    if not condition:
        raise ValueError(message)


def extract(iso, directory):
    subprocess.run(["xorriso", "-osirrox", "on", "-indev", iso, "-extract", "/", directory], check=True)


def measure(kernel_tools, elf):
    return subprocess.check_output([sys.executable, kernel_tools / "measure.py", elf], text=True).strip()


def check_boot_table(iso, boot):
    # Inspect the address fields and checksum xorriso updates when it replays the BIOS boot image.
    raw = iso.read_bytes()
    pvd, lba, length, checksum = struct.unpack_from("<4I", boot, 8)
    require(raw[pvd*2048:pvd*2048+7] == b"\x01CD001\x01", "Invalid volume descriptor address")
    require(length == len(boot) and raw[lba*2048:lba*2048+length] == boot, "Invalid boot extent")
    data = boot[64:] + bytes(-len(boot[64:]) % 4)
    require(sum(word for word, in struct.iter_unpack("<I", data)) % 2**32 == checksum,
            "Invalid boot info checksum")
    return lba


def inspect_catalog(iso, catalog, boot_lba):
    # El Torito validation entry and default x86 no-emulation boot entry.
    require(len(catalog) >= 64 and catalog[0:2] == b"\x01\x00" and
            catalog[30:32] == b"\x55\xaa" and sum(struct.unpack("<16H", catalog[:32])) % 65536 == 0,
            "Invalid El Torito validation entry")
    require(catalog[32:34] == b"\x88\x00" and struct.unpack_from("<I", catalog, 40)[0] == boot_lba,
            "Invalid BIOS boot catalog entry")
    raw = iso.read_bytes()
    for off in range(16*2048, len(raw), 2048):
        descriptor = raw[off:off+2048]
        if descriptor[:7] == b"\x00CD001\x01" and b"EL TORITO SPECIFICATION" in descriptor[7:39]:
            catalog_lba = struct.unpack_from("<I", descriptor, 71)[0]
            require(raw[catalog_lba*2048:catalog_lba*2048+len(catalog)] == catalog,
                    "Boot record points to a different catalog")
            return
        if descriptor[:7] == b"\xffCD001\x01":
            break
    raise ValueError("El Torito boot record missing")


def build_epoch(os_source):
    value = os.environ.get("SOURCE_DATE_EPOCH")
    if value is None:
        value = subprocess.check_output(["git", "-C", os_source, "show", "-s", "--format=%ct", OS_COMMIT],
                                        text=True).strip()
    require(re.fullmatch(r"[0-9]+", value), "Expected integer seconds in SOURCE_DATE_EPOCH")
    epoch = int(value)
    require(epoch <= 4354819199, "Build date exceeds the ZIP timestamp range (2107)")
    return epoch


def prepare(distribution, os_source, out, retained):
    require(digest(distribution) == ISO_SHA, "Unexpected public CD")
    actual = subprocess.check_output(["git", "-C", os_source, "rev-parse", "HEAD"], text=True).strip()
    require(actual == OS_COMMIT, "Unexpected PCP OS source revision")
    kernel = os_source / "PCP_OS_Rust/crates/pcpos-kernel"
    out.mkdir(parents=True, exist_ok=True)
    iso, elf = out / "candidate.iso", out / "kernel.elf32"
    tools = kernel / "tools"
    with tempfile.TemporaryDirectory() as tmp:
        work = Path(tmp)
        original, candidate = work / "original", work / "candidate"
        extract(distribution, original)
        require(digest(original / "kernel.elf32") == ORIGINAL_KERNEL and
                measure(tools, original / "kernel.elf32") == IMAGE_SHA, "Unexpected original kernel")
        if retained:
            with zipfile.ZipFile(retained) as archive:
                require(sorted(archive.namelist()) == ["candidate.iso", "kernel.elf32"], "Unexpected bundle")
                for target in (elf, iso):
                    target.write_bytes(archive.read(target.name))
        else:
            elf.write_bytes((kernel / "target/pcpos-kernel.elf32").read_bytes())
        image = measure(tools, elf)
        require(re.fullmatch(r"[a-f0-9]{64}", image) and image != IMAGE_SHA, "Expected a new measured image")
        old = (original / "limine.conf").read_bytes()
        key = ("image=" + IMAGE_SHA).encode("ascii")
        require(old.count(key) == 1, "Expected one measured-image grant")
        config = work / "limine.conf"
        config.write_bytes(old.replace(key, ("image=" + image).encode("ascii")))
        if not retained:
            require(not iso.exists(), "Use a fresh output directory for a new candidate")
            epoch = build_epoch(os_source)
            volume_date = time.strftime("%Y%m%d%H%M%S00", time.gmtime(epoch))
            environment = dict(os.environ, SOURCE_DATE_EPOCH=str(epoch), TZ="UTC")
            subprocess.run(["xorriso", "-no_rc", "-indev", distribution, "-outdev", iso,
                            "-map", elf, "/kernel.elf32", "-map", config, "/limine.conf",
                            "-chown", "0", "/kernel.elf32", "/limine.conf", "--",
                            "-chgrp", "0", "/kernel.elf32", "/limine.conf", "--",
                            "-chmod", "0644", "/kernel.elf32", "/limine.conf", "--",
                            "-boot_image", "any", "replay", "-volume_date", "uuid", volume_date,
                            "-volume_date", "all_file_dates", f"={epoch}", "-commit"], check=True, env=environment)
            # ECMA-119 primary volume descriptor on this pinned BIOS layout, sector 16.
            with iso.open("rb") as stream:
                stream.seek(16 * 2048)
                descriptor = stream.read(2048)
            expected_date = volume_date.encode("ascii") + b"\x00"
            require(descriptor[:7] == b"\x01CD001\x01" and
                    descriptor[813:830] == descriptor[830:847] == expected_date,
                    "Rebuilt volume creation or modification time differs from the requested epoch")
        extract(iso, candidate)
        files = lambda directory: {p.relative_to(directory).as_posix() for p in directory.rglob("*") if p.is_file()}
        require(files(original) == files(candidate), "CD file sets differ")
        require((candidate / "kernel.elf32").read_bytes() == elf.read_bytes(), "CD kernel differs from built ELF")
        require((candidate / "limine.conf").read_bytes() == config.read_bytes(), "Unexpected boot grant")
        bootname = "limine-bios-cd.bin"
        boots = [(directory / bootname).read_bytes() for directory in (original, candidate)]
        require(boots[0][:8] == boots[1][:8] and boots[0][24:] == boots[1][24:], "Boot code changed")
        for optical, directory, boot in zip((distribution, iso), (original, candidate), boots):
            lba = check_boot_table(optical, boot)
            inspect_catalog(optical, (directory / "boot.cat").read_bytes(), lba)
        entries = {}
        for name in sorted(files(original)):
            before, after = digest(original / name), digest(candidate / name)
            if name not in {"kernel.elf32", "limine.conf", "boot.cat", bootname}:
                require(before == after, f"Carried file differs: {name}")
            entries[name] = {"released": before, "candidate": after}
    identities = {"source_commit": OS_COMMIT, "released_iso": ISO_SHA, "released_image": IMAGE_SHA,
                  "candidate_iso": digest(iso), "candidate_image": image, "files": entries}
    if retained:
        pins = json.loads(retained.with_name("identity.json").read_text())
        require(identities == pins, "Retained CD or kernel differs from the versioned pins")
    else:
        # ZIP stores UTC here by convention, at two-second resolution, starting in 1980.
        timestamp = time.gmtime(max(epoch, 315532800))[:6]
        with zipfile.ZipFile(out / BUNDLE, "w") as archive:
            for target in (iso, elf):
                entry = zipfile.ZipInfo(target.name, timestamp)
                entry.create_system = 3
                entry.external_attr = 0o100644 << 16
                archive.writestr(entry, target.read_bytes(), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
    (out / "identity.json").write_text(json.dumps(identities, indent=2) + "\n")


def exercise_clock(os_source, out, clock):
    identities = json.loads((out / "identity.json").read_text())
    evidence = out / clock
    check(out / "candidate.iso", evidence, clock=clock, capture_audio=True, capture_video=True,
          expected_iso=identities["candidate_iso"], expected_image=identities["candidate_image"])
    serial = (evidence / "serial.txt").read_text()
    frames = [int(n) for n in re.findall(r"^SURFBIRD media-frame (\d+)$", serial, re.M)]
    require(frames == list(range(32)), "Expected all 32 media frames in order")
    verifier = os_source / "apps/surfbird/guest/replay_local_media.py"
    for verify in (check_audio, check_video):
        verify(out / "candidate.iso", evidence, verifier, expected_iso=identities["candidate_iso"])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("build", "inspect", "wall", "instructions"))
    parser.add_argument("distribution", type=Path)
    parser.add_argument("os_source", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    if args.action in {"wall", "instructions"}:
        exercise_clock(args.os_source.resolve(), args.output.resolve(), args.action)
    else:
        bundle = Path(__file__).with_name(BUNDLE) if args.action == "inspect" else None
        prepare(args.distribution.resolve(), args.os_source.resolve(), args.output.resolve(), bundle)
