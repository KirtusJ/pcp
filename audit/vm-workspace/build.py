"""Package the opt-in vm-store kernel and two source-built native guests from one PCP OS revision."""
import argparse
from hashlib import sha256
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import zipfile

HERE = Path(__file__).resolve().parent


def build(source, optical, companion, output):
    receipt = json.loads((optical / "receipt.json").read_bytes())
    iso = optical / "pcp-os-tester.iso"
    rev = subprocess.check_output(["git", "-C", source, "rev-parse", "HEAD"], text=True).strip()
    tree = subprocess.check_output(["git", "-C", source, "rev-parse", "HEAD^{tree}"], text=True).strip()
    if (rev != receipt["source_commit"] or tree != receipt["source_tree"] or receipt["uncommitted_changes"]
            or sha256(iso.read_bytes()).hexdigest() != receipt["iso_sha256"]):
        raise ValueError("Source checkout or optical inputs do not match the build receipt")
    # The workflow builds the feature-enabled ELF separately from the optical kernel.
    kernel = source / "PCP_OS_Rust/crates/pcpos-kernel"
    elf = kernel / "target/pcpos-kernel.elf32"
    measurement = subprocess.check_output(["python3", kernel / "tools/measure.py", elf], text=True).strip()
    with tempfile.TemporaryDirectory() as temp:
        work = Path(temp)
        for name in ("surf.elf", "clip.ppm", "clip.wav", "rdesk.elf", "notice.md", "notices.txt", "limine.txt"):
            dest = work / name
            subprocess.run(["xorriso", "-osirrox", "on", "-indev", iso, "-extract", "/" + name, dest], check=True)
            if sha256(dest.read_bytes()).hexdigest() != receipt["on_disc"][name]["sha256"]:
                raise ValueError(f"Optical member differs from its receipt: {name}")
        with zipfile.ZipFile(companion) as archive:
            notices = archive.read("Third-party-notices.txt")
        if sha256(notices).hexdigest() != "9cf931e506692875ce1e2616594b590893116c2888ae87c4e6e6cfe0fb256af1":
            raise ValueError("Unexpected toolchain and font notices")
        (work / "Third-party-notices.txt").write_bytes(notices)
        shutil.copyfile(elf, work / "kernel.elf")
        shutil.copyfile(source / "examples/vm-store/create.py", work / "create.py")
        shutil.copyfile(HERE / "start.py", work / "start.py")
        renderer = subprocess.check_output(
            ["git", "-C", source, "show", f"{rev}:PCP_OS_Rust/crates/pcpos-kernel/src/session.rs"],
            text=True,
        )
        guide = HERE / "QUICKSTART.md"
        if "fn power_prompt(" in renderer:
            guide = HERE.parent / "public-live-cd" / "desktop-first.md"
        shutil.copyfile(guide, work / "QUICKSTART.md")
        hashes = {item.name: sha256(item.read_bytes()).hexdigest() for item in sorted(work.iterdir())}
        info = dict(source_commit=rev, source_tree=tree, kernel_features=["vm-store"], toolchain=receipt["rustc"],
                    kernel_measurement=measurement, optical_iso_sha256=receipt["iso_sha256"], files=hashes)
        (work / "build.json").write_text(json.dumps(info, indent=2) + "\n", encoding="utf-8")
        with zipfile.ZipFile(output, "x") as archive:
            for item in sorted(work.iterdir()):
                entry = zipfile.ZipInfo(item.name, (2026, 11, 20, 0, 0, 0))
                entry.create_system = 3
                entry.external_attr = 0o100644 << 16
                archive.writestr(entry, item.read_bytes(), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
    print(sha256(output.read_bytes()).hexdigest(), output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    for arg in ("source", "optical", "companion", "output"):
        parser.add_argument(arg, type=Path)
    args = parser.parse_args()
    build(args.source.resolve(), args.optical.resolve(), args.companion, args.output)
