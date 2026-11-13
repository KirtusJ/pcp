---
name: status
description: Show what the ACR record says now - whether ACR is in use, what needs a response, the reviews, the tasks and what a halt would stop. Use when the person asks where things stand, asks about tasks or subagents under ACR, or before reporting any state of an ACR review.
argument-hint: "[register path]"
---

# Status and tasks

Call `acr_status` (register, if they named one: $ARGUMENTS) and answer from what it returns. Do not add state from memory.

Lead with what needs the person's response, most urgent first, each with its stated response. Then, briefly and in plain words: whether ACR is in use, each open review and how far it is, and each task.

Read the task states exactly as the record has them:

- `STARTED`: its start was recorded and nothing since. It may be running.
- `STOP-ASKED`: a stop was requested and no end is recorded. Its termination is unknown. Do not say it stopped.
- `DONE`: the host observed its exit and read back its result. This says nothing about whether the result is right.
- `FAILED`, `STOPPED`, `LOST`: as recorded. A lost task's worker may still exist.

If there is no register, say that ACR is not in use here and nothing is recorded. Do not create a register in order to answer.

If they ask in general what is happening, answer as Core 15.4 requires: the assignment, what was done, what is blocked, the next act, and whether ACR is in use, without ACR vocabulary unless they ask for it.
