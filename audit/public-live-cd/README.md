# First boot of the PCP OS 0.3.1 live CD

Start with a disposable **x86-64 virtual machine using legacy PC BIOS (SeaBIOS)**. The published CD opens a graphical launcher and runs a local Surfbird demo. The guest store lasts for one boot. Attach only the virtual CD. Keep physical drives and existing virtual disks out of the VM. Leave the host computer’s firmware settings as they are.

## Choose and verify the image

For the published version, download [PCP-OS.iso at the tested revision](https://raw.githubusercontent.com/KirtusJ/pcp/983fc4a45dbbada52b507dd0e413b9f7d3ca0c9d/PCP-OS.iso). Its size is **1,859,584 bytes** and its SHA-256 is `93ed3b599ad7be0e1e88a64813b1f2b5299d51507df2edca691aaf6189d10d15`. Run the command for your host in the download directory and compare the full digest before booting.

| Host | SHA-256 command |
| --- | --- |
| Linux | `sha256sum PCP-OS.iso` |
| macOS | `shasum -a 256 PCP-OS.iso` |
| Windows PowerShell | `Get-FileHash .\PCP-OS.iso -Algorithm SHA256` |

If you received the ISO separately, the same byte count and digest identify the tested image.

To check the committed **Enterprise edition** from a Linux x86-64 Git checkout, run `python3 audit/enterprise-checkout/check.py HEAD`. The script checks three temporary working trees and both plugin copies. The standalone `verify_edition.py` expects the exact extracted edition inventory. The repository also carries the optical image, workflows and audit files. For a downloaded ISO alone, use the ISO checksum above.

Use [keyboard-01](candidates/keyboard-01/) only when testing the keyboard timing changes. It carries a different ISO and kernel while displaying the same 0.3.1 label. Keep the two images in separate directories and record the digest of the one you ran.

## Boot and exit

With QEMU's x86 system emulator and its PC BIOS firmware installed, run this single command in the directory containing the verified ISO. It uses software CPU emulation, a virtual CD, an instruction-counted clock and a silent audio device. It attaches no writable disk or network interface. QEMU writes the serial log on the host.

```text
qemu-system-x86_64 -machine pc -accel tcg -cpu qemu64 -m 64M -boot order=d -cdrom PCP-OS.iso -vga std -nic none -icount shift=3,align=off,sleep=off -audiodev none,id=snd0 -device AC97,audiodev=snd0 -serial file:pcp-live-cd.log
```

1. Leave the keyboard alone until the launcher appears. The expected screen reads **Verified at start: all 71 self-tests passed**. In `pcp-live-cd.log`, look for kernel 0.3.1, long mode and the measured code and read-only data hash `0232c02a8946d66216da0ac65953a246ce3d41d7a966ae31aa83c3335b3259e3`.
2. Press **Enter** to open Surfbird and **Space** at its media menu to play the bundled clip. To stop an active app, send **Ctrl+Alt+Delete** to the *guest*. Use the emulator's send-key control if your host intercepts the chord.
3. Press **P** at the launcher to power off. Keep the serial log outside the guest. If startup shows **SAFE**, save the screen and log, including the failed checks. The guest disables app startup in that state. Report the ISO digest, QEMU version, machine, firmware and clock settings with the result.

The published image can enter SAFE during keyboard self-tests on the ordinary wall clock. The four Linux boots reported below used the instruction-counted setting. If another hypervisor reports SAFE, record the failed check and clock configuration along with the verified image digest. To test audible playback where a host audio backend is configured, replace `-audiodev none,id=snd0 -device AC97,audiodev=snd0` with `-device AC97`. [QEMU system invocation](https://www.qemu.org/docs/master/system/invocation.html)

## Firmware and desktop coverage

| Target | Evidence and scope |
| --- | --- |
| x86-64 QEMU, SeaBIOS | On a Linux host with QEMU 10.0.13 TCG, the published ISO and keyboard-01 each reached the verified launcher and powered off with **P** on both `pc` and `q35`. Each of these four fresh instruction-counted boots showed 71 passing checks. QEMU reported a guest-requested shutdown and exited with status 0 in every case. |
| UEFI optical boot | Both ISO boot catalogs contain one bootable x86 BIOS entry (platform ID `0x00`) and no EFI entry (`0xEF`). Select legacy BIOS **in the VM** for these images. A separate GRUB/OVMF experiment reached SAFE and exposed an overlap between the kernel’s fixed load address range and firmware-reserved memory. [UEFI placement evidence](uefi-probe/README.md) [UEFI optical media format, §13.3.2.1](https://uefi.org/specs/UEFI/2.10/13_Protocols_Media_Access.html) |
| Physical desktops and laptops | Native hardware, Secure Boot, USB boot, installation, persistent home storage, suspend/resume and device compatibility require separate qualification. These CD tests cover a temporary demo. Use the VM path for this tester round. |
| macOS and Windows hosts | The **published** ISO reached the verified launcher and shut down from **P** on macOS 15.8.2 (arm64) and Windows Server 2025 (AMD64). Both used QEMU 11.1.3, TCG, the x86-64 PC guest and only a read-only CD. Each reported 71 startup checks, the expected kernel measurement and a guest-requested shutdown with exit 0. These runs cover the headless emulated guest. Native ARM boot, interactive host keyboard capture, host audio and other hypervisors remain untested by this check. [macOS receipt](observations/desktop-hosts-20261120/optical-boot-macos-15.zip) · [Windows receipt](observations/desktop-hosts-20261120/optical-boot-windows-2025.zip) · [Original run](https://github.com/KirtusJ/pcp/actions/runs/44843127105) |

To repeat the desktop host check, run `python3 audit/public-live-cd/check_host_boot.py PCP-OS.iso host-boot` from the repository root (use `python` on Windows). QEMU must be on PATH, or supply `--qemu` with its full path. Choose a new output directory. The check saves the original framebuffer, serial log, list of inserted media and shutdown record. [QEMU downloads for each host](https://www.qemu.org/download/)

## Repeat the keyboard check

On Linux with QEMU, SeaBIOS, Tesseract (English) and Python 3, run the following from the repository root. Choose a new output directory for each run.

```sh
python3 audit/public-live-cd/check.py PCP-OS.iso /tmp/pcp-live-cd-run
```

The check uses an instruction-counted guest clock, reads the actual launcher framebuffer, exercises normal playback and the stop chord separately, and checks the guest’s final register and shutdown result. Its headless audio backend tests the guest’s playback path. Audible output requires a listening test with a working host audio backend.

[QEMU system invocation](https://www.qemu.org/docs/master/system/invocation.html) · [Coordination and wall-clock result](https://github.com/KirtusJ/pcp-os/issues/132#issuecomment-6913785729)

## Capture the emulator's audio output

To record the released CD's playback, add `--capture-audio` to the command above. The public-CD workflow also extracts `/clip.wav` from the pinned ISO with xorriso and checks the four bursts in both the extracted track and QEMU’s recorded audio. The expected sequence is 500 Hz on the left, 750 Hz on the right, 600 Hz on the left and 375 Hz on the right. The check measures duration, spacing and leakage into the other channel. The output directory contains the original `capture.wav`, a `captured-playable.wav` with finalized header lengths, and the measurements in `audio.json`. Loudspeaker output requires a separate listening test. [PCP OS waveform verifier](https://github.com/KirtusJ/pcp-os/blob/946ef854d908c9beb37436cf3f37284a2ad86610/apps/surfbird/guest/replay_local_media.py) · [QEMU WAV backend](https://www.qemu.org/docs/master/system/qemu-manpage.html).

## Keyboard timing fixes in kernel source

The distributed 0.3.1 CD uses the ISO and running-kernel hashes above. Later PCP OS source changes pace the blocked-reader test from an actual keyboard wait and send the longest-sleep Stop chord after ten observed idle periods. Both fixes are present at `946ef854d908c9beb37436cf3f37284a2ad86610`. [Blocked-reader change](https://github.com/KirtusJ/pcp-os/pull/63) · [Longest-sleep change](https://github.com/KirtusJ/pcp-os/pull/164).

A separately built BIOS CD with those kernel sources and the public demo payloads reached the launcher unattended on both the ordinary and instruction-counted QEMU clocks. The instruction-counted run played all 32 demo frames, returned to the launcher, stopped the relaunched app on the keyboard chord, and powered off with exit 33. Its measured kernel was `28d5db873d8b21aed141a2bf0df0064ff79fa76d73fdc9078cac006c25d86859`. [Boot configuration, media identities and retained serials](https://github.com/KirtusJ/pcp-os/pull/164#issuecomment-6915886530).

The [keyboard-01 BIOS CD candidate](candidates/keyboard-01/) carries the merged keyboard fixes. Its versioned handoff includes the ISO, rebuilt kernel and full playback and Stop observations under both guest clocks.

## Check displayed playback frames

Add `--capture-video` to the optical check to save four QEMU framebuffers during playback. Run the following command with the same ISO and output directory, and a checkout of PCP OS at `946ef854d908c9beb37436cf3f37284a2ad86610`.

```sh
python3 audit/public-live-cd/check_video.py PCP-OS.iso "$output" \
  "$OS_SOURCE/apps/surfbird/guest/replay_local_media.py"
```

The checker extracts the 32 pictures from the disc’s pinned `clip.ppm`. It compares every pixel in each captured 640 × 360 screen, including the border, with the corresponding magnified source image. Serial markers 3, 11, 19 and 27 trigger the captures. The display can advance while QEMU takes a screenshot, so each capture must identify a unique source frame in the intended eight-frame scene. Read `video.json` for the actual frame numbers and screenshot digests. The serial log records all 32 frame numbers. [PCP OS framebuffer comparison](https://github.com/KirtusJ/pcp-os/blob/946ef854d908c9beb37436cf3f37284a2ad86610/apps/surfbird/guest/replay_local_media.py) · [QEMU screen capture](https://www.qemu.org/docs/master/interop/qemu-qmp-ref.html#command-QMP.screendump) · [Netpbm PPM format](https://netpbm.sourceforge.net/doc/ppm.html)
