"""Boot the published ISO on a desktop host with only a virtual optical disc."""
import argparse
import asyncio
import hashlib
import json
from pathlib import Path
import platform
import shutil
import subprocess
import sys
import tempfile
import zipfile

from check import IMAGE_SHA, ISO_SHA

COMBINED_ZIP = "ba95de848dea3aacd2c95cfca7018c4fcd38dc859d5e0c05ad961cebf17b2174"
COMBINED_ISO = "5264e891b70a37d66541393e1fc0b135fd301b8e2097022e9b698aacdc5b3d8d"
COMBINED_KERNEL = "a9be6b1599bb10eead1344ae4a2ca53ec978074ae9aef1d30e8da10f04d044f3"


# RGB pixels in the complete "Verified at start: all 71 self-tests passed." row
# of the released CD's 1024 x 768 launcher, excluding the changing register head.
VERIFIED_ROW_SHA256 = "100fc821e22cf5bda99d4f96cf1d4d442deb15cd3f3a2869cc30e5e7cc33971c"


def verified_row(ppm):
    header = b"P6\n1024 768\n255\n"
    if not ppm.startswith(header) or len(ppm) != len(header) + 1024 * 768 * 3:
        return False
    pixels = memoryview(ppm)[len(header):]
    digest = hashlib.sha256()
    for y in range(98, 120):
        digest.update(pixels[(y * 1024 + 180) * 3:(y * 1024 + 642) * 3])
    return digest.hexdigest() == VERIFIED_ROW_SHA256


async def read_qmp(guest):
    line = await guest.stdout.readline()
    if not line:
        raise RuntimeError("QEMU closed the monitor early; inspect qemu-stderr.txt")
    return json.loads(line)


async def exercise(guest, output, iso, evidence, expected_kernel):
    if "QMP" not in await read_qmp(guest):
        raise RuntimeError("Expected a QMP greeting")
    events = []

    async def rpc(command, **arguments):
        request = json.dumps({"execute": command, "arguments": arguments})
        guest.stdin.write((request + "\n").encode())
        await guest.stdin.drain()
        while True:
            reply = await read_qmp(guest)
            if "error" in reply:
                raise RuntimeError(f"{command}: {reply['error']}")
            if "event" in reply:
                events.append(reply)
            if "return" in reply:
                return reply["return"]

    await rpc("qmp_capabilities")
    inserted = [d["inserted"] for d in await rpc("query-block") if "inserted" in d]
    evidence["inserted_media"] = inserted
    if len(inserted) != 1 or not inserted[0]["ro"] or Path(inserted[0]["file"]).resolve() != iso:
        raise RuntimeError("Expected exactly one inserted read-only image matching the selected ISO")

    serial = output / "serial.txt"
    frame = output / "launcher.ppm"
    while True:
        log = serial.read_text(errors="replace") if serial.exists() else ""
        if "it is in SAFE" in log:
            raise RuntimeError("Guest reported SAFE; inspect serial.txt")
        if "leaves no memory behind" in log:
            await rpc("screendump", filename=str(frame))
            if verified_row(frame.read_bytes()):
                break
        await asyncio.sleep(0.2)

    evidence["startup_pass_lines"] = sum(line.startswith("  pass ") for line in log.splitlines())
    if evidence["startup_pass_lines"] != 71 or expected_kernel + " (measured; equal" not in log:
        raise RuntimeError("Unexpected startup checks or kernel measurement")
    evidence["verified_row_sha256"] = VERIFIED_ROW_SHA256

    await rpc("send-key", keys=[{"type": "qcode", "data": "p"}], **{"hold-time": 80})
    while not any(e.get("event") == "SHUTDOWN" for e in events):
        events.append(await read_qmp(guest))
    shutdown = next(e["data"] for e in events if e.get("event") == "SHUTDOWN")
    evidence["shutdown"] = shutdown
    evidence["exit_code"] = await guest.wait()
    if shutdown != {"guest": True, "reason": "guest-shutdown"} or guest.returncode != 0:
        raise RuntimeError("Expected guest-requested shutdown and QEMU exit 0")
    if "ALL SELF-TESTS PASS." not in serial.read_text(errors="replace"):
        raise RuntimeError("Missing the guest's final self-test result")


async def main(iso, output, emulator, *, combined=False):
    iso = iso.resolve(strict=True)
    actual = hashlib.sha256(iso.read_bytes()).hexdigest()
    expected_iso, expected_kernel = (COMBINED_ISO, COMBINED_KERNEL) if combined else (ISO_SHA, IMAGE_SHA)
    if actual != expected_iso:
        raise ValueError(f"Distributed ISO digest mismatch: {actual}")
    output = output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    args = [emulator, "-machine", "pc", "-accel", "tcg", "-cpu", "qemu64",
            "-m", "64M", "-boot", "order=d", "-cdrom", str(iso), "-vga", "std",
            "-nic", "none", "-audiodev",
            "none,id=snd0", "-device", "AC97,audiodev=snd0", "-display", "none",
            "-monitor", "none", "-qmp", "stdio", "-serial", "file:serial.txt"]
    if not combined:
        args.extend(["-icount", "shift=3,align=off,sleep=off"])
    evidence = {"clock": "ordinary" if combined else "instruction-counted",
                "expected_kernel_sha256": expected_kernel, "host": platform.platform(), "host_architecture": platform.machine(),
                "iso_sha256": actual, "argv": args, "qemu_version":
                subprocess.check_output([emulator, "--version"], text=True).splitlines()[0]}
    if combined:
        evidence["source_zip_sha256"] = COMBINED_ZIP
    with (output / "qemu-stderr.txt").open("wb") as err:
        guest = await asyncio.create_subprocess_exec(
            *args, cwd=output, stdin=asyncio.subprocess.PIPE,
            stdout=asyncio.subprocess.PIPE, stderr=err)
        try:
            await asyncio.wait_for(exercise(guest, output, iso, evidence, expected_kernel), timeout=120)
        finally:
            if guest.returncode is None:
                guest.kill()
                await guest.wait()
            (output / "result.json").write_text(json.dumps(evidence, indent=2) + "\n")
    print(json.dumps(evidence, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("media", type=Path, help="published ISO, or the pinned opt-in ZIP with --combined-zip")
    parser.add_argument("--combined-zip", action="store_true", help="boot the combined BIOS tester archive on the ordinary clock")
    parser.add_argument("output", type=Path, help="new directory for serial, framebuffer and result")
    parser.add_argument("--qemu", default="qemu-system-x86_64")
    args = parser.parse_args()
    emulator = shutil.which(args.qemu)
    if not emulator:
        sys.exit("QEMU x86 system emulator was not found")
    emulator = str(Path(emulator).resolve())
    if args.combined_zip:
        if hashlib.sha256(args.media.read_bytes()).hexdigest() != COMBINED_ZIP:
            parser.error("Unexpected combined tester archive SHA-256")
        with tempfile.TemporaryDirectory() as temp, zipfile.ZipFile(args.media) as archive:
            name = "no-write-candidate.iso"
            if archive.namelist() != [name] or archive.getinfo(name).file_size != 2293760:
                parser.error("Unexpected combined tester archive inventory")
            iso = Path(temp, name)
            iso.write_bytes(archive.read(name))
            asyncio.run(main(iso, args.output, emulator, combined=True))
    else:
        asyncio.run(main(args.media, args.output, emulator))
