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

The checked-in ISO is the exact output of the launcher correction’s source-CD run. Its receipt records source commit `f1876b8ee8067ab79ba90f848376b6647bd9813e`, Rust 1.97.0 and a default-feature kernel with guest Ethernet disabled. The kernel text and read-only data measure `4732843ca93272f5b553a0ba7a6fb89a96f4672044edc686d4518567651e5bf4`. A fresh build can differ with toolchain paths or source revision. [Source and archived build run](https://github.com/KirtusJ/pcp-os/actions/runs/44859917889).

On Linux, PC and Q35 each completed playback, keyboard Stop, register inspection and shutdown under both the ordinary and instruction-counted clocks. Each guest returned to the launcher on Escape, accepted a second Escape and reopened the same register before powering off on P. The older image powered off on the second Escape in all four control runs. [Corrected image](https://github.com/KirtusJ/pcp-os/actions/runs/44859917889) · [Earlier control](https://github.com/KirtusJ/pcp-os/actions/runs/44859694004).

The CD carries PCP OS and Limine notices and license texts for nine registry crates. The ZIP adds upstream notices for Rust, compiler-builtins and the DejaVu typeface. The scope is a BIOS VM with a volatile store. USB installation, physical laptops, UEFI and Secure Boot require separate evidence.
