# Download and restore the BIOS CD

These links point to the files as published in PCP commit `0f0b34b1dbccabe9c4fe8cea80872e82e94e1de4`. Both images show kernel version 0.3.1. Use the SHA-256 digest to distinguish them. The steps below use QEMU on Linux with SeaBIOS and standard VGA. They attach only optical media. Files created inside either live guest last until it powers off.

## Try keyboard-01

1. Start in an empty directory. Download [keyboard-01.zip](https://raw.githubusercontent.com/KirtusJ/pcp/0f0b34b1dbccabe9c4fe8cea80872e82e94e1de4/audit/public-live-cd/candidates/keyboard-01/keyboard-01.zip) into it.
2. Check the archive, extract the optical image and check its digest. Continue only if both checks print `OK`.

   ```sh
   echo '995b4cb4af06163c92cf82150d61598e577dafbe70500b263718478b846c8de4  keyboard-01.zip' | sha256sum -c -
   unzip keyboard-01.zip candidate.iso
   echo '09e61116cc295f45a91061253d3913301ef867d790ee08678bd0fb25c1a0a00d  candidate.iso' | sha256sum -c -
   ```

3. Boot the candidate. Wait for the launcher, press Enter for Surfbird, and press Space to play. After the launcher returns, press P to power off.

   ```sh
   qemu-system-x86_64 -machine pc -accel tcg -cpu qemu64 -m 64M -boot order=d \
     -cdrom candidate.iso -vga std -nic none -device AC97 -serial file:candidate.log
   ```

## Return to the preceding public CD

1. After the candidate VM closes, open another empty directory. Download [PCP-OS.iso](https://raw.githubusercontent.com/KirtusJ/pcp/0f0b34b1dbccabe9c4fe8cea80872e82e94e1de4/PCP-OS.iso) there. This download is the original 0.3.1 optical image. It works even if you discarded every local copy of the original.
2. Check the digest. It must match the one below.

   ```sh
   echo '93ed3b599ad7be0e1e88a64813b1f2b5299d51507df2edca691aaf6189d10d15  PCP-OS.iso' | sha256sum -c -
   ```

3. Start a new VM from this file. The boot command below uses instruction-counted timing because the original CD can enter SAFE during keyboard self-tests under ordinary wall-clock timing.

   ```sh
   qemu-system-x86_64 -machine pc -accel tcg -cpu qemu64 -m 64M -boot order=d \
     -icount shift=3,align=off,sleep=off -cdrom PCP-OS.iso -vga std -nic none \
     -device AC97 -serial file:previous.log
   ```

4. Before entering any keys, check that the launcher appears. The recovered kernel’s measured image in `previous.log` is `0232c02a8946d66216da0ac65953a246ce3d41d7a966ae31aa83c3335b3259e3`. Enter opens Surfbird and Space plays the clip. After returning to the launcher, P powers off.

To review an application run before powering off, press **R** at the launcher. Use **Up** and **Down** to scroll the kernel register. A normal exit appears as `DONE`. Stopping a running app with **Ctrl+Alt+Delete** appears as `STOPPED`. Press **Esc** once to return to the launcher.

The scope here is switching bootable optical media. For the original public CD observations and SAFE behavior see the [public boot guide](../../README.md). [GitHub commit permalinks](https://docs.github.com/en/repositories/working-with-files/using-files/getting-permanent-links-to-files) · [QEMU guest clock options](https://www.qemu.org/docs/master/system/invocation.html)
