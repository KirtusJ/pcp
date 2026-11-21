"""Boot a pinned PCP BIOS image on a desktop host with only a virtual optical disc."""
import argparse
import asyncio
import hashlib
import json
from pathlib import Path
import platform
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile

from check import IMAGE_SHA, ISO_SHA
from desktop_screens import DesktopScreens

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


async def exercise(guest, output, iso, evidence, expected_kernel, screens):
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
    async def wait_screen(name, matches):
        path = output / (name + ".ppm")
        while True:
            log = serial.read_text(errors="replace") if serial.exists() else ""
            if "it is in SAFE" in log:
                raise RuntimeError("Guest reported SAFE; inspect serial.txt")
            if "leaves no memory behind" in log:
                await rpc("screendump", filename=str(path))
                if matches(path.read_bytes()):
                    return log
            await asyncio.sleep(0.2)

    async def key(code):
        await rpc("send-key", keys=[{"type": "qcode", "data": code}], **{"hold-time": 80})

    if screens is None:
        log = await wait_screen("launcher", verified_row)
        evidence["verified_row_sha256"] = VERIFIED_ROW_SHA256
    else:
        log = await wait_screen("home", lambda frame: screens.matches(frame, "home"))
        evidence["home_form"] = screens.home_form
        hashes = evidence["screen_sha256"] = {"home": hashlib.sha256((output / "home.ppm").read_bytes()).hexdigest()}

        async def capture(name, expected):
            await wait_screen(name, lambda frame: screens.matches(frame, expected))
            hashes[name] = hashlib.sha256((output / (name + ".ppm")).read_bytes()).hexdigest()
            return hashes[name]

        if screens.has_verification_page:
            await key(screens.verification_key)
            await capture("verification", "verification")
            await key("esc")
            await capture("home-after-verification", "home")
        await key("spc")
        await capture("launcher", "surf.elf")
        if screens.confirm_power:
            selected = "surf.elf"
            before = hashes["launcher"]
            if "rdesk.elf" in screens.program_hashes:
                await key("down")
                selected = "rdesk.elf"
                before = await capture("queue-selected", selected)
            await screens.cancel_power(key, capture, "launcher", selected, before)
        await key("esc")
        await capture("home-after-escape", "home")
        if screens.confirm_power:
            await screens.cancel_power(key, capture, "home", "home", hashes["home"])
        if any(value != hashes["home"] for name, value in hashes.items() if name.startswith("home-after-")):
            raise ValueError("Returning to the desktop changed the initial Home frame")

    evidence["startup_pass_lines"] = sum(line.startswith("  pass ") for line in log.splitlines())
    if evidence["startup_pass_lines"] != 71 or expected_kernel + " (measured; equal" not in log:
        raise RuntimeError("Unexpected startup checks or kernel measurement")

    if screens is not None and screens.confirm_power:
        await key("f10")
        await capture("confirm-shutdown", "power")
        await key("ret")
    else:
        await key("p")
    while not any(e.get("event") == "SHUTDOWN" for e in events):
        events.append(await read_qmp(guest))
    shutdown = next(e["data"] for e in events if e.get("event") == "SHUTDOWN")
    evidence["shutdown"] = shutdown
    evidence["exit_code"] = await guest.wait()
    if shutdown != {"guest": True, "reason": "guest-shutdown"} or guest.returncode != 0:
        raise RuntimeError("Expected guest-requested shutdown and QEMU exit 0")
    if "ALL SELF-TESTS PASS." not in serial.read_text(errors="replace"):
        raise RuntimeError("Missing the guest's final self-test result")


def digest_arg(value):
    if re.fullmatch(r"[0-9a-f]{64}", value):
        return value
    raise argparse.ArgumentTypeError("expected 64 lowercase hexadecimal digits")


async def main(iso, output, emulator, *, combined=False, source_build=None, desktop_build=None):
    iso = iso.resolve(strict=True)
    actual = hashlib.sha256(iso.read_bytes()).hexdigest()
    expected_iso, expected_kernel = (COMBINED_ISO, COMBINED_KERNEL) if combined else (ISO_SHA, IMAGE_SHA)
    if source_build is not None:
        if combined:
            raise ValueError("Choose one image profile")
        expected_iso, expected_kernel = source_build
    screens = None
    if desktop_build is not None:
        source, receipt_path = desktop_build
        receipt_bytes = receipt_path.read_bytes()
        receipt = json.loads(receipt_bytes)
        revision, tree = subprocess.check_output(
            ["git", "-C", source, "rev-parse", "HEAD", "HEAD^{tree}"], text=True).splitlines()
        if (receipt["format"] != "pcp-os-tester-cd/1" or receipt["uncommitted_changes"] is not False
                or (receipt["source_commit"], receipt["source_tree"]) != (revision, tree)):
            raise ValueError("Desktop build receipt differs from the source checkout")
        expected_iso, expected_kernel = digest_arg(receipt["iso_sha256"]), digest_arg(receipt["kernel_measurement"])
        program_hashes = {name: digest_arg(entry["sha256"]) for name, entry in receipt["on_disc"].items()
                          if name.endswith(".elf")}
        screens = DesktopScreens(source, program_hashes)
    ordinary_clock = combined or source_build is not None or desktop_build is not None
    if actual != expected_iso:
        raise ValueError(f"ISO digest mismatch: {actual}")
    output = output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    args = [emulator, "-machine", "pc", "-accel", "tcg", "-cpu", "qemu64",
            "-m", "64M", "-boot", "order=d", "-cdrom", str(iso), "-vga", "std",
            "-nic", "none", "-audiodev",
            "none,id=snd0", "-device", "AC97,audiodev=snd0", "-display", "none",
            "-monitor", "none", "-qmp", "stdio", "-serial", "file:serial.txt"]
    if not ordinary_clock:
        args.extend(["-icount", "shift=3,align=off,sleep=off"])
    evidence = {"clock": "ordinary" if ordinary_clock else "instruction-counted",
                "expected_kernel_sha256": expected_kernel, "host": platform.platform(), "host_architecture": platform.machine(),
                "iso_sha256": actual, "argv": args, "qemu_version":
                subprocess.check_output([emulator, "--version"], text=True).splitlines()[0]}
    if desktop_build is not None:
        evidence.update(source_commit=revision, source_tree=tree, receipt_sha256=hashlib.sha256(receipt_bytes).hexdigest())
    if combined:
        evidence["source_zip_sha256"] = COMBINED_ZIP
    with (output / "qemu-stderr.txt").open("wb") as err:
        guest = await asyncio.create_subprocess_exec(
            *args, cwd=output, stdin=asyncio.subprocess.PIPE,
            stdout=asyncio.subprocess.PIPE, stderr=err)
        try:
            await asyncio.wait_for(exercise(guest, output, iso, evidence, expected_kernel, screens), timeout=120)
        finally:
            if guest.returncode is None:
                guest.kill()
                await guest.wait()
            (output / "result.json").write_text(json.dumps(evidence, indent=2) + "\n")
    print(json.dumps(evidence, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("media", type=Path, help="ISO to boot, or the pinned opt-in ZIP with --combined-zip")
    profile = parser.add_mutually_exclusive_group()
    profile.add_argument("--source-build", nargs=2, type=digest_arg, metavar=("ISO_SHA256", "KERNEL_MEASUREMENT"),
                         help="boot a source-built BIOS ISO on the ordinary clock using both independently obtained digests")
    profile.add_argument("--desktop-build", nargs=2, type=Path, metavar=("PCP_OS_SOURCE", "BUILD_RECEIPT"),
                         help="exercise the graphical Home / launcher round trip on a source-built ISO with its matching checkout and receipt")
    profile.add_argument("--combined-zip", action="store_true", help="boot the combined BIOS tester archive on the ordinary clock")
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
        asyncio.run(main(args.media, args.output, emulator, source_build=args.source_build, desktop_build=args.desktop_build))
