# Boot the PCP OS 0.3.1 live CD

The repository's [PCP-OS.iso](../../PCP-OS.iso) is a BIOS optical image for an x86-64 PC. It boots a graphical launcher with a local Surfbird audiovisual demo. The guest store lasts for the current boot.

From the repository root, check the ISO and boot it in QEMU with PC firmware, standard VGA and an emulated AC’97 sound card. This example uses the host’s default audio backend and specifies no writable guest disk.

```sh
echo '93ed3b599ad7be0e1e88a64813b1f2b5299d51507df2edca691aaf6189d10d15  PCP-OS.iso' | sha256sum -c -
qemu-system-x86_64 -machine pc -accel tcg -cpu qemu64 -m 64M \
  -boot order=d -cdrom PCP-OS.iso -vga std -nic none \
  -device AC97 -serial file:pcp-live-cd.log
```

The CD has one Limine entry and a zero-second timeout. Leave the keyboard alone during startup. The serial log should identify kernel 0.3.1, report long mode and show the measured code and read-only data hash `0232c02a8946d66216da0ac65953a246ce3d41d7a966ae31aa83c3335b3259e3`.

Once the launcher shows that verification passed, press **Enter** to open Surfbird. Press **Space** at its media menu to play the bundled clip. To stop an active app and return to the launcher, send **Ctrl+Alt+Delete** to the guest. Press **P** at the launcher to power off. If a keyboard self-test fails and the guest reports **SAFE**, it disables app startup. Keep the serial log when reporting that outcome. On one unattended wall-clock TCG boot, two keyboard-interrupt checks failed.

## Repeat the keyboard check

On Linux with QEMU, SeaBIOS, Tesseract (English) and Python 3, run the following from the repository root. Choose a new output directory for each run.

```sh
python3 audit/public-live-cd/check.py PCP-OS.iso /tmp/pcp-live-cd-run
```

The check uses an instruction-counted guest clock, reads the actual launcher framebuffer, exercises normal playback and the stop chord separately, and checks the guest’s final register and shutdown result. Its headless audio backend tests the guest’s playback path. Audible output requires a listening test with a working host audio backend.

[QEMU system invocation](https://www.qemu.org/docs/master/system/invocation.html) · [Coordination and wall-clock result](https://github.com/KirtusJ/pcp-os/issues/132#issuecomment-6913785729)
