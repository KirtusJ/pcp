"""Check the released kernel's fixed ELF load ranges against a live GRUB/OVMF memory inventory."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import struct
import subprocess
import tempfile
import time

SOURCE_SHA = "93ed3b599ad7be0e1e88a64813b1f2b5299d51507df2edca691aaf6189d10d15"
KERNEL_SHA = "d2fae4ef3df316ff4fa0c1a88744e66cc17bd794856979fa55188b8402f7222f"
BEGIN = "PCP-PREBOOT-MEMORY-MAP-BEGIN"
END = "PCP-PREBOOT-MEMORY-MAP-END"
RECORD = re.compile(r"base_addr = (0x[\da-fA-F]+), length = (0x[\da-fA-F]+), (.+)")


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_ranges(elf):
    if elf[:6] != b"\x7fELF\x01\x01" or len(elf) < 52:
        raise ValueError("Expected a little-endian ELF32 image")
    kind, machine = struct.unpack_from("<HH", elf, 16)
    offset, = struct.unpack_from("<I", elf, 28)
    size, count = struct.unpack_from("<HH", elf, 42)
    if (kind, machine) != (2, 3) or size != 32 or not count or offset + size * count > len(elf):
        raise ValueError("Unexpected i386 executable program headers")
    segments = []
    for i in range(count):
        kind, pos, _, physical, file_size, memory_size, _, _ = struct.unpack_from("<8I", elf, offset + i * size)
        if kind == 1 and memory_size:
            if file_size > memory_size or pos + file_size > len(elf) or physical + memory_size > 1 << 32:
                raise ValueError("Invalid ELF load segment")
            segments.append((physical, physical + memory_size))
    if not segments:
        raise ValueError("ELF has no loadable memory")
    return segments


def memory_ranges(serial):
    begin = serial.index(BEGIN)
    end = serial.index(END, begin + len(BEGIN))
    ranges = set()
    for line in serial[begin + len(BEGIN):end].splitlines():
        line = line.strip()
        if not line or line == BEGIN:
            continue
        match = RECORD.fullmatch(line)
        if not match:
            raise ValueError(f"Unparsed GRUB memory record: {line!r}")
        base, length = (int(value, 16) for value in match.groups()[:2])
        if length:
            ranges.add((base, base + length, match[3]))
    if not ranges:
        raise ValueError("GRUB returned an empty memory map")
    return sorted(ranges)


def conflicts(segments, memory):
    hits = []
    for start, end in segments:
        bounds = {start, end}
        for lo, hi, _ in memory:
            if lo < end and start < hi:
                bounds.update((max(start, lo), min(end, hi)))
        ordered = sorted(bounds)
        for a, b in zip(ordered, ordered[1:]):
            types = {name for lo, hi, name in memory if lo <= a and b <= hi}
            if types != {"available RAM"}:
                hits.append({"start": a, "end": b, "types": sorted(types) or ["unreported"]})
    return hits


def collect(source, out, work):
    if digest(source) != SOURCE_SHA:
        raise ValueError("Expected the published PCP-OS.iso")
    kernel = work / "kernel.elf32"
    subprocess.run(["xorriso", "-osirrox", "on", "-indev", source, "-extract", "/kernel.elf32", kernel], check=True)
    if digest(kernel) != KERNEL_SHA:
        raise ValueError("Unexpected kernel payload")
    segments = load_ranges(kernel.read_bytes())

    # The diagnostic CD contains GRUB and its inventory command. The PCP kernel stays on the host.
    root = work / "inventory-cd"
    grub = root / "boot/grub"
    grub.mkdir(parents=True)
    (grub / "grub.cfg").write_text("serial --unit=0 --speed=115200\nterminal_output serial\n"
        'echo PCP-FIRMWARE-${grub_platform}\n' + f"echo {BEGIN}\nlsmmap\necho {END}\nhalt\n")
    cd = work / "inventory.iso"
    subprocess.run(["grub-mkrescue", "-d", "/usr/lib/grub/x86_64-efi", "-o", cd, root], check=True)
    code = Path("/usr/share/OVMF/OVMF_CODE_4M.fd")
    template = Path("/usr/share/OVMF/OVMF_VARS_4M.fd")
    variables = work / "vars.fd"
    shutil.copyfile(template, variables)
    serial = out / "serial.txt"
    cmd = ["qemu-system-x86_64", "-machine", "q35", "-accel", "tcg", "-cpu", "max", "-m", "256M",
           "-smp", "1", "-vga", "std", "-nic", "none", "-display", "none", "-monitor", "none",
           "-serial", "file:" + str(serial), "-drive", f"if=pflash,unit=0,format=raw,readonly=on,file={code}",
           "-drive", f"if=pflash,unit=1,format=raw,file={variables}", "-boot", "order=d,strict=on",
           "-cdrom", str(cd), "-icount", "shift=3,align=off,sleep=off"]
    (out / "command.json").write_text(json.dumps(cmd, indent=2) + "\n")
    (out / "environment.txt").write_text(subprocess.check_output(
        ["dpkg-query", "-W", "ovmf", "grub-efi-amd64-bin", "qemu-system-x86", "xorriso"], text=True))
    with (out / "qemu-stderr.txt").open("wb") as err, subprocess.Popen(cmd, stderr=err) as vm:
        try:
            deadline = time.monotonic() + 90
            while time.monotonic() < deadline:
                log = serial.read_text(errors="replace") if serial.exists() else ""
                if END in log:
                    break
                if vm.poll() is not None:
                    raise RuntimeError("Firmware exited before finishing the inventory")
                time.sleep(0.1)
            else:
                raise TimeoutError("GRUB inventory did not finish")
        finally:
            if vm.poll() is None:
                vm.kill()
                vm.wait()
    if "PCP-FIRMWARE-efi" not in log:
        raise ValueError("Missing GRUB EFI marker")
    memory = memory_ranges(log)
    blocked = conflicts(segments, memory)
    result = {"firmware_code_sha256": digest(code), "vars_template_sha256": digest(template),
              "inventory_cd_sha256": digest(cd), "published_iso_sha256": SOURCE_SHA,
              "kernel_sha256": KERNEL_SHA, "kernel_loaded": False, "load_ranges": segments,
              "grub_map": memory, "conflicts": blocked}
    (out / "placement.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(blocked))
    if not any("ACPI non-volatile storage RAM" in row["types"] for row in blocked):
        raise RuntimeError("Expected ACPI NVS overlap changed; inspect placement.json")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("iso", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=False)
    with tempfile.TemporaryDirectory() as tmp:
        collect(args.iso.resolve(), args.output.resolve(), Path(tmp))
