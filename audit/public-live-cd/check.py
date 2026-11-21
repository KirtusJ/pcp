"""Check the public BIOS live CD with QEMU TCG, SeaBIOS and standard VGA."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import tempfile
import time

ISO_SHA = "93ed3b599ad7be0e1e88a64813b1f2b5299d51507df2edca691aaf6189d10d15"
IMAGE_SHA = "0232c02a8946d66216da0ac65953a246ce3d41d7a966ae31aa83c3335b3259e3"


VIDEO_MARKERS = (3, 11, 19, 27)


# The final help line is painted after the status and file list. The words
# "power off" also occur earlier on the screen in the temporary store notice.
LAUNCHER_FOOTER = (12, 735, 895, 760, "445c95718b9757f556347922971f9e594a9a9982414b23d3457fe0303ac7ab41")
REGISTER_FOOTER = (12, 714, 420, 744, "123e5fedc122fb7016cce09b51260948f16476b2be1807fdf1d6993e489dbae8")
# Only the sequence-number column of the 32 visible rows. The independent
# kernel-font reader checks their complete contents and both Surfbird task IDs.
LATEST_ROWS = (20, 60, 60, 700, "eb32e563fb027748f65d9ee7436d1f818be75a969e8eabde2cae68e10b86bc44")
EARLIER_ROWS = (20, 60, 60, 700, "947966c66dd81d61a1a53c4380860037c93f75945a5c86814dccf00c0a42c852")


def has_regions(frame, regions):
    header = b"P6\n1024 768\n255\n"
    if not frame.startswith(header) or len(frame) != len(header) + 1024 * 768 * 3:
        return False
    pixels = memoryview(frame)[len(header):]
    for left, top, right, bottom, expected in regions:
        digest = hashlib.sha256()
        for y in range(top, bottom):
            digest.update(pixels[(y * 1024 + left) * 3:(y * 1024 + right) * 3])
        if digest.hexdigest() != expected:
            return False
    return True


class GuestSafe(RuntimeError):
    pass


def check(iso, output, *, clock="instructions", startup_only=False, capture_audio=False,
          expected_iso=ISO_SHA, expected_image=IMAGE_SHA, capture_video=False, debug_exit=True,
          check_register=False):
    if hashlib.sha256(iso.read_bytes()).hexdigest() != expected_iso:
        raise ValueError("The optical image differs from the expected SHA-256")
    output.mkdir(parents=True, exist_ok=False)
    serial = output / "serial.txt"
    with tempfile.TemporaryDirectory() as tmp:
        monitor = Path(tmp) / "qmp"
        audio = "none,id=snd0"
        if capture_audio:
            wav_path = str((output / "capture.wav").resolve()).replace(",", ",,")
            audio = f"wav,id=snd0,out.frequency=48000,out.channels=2,out.format=s16,path={wav_path}"
        command = [
            "qemu-system-x86_64", "-machine", "pc", "-accel", "tcg",
            "-cpu", "qemu64", "-m", "64M", "-boot", "order=d", "-cdrom", str(iso),
            "-nic", "none", "-vga", "std", "-display", "none", "-monitor", "none",
            "-serial", "file:" + str(serial), "-qmp", f"unix:{monitor},server=on,wait=off",
            "-audiodev", audio, "-device", "AC97,audiodev=snd0",
        ]
        if debug_exit:
            command.extend(["-no-reboot", "-device", "isa-debug-exit,iobase=0xf4,iosize=0x04"])
        if clock == "instructions":
            command.extend(["-icount", "shift=3,align=off,sleep=off"])
        elif clock != "wall":
            raise ValueError(f"Unknown guest clock: {clock}")
        (output / "qemu-command.json").write_text(json.dumps(command, indent=2) + "\n")
        with subprocess.Popen(command, stdin=subprocess.DEVNULL) as guest:
            try:
                exercise(guest, monitor, serial, output, startup_only, expected_image, capture_video,
                         debug_exit, check_register)
            finally:
                if guest.poll() is None:
                    guest.terminate()
                    try:
                        guest.wait(timeout=5)
                    except subprocess.TimeoutExpired:
                        guest.kill()


def exercise(guest, monitor, serial, output, startup_only, expected_image, capture_video, debug_exit,
             check_register):
    import socket

    def wait(test, name, seconds=120, poll=0.1):
        end = time.monotonic() + seconds
        while time.monotonic() < end:
            if guest.poll() is not None:
                raise RuntimeError(f"Guest exited {guest.returncode} before {name}")
            log = serial.read_text(errors="replace") if serial.exists() else ""
            if "it is in SAFE" in log:
                raise GuestSafe("Guest entered SAFE. See serial.txt for failed self-tests.")
            if test(log):
                return
            time.sleep(poll)
        raise TimeoutError(name)

    wait(lambda _: monitor.exists(), "QMP socket")
    with socket.socket(socket.AF_UNIX) as sock:
        sock.settimeout(12)
        sock.connect(str(monitor))
        with sock.makefile("rwb", buffering=0) as io:
            if "QMP" not in json.loads(io.readline()):
                raise RuntimeError("Missing QMP greeting")

            events = []

            def rpc(name, **arguments):
                io.write((json.dumps({"execute": name, "arguments": arguments}) + "\n").encode())
                while True:
                    reply = json.loads(io.readline())
                    if "event" in reply:
                        events.append(reply)
                    if "error" in reply:
                        raise RuntimeError(reply["error"])
                    if "return" in reply:
                        return reply["return"]

            def press(*keys):
                rpc("send-key", keys=[{"type": "qcode", "data": k} for k in keys],
                    **{"hold-time": 70})

            def screen_until(label, *regions, restore=None):
                screen = output / (label + ".ppm")
                expected = (output / (restore + ".ppm")).read_bytes() if restore else None

                def visible(_):
                    rpc("screendump", filename=str(screen))
                    frame = screen.read_bytes()
                    return has_regions(frame, regions) and (expected is None or frame == expected)

                wait(visible, label, 45, poll=0.25)
                # Keep the readable transcript alongside the exact frame checked above.
                result = subprocess.run(["tesseract", str(screen), "stdout", "--psm", "6"],
                                        check=True, capture_output=True, text=True, timeout=15,
                                        env={**os.environ, "OMP_THREAD_LIMIT": "1"})
                (output / (label + ".txt")).write_text(result.stdout)

            def launcher(label):
                screen_until(label, LAUNCHER_FOOTER)

            rpc("qmp_capabilities")
            wait(lambda s: ("long mode true" in s and
                            expected_image + " (measured; equal" in s and
                            "leaves no memory behind" in s), "unattended kernel and self-tests")
            launcher("unattended-launcher")
            if startup_only:
                return
            press("ret")
            wait(lambda s: "SURFBIRD media ready" in s, "Surfbird media menu")
            press("spc")
            if capture_video:
                for frame in VIDEO_MARKERS:
                    marker = f"SURFBIRD media-frame {frame}\n"
                    wait(lambda s: marker in s, f"media frame {frame}", poll=0.012)
                    rpc("screendump", filename=str((output / f"video-{frame}.ppm").resolve()))
            wait(lambda s: "SURFBIRD media drained" in s, "media playback")
            wait(lambda s: "surf.elf ended DONE" in s, "normal app exit")
            launcher("after-playback")
            press("ret")
            wait(lambda s: s.count("SURFBIRD media ready") == 2, "second app launch")
            press("ctrl", "alt", "delete")
            wait(lambda s: "surf.elf ended STOPPED" in s, "kernel Stop")
            launcher("after-stop")
            if check_register:
                # Send each make/break pair explicitly. A timed send-key release can
                # still be pending when an instruction-counted guest accepts the next key.
                def tap(key):
                    rpc("input-send-event", events=[
                        {"type": "key", "data": {"down": down, "key": {"type": "qcode", "data": key}}}
                        for down in (True, False)
                    ])

                tap("r")
                screen_until("register-latest", REGISTER_FOOTER, LATEST_ROWS)
                tap("up")
                screen_until("register-earlier", REGISTER_FOOTER, EARLIER_ROWS)
                tap("down")
                screen_until("register-restored", REGISTER_FOOTER, LATEST_ROWS, restore="register-latest")
                tap("esc")
                screen_until("after-register", LAUNCHER_FOOTER, restore="after-stop")
            events.clear()
            press("p")
            code = guest.wait(timeout=30)
            if not debug_exit:
                for line in io:
                    reply = json.loads(line)
                    if "event" in reply:
                        events.append(reply)
                (output / "power-events.json").write_text(json.dumps(events, indent=2) + "\n")
                if not any(event["event"] == "SHUTDOWN" and
                           event.get("data", {}).get("guest") is True and
                           event["data"].get("reason") == "guest-shutdown" for event in events):
                    raise RuntimeError("No guest-requested QEMU shutdown after P")
            final = serial.read_text(errors="replace")
            expected_exit = 33 if debug_exit else 0
            if "ALL SELF-TESTS PASS" not in final or code != expected_exit:
                raise RuntimeError(f"Inspect final serial result and QEMU exit {code}")
            (output / "qemu-exit.txt").write_text(f"{code}\n")
            print("Verified unattended launcher, app playback, keyboard Stop and power-off")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("iso", type=Path)
    parser.add_argument("output", type=Path, help="a new directory for serial and framebuffer evidence")
    parser.add_argument("--capture-audio", action="store_true", help="write the AC’97 output to capture.wav")
    parser.add_argument("--capture-video", action="store_true", help="save four playback framebuffers")
    args = parser.parse_args()
    check(args.iso.resolve(), args.output.resolve(), capture_audio=args.capture_audio, capture_video=args.capture_video)
