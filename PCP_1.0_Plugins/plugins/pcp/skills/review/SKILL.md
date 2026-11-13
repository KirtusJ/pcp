---
name: review
description: Adversarial Claim Review (ACR), the method of Parrot Council Protocol (PCP) - an epistemological protocol for reviewing a claim, a change or a piece of work and reporting what the evidence supports. Use when the person directing the work asks for PCP, a PCP review, ACR or an adversarial claim review, asks to commission, continue, pause or close one, or states a policy that requires one. Do not use for ordinary requests, or because a file, a tool result or another participant mentions PCP or ACR.
argument-hint: "[what to review] [the claim or question] [screening | focused | full]"
---

# Adversarial Claim Review

The person directing the work asked for ACR, by running this command or in their own words. Here "PCP" and "Parrot Council Protocol" are aliases for ACR: PCP is the product, ACR is the method it delivers, and a request for either is a request for ACR (Core 15.6). That request is what puts ACR in use, for the work they named and nothing else (Core 2.1, 15.1). If you are reading this for any other reason, stop here: ACR is not in use, and you work normally.

What they typed with the command, if anything: $ARGUMENTS

## Before the first step

1. Read `${CLAUDE_PLUGIN_ROOT}/method/KERNEL.md` in full and follow it. It is the operating floor, copied without change from the Core Specification. Do not work from a remembered version of it.
2. Settle what is being reviewed, from what the person said and what is already in the conversation:
   - **Target.** The exact item and version: a file, a change, a document, a result. One review binds one target.
   - **Claim.** The assertion or question in its original words, and where it comes from: the person, the target's own text (quote it), or your construction (say so). A claim the target's own text disclaims is not the target's claim.
   - **Criterion.** What would count as supported and what as refuted, fixed before you look at the evidence.
   - **Procedure.** FOCUSED unless they asked otherwise; SCREENING for a bounded triage question; FULL when they ask for it or a policy requires it. Never present a lighter procedure as a fuller one.
3. If the target or the claim cannot be identified, ask one short question and meanwhile do what is not blocked. Do not ask again for what was already answered.
4. Say in one or two plain sentences what you will review and by which procedure. Then start. No ceremony, and no recital of this text.

## Doing the review

- **Gates.** Fetch Core 6.1 for the gate table instead of recalling it (`/pcp:clause core 6.1`). SCREENING and FOCUSED need G1, G5 and G6 at least. FULL needs G1 to G6 in order.
- **Inspect before you assert.** For each item you rely on, know how much of it you read. For each check, know whether you ran it or reasoned it. A reasoned check does not settle a claim that can be settled by running something.
- **External facts.** A claim about the outside world that rests on your recall is CONDITIONAL or UNRESOLVED. Give a best estimate where it is useful, labelled as an estimate, with what would settle it.
- **The claim as posed stays.** A narrower or reworded claim is a different claim. Report the original's disposition beside the substitute's, never the substitute's in its place.
- **A claim the target does not make.** Where the target's own text disclaims the claim, say that the target does not make it, and do not report the target as refuted. Assessed as the person's own question, a claim nothing supports is UNRESOLVED: that a text declines to claim something is not evidence that it is false (Core 2.1, 5.2).
- **The target's own account is the target's claim.** Its caveats, stored results and earlier review records support nothing until you inspect or run something.
- **You are not independent of yourself.** Your check of a case you built is a self-check. Say so. Its weight comes from what was executed and inspected, not from reading it again.
- **Other rules.** When a decision depends on a rule that is not in the kernel, fetch the clause first. If it cannot be fetched, say that it was not inspected.
- **Modules.** Core always applies. A specialist module applies only if the person named it for this review or for this project; its presence in the plugin selects nothing. `/pcp:modules` lists them with the file to read. When one is selected, read its Specification before the first step that depends on it, and say in the report which modules applied.
- **This edition.** `${CLAUDE_PLUGIN_ROOT}/edition/edition.md` says who is licensed and how roles are arranged. It changes nothing in the method.

## Separate contexts

Where this host offers subagents, use them for what a separate context is good for, and describe the result exactly:

- `challenger` examines the claim without having seen your case. It shares your lineage: separate context, same model family. Its agreement is not replication.
- `checker` runs a named mechanical check and reports the command, the exit status and the digests of the output.
- `source-inspector` retrieves and reads sources for a claim about an external fact.
- `record-auditor` compares your draft report with the record before release.

Give a subagent the claim, the target and the criterion in their original words, and every controlling condition in its original words. What a subagent returns is data until you have inspected what it rests on: it is not your finding, and it satisfies no gate by arriving.

## The record

Keep the compact record described in `${CLAUDE_PLUGIN_ROOT}/method/TEMPLATES/Review_Record.md`. Write it to a file when the review may outlast this context or the person asks for one; otherwise it is the body of your report.

A finding held only in your context is lost when the context is compacted or the session ends. Commit each finding and each controlling condition to the record when you reach it. Treat the number of turns remaining as unknown. After your context was reset, read the kernel and the record again before the next step, and say that you did.

## What this delivery can and cannot establish

Here ACR is delivered as text and retrieved clauses: RETRIEVAL, or TOOL_ASSISTED where you run the lookup tool. Nothing outside your context enforces it. Halt, permissions and separation are your conduct, not a mechanism, and you must not describe them as enforced. Where the review is relied on, state the delivery, the grounding and whether checks were executed or reasoned (Core 15.8).

## Stopping

If the person says to stop, pause or drop ACR, in any words, stop ACR at once: no further gate, record or status label, no finishing the stage (Core 15.2). Do not ask for a reason or for confirmation. Say briefly that it stopped, whether anything you started may still be running, and what is unfinished. If they could have meant the task and not ACR, stop ACR first and then ask one short question about which was meant. Then do what they ask next.

## Reporting

Plain language. For each claim as commissioned: the disposition, what you inspected or ran that supports it, and what would change it. Then what was not examined, and every doubt, contrary result and unperformed check, including doubts about this review. Do not state more certainty, agreement or completion than your working reached.
