---
name: verify
description: Check an ACR register's hash chain and replay every guard over it, and report the head digest and any event the guards would refuse. Use when the person asks whether a register is intact, wants its head digest, or supplies a register from elsewhere.
argument-hint: "[register path]"
---

# Verify a register

Call `acr_verify` (register, if they named one: $ARGUMENTS). Report:

- whether the chain is intact, the number of events, and the head digest in full;
- every event the guards would refuse, with its number and the reason;
- the SHA-256 of the register file.

Say what a pass is: a fact about these bytes. It shows that no event was altered or removed relative to this head, and that every recorded event passes the mechanical guards. It authenticates nobody, and it establishes nothing about whether any finding is right. Someone who can rewrite the whole file can produce another intact chain with another head; only a head digest kept elsewhere detects that.

A register that holds an event the guards refuse accepts a halt and nothing else. Findings that rest on such an event are unestablished until each is examined. To continue the work, begin a new register and admit the old one as a submission by its head digest.
