# x86-64 UEFI optical placement check

The published CD supports BIOS optical boot in a virtual machine. The **published kernel has an address conflict with OVMF** in the tested x86-64 UEFI configuration. Use the [diskless BIOS tester instructions](../README.md) for the public image.

A disposable Q35 guest with 256 MiB of RAM booted GRUB 2.12 from an experimental UEFI CD. The unmodified kernel measured as `0232c02a8946d66216da0ac65953a246ce3d41d7a966ae31aa83c3335b3259e3` and received the three original demo files. It allocated zero program frames, passed 37 of the 40 self-tests it ran and entered SAFE. Frame allocation, mapped-memory bounds and frame permissions failed. It refused to start a program. The screen showed a Bochs display and a PS/2 keyboard. The kernel reported no usable sound device.

A second boot recorded GRUB's firmware memory map before loading the kernel and reproduced SAFE. The ELF's writable data/BSS segment occupies physical addresses `[0x182000, 0x1227000)`. Its fixed 16 MiB heap intersects three GRUB-reported ACPI nonvolatile storage ranges.

| Start (inclusive) | End (exclusive) |
| --- | --- |
| `0x800000` | `0x808000` |
| `0x80b000` | `0x80c000` |
| `0x810000` | `0x900000` |

The conflict occurs at kernel placement, before the program-frame allocator selects RAM. These observations do not establish whether firmware data changed. A UEFI loader or kernel layout must avoid reserved ranges throughout the full in-memory ELF footprint, including zero-filled sections. The original kernel and published ISO remain pinned to their recorded hashes.

| Historical experiment | Original receipt | ZIP SHA-256 |
| --- | --- | --- |
| [First GRUB handoff](https://github.com/KirtusJ/pcp/actions/runs/44844660395) | [Framebuffer, serial and machine configuration](initial-safe-control.zip) | `849ea2fcc655343e7a7e8288e958a55996f5bdfe5f074218b4e488082e3b2c59` |
| [Repeated handoff with pre-boot inventory](https://github.com/KirtusJ/pcp/actions/runs/44845184441) | [Original memory listing and SAFE result](memory-map-safe-control.zip) | `f549cbf051a937bda61c957d712ff39e6eedc2b7967c29211c6c4c234557a8e5` |

The [placement workflow](../../../.github/workflows/uefi-optical-probe.yml) boots a GRUB-only diagnostic CD. The PCP kernel stays on the host. The checker validates the published ISO and kernel SHA-256, reads each ELF program header's physical address and memory size, and compares its entire load range with the live GRUB inventory. Unreported memory and overlapping reserved descriptors count as conflicts. The job passes when it reproduces the known ACPI NVS conflict. It provides a firmware diagnosis. Verified native UEFI startup, Secure Boot, physical USB and laptop support remain open.
