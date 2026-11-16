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
