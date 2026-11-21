# PCP OS VM workspace

Extract the entire ZIP into one folder. Open a terminal in that folder with Python 3.10 or later and the QEMU x86 system emulator available. On systems that name Python 3 `python3`, use that name in both commands.

```text
python start.py init my-volume
python start.py run my-volume
```

The first command creates a new folder containing `data.raw` and its volume ID. Run the second command again whenever you want to reopen this VM. Keep both volume files together. To make a backup, shut down the guest with P and copy the folder.

The x86-64 guest uses QEMU software emulation, 128 MiB of RAM, one dedicated writable virtual disk, a silent audio backend and no network. The kernel selects the disk by its virtual device role, size and random volume ID. The writable store holds up to 64 KiB of file names and content.

The first launcher entry is Surfbird. Enter opens it and Space plays the local clip. Down selects the native queue desk. Enter opens it, N starts a request, and Enter saves the label you typed. Look for **Disk save**. Esc returns to the launcher and P powers the guest off. On your next boot, reopen the desk and look for your label and **Queue restored**. F marks the selected request finished.

The app explicitly syncs its journal when it saves a change. Closing an arbitrary file or powering off alone does not request a save. Start one VM at a time per volume. Physical installation, Secure Boot and recovery from host power loss require separate qualification.
