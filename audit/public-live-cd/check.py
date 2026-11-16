"""Check the public BIOS live CD with QEMU TCG, SeaBIOS and standard VGA."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import tempfile
import time

ISO_SHA = "93ed3b599ad7be0e1e88a64813b1f2b5299d51507df2edca691aaf6189d10d15"
IMAGE_SHA = "0232c02a8946d66216da0ac65953a246ce3d41d7a966ae31aa83c3335b3259e3"


class GuestSafe(RuntimeError):
    pass


def check(iso, output, *, clock="instructions", startup_only=False):
    if hashlib.sha256(iso.read_bytes()).hexdigest() != ISO_SHA:
        raise ValueError("The optical image differs from the published 0.3.1 CD")
    output.mkdir(parents=True, exist_ok=False)
    serial = output / "serial.txt"
    with tempfile.TemporaryDirectory() as tmp:
        monitor = Path(tmp) / "qmp"
        command = [
            "qemu-system-x86_64", "-machine", "pc", "-accel", "tcg",
            "-cpu", "qemu64", "-m", "64M", "-boot", "order=d", "-cdrom", str(iso),
            "-nic", "none", "-vga", "std", "-display", "none", "-monitor", "none",
            "-serial", "file:" + str(serial), "-qmp", f"unix:{monitor},server=on,wait=off",
            "-audiodev", "none,id=snd0", "-device", "AC97,audiodev=snd0",
            "-no-reboot",
            "-device", "isa-debug-exit,iobase=0xf4,iosize=0x04",
        ]
        if clock == "instructions":
            command.extend(["-icount", "shift=3,align=off,sleep=off"])
        elif clock != "wall":
            raise ValueError(f"Unknown guest clock: {clock}")
        with subprocess.Popen(command, stdin=subprocess.DEVNULL) as guest:
            try:
                exercise(guest, monitor, serial, output, startup_only)
            finally:
                if guest.poll() is None:
                    guest.terminate()
                    try:
                        guest.wait(timeout=5)
                    except subprocess.TimeoutExpired:
                        guest.kill()


def exercise(guest, monitor, serial, output):
    import socket

    def wait(test, name, seconds=120):
        end = time.monotonic() + seconds
        while time.monotonic() < end:
            if guest.poll() is not None:
                raise RuntimeError(f"Guest exited {guest.returncode} before {name}")
            log = serial.read_text(errors="replace") if serial.exists() else ""
            if "it is in SAFE" in log:
                raise GuestSafe("Guest entered SAFE. See serial.txt for failed self-tests.")
            if test(log):
                return
            time.sleep(0.1)
        raise TimeoutError(name)

    wait(lambda _: monitor.exists(), "QMP socket")
    with socket.socket(socket.AF_UNIX) as sock:
        sock.settimeout(12)
        sock.connect(str(monitor))
        with sock.makefile("rwb", buffering=0) as io:
            if "QMP" not in json.loads(io.readline()):
                raise RuntimeError("Missing QMP greeting")

            def rpc(name, **arguments):
                io.write((json.dumps({"execute": name, "arguments": arguments}) + "\n").encode())
                while True:
                    reply = json.loads(io.readline())
                    if "error" in reply:
                        raise RuntimeError(reply["error"])
                    if "return" in reply:
                        return reply["return"]

            def press(*keys):
                rpc("send-key", keys=[{"type": "qcode", "data": k} for k in keys],
                    **{"hold-time": 70})

            def launcher(label):
                screen = output / (label + ".ppm")
                def visible(_):
                    rpc("screendump", filename=str(screen))
                    result = subprocess.run(["tesseract", str(screen), "stdout", "--psm", "6"],
                                            check=True, capture_output=True, text=True)
                    (output / (label + ".txt")).write_text(result.stdout)
                    return "power off" in result.stdout.lower()
                wait(visible, label, 45)

            rpc("qmp_capabilities")
            wait(lambda s: ("long mode true" in s and
                            IMAGE_SHA + " (measured; equal" in s and
                            "leaves no memory behind" in s), "unattended kernel and self-tests")
            launcher("unattended-launcher")
            if startup_only:
                return
            press("ret")
            wait(lambda s: "SURFBIRD media ready" in s, "Surfbird media menu")
            press("spc")
            wait(lambda s: "SURFBIRD media drained" in s, "media playback")
            wait(lambda s: "surf.elf ended DONE" in s, "normal app exit")
            launcher("after-playback")
            press("ret")
            wait(lambda s: s.count("SURFBIRD media ready") == 2, "second app launch")
            press("ctrl", "alt", "delete")
            wait(lambda s: "surf.elf ended STOPPED" in s, "kernel Stop")
            launcher("after-stop")
            press("p")
            code = guest.wait(timeout=30)
            final = serial.read_text(errors="replace")
            if "ALL SELF-TESTS PASS" not in final or code != 33:
                raise RuntimeError(f"Inspect final serial result and QEMU exit {code}")
            print("Verified unattended launcher, app playback, keyboard Stop and power-off")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("iso", type=Path)
    parser.add_argument("output", type=Path, help="a new directory for serial and framebuffer evidence")
    args = parser.parse_args()
    check(args.iso.resolve(), args.output.resolve())
