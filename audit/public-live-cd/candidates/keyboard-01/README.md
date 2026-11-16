# Keyboard-01 BIOS CD candidate

Download [keyboard-01.zip](keyboard-01.zip) and extract `candidate.iso` to boot this qualification build in a disposable x86 BIOS VM. The archive also contains the exact `kernel.elf32` carried on the CD. The public distribution still ships the original 0.3.1 ISO. Director 1 requested this candidate after both keyboard timing fixes landed. [Assignment](https://github.com/KirtusJ/pcp-os/issues/132#issuecomment-6918060897) · [PCP OS source](https://github.com/KirtusJ/pcp-os/tree/946ef854d908c9beb37436cf3f37284a2ad86610)

| Object | SHA-256 |
| --- | --- |
| Downloadable ZIP | `995b4cb4af06163c92cf82150d61598e577dafbe70500b263718478b846c8de4` |
| Original public 0.3.1 ISO | `93ed3b599ad7be0e1e88a64813b1f2b5299d51507df2edca691aaf6189d10d15` |
| Original kernel ELF | `d2fae4ef3df316ff4fa0c1a88744e66cc17bd794856979fa55188b8402f7222f` |
| Candidate ISO | `09e61116cc295f45a91061253d3913301ef867d790ee08678bd0fb25c1a0a00d` |
| Candidate kernel ELF | `db4ea90ea62885e0aee46cbaabbea847292c3527070935e0f7709d79d81446ef` |
| Candidate kernel measurement used by the loader grant | `a9be6b1599bb10eead1344ae4a2ca53ec978074ae9aef1d30e8da10f04d044f3` |

## Observed boots

Two fresh QEMU 8.2.2 TCG guests booted the same optical bytes using SeaBIOS, standard VGA, emulated AC’97, 64 MiB of RAM and no NIC or writable disk. The first screenshot preceded any injected key. Enter opened Surfbird, Space started the complete bundled clip, and a second Enter reopened the app after normal exit. Ctrl+Alt+Delete stopped that second launch at its media menu. The launcher reappeared after both exits. P powered off each guest.

| Observation | Ordinary wall clock | Fixed instruction clock, shift 3 |
| --- | --- | --- |
| Unattended launcher | 71 startup self-tests, launcher visible | 71 startup self-tests, launcher visible |
| Playback | Frames 0–31 in order, drained, DONE, exit 0 | Frames 0–31 in order, drained, DONE, exit 0 |
| Stereo capture | Four 400 ms bursts, L/R/L/R | Four 400 ms bursts, L/R/L/R |
| Keyboard Stop and return | STOPPED, launcher visible | STOPPED, launcher visible |
| Power-off | All self-tests passed, QEMU exit 33 | All self-tests passed, QEMU exit 33 |

Surfbird reported 3,200 ms of audio with zero device underruns in each playback. The captured stereo tracks contained 500, 750, 600 and 375 Hz starting at 200, 1000, 1800 and 2600 ms. These measurements come from the emulated device output. Each clock has its own serial log, three framebuffers and OCR transcripts, WAV capture, waveform results and exit status in the [retained observations](observations.zip). The observation archive SHA-256 is `d0b3ff40d1562e994941a5a832d69c8a41f16081bbf4377eecfbf6103e52d750`. [Original qualification run](https://github.com/KirtusJ/pcp/actions/runs/43881508882/job/133348291961)

## Distribution differences

The ELF comes from PCP OS `946ef854d908c9beb37436cf3f37284a2ad86610`, built with Rust 1.100.0. The loader configuration changes one measured-image grant. Replaying the El Torito boot equipment changes the catalog and location fields of the BIOS boot image. The script checks their recorded extents and checksums against each raw ISO. The carried app, assets, loader code outside those fields, and notices match the original. The [per-file inventory](identity.json) records both hashes for every file. [GNU xorriso manual](https://www.gnu.org/software/xorriso/man_1_xorriso.html) · [QEMU clock documentation](https://www.qemu.org/docs/master/devel/tcg-icount.html)

The screen and carried documentation still identify 0.3.1. A release decision, release version, publisher authentication and publication of a replacement default image remain open. The tests cover this emulator configuration. Physical hardware, speaker output, UEFI, installed-disk persistence and the full daily-driver workload remain unqualified here. The [public CD audit](../../README.md) retains the results for the shipping image.

## Repeat the check

The [workflow](../../../../.github/workflows/bios-cd-candidate.yml) pins the OS revision, rebuilds the ELF, compares it with the retained ELF, checks every CD file and boots the retained ISO twice. On an Ubuntu host with the tools listed in that workflow, set `OS_SOURCE` to a checkout of that OS revision and run from the PCP repository root.

```sh
candidate=audit/public-live-cd/candidates/keyboard-01/candidate.py
out=$(mktemp -d)
python3 "$candidate" inspect PCP-OS.iso "$OS_SOURCE" "$out"
python3 "$candidate" wall PCP-OS.iso "$OS_SOURCE" "$out"
python3 "$candidate" instructions PCP-OS.iso "$OS_SOURCE" "$out"
```

To assemble another disposable CD, build the kernel with the pinned toolchain and use `build` in a fresh output directory. By default the script uses the pinned OS commit’s timestamp for the ISO and ZIP. Set `SOURCE_DATE_EPOCH` to supply a different build timestamp. Use the same source CD, kernel bytes, build timestamp and tool versions when comparing rebuilds. `identity.json` records the newly assembled ISO’s digest. The published keyboard-01 archive predates this timestamp convention and has its own digest in the table above. [GNU xorriso timestamps](https://www.gnu.org/software/xorriso/man_1_xorriso.html) · [Reproducible Builds timestamp specification](https://reproducible-builds.org/specs/source-date-epoch/)

To try this candidate and then boot the preceding public CD, follow [Download and restore the BIOS CD](restore.md). It includes a pinned download of the original image for use from an empty directory.

To compare cold starts under CPU contention, run the following after `candidate.py inspect` has written the retained candidate into `$out`.

```sh
python3 audit/public-live-cd/compare_contention.py PCP-OS.iso "$out/contention" \
  --candidate "$out/candidate.iso"
```

Each image boots four times on the ordinary guest clock. The emulator shares one host CPU with a busy process. The order of the two images reverses in each successive pair. Read `contention/summary.json` for the measured kernel checks, keyboard self-test observations, launcher or SAFE outcomes, and CPU time consumed by the competing process. Each trial keeps its serial log. A SAFE startup on the original is recorded. A SAFE startup on keyboard-01 fails this candidate check. [Linux CPU affinity](https://man7.org/linux/man-pages/man2/sched_setaffinity.2.html)
