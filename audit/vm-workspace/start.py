"""Create a private PCP OS data volume or boot the packaged VM with an existing volume."""
import argparse
from hashlib import sha256
import json
from pathlib import Path
import re
import shutil
import stat
import subprocess

from create import create

HERE = Path(__file__).resolve().parent
BOOT_FILES = ("kernel.elf", "surf.elf", "clip.ppm", "clip.wav", "rdesk.elf")


def verified_payload(directory):
    info = json.loads((directory / "build.json").read_text(encoding="utf-8"))
    for name in BOOT_FILES:
        if sha256((directory / name).read_bytes()).hexdigest() != info["files"][name]:
            raise ValueError(f"The packaged {name} differs from its build receipt")
    if not re.fullmatch(r"[0-9a-f]{64}", info["kernel_measurement"]):
        raise ValueError("Invalid kernel measurement")
    return info


def disk_identity(directory):
    disk = directory / "data.raw"
    if disk.is_symlink() or not stat.S_ISREG(disk.stat().st_mode) or disk.stat().st_size != 259 * 512:
        raise ValueError("Expected the provisioned 132,608-byte regular data file")
    volume_id = (directory / "volume-id.txt").read_text(encoding="ascii").strip()
    if not re.fullmatch(r"[0-9a-f]{32}", volume_id) or int(volume_id, 16) == 0:
        raise ValueError("Invalid VM volume ID")
    with disk.open("rb") as source:
        header = source.read(512)
    marker = bytearray(512)
    prefix = b"PCPOS USER STORE 2\n"
    marker[:len(prefix)] = prefix
    marker[32:48] = bytes.fromhex(volume_id)
    if header != marker:
        raise ValueError("The data file and volume ID do not match")
    return disk.resolve(), volume_id


def command(package, volume, emulator):
    info = verified_payload(package)
    disk, identity = disk_identity(volume)
    # A JSON block backend keeps punctuation in an ordinary filesystem path literal.
    backend = json.dumps({"driver": "file", "node-name": "userdata", "filename": str(disk)})
    return [emulator, "-machine", "pc", "-accel", "tcg", "-cpu", "qemu64", "-m", "128M", "-smp", "1",
            "-nic", "none", "-vga", "std", "-audiodev", "none,id=snd", "-device", "AC97,audiodev=snd",
            "-kernel", BOOT_FILES[0], "-initrd", ",".join(BOOT_FILES[1:]),
            "-append", f"store=ide0 store_id={identity} image={info['kernel_measurement']}",
            "-blockdev", backend, "-blockdev", "driver=raw,node-name=store,file=userdata",
            "-device", "ide-hd,drive=store,bus=ide.0,unit=0,serial=PCP-VM-STORE"]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="action", required=True)
    init = sub.add_parser("init", help="create a new data folder")
    init.add_argument("volume", type=Path)
    boot = sub.add_parser("run", help="open the VM with an existing data folder")
    boot.add_argument("volume", type=Path)
    boot.add_argument("--qemu", default="qemu-system-x86_64")
    args = parser.parse_args()
    if args.action == "init":
        create(args.volume)
        print(f"Created {args.volume}")
        return 0
    emulator = shutil.which(args.qemu)
    if not emulator:
        parser.error("QEMU x86 system emulator was not found")
    return subprocess.run(command(HERE, args.volume, emulator), cwd=HERE).returncode


if __name__ == "__main__":
    raise SystemExit(main())
