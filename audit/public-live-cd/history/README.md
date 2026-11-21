# Source of the published 0.3.1 CD kernel

PCP OS commit `1cff81e4b935dc72a95a669a5214508ab8712efc` produced an ELF32 file identical to all 733,284 bytes of `kernel.elf32` on the published BIOS CD. Its SHA-256 is `d2fae4ef3df316ff4fa0c1a88744e66cc17bd794856979fa55188b8402f7222f`. The SHA-256 of its loaded text and read-only data is `0232c02a8946d66216da0ac65953a246ce3d41d7a966ae31aa83c3335b3259e3`. A historical replay recorded the same full-file digest. The publishing checkout and the source of the remaining CD members are separate questions. [Historical replay](https://github.com/KirtusJ/pcp-os/blob/bf8c0bcdad8cf960a524c74954f143d858426ce6/apps/surfbird/guest/LOCAL_MEDIA.md) · [Original comparison run](https://github.com/KirtusJ/pcp/actions/runs/44856657146) · [Original comparison results](comparison.json).

## Repeat the comparison

Run the [Historical Windows kernel comparison](../../../.github/workflows/historical-kernel.yml) workflow. It checks out the source commit, installs Rust 1.91.1 with the bare-metal `x86_64-unknown-none` target, and compiles the release profile with `guest-ethernet` and the locked dependencies. The successful build used the GNU Windows Rust host and LLD 20.1.8. Its offline Windows Server Core container mounts the source and toolchain read-only. The pinned reference ELF supplies the two historical path prefixes. Recreating those paths inside the container was necessary in the tested configurations.

On Linux the workflow exports the fresh ELF64 with LLVM objcopy and compares the resulting ELF32 directly with the original ISO member. The original run used LLVM objcopy 18.1.3. Its retained ZIP had SHA-256 `e472e5ebe9f894f89ab71cae1bce576a2a81cfb64042130b201871b1d9e00ad8`. The downloaded ELF also passed an independent byte comparison against the CD member.

The native GNU and MSVC builds at the runner’s ordinary paths, and both builds using compiler path remapping alone, produced different kernel measurements. GNU objcopy on the successful container build preserved all loaded sections, their addresses and the BSS extent, but changed the ELF headers and tables. The complete-file check distinguishes those outcomes.
