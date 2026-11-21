# Combined BIOS tester CD

[Download the tester ZIP](keyboard-01-limine-10.zip), verify it, then extract `no-write-candidate.iso`. This opt-in image combines the keyboard-01 kernel and Limine 10.8.5. Use a fresh x86-64 QEMU VM with SeaBIOS. Attach only the virtual CD. The guest store lasts until power-off.

| File | Bytes | SHA-256 |
| --- | ---: | --- |
| `keyboard-01-limine-10.zip` | 448,347 | `ba95de848dea3aacd2c95cfca7018c4fcd38dc859d5e0c05ad961cebf17b2174` |
| `no-write-candidate.iso` | 2,293,760 | `5264e891b70a37d66541393e1fc0b135fd301b8e2097022e9b698aacdc5b3d8d` |

For either file, use `sha256sum` on Linux, `shasum -a 256` on macOS or `Get-FileHash -Algorithm SHA256` in Windows PowerShell. Compare the full digest.

## First boot

Run this command on one line from the directory containing the extracted ISO. It starts the emulated x86-64 PC with 64 MiB of RAM, its ordinary clock, a virtual optical drive and a silent audio device.

```text
qemu-system-x86_64 -machine pc -accel tcg -cpu qemu64 -m 64M -smp 1 -nic none -audiodev none,id=snd -device AC97,audiodev=snd -boot order=d,strict=on -cdrom no-write-candidate.iso
```

Wait for the verified launcher with 71 startup checks. Enter opens Surfbird and Space plays the clip. After it finishes, Enter opens the app again. Send Ctrl+Alt+Delete to the guest to stop the second launch. R opens the register, Esc returns to the launcher, and P powers off.

## What was exercised

The archived ZIP is the original output of the [qualification run](https://github.com/KirtusJ/pcp-os/actions/runs/44845429407). The extracted ISO also matches an independent local rebuild. The source [keyboard-01 CD](../keyboard-01/) used Limine 9.2.3. The combined CD identifies Limine 10.8.5 in its `readme.txt` and carries the corresponding copyright and license text in `limine.txt` (SHA-256 `f174b8ff78f6f8982a1fc992668f8486eb8cf598f6938923c22e9bb50f8338a8`). It preserves the source CD’s `license.md` and `notices.txt`. The combined kernel measurement is `a9be6b1599bb10eead1344ae4a2ca53ec978074ae9aef1d30e8da10f04d044f3`.

Linux-hosted QEMU completed playback, keyboard stop, register navigation and guest shutdown on both PC and Q35. With a disposable 512-byte-sector disk, each old-loader control wrote sector zero. The combined CD read the disk, issued zero writes and preserved every byte. Local PC and Q35 runs also completed with the CD as the only inserted medium. The 0.3.1 label on the guest screen is shared by multiple images. Use the ISO digest to report the one tested.

## Windows and macOS first-boot observations

The [desktop-host run](https://github.com/KirtusJ/pcp/actions/runs/44846392498) booted the committed ZIP on both hosts using QEMU 11.1.3, x86-64 software emulation, 64 MiB of guest RAM and the ordinary QEMU clock. Each VM had one inserted read-only CD. The guest measured the expected kernel, passed all 71 startup checks, displayed the verified launcher and powered off with QEMU exit 0. The final serial also records a successful shutdown-register check.

| Host | Original receipt | Receipt ZIP SHA-256 |
| --- | --- | --- |
| macOS 15.8.2, arm64 | [Serial, launcher and machine record](observations/macos-15.zip) | `dfb6d1c873086e351b09d5514da355ec23d39ba953b21053cc13446b1230568e` |
| Windows Server 2025, AMD64 | [Serial, launcher and machine record](observations/windows-2025.zip) | `8ec09e92edb6b537d42d94cadd7586a0b0204da16986c1a4b2c1173ea65279f0` |

Physical desktop and laptop installation, UEFI, durable storage and recovery are outside this BIOS VM qualification. [Build, checks and sources](https://github.com/KirtusJ/pcp-os/tree/a09251990402c4ce63c942d8ac21ba6cb58ecdb1/examples/optical-disk-check) · [Public 0.3.1 first boot](../../README.md)
