"""Boot a packaged VM workspace twice and verify the saved request across QEMU processes."""
import argparse
import asyncio
import hashlib
import json
from pathlib import Path
import platform
import re
import runpy
import shutil
import subprocess
import sys
import tempfile
import zipfile

PAYLOAD = {"kernel.elf", "surf.elf", "clip.ppm", "clip.wav", "rdesk.elf", "start.py", "create.py",
           "build.json", "QUICKSTART.md", "notice.md", "notices.txt", "limine.txt", "Third-party-notices.txt"}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha(data):
    return hashlib.sha256(data).hexdigest()


async def observe(package, volume, out, second, start, checks, emulator, screens=None):
    out.mkdir()
    serial = out / "serial.txt"
    argv = start["command"](package, volume, emulator) + [
        "-display", "none", "-monitor", "none", "-qmp", "stdio", "-serial", "file:" + str(serial)]
    report = {"argv": argv, "host": platform.platform(), "architecture": platform.machine(),
              "qemu": subprocess.check_output([emulator, "--version"], text=True).splitlines()[0]}
    (out / "command.json").write_text(json.dumps(report, indent=2) + "\n")
    with (out / "qemu.stderr").open("wb") as err:
        proc = await asyncio.create_subprocess_exec(*argv, cwd=package, stdin=asyncio.subprocess.PIPE,
                                                     stdout=asyncio.subprocess.PIPE, stderr=err)
        async def message():
            line = await proc.stdout.readline()
            if not line:
                raise RuntimeError("QEMU monitor closed")
            return json.loads(line)

        events = []
        async def rpc(name, **arguments):
            proc.stdin.write((json.dumps(dict(execute=name, arguments=arguments)) + "\n").encode())
            await proc.stdin.drain()
            while True:
                reply = await message()
                if "return" in reply:
                    return reply["return"]
                if "error" in reply:
                    raise RuntimeError(reply["error"])
                if "event" in reply:
                    events.append(reply)

        def log():
            return serial.read_text(errors="replace") if serial.exists() else ""

        async def wait(token):
            while token not in log():
                if proc.returncode is not None or "in SAFE" in log() or "could not be mounted" in log():
                    raise RuntimeError("guest stopped before " + token)
                await asyncio.sleep(.1)

        async def key(name):
            await rpc("send-key", keys=[dict(type="qcode", data=name)], **{"hold-time": 80})
            await asyncio.sleep(.2)

        async def surface(capture_name, expected):
            capture = out / (capture_name + ".ppm")
            clock = asyncio.get_running_loop()
            deadline = clock.time() + 20
            while clock.time() < deadline:
                if proc.returncode is not None:
                    raise RuntimeError(f"guest stopped before {capture_name}")
                await rpc("screendump", filename=str(capture))
                frame = capture.read_bytes()
                if screens.matches(frame, expected):
                    digest = sha(frame)
                    report.setdefault("screen_checks", {})[capture.name] = {"surface": expected, "sha256": digest}
                    return digest
                await asyncio.sleep(.2)
            raise TimeoutError(f"{capture_name} did not show {expected}")

        async def flow():
            require("QMP" in await message(), "missing QMP greeting")
            await rpc("qmp_capabilities")
            media = [b["inserted"] for b in await rpc("query-block") if "inserted" in b]
            require(len(media) == 1 and not media[0]["ro"] and media[0]["image"]["virtual-size"] == 259*512,
                    "expected only the dedicated writable VM disk")
            await wait("VM checkpoint store mounted: " + ("1 file(s)" if second else "0 file(s)"))
            await wait("leaves no memory behind")
            await asyncio.sleep(.5)
            if screens is not None:
                await surface("home-at-start", "home")
                if screens.has_verification_page:
                    await key(screens.verification_key)
                    await surface("verification", "verification")
                    await key("esc")
                    await surface("home-after-verification", "home")
                await key("spc")
                await surface("launcher-first", "surf.elf")
                await key("esc")
                await surface("home-after-escape", "home")
                await key("spc")
                await surface("launcher-reopened", "surf.elf")
            if not second:
                await key("ret")
                await wait("SURFBIRD media ready")
                await rpc("screendump", filename=str(out / "surfbird.ppm"))
                await key("spc")
                await wait("surf.elf ended DONE: exit 0")
                playback = next(line for line in log().splitlines() if line.startswith("surf.elf ended DONE:"))
                frames = re.search(r"(\d+) frames shown", playback)
                sound = re.search(r"(\d+) ms of sound played", playback)
                require(frames and int(frames[1]) >= 32 and sound and int(sound[1]) >= 3000,
                        "incomplete local media playback: " + playback)
                await asyncio.sleep(.5)
                if screens is not None:
                    await surface("launcher-after-surfbird", "surf.elf")
            await key("down")
            if screens is not None:
                await surface("queue-selected", "rdesk.elf")
            await key("ret")
            await wait("PARROTS READY")
            active = "PARROTS QUEUE total=1 active=1 selected=1 state=ACTIVE store="
            if second:
                await wait(active + "Queue restored")
            else:
                await wait("PARROTS QUEUE total=0 active=0 selected=0 state=NONE store=New queue")
                for code in ("n", *checks["LABEL"], "ret"):
                    await key("spc" if code == " " else code)
                await wait(active + "Disk save")
            capture = out / "queue.ppm"
            await rpc("screendump", filename=str(capture))
            checks["check_frame"](capture.read_bytes(), "Queue restored" if second else "Disk save")
            await key("esc")
            await wait("rdesk.elf ended DONE: exit 0")
            await asyncio.sleep(.5)
            if screens is not None:
                selected = await surface("launcher-after-queue", "rdesk.elf")
                if screens.confirm_power:
                    await screens.cancel_power(key, surface, "launcher", "rdesk.elf", selected)
                await key("esc")
                await surface("home-before-shutdown", "home")
            if screens is not None and screens.confirm_power:
                await key("f10")
                await surface("confirm-shutdown", "power")
                await key("ret")
            else:
                await key("p")
            while not any(e.get("event") == "SHUTDOWN" for e in events):
                events.append(await message())
            require(any(e.get("data") == {"guest": True, "reason": "guest-shutdown"} for e in events),
                    "not a guest-requested shutdown")
            require(await proc.wait() == 0 and "ALL SELF-TESTS PASS." in log(), "guest exit failed")
            info = start["verified_payload"](package)
            require(info["kernel_measurement"] + " (measured; equal to the value the loader named)" in log(), "kernel measurement")
            report.update(exit_code=proc.returncode, events=events, screenshot_sha256=sha(capture.read_bytes()))
            (out / "result.json").write_text(json.dumps(report, indent=2) + "\n")
        try:
            await asyncio.wait_for(flow(), 120)
        finally:
            if proc.returncode is None:
                proc.kill()
                await proc.wait()


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for argument in ("archive", "source", "output"):
        p.add_argument(argument, type=Path)
    p.add_argument("--qemu", default="qemu-system-x86_64")
    p.add_argument("--desktop-first", action="store_true",
                   help="verify the Home and launcher screens for a desktop-first source package")
    args = p.parse_args()
    emulator = shutil.which(args.qemu)
    if not emulator:
        p.error("QEMU is required")
    out = args.output.resolve()
    out.mkdir()
    store_tests = args.source.resolve() / "examples/vm-store"
    sys.path.insert(0, str(store_tests))
    checks = runpy.run_path(str(store_tests / "check_queue.py"))
    with tempfile.TemporaryDirectory() as tmp:
        package = Path(tmp) / "workspace"
        package.mkdir()
        with zipfile.ZipFile(args.archive) as z:
            require(len(z.namelist()) == len(PAYLOAD) and set(z.namelist()) == PAYLOAD, "unexpected ZIP inventory")
            for name in PAYLOAD:
                (package / name).write_bytes(z.read(name))
        sys.path.insert(0, str(package))
        sys.modules.pop("create", None)
        starter = runpy.run_path(str(package / "start.py"))
        info = starter["verified_payload"](package)
        require(set(info["files"]) == PAYLOAD - {"build.json"}, "incomplete build receipt")
        for name, expected in info["files"].items():
            require(sha((package / name).read_bytes()) == expected, "unexpected bytes in " + name)
        for field, revision in (("source_commit", "HEAD"), ("source_tree", "HEAD^{tree}")):
            actual = subprocess.check_output(["git", "-C", args.source, "rev-parse", revision], text=True).strip()
            require(info[field] == actual, "source checkout differs from " + field)
        screens = None
        if args.desktop_first:
            reader = Path(__file__).resolve().parents[1] / "public-live-cd/desktop_screens.py"
            screens = runpy.run_path(str(reader))["DesktopScreens"](args.source.resolve(), info["files"])
        volume = Path(tmp) / "data files, one"
        init = [sys.executable, str(package / "start.py"), "init", str(volume)]
        subprocess.run(init, check=True)
        require(subprocess.run(init, capture_output=True).returncode != 0, "provisioning accepted an existing volume")
        disk = volume / "data.raw"
        before = disk.read_bytes()
        asyncio.run(observe(package, volume, out / "first", False, starter, checks, emulator, screens))
        saved = disk.read_bytes()
        require(before != saved and saved[:512] == before[:512], "save or volume marker differs")
        checks["check_journal"](saved)
        asyncio.run(observe(package, volume, out / "cold", True, starter, checks, emulator, screens))
        require(disk.read_bytes() == saved, "cold read changed the disk")
        (out / "fixture.raw").write_bytes(saved)
        (out / "result.json").write_text(json.dumps({"zip_sha256": sha(args.archive.read_bytes()),
                "first_disk_sha256": sha(before), "saved_disk_sha256": sha(saved), "read_back_label": checks["LABEL"]},
                indent=2) + "\n")


if __name__ == "__main__":
    main()
