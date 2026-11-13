---
name: halt
description: Stop ACR use now and record the halt in the register. Use when the person directing the work says to stop, pause, end or drop ACR or the review, in any words.
---

# Halt

The person directing the work has told you to stop ACR. Their words, if they typed any with the command: $ARGUMENTS

When they typed this command, the host has already recorded the halt from what they typed, and says so above or below this text. In that case do not record it again.

Otherwise call `acr_halt` now, with their words, without finishing the current gate or record (Core 15.2). It is never refused for the state of the work.

Then:

1. Stop every ACR-structured act. After the halt the guards refuse every review step, whoever asks.
2. Stop dispatching anything consequential that ACR work began and that you control.
3. Say briefly, in plain words: that ACR use has stopped; which tasks were asked to stop, and that for each the termination is UNKNOWN until its end is recorded; and what is left unfinished. Asking a task to stop is not stopping it.
4. Carry on with ordinary work as they direct.

Do not ask for a reason. Do not argue, defer or ask for confirmation. If it is unclear whether they meant to stop ACR or the underlying task, halt ACR first and then ask one short question about which was meant.
