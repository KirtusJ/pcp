# Source-built BIOS tester CD

[Download the tester ZIP](source-bios-tester.zip?raw=1). It contains a source-built x86-64 PCP OS CD, the original build receipt and companion third-party notices. Use a fresh QEMU virtual machine with SeaBIOS, its ordinary clock, and only the virtual optical drive. Files created during the session last until power-off.

| File | Bytes | SHA-256 |
| --- | ---: | --- |
| `source-bios-tester.zip` | 469,888 | `7f5eb3d4c8057da6e16eaaf593a6181c989b129c72ff5edff00958a55b691c30` |
| `pcp-os-tester.iso` | 2,445,312 | `7c1cd0d0ef7959f7dd095588106ad10bb5a87db2c3a9a0b09535f1debb6e10eb` |

Use `sha256sum` on Linux, `shasum -a 256` on macOS, or `Get-FileHash -Algorithm SHA256` in Windows PowerShell. Compare the ZIP digest, extract it, then compare the ISO digest. In a checkout, `python verify.py pcp-os-tester.iso` in this folder verifies the package and writes the ISO to a new file.

## First session

With QEMU installed, run this from the directory containing the extracted ISO. The command uses software emulation so the x86-64 guest can also run on an Arm-based Mac.

```text
qemu-system-x86_64 -machine pc -accel tcg -cpu qemu64 -m 64M -smp 1 -nic none -audiodev none,id=snd -device AC97,audiodev=snd -boot order=d,strict=on -cdrom pcp-os-tester.iso
```

Wait for the graphical launcher to show 71 passed self-tests. Press Enter to open Surfbird and Space to play the bundled clip. The command uses a silent audio backend. After playback, open it again and send Ctrl+Alt+Delete **to the guest** to stop it. If the host intercepts the chord, use QEMU's monitor and enter `sendkey ctrl-alt-delete`. R opens the task register, Esc returns to the launcher, and P powers off.

## What was tested

The checked-in ISO is the exact output of the merged build recipe's final pull-request run. Its receipt records source commit `ac6580a649b900e537ed611521939f9eba1327b6`, Rust 1.97.0 and a default-feature kernel with guest Ethernet disabled. The kernel text and read-only data measure `82b96a61b5e949caa63abb9e262f0c7e135de443c8a8576344687aa84f2d6cde`. A fresh build can differ with toolchain paths or source revision. [Source and archived build run](https://github.com/KirtusJ/pcp-os/actions/runs/44858643525).

Linux-hosted PC and Q35 guests each completed playback, keyboard Stop, register inspection and shutdown under both the ordinary and instruction-counted clocks. In separate tests with this ISO, four writable virtual disks reported zero guest writes. They covered PC IDE, Q35 IDE and Q35 NVMe with 512-byte and 4,096-byte sectors. Each write control changed the intended sector. [Boot verification](https://github.com/KirtusJ/pcp-os/pull/291#issuecomment-7056327472) · [Disk checks](https://github.com/KirtusJ/pcp-os/pull/291#issuecomment-7056317599).

The CD carries PCP OS and Limine notices and license texts for nine registry crates. The ZIP adds upstream notices for Rust, compiler-builtins and the DejaVu typeface. The scope is a BIOS VM with a volatile store. USB installation, physical laptops, UEFI and Secure Boot require separate evidence.
