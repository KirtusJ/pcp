# Source-built BIOS tester CD

[Download the tester ZIP](source-bios-tester.zip?raw=1). It contains a source-built x86-64 PCP OS CD, the original build receipt and companion third-party notices. Use a fresh QEMU virtual machine with SeaBIOS, its ordinary clock, and only the virtual optical drive. Files created during the session last until power-off.

| File | Bytes | SHA-256 |
| --- | ---: | --- |
| `source-bios-tester.zip` | 469,964 | `936f8366a714cb5d57b129f801d29caf1679f171860744ebf82cb3feb9b4e71b` |
| `pcp-os-tester.iso` | 2,445,312 | `f904f393c9332c32ea5de8d73c5d81762717c6c31166708d6ce9ffdaa63e6f96` |

Use `sha256sum` on Linux, `shasum -a 256` on macOS, or `Get-FileHash -Algorithm SHA256` in Windows PowerShell. Compare the ZIP digest, extract it, then compare the ISO digest. In a checkout, `python verify.py pcp-os-tester.iso` in this folder verifies the package and writes the ISO to a new file.

## First session

With QEMU installed, run this from the directory containing the extracted ISO. The command uses software emulation so the x86-64 guest can also run on an Arm-based Mac.

```text
qemu-system-x86_64 -machine pc -accel tcg -cpu qemu64 -m 64M -smp 1 -nic none -audiodev none,id=snd -device AC97,audiodev=snd -boot order=d,strict=on -cdrom pcp-os-tester.iso
```

Wait for the graphical launcher to show 71 passed self-tests. Press Enter to open Surfbird and Space to play the bundled clip. The command uses a silent audio backend. After playback, open it again and send Ctrl+Alt+Delete **to the guest** to stop it. If the host intercepts the chord, use QEMU's monitor and enter `sendkey ctrl-alt-delete`. R opens the task register. Esc returns to the launcher. Pressing Esc again keeps the session open. P powers off.

## What was tested

The checked-in ISO is the exact output of the launcher correction’s source-CD run. Its receipt records GitHub’s temporary pull-request test merge `f1876b8ee8067ab79ba90f848376b6647bd9813e`, Rust 1.97.0 and a default-feature kernel with guest Ethernet disabled. The kernel text and read-only data measure `4732843ca93272f5b553a0ba7a6fb89a96f4672044edc686d4518567651e5bf4`. A fresh build can differ with toolchain paths or source revision. [Source and archived build run](https://github.com/KirtusJ/pcp-os/actions/runs/44859917889).

The [original signed Git commit object](source-commit.txt) preserves the source identity after the temporary pull-request ref expires. In this directory, `git hash-object -t commit source-commit.txt` returns the full test-merge ID above. Its first line names root tree `9133d6de1476fad2929a347042b9eca2be894c93`. In a PCP OS source checkout, `git rev-parse '19bc229f976b43450a581ad58a7551dbac3ed617^{tree}'` returns that same tree for the permanent master merge. This verifies the source files identified by the build receipt. A byte-identical reconstruction also depends on the recorded build environment. [Permanent source revision](https://github.com/KirtusJ/pcp-os/tree/19bc229f976b43450a581ad58a7551dbac3ed617).

On Linux, PC and Q35 each completed playback, keyboard Stop, register inspection and shutdown under both the ordinary and instruction-counted clocks. Each guest returned to the launcher on Escape, accepted a second Escape and reopened the same register before powering off on P. The older image powered off on the second Escape in all four control runs. [Corrected image](https://github.com/KirtusJ/pcp-os/actions/runs/44859917889) · [Earlier control](https://github.com/KirtusJ/pcp-os/actions/runs/44859694004).

The packaged ISO reached the verified launcher on Ubuntu 24.04 x86-64 (QEMU 8.2.2), macOS 15 Arm64 and Windows Server 2025 AMD64 (both QEMU 11.1.3). On all three hosts, the x86-64 guest ran 71 startup checks and powered off on P with exit code zero. The [original desktop observations](desktop-observations.zip) contain the three host archives, including raw launcher frames and serial logs. Enclosing ZIP SHA-256 is `b2c880c7f4cfba67bc198241046bad96783546112dbb20b03b960f1a207459a8`. [Qualification run](https://github.com/KirtusJ/pcp/actions/runs/44860353373).

The same packaged ISO completed a full session with a disposable writable disk on PC IDE, Q35 IDE, and Q35 NVMe with 512- and 4,096-byte sectors. All four disks registered reads, zero guest writes and matching before/after digests. Each of four separate monitor write controls changed precisely its selected fixture sector. The [original disk observations](disk-observations.zip) contain the counters, screens and serial traces. ZIP SHA-256 is `00fefebf780528392f105a5bfdf583a4d444810c281293e1ae3ccb19d869f1b7`. Ordinary tester boots use only the read-only CD.

The CD carries PCP OS and Limine notices and license texts for nine registry crates. The ZIP adds upstream notices for Rust, compiler-builtins and the DejaVu typeface. The scope is a BIOS VM with a volatile store. USB installation, physical laptops, UEFI and Secure Boot require separate evidence.
