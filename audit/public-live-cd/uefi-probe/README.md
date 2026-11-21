# x86-64 UEFI optical handoff

The unmodified published kernel reached its graphical SAFE screen when started by GRUB 2.12 from an experimental x86-64 UEFI CD under Q35 and OVMF. The published CD itself has only a BIOS boot entry. The VM had 256 MiB RAM, standard VGA and no attached data disk.

The loader supplied all three demo files. The kernel measured as `0232c02a8946d66216da0ac65953a246ce3d41d7a966ae31aa83c3335b3259e3`, reported 7,168 KiB of upper memory, and allocated zero program frames. Of the 40 checks it ran, 37 passed. Frame allocation, checking the limits of mapped memory and frame-memory permissions failed. The kernel refused to start a program. It found a PS/2 keyboard and a Bochs display. Its AC’97 driver did not find usable sound in this configuration.

[Original run](https://github.com/KirtusJ/pcp/actions/runs/44844660395) · [Receipt ZIP](initial-safe-control.zip) (SHA-256 `849ea2fcc655343e7a7e8288e958a55996f5bdfe5f074218b4e488082e3b2c59`). The ZIP contains the framebuffer, serial, firmware and package versions, and the QEMU invocation. A verified launcher and guest shutdown remain required for a passing probe.

To repeat on Ubuntu 24.04, see the [workflow](../../../.github/workflows/uefi-optical-probe.yml). It rebuilds the disposable CD with the original kernel and modules and keeps the observations. The GRUB memory listing is captured before the Multiboot handoff. Secure Boot, USB installation and physical systems require separate testing.
