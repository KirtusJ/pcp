# The program

`pcpos` is the PCP OS host program, version 1.0.19, built from the PCP OS Rust workspace (`crates/pcpos-host`) over the same native core as the kernel, with rustc 1.97.0.

| File | For | SHA-256 | How it was tried |
| --- | --- | --- | --- |
| `linux-x86_64/pcpos` | Linux on x86_64 | `5d30c7be3f536b2086e0126851c2180ea7f8db31ed0980096c5edfc9848abd73` | Every test and scenario of the release was run on it |
| `linux-aarch64/pcpos` | Linux on 64-bit ARM | `a511c57f57e884a25f3662b213a977d46b6a5730211844fd9d1bc0ee37d70647` | The scenarios of the release were run on it under QEMU user-mode emulation. It has not been run on an ARM machine |

Each is one statically linked file: it needs no library from the system it runs on, whichever distribution that is. Neither is signed, and nothing in an edition lets you check that a program was built from its source: the source is the rights holder's and is not supplied.

`pcpos` in this folder is a short shell script that starts the program built for the system it finds itself on. Where there is none, the hooks do nothing and say nothing, and the tool server reports that it is missing. Where the program is there and has lost its permission to run, which happens when an archive is extracted by a tool that drops permissions, the script says so and gives the `chmod` command; the hooks then report an error that does not block your work.

There is no program here for macOS or for Windows. WSL 2 is Linux on x86_64, and the program was not tried there. On those systems the hooks do nothing and the tool server reports that it is missing; the `pcp` plugin, which is text, works there. The script looks for a folder named `<system>-<machine>` as `uname -s` (in lower case) and `uname -m` print them, so a program built for another system by someone who holds the source goes in such a folder.
