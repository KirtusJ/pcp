"""Probe a GRUB x86-64 UEFI optical handoff in an isolated Q35/OVMF guest (Linux)."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import time

ISO_HASH = "93ed3b599ad7be0e1e88a64813b1f2b5299d51507df2edca691aaf6189d10d15"
MEASUREMENT = "0232c02a8946d66216da0ac65953a246ce3d41d7a966ae31aa83c3335b3259e3"
PAYLOADS = {
    "kernel.elf32": "d2fae4ef3df316ff4fa0c1a88744e66cc17bd794856979fa55188b8402f7222f",
    "surf.elf": "b87f1185f86961ff8afdb21315c811f0c071c474d09737613146be46cbb98b34",
    "clip.ppm": "f6a1d9a0702f472f5b02cf0a528586e6d4447acbad2bd92eb0fc6d70eea4df4d",
    "clip.wav": "70ca6a81bc6f94db7d14a61630ff02c517d20a65c31273b16ff02e233018e244",
}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def make_cd(source, work):
    root = work / "cd"
    grub = root / "boot/grub"
    grub.mkdir(parents=True)
    for name, expected in PAYLOADS.items():
        dest = root / name
        subprocess.run(["xorriso", "-osirrox", "on", "-indev", source, "-extract", "/" + name,
                        dest], check=True, stdout=subprocess.DEVNULL)
        if sha(dest) != expected:
            raise ValueError(f"Input payload differs: {name}")
    config = """serial --unit=0 --speed=115200
terminal_output serial console
echo PCP-OPTICAL-FIRMWARE-${grub_platform}
if [ "${grub_platform}" = "efi" ]; then
    echo PCP-PREBOOT-MEMORY-MAP-BEGIN
    lsmmap
    echo PCP-PREBOOT-MEMORY-MAP-END
    multiboot /kernel.elf32 image=KERNEL_HASH
    module /surf.elf surf.elf
    module /clip.ppm clip.ppm
    module /clip.wav clip.wav
    echo PCP-OPTICAL-BOOT-COMMAND
    boot
fi
"""
    (grub / "grub.cfg").write_text(config.replace("KERNEL_HASH", MEASUREMENT))
    optical = work / "uefi-test.iso"
    subprocess.run(["grub-mkrescue", "-d", "/usr/lib/grub/x86_64-efi",
                    "-o", optical, root], check=True)
    return optical


def run_guest(optical, code, variables, work, evidence):
    variables_copy = work / "vars.fd"
    shutil.copyfile(variables, variables_copy)
    serial = evidence / "serial.txt"
    args = ["qemu-system-x86_64", "-machine", "q35", "-accel", "tcg", "-cpu", "max",
            "-m", "256M", "-smp", "1", "-vga", "std", "-nic", "none", "-audiodev",
            "none,id=snd", "-device", "AC97,audiodev=snd", "-display", "none", "-qmp",
            "stdio", "-monitor", "none", "-serial", "file:" + str(serial),
            "-drive", f"if=pflash,unit=0,format=raw,readonly=on,file={code}",
            "-drive", f"if=pflash,unit=1,format=raw,file={variables_copy}",
            "-boot", "order=d,strict=on", "-cdrom", str(optical),
            "-icount", "shift=3,align=off,sleep=off"]
    result = {"published_iso_sha256": ISO_HASH, "iso_sha256": sha(optical), "firmware_code_sha256": sha(code),
              "vars_template_sha256": sha(variables), "payloads": PAYLOADS, "argv": args}
    (evidence / "environment.txt").write_text(subprocess.check_output(
        ["dpkg-query", "-W", "ovmf", "qemu-system-x86", "grub-efi-amd64-bin",
         "grub-common", "xorriso"], text=True))
    events = []
    with (evidence / "qemu-stderr.txt").open("wb") as err, subprocess.Popen(
            args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=err) as vm:
        def receive():
            line = vm.stdout.readline()
            if not line:
                raise RuntimeError("QEMU closed its monitor")
            return json.loads(line)

        def call(name, **kw):
            vm.stdin.write((json.dumps({"execute": name, "arguments": kw}) + "\n").encode())
            vm.stdin.flush()
            while True:
                reply = receive()
                if "event" in reply:
                    events.append(reply)
                if "error" in reply:
                    raise RuntimeError(reply["error"])
                if "return" in reply:
                    return reply["return"]

        try:
            if "QMP" not in receive():
                raise RuntimeError("Missing QMP greeting")
            call("qmp_capabilities")
            deadline = time.monotonic() + 100
            while time.monotonic() < deadline:
                log = serial.read_text(errors="replace") if serial.exists() else ""
                if "leaves no memory behind" in log or "it is in SAFE" in log:
                    break
                time.sleep(0.2)
            result["efi_loader_seen"] = "PCP-OPTICAL-FIRMWARE-efi" in log
            result["boot_command_seen"] = "PCP-OPTICAL-BOOT-COMMAND" in log
            result["safe"] = "it is in SAFE" in log
            result["failed_checks"] = [line.strip() for line in log.splitlines() if line.startswith("  FAIL ")]
            result["kernel_seen"] = "PCP OS kernel 0.3.1" in log
            result["kernel_measurement_matches"] = MEASUREMENT + " (measured; equal" in log
            result["startup_pass_lines"] = sum(s.startswith("  pass ") for s in log.splitlines())
            deadline = time.monotonic() + (20 if result["startup_pass_lines"] == 71 else 0)
            while True:
                screen = evidence / "last-screen.ppm"
                call("screendump", filename=str(screen))
                words = subprocess.check_output(["tesseract", screen, "stdout", "--psm", "6"],
                                                text=True, stderr=subprocess.DEVNULL, timeout=10)
                (evidence / "last-screen.txt").write_text(words)
                result["verified_launcher"] = ("all 71 self-tests passed" in words.lower()
                                               and "files from the loader" in words.lower())
                if result["verified_launcher"] or time.monotonic() >= deadline:
                    break
                time.sleep(0.15)
            if not (result["efi_loader_seen"] and result["boot_command_seen"]
                    and result["kernel_measurement_matches"] and result["verified_launcher"]
                    and result["startup_pass_lines"] == 71):
                raise RuntimeError("UEFI handoff did not reach all launcher criteria")
            call("send-key", keys=[{"type": "qcode", "data": "p"}], **{"hold-time": 80})
            vm.wait(timeout=18)
            for line in vm.stdout:
                reply = json.loads(line)
                if "event" in reply:
                    events.append(reply)
            result["guest_shutdown"] = any(e.get("event") == "SHUTDOWN" and
                e.get("data") == {"guest": True, "reason": "guest-shutdown"} for e in events)
            result["exit_code"] = vm.returncode
            if vm.returncode != 0 or not result["guest_shutdown"]:
                raise RuntimeError("Guest-requested shutdown missing")
        finally:
            if vm.poll() is None:
                vm.kill()
                vm.wait()
            result["qmp_events"] = events
            (evidence / "result.json").write_text(json.dumps(result, indent=2) + "\n")
            print(json.dumps({k: v for k, v in result.items() if isinstance(v, (int, bool))}))


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("iso", type=Path)
    p.add_argument("evidence", type=Path)
    p.add_argument("--code", type=Path, default=Path("/usr/share/OVMF/OVMF_CODE_4M.fd"))
    p.add_argument("--vars", type=Path, default=Path("/usr/share/OVMF/OVMF_VARS_4M.fd"))
    args = p.parse_args()
    if sha(args.iso) != ISO_HASH:
        p.error("expected the published 0.3.1 optical image")
    args.evidence.mkdir(parents=True, exist_ok=False)
    with tempfile.TemporaryDirectory() as temp:
        work = Path(temp)
        run_guest(make_cd(args.iso.resolve(), work), args.code.resolve(strict=True),
                  args.vars.resolve(strict=True), work, args.evidence.resolve())
