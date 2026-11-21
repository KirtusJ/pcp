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

The ZIP is 349,404 bytes. Compare its SHA-256 with `1d60a0648ce3c03cbadc39544e8a288cca88441549b79e6d452c51d71622a5c6`. Use `sha256sum pcp-vm-workspace.zip` on Linux, `shasum -a 256 pcp-vm-workspace.zip` on macOS or `Get-FileHash pcp-vm-workspace.zip -Algorithm SHA256` in PowerShell.

The package uses PCP OS source `4c482cfd33c564526722a8b4e08d830da0f30164`, tree `89855dd32e4d68b06d1210ef34bb118a5ee13865`, with Rust 1.97.0 and the kernel's opt-in `vm-store` feature. The measured kernel code and read-only data hash to `f386f183029fd1a6408db99181ce1702b9930a4cbb85e94953410ba66a157b5b`. A clean build reproduced the checked-in ZIP byte for byte. File digests and toolchain details are in `build.json` inside the package. [Kernel, guests and provisioner](https://github.com/KirtusJ/pcp-os/tree/4c482cfd33c564526722a8b4e08d830da0f30164).

## Host qualification

The test drove the guest keyboard and read the guest framebuffer in headless QEMU. On each host, Surfbird played 33 frames and submitted 3,200 ms of audio to the silent device. The queue saved the typed label `cold morning`. A separate QEMU process reopened the same volume, drew the same label and left the disk byte-identical. Both sessions ended with guest-requested shutdowns. Host window presentation and speaker output remain untested.

| Host runner | Host architecture | QEMU |
| --- | --- | --- |
| Ubuntu 24.04 | x86-64 | 8.2.2 |
| macOS 15 | arm64 | 11.1.3 |
| Windows Server 2025 | x86-64 | 11.1.3 |

The 86,055-byte evidence archive has SHA-256 `8c781ae5271bb917626f1c31886c600e155b483b0308adba9ee98a6716c55605`. It preserves each original runner artifact, including serial logs, QEMU arguments and shutdown events, guest screenshots and the saved test disk. [Original observations](host-observations.zip?raw=1) · [Qualification run](https://github.com/KirtusJ/pcp/actions/runs/44862756228) · [Rebuild and boot workflow](../../.github/workflows/vm-workspace.yml).
