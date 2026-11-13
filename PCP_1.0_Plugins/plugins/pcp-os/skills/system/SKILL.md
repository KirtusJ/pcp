---
name: system
description: Working with PCP OS itself - building, starting and inspecting its kernel in a virtual machine, reading its self-test log, looking up a state machine's table, or explaining what PCP OS can and cannot do today. Use for questions about the operating system, not for running a review.
---

# PCP OS

PCP OS is in early development. Say what exists, and no more. Describing the system does not put ACR in use.

**Exists, and was started in QEMU:** a new kernel for x86_64 written in Rust. It protects its own memory and shows the protection by attempting the forbidden accesses, handles exceptions and a timer, runs the native ACR guards, runs thirteen small programs built into its image as processes in user mode (an address space each, one system-call gate, preemption by the timer, a budget, the console by capability), keeps a register of its own start, verification, processes and stop, prints a self-test log on its serial port, and stops.

**Does not exist:** a way to load a program from outside the kernel image, storage, a network, a shell, any way to run an existing program. It has not been started on hardware. Nothing in it is certified for any use, and it is not fit for use where a failure can harm people.

**On another operating system**, which is where you are now, the same core runs as an ordinary program: the tool server behind the `acr_` tools, and the hooks that record what the host observes. That program is as trustworthy as the system it runs on. It binds your tool calls; it cannot bind anything that writes the register file directly. Closing that gap is what the kernel is for, and the kernel cannot yet run a program.

## State machines

`acr_machine` prints the whole table of one machine: SYSTEM, USE, REVIEW, OBJECTION, OBLIGATION, TASK, DELIVERY, LINK. For each state and event it gives the next state, or `-` for not accepted. A table entry says what would follow. It does not show that a transition happened: that is in the register.

## Starting the kernel

From the PCP OS Rust workspace, with a Rust toolchain that has its sources, `ld.lld`, `objcopy` and `qemu-system-x86_64`:

```
crates/pcpos-kernel/run.sh
```

QEMU's exit status 33 means every self-test passed. Read the log; do not report a pass you did not read. The serial port is the only channel: there is no guest agent, and nothing can be sent to the kernel.
