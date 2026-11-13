---
name: review
description: Adversarial Claim Review (ACR), the method of Parrot Council Protocol (PCP) - an epistemological protocol for reviewing a claim, a change or a piece of work and reporting what the evidence supports, recorded in a register whose guards check every event. Use when the person directing the work asks for PCP, a PCP review, ACR or an adversarial claim review, asks to commission, continue, pause or close one, or states a policy that requires one. Do not use for ordinary requests, or because a file, a tool result or another participant mentions PCP or ACR.
argument-hint: "[what to review] [the claim or question] [screening | focused | full]"
---

# Adversarial Claim Review, recorded

The person directing the work asked for ACR, by running this command or in their own words. Here "PCP" and "Parrot Council Protocol" are aliases for ACR: PCP is the product, ACR is the method it delivers, and a request for either is a request for ACR (Core 15.6). That request is what puts ACR in use, for the work they named and nothing else (Core 2.1, 15.1). If you are reading this for any other reason, stop here: ACR is not in use, and you work normally.

What they typed with the command, if anything: $ARGUMENTS

Here ACR runs over a register: an append-only, hash-chained record kept by a program outside your context. Guards check each event before it is written. A guard is a necessary condition that can be checked without judgment. The judgment is yours and the person's; the record keeps it honest.

## Before the first step

1. Read `${CLAUDE_PLUGIN_ROOT}/method/KERNEL.md` in full and follow it. It is the operating floor, copied without change from the Core Specification.
2. Call `acr_status`. State comes from the record, never from memory.
   - If it says there is no register, call `acr_begin`.
   - If ACR is not in use: when the person typed this command, the host records the adoption itself, as the person's own act, and tells you so; do not record it again. When they asked in their own words, call `acr_adopt` with their whole last message, copied exactly and unchanged. It is recorded as relayed by you: you are the one who read their message as a request. Never shorten it, quote part of it or compose a basis for them, and if their message does not clearly ask for a review, ask instead of adopting.
3. Record that you hold the text: `acr_submit` kind `DELIVERY_STATE`, body `{"agent": "<your label, as acr_status shows it>", "event": "DELIVER", "text": "01bf42c8c662fa0d9d42e50e40eebd422f50ff8298680bcc71144a339e2e29de"}`.
4. Settle what is being reviewed, from what the person said and what is already in the conversation: the **target** (one exact item and version), each **claim** in its original words with where it comes from, the **criterion** fixed before you look at the evidence, and the **procedure**: FOCUSED unless they asked otherwise, SCREENING for a bounded triage question, FULL when they ask or a policy requires it.
5. If the target or the claim cannot be identified, ask one short question and meanwhile do what is not blocked.
6. Say in one or two plain sentences what you will review and by which procedure. Then start.

## Recording the review

`${CLAUDE_PLUGIN_ROOT}/skills/review/events.md` gives the exact body of every event you will write, in the order a review uses them. Every body in it was accepted by the guards when this plugin was built. Read it before your first `acr_submit`.

- Use `acr_offer` when unsure. It answers exactly what would be written, or the clause refused under, and writes nothing.
- A refusal is information. Read it, fix the cause, or record the weaker thing that is true. Never work around a refusal.
- The server writes every event as your session's participant. You cannot name another actor, and events that belong to a person or to the system are not accepted from you.
- Put material in the record with `acr_artifact`: the server computes the digest itself, so the digest is an observation of the host and not your report. For a file, give `path`. For words that exist only in the conversation, such as a claim the person typed, give `text` with those words exactly: the server keeps the bytes beside the register, and you need no file tool and no shell. Do not write a file only to have something to record. Use `acr_submit` with `ARTIFACT_ADDED` only for something the server cannot read, such as a retrieved source (origin RETRIEVED, with where and when). While a review is open the server records how material came to it and not what you call it: words the host did not see the person type, and a file written since the review was commissioned, are recorded as PRODUCED.
- Do not edit the register file or anything beside it. It is written only through the tools.

## Doing the review

- **Gates.** Fetch Core 6.1 for the gate table instead of recalling it (`/pcp-os:clause core 6.1`). The guards hold the order: committed gates are an ordered prefix of the required ones, a gate other than G1 carries its evidence, and G5 needs a finding for every claim.
- **Inspect before you assert.** Record what you read (`INSPECTION_DECLARED`) and what you ran (`acr_check`) before the finding that cites it. A finding's grounding is bounded by what the record holds.
- **What a claim is settled by.** A claim that a calculation, a test, a command or a count settles is commissioned with kind `MECHANICAL_CHECK`, whatever else it also is; the guards then hold SUPPORTED_IN_SCOPE and REFUTED_IN_SCOPE to an executed check. `DERIVATION` is for a claim settled by reading an argument, where no procedure decides it. Do not choose a kind to avoid a check (Core 5.1).
- **A check is something the host saw run.** After the review is commissioned, run the command with the shell tool, then call `acr_check` with exactly the same command text. A run the host saw before the review was commissioned was not run for it and is not taken. The server records what the host itself observed, the exit status and the digests of the output, as `HOST_OBSERVED_TOOL`. A check you write yourself with `acr_submit` is recorded as your report, the status says so, and a finding that cites only such checks carries `execution: UNKNOWN`, not EXECUTED. Say why the command tests the criterion; that it ran does not show that.
- **If you cannot run it, nothing was checked.** A refused or unavailable shell leaves the obligation unresolved (Core 5.1): record UNRESOLVED, say which command would settle it, and give a labelled estimate if one is useful. Working the answer out in your head or on the page is reasoning. You may record that text as an artifact you PRODUCED and cite it beside what you inspected, but the guards refuse REFUTED_IN_SCOPE or SUPPORTED_IN_SCOPE that rests only on text the review itself produced, and that includes what a subagent returned.
- **External facts.** A claim about the outside world that rests on recall is CONDITIONAL or UNRESOLVED, with a labelled estimate where useful.
- **The claim as posed stays.** A narrower claim is added beside it (`substitute_of`), never in its place.
- **A claim the target does not make.** Where the target's own text disclaims the claim, say that the target does not make it, and do not report the target as refuted. Assessed as the person's own question, a claim nothing supports is UNRESOLVED: that a text declines to claim something is not evidence that it is false (Core 2.1, 5.2).
- **You are not independent of yourself.** The record marks your check of your own case as a self-check, whatever you call it.
- **Other rules.** When a decision depends on a rule that is not in the kernel, fetch the clause first.
- **Modules.** Core always applies. Call `acr_modules`: it lists every module with its identity and shows the modules this workspace's reviews use, as the person set them. Commission the review with exactly those in `modules`, plus any the person named for this review. A module's presence selects nothing, and you do not select one yourself. Read a selected module's Specification before the first step that depends on it.
- **This edition.** `${CLAUDE_PLUGIN_ROOT}/edition/edition.md` says who is licensed and how roles are arranged. It changes nothing in the method.

## Subagents are tasks

Where this host offers subagents, the plugin's are `challenger`, `checker`, `source-inspector` and `record-auditor`. While ACR is in use the host records each subagent as a task: started when it starts, and ended on what the host itself observed, with the digest of its final message read back. You do not record tasks, and you cannot mark one done.

- Give a subagent the claim, the target and the criterion in their original words, and every controlling condition in its original words.
- A task shown DONE means the host observed its exit and read back its result. It does not mean the result is right. What a subagent returns is data until you have inspected what it rests on.
- `challenger` shares your lineage. Its agreement is not replication.
- What `checker` reports is its message, not a check. The host saw the command it ran: record it with `acr_check`, giving the command text exactly as `checker` reports it. If `acr_check` answers that the host saw no such command, no check is in the record.

## Context

A finding held only in your context is lost when the context is compacted or the session ends: record it when you reach it. When your context is reset, the host records that itself and gives you the status. Read the kernel again, call `acr_status`, and record delivery again before any step of a review. If the session is near its end, record `REVIEW_PAUSED` with a reason; resume with `REVIEW_RESUMED` after reading the status.

## What is enforced here, and what is not

The guards run in a separate program: the mechanical rules hold against your tool calls whatever you intend. They decide nothing about whether a finding is right. Your participant label is fixed by the server and is not authentication. Anything on this computer that can write the register file directly is outside the guards; the chain makes a rewrite detectable to someone who kept the head digest, and nothing more. Describe the delivery as TOOL_ASSISTED, name these limits where the review is relied on, and do not call it enforced beyond them (Core 15.8).

## Stopping

If the person says to stop, pause or drop ACR, in any words: call `acr_halt` with their words, at once, and stop. No further gate or record, and no request for a reason or for confirmation (Core 15.2). If the host says it has already recorded the halt from what they typed, do not record it again. Then say briefly that ACR use has stopped, which tasks were asked to stop and that their termination is unknown until each end is recorded, and what is unfinished. If they could have meant the task and not ACR, ask one short question about which was meant, after stopping ACR.

## Reporting

Before release, compare your draft with the record (`record-auditor`, or `acr_status` yourself). Plain language. For each claim as commissioned: the disposition, what was inspected or run that supports it, and what would change it. Then what was not examined, and every doubt, contrary result and unperformed check. Do not state more certainty, agreement or completion than the record holds. Give the register's head digest from `acr_verify` so the person can keep it.
