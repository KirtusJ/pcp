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


def recorded_paths(data):
    # The hash-pinned ELF supplies compiler display names and container-only mount
    # destinations. The host never creates a path supplied by the binary.
    def prefix(suffix):
        pattern = rb'([A-Z]:[\\/][\x20-\x7e]{1,255}?)' + re.escape(suffix)
        matches = {m.group(1).decode('ascii') for m in re.finditer(pattern, data)}
        if len(matches) != 1:
            raise ValueError("Ambiguous historical compiler path")
        return matches.pop()
    old_crates = prefix(rb'\pcpos-core\src\task.rs')
    old_cargo = prefix(rb'\registry\src\index.crates.io-1949cf8c6b5b557f\sha2-0.10.9')
    return old_crates, old_cargo


def path_flags(data, source, cargo_home):
    crates = source / "PCP_OS_Rust" / "crates"
    old_crates, old_cargo = recorded_paths(data)
    return [f"--remap-path-prefix={crates}={old_crates}",
            f"--remap-path-prefix={cargo_home}={old_cargo}"]


def container_build(source, args, kernel, env):
    """Use recovered paths only inside a disposable, offline Windows container."""
    old_crates, old_registry = recorded_paths(original(args.iso))
    old_root = Path(old_crates).parent.parent
    registry = Path(old_registry)
    for destination in (old_root, registry):
        if (destination.drive.upper() != "C:" or len(destination.parts) < 5
                or destination.parts[1].lower() != "users" or ".." in destination.parts
                or any(c in str(destination) for c in ',%"')):
            raise ValueError("Invalid historical mount destination")
    temp = args.out.resolve()
    base = temp / "cargo"
    env = {**env, "CARGO_HOME": str(base)}
    subprocess.run(["cargo", "fetch", "--locked", "--target", "x86_64-unknown-none"], cwd=kernel, env=env, check=True)
    sysroot = Path(subprocess.check_output(["rustc", "--print", "sysroot"], text=True).strip())
    gcc = shutil.which("gcc.exe")
    if not gcc:
        raise RuntimeError("GNU host linker unavailable")
    image = "mcr.microsoft.com/windows/servercore@sha256:f1a914079973258061ddbc95a9af579eab2ee252a6fddb254b1be5d769761acd"
    cmd = ["docker", "run", "--rm", "--isolation=process", "--network", "none"]
    for src, dst, writable in ((source, old_root, False), (sysroot, r"C:\rust", False),
                               (Path(gcc).parent.parent, r"C:\mingw", False),
                               (Path(env["CARGO_TARGET_X86_64_UNKNOWN_NONE_LINKER"]).parent, r"C:\llvmbin", False),
                               (base, registry, True), (temp / "target", r"C:\out", True)):
        if writable:
            src.mkdir(parents=True, exist_ok=True)
        cmd += ["--mount", f"type=bind,source={src},target={dst}" + ("" if writable else ",readonly")]
    cmd += ["--workdir", str(old_root / "PCP_OS_Rust/crates/pcpos-kernel"),
            "-e", "CARGO_HOME=" + old_registry, "-e", r"CARGO_TARGET_DIR=C:\out",
            "-e", r"CARGO_TARGET_X86_64_UNKNOWN_NONE_LINKER=C:\llvmbin\ld.lld.exe",
            "-e", r"PATH=C:\rust\bin;C:\mingw\bin;C:\llvmbin;C:\Windows\system32;C:\Windows",
            image, r"C:\rust\bin\cargo.exe", "build", "--offline", "--locked", "--release", "--features", "guest-ethernet"]
    result = subprocess.run(cmd, capture_output=True, text=True, errors="replace")
    if result.returncode:
        # Diagnostics can contain historical developer paths.
        diagnostic = result.stderr
        for private in {str(old_root), str(registry), old_registry, str(old_root.parents[-3])}:
            diagnostic = diagnostic.replace(private, "<historical path>")
        diagnostic = re.sub(r"(?i)[a-z]:[\\/]users[\\/][^\\/\s]+", "<profile>", diagnostic)
        print(diagnostic[-3000:])
        raise RuntimeError(f"Container build exited {result.returncode}")


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
    if args.mode == "historical":
        container_build(source, args, kernel, env)
    else:
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
        if mode == "kernel-gnu-historical":
            subprocess.run(["llvm-objcopy", "-I", "elf64-x86-64", "-O", "elf32-i386", candidate, flat], check=True)
            results[mode]["llvm_objcopy"] = compare(ref, flat.read_bytes())
            results[mode]["llvm_version"] = subprocess.check_output(["llvm-objcopy", "--version"], text=True).splitlines()[:2]
            if results[mode]["llvm_objcopy"]["whole_elf_equal"]:
                flat.rename(args.out / "reproduced-kernel.elf32")
            else:
                flat.unlink()
    expected = {f"kernel-{host}-{mode}" for host in ("msvc", "gnu") for mode in ("native", "remapped")}
    expected.add("kernel-gnu-historical")
    if results.keys() != expected:
        raise ValueError("Expected both Windows toolchains and both path modes")
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
    b.add_argument("mode", choices=["native", "remapped", "historical"])
    inspect_cli = modes.add_parser("compare")
    inspect_cli.add_argument("inputs", type=Path)
    for p in (b, inspect_cli):
        p.add_argument("iso", type=Path)
        p.add_argument("out", type=Path)
    opts = cli.parse_args()
    opts.out.mkdir(parents=True, exist_ok=True)
    (build if opts.action == "build" else inspect)(opts)
