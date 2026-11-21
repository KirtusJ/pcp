"""Compare an identified historical Rust kernel with the original optical ELF."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import struct
import subprocess


ISO = "93ed3b599ad7be0e1e88a64813b1f2b5299d51507df2edca691aaf6189d10d15"
ELF = "d2fae4ef3df316ff4fa0c1a88744e66cc17bd794856979fa55188b8402f7222f"
SOURCE = "1cff81e4b935dc72a95a669a5214508ab8712efc"
RUST = "ed61e7d7e242494fb7057f2657300d9e77bb4fcb"


def sha(data):
    return hashlib.sha256(data).hexdigest()


def original(cd):
    data = cd.read_bytes()
    if sha(data) != ISO:
        raise ValueError("Unexpected source ISO")
    # This pinned ISO's file is contiguous. Require exactly one ELF matching the
    # complete original checksum, independently of filenames and catalog offsets.
    found = [data[i:i + 733284] for i in range(0, len(data), 2048)
             if data[i:i + 4] == b'\x7fELF' and sha(data[i:i + 733284]) == ELF]
    if len(found) != 1:
        raise ValueError("Expected one matching original kernel")
    return found[0]


def sections(data):
    if data[:4] != b'\x7fELF' or data[5] != 1:
        raise ValueError("Expected little-endian ELF")
    if data[4] == 1:
        at = struct.unpack_from("<I", data, 32)[0]
        stride, count, table = struct.unpack_from("<HHH", data, 46)
        layout = "<IIIIII"
    elif data[4] == 2:
        at = struct.unpack_from("<Q", data, 40)[0]
        stride, count, table = struct.unpack_from("<HHH", data, 58)
        layout = "<IIQQQQ"
    else:
        raise ValueError("Unexpected ELF class")
    headers = [struct.unpack_from(layout, data, at + i * stride) for i in range(count)]
    _, _, _, _, offset, size = headers[table]
    names = data[offset:offset + size]
    result = {}
    for idx, kind, _, addr, start, size in headers:
        name = names[idx:names.index(b'\0', idx)].decode()
        if name in {'.boot', '.text', '.rodata', '.data', '.got', '.bss'}:
            result[name] = (addr, size, b'' if kind == 8 else data[start:start + size])
    return result


def compare(reference, candidate):
    old, new = sections(reference), sections(candidate)
    return {
        "bytes": len(candidate), "sha256": sha(candidate), "whole_elf_equal": reference == candidate,
        "measurement": sha(new[".text"][2] + new[".rodata"][2]),
        "sections": {s: {"reference_size": old[s][1], "built_size": new[s][1],
                          "address_equal": old[s][0] == new[s][0],
                          "bytes_and_size_equal": old[s][1:] == new[s][1:],
                          "sha256": sha(new[s][2]) if s != ".bss" else None}
                     for s in old},
    }


def path_flags(data, source, cargo_home):
    # Use historical names only as compiler display strings. Never create a
    # directory named by the binary or use any recovered string in a shell.
    def prefix(suffix):
        pattern = rb'([A-Z]:[\\/][\x20-\x7e]{1,255}?)' + re.escape(suffix)
        matches = {m.group(1).decode('ascii') for m in re.finditer(pattern, data)}
        if len(matches) != 1:
            raise ValueError("Ambiguous historical compiler path")
        return matches.pop()
    crates = source / "PCP_OS_Rust" / "crates"
    old_crates = prefix(rb'\pcpos-core\src\task.rs')
    old_cargo = prefix(rb'\registry\src\index.crates.io-1949cf8c6b5b557f\sha2-0.10.9')
    return [f"--remap-path-prefix={crates}={old_crates}",
            f"--remap-path-prefix={cargo_home}={old_cargo}"]


def build(args):
    source = args.source.resolve()
    if subprocess.check_output(["git", "-C", source, "rev-parse", "HEAD"], text=True).strip() != SOURCE:
        raise ValueError("Unexpected historical checkout")
    cargo = Path(os.environ.get("CARGO_HOME") or Path.home() / ".cargo").resolve()
    version = subprocess.check_output(["rustc", "-vV"], text=True)
    if "commit-hash: " + RUST not in version:
        raise ValueError("Unexpected compiler")
    kernel = source / "PCP_OS_Rust/crates/pcpos-kernel"
    target = args.out.resolve() / "target"
    env = {**os.environ, "CARGO_TARGET_DIR": str(target), "CARGO_HOME": str(cargo)}
    linker = shutil.which("ld.lld.exe")
    if linker is None:
        raise RuntimeError("Windows ELF linker unavailable")
    env["CARGO_TARGET_X86_64_UNKNOWN_NONE_LINKER"] = linker
    command = ["cargo", "build", "--release", "--locked", "--features", "guest-ethernet"]
    if args.mode == "remapped":
        # Cargo appends this array to the flags in the historical config.
        flags = path_flags(original(args.iso), source, cargo)
        command += ["--config", "target.x86_64-unknown-none.rustflags=" + json.dumps(flags)]
    result = subprocess.run(command, env=env, cwd=kernel, capture_output=True, text=True, errors="replace")
    if result.returncode:
        lines = [line for line in result.stderr.splitlines() if line.startswith("error")]
        raise RuntimeError(f"Cargo exited {result.returncode}: " + "; ".join(lines)[:500])
    shutil.copyfile(target / "x86_64-unknown-none/release/pcpos-kernel", args.out / "kernel.elf64")
    print(version.strip())


def inspect(args):
    ref = original(args.iso)
    results = {}
    for candidate in sorted(args.inputs.glob("*/kernel.elf64")):
        mode = candidate.parent.name
        flat = args.out / (mode + ".elf32")
        subprocess.run(["objcopy", "-I", "elf64-x86-64", "-O", "elf32-i386", candidate, flat], check=True)
        results[mode] = compare(ref, flat.read_bytes())
        flat.unlink()
    if len(results) != 2:
        raise ValueError("Both independent build modes are required")
    receipt = {"source": SOURCE, "compiler": RUST, "compile_host": "windows-2022",
               "features": ["guest-ethernet"], "reference_iso": ISO, "reference_elf": ELF,
               "reference_measurement": compare(ref, ref)["measurement"],
               "objcopy": subprocess.check_output(["objcopy", "--version"], text=True).splitlines()[0],
               "results": results}
    (args.out / "comparison.json").write_text(json.dumps(receipt, indent=2) + "\n")
    for name, result in results.items():
        print(name, result["bytes"], result["sha256"], "whole ELF equal:", result["whole_elf_equal"])


if __name__ == "__main__":
    cli = argparse.ArgumentParser(description=__doc__)
    modes = cli.add_subparsers(dest="action", required=True)
    b = modes.add_parser("build")
    b.add_argument("source", type=Path)
    b.add_argument("mode", choices=["native", "remapped"])
    inspect_cli = modes.add_parser("compare")
    inspect_cli.add_argument("inputs", type=Path)
    for p in (b, inspect_cli):
        p.add_argument("iso", type=Path)
        p.add_argument("out", type=Path)
    opts = cli.parse_args()
    opts.out.mkdir(parents=True, exist_ok=True)
    (build if opts.action == "build" else inspect)(opts)
