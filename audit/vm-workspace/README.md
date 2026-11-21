# PCP OS VM workspace

[Download the VM workspace](pcp-vm-workspace.zip?raw=1). The x86-64 guest plays a local Surfbird clip and keeps a task queue across shutdowns. It runs in QEMU software emulation with 128 MiB of guest RAM. Its only attached disk is the data file you create for it.

## First boot

Install Python 3.10 or later and the QEMU x86 system emulator. Put `qemu-system-x86_64` on your path, or give `start.py run` its location with `--qemu`. Extract the complete ZIP and open a terminal in the extracted folder. Substitute `python3` if your system uses that name.

```text
python start.py init my-volume
python start.py run my-volume
```

Enter opens Surfbird and Space plays the clip. At the launcher, Down selects the queue desk. Press Enter to open it, N to start a task, type a label and press Enter to save. Look for **Disk save**. Press Esc to return to the launcher and P to power off. Run the second command again and reopen the desk to see your label and **Queue restored**.

Keep the volume's two files together. To back up the queue, copy the volume folder after the guest shuts down. The store has a 64 KiB checkpoint capacity. Audio uses a silent backend and the guest has no network interface. Physical installation, Secure Boot, host power-loss recovery and general daily use remain unqualified.

## Download and source verification

The ZIP is 349,533 bytes. Compare its SHA-256 with `671482e070add2bea6f38b159f3a28b63263045a45e8c5234412f909f3daf5fe`. Use `sha256sum pcp-vm-workspace.zip` on Linux, `shasum -a 256 pcp-vm-workspace.zip` on macOS or `Get-FileHash pcp-vm-workspace.zip -Algorithm SHA256` in PowerShell.

This package includes the guest file-open fixes in [PCP OS #303](https://github.com/KirtusJ/pcp-os/pull/303). If an app asks to create a file exclusively and the name already exists, the kernel returns an error. If the app has no free file descriptors, a failed open preserves the existing contents and leaves a new name available.

The package uses PCP OS source `0a037b45bb18d6c1c61c2a207a62da5f3057933d`, tree `e1367fbabebc1732ad3d380d47361138c61f48a2`, with Rust 1.97.0 and the kernel's opt-in `vm-store` feature. The measured kernel code and read-only data hash to `62d3a6b6c16035bec8979c9502b6dfb79c6c846bec094130cbe652141bdd247b`. File digests and toolchain details are in `build.json` inside the package. [Kernel, guests and provisioner](https://github.com/KirtusJ/pcp-os/tree/0a037b45bb18d6c1c61c2a207a62da5f3057933d).

## Host qualification

Host results for this package are pending. The three-host results for the previous package remain available with the [previous download and evidence](https://github.com/KirtusJ/pcp/tree/8081a5b2d5cfe5ccad6afd0bbd936c1986245fe6/audit/vm-workspace).
