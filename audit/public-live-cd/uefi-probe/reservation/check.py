"""Test the released ELF's full physical reservation and a firmware-selected reservation in OVMF."""
import argparse
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from inventory import KERNEL_SHA, SOURCE_SHA, digest, load_ranges

PAGE = 4096
EFI_NOT_FOUND = (1 << 63) | 14


def footprint(elf):
    ranges = sorted((start // PAGE, (end + PAGE - 1) // PAGE) for start, end in load_ranges(elf))
    first, last = ranges[0]
    for start, end in ranges[1:]:
        if start > last:
            raise ValueError("The pinned ELF no longer has one contiguous page footprint")
        last = max(last, end)
    return first * PAGE, last - first


def make_probe(iso, work):
    kernel = work / "kernel.elf32"
    if digest(iso) != SOURCE_SHA:
        raise ValueError("Unexpected source ISO")
    subprocess.run(["xorriso", "-osirrox", "on", "-indev", iso, "-extract", "/kernel.elf32", kernel], check=True)
    if digest(kernel) != KERNEL_SHA:
        raise ValueError("Unexpected kernel ELF")
    base, pages = footprint(kernel.read_bytes())
    (work / "footprint.h").write_text(f"#define KERNEL_BASE {base}ULL\n#define KERNEL_PAGES {pages}UL\n")
    source = Path(__file__).resolve().with_name("reserve.c")
    def run(*args):
        subprocess.run(args, cwd=work, check=True)
    run("gcc", "-Wall", "-Wextra", "-Werror", "-DEFI_FUNCTION_WRAPPER", "-fpic", "-fshort-wchar",
        "-fno-stack-protector", "-mno-red-zone", "-I/usr/include/efi", "-I/usr/include/efi/x86_64",
        "-I.", "-c", source, "-o", "reserve.o")
    run("ld", "-nostdlib", "-znocombreloc", "-T", "/usr/lib/elf_x86_64_efi.lds", "-shared",
        "-Bsymbolic", "/usr/lib/crt0-efi-x86_64.o", "reserve.o", "-L/usr/lib", "-lefi", "-lgnuefi",
        "-o", "reserve.so")
    run("objcopy", "-j", ".text", "-j", ".sdata", "-j", ".data", "-j", ".dynamic", "-j", ".dynsym",
        "-j", ".rel", "-j", ".rela", "-j", ".reloc", "--target=efi-app-x86_64", "reserve.so", "BOOTX64.EFI")
    cd = work / "cd"
    cd.mkdir()
    esp = cd / "efi.img"
    with esp.open("wb") as disk:
        disk.truncate(8 << 20)
    run("mkfs.vfat", esp)
    run("mmd", "-i", esp, "::/EFI", "::/EFI/BOOT")
    run("mcopy", "-i", esp, "BOOTX64.EFI", "::/EFI/BOOT/")
    run("xorriso", "-as", "mkisofs", "-quiet", "-eltorito-alt-boot", "-e", "efi.img",
        "-no-emul-boot", "-o", "reserve.iso", cd)
    return work / "reserve.iso", base, pages


def observe(cd, base, pages, ram, work, out):
    code = Path("/usr/share/OVMF/OVMF_CODE_4M.fd")
    template = Path("/usr/share/OVMF/OVMF_VARS_4M.fd")
    variables = work / f"vars-{ram}.fd"
    shutil.copyfile(template, variables)
    trace = out / f"firmware-{ram}.txt"
    cmd = ["qemu-system-x86_64", "-machine", "q35", "-accel", "tcg", "-cpu", "max", "-m", str(ram),
           "-smp", "1", "-nic", "none", "-display", "none", "-monitor", "none", "-serial", "none",
           "-debugcon", "file:" + str(trace), "-global", "isa-debugcon.iobase=0xe9",
           "-drive", f"if=pflash,unit=0,format=raw,readonly=on,file={code}",
           "-drive", f"if=pflash,unit=1,format=raw,file={variables}", "-boot", "order=d,strict=on",
           "-cdrom", str(cd), "-no-reboot"]
    (out / f"command-{ram}.json").write_text(json.dumps(cmd, indent=2) + "\n")
    with (out / f"stderr-{ram}.txt").open("wb") as err:
        subprocess.run(cmd, stderr=err, timeout=90, check=True)
    values = {}
    for line in trace.read_text().splitlines():
        name, value = line.split("=")
        if name in values or len(value) != 16:
            raise ValueError("Invalid or repeated firmware status")
        values[name] = int(value, 16)
    chosen = values.get("chosen_base", -1)
    expected = dict(fixed_base=base, pages=pages, fixed_status=EFI_NOT_FOUND, chosen_status=0,
                    chosen_base=chosen, occupied_status=EFI_NOT_FOUND, chosen_free=0,
                    reacquire_status=0, reacquire_free=0, done=1)
    if values != expected or chosen < 0 or chosen % PAGE or chosen + pages * PAGE > 1 << 30:
        raise ValueError(f"Unexpected firmware result for {ram} MiB: {values}")
    return {"ram_mib": ram, "statuses": values, "code_sha256": digest(code), "vars_sha256": digest(template)}


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("iso", type=Path)
    p.add_argument("out", type=Path)
    args = p.parse_args()
    out = args.out.resolve()
    out.mkdir(parents=True, exist_ok=False)
    (out / "versions.txt").write_text(subprocess.check_output(
        ["dpkg-query", "-W", "gnu-efi", "ovmf", "qemu-system-x86", "xorriso", "gcc", "binutils"], text=True))
    with tempfile.TemporaryDirectory() as temp:
        work = Path(temp)
        cd, base, pages = make_probe(args.iso.resolve(), work)
        observations = [observe(cd, base, pages, ram, work, out) for ram in (128, 256)]
        report = {"iso_sha256": SOURCE_SHA, "kernel_sha256": KERNEL_SHA,
                  "probe_sha256": digest(work / "BOOTX64.EFI"), "diagnostic_cd_sha256": digest(cd),
                  "observations": observations}
        (out / "results.json").write_text(json.dumps(report, indent=2) + "\n")
