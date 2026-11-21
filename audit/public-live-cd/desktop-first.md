# First boot of the desktop candidate

These instructions apply to the source-built PCP OS candidate that opens on a Programs bar and shows **F1 keys**. Its optical CD lasts one session. The separate two-app VM package can save a queue on its dedicated virtual disk.

## Boot the optical CD

Use QEMU with x86-64 legacy PC BIOS (SeaBIOS). Compare the SHA-256 of `pcp-os-tester.iso` with `iso_sha256` in its accompanying `receipt.json`. From the ISO directory, run the following command. It attaches only the read-only CD and writes the serial log to the host.

```text
qemu-system-x86_64 -machine pc -accel tcg -cpu qemu64 -m 64M -boot order=d -cdrom pcp-os-tester.iso -vga std -nic none -audiodev none,id=snd0 -device AC97,audiodev=snd0 -serial file:desktop-cd.log
```

## Boot the persistent VM

Extract the entire workspace ZIP. Open a terminal in the extracted directory with Python 3.10 or later and the QEMU x86 system emulator on your path. Use `python3` if your system uses that name.

```text
python start.py init my-volume
python start.py run my-volume
```

The first command creates a new 64 KiB-capacity store in `my-volume`. The second boots with that volume as its sole writable disk. Keep `data.raw` and `volume-id.txt` together. Open one VM per volume. To back it up, copy the directory after the guest shuts down.

## Use the desktop

1. Wait for **Programs**, **F1 keys** and **verified** on the bar. Press **F5** to read the startup checks, then **Esc** to return. If you see **SAFE**, keep the serial log and screen for the failed checks.
2. Press **Space** on Home to open Programs. Use **Up/Down** to select an app and **Enter** to start it. In Surfbird, press **Space** to play the local clip. In the two-app VM, select Queue Desk, press **N**, type a label and press **Enter**. Wait for **Disk save**. After a cold restart, reopen Queue Desk and look for **Queue restored** and your label.
3. On Home, **F2** opens Settings. Use **Up/Down** and **Enter** to choose the full-width bar or centered dock for this session, then **Esc** to return. **F3** opens Files and **F4** opens the register. In Programs, **Ctrl+P** changes whether an app is pinned and **Ctrl+D** opens Details.
4. To power off from Home or Programs, release any held keys, then press **F10**. Wait for **POWER OFF** and **Enter switch off    Esc go back**. **Esc** returns to your previous selection. To confirm, press and release **Enter** once the question appears.
