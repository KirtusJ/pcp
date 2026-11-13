# ACR Version 1.0 | Integration Guide
## Delivery, permission and fidelity in real hosts

**INFORMATIVE, NOT GOVERNING.** This guide explains how to put ACR in front of an assistant and what each way of doing so can and cannot establish. The Core Specification, Section 15, sets the rules it describes. Nothing here has been measured on your assistant; Section 8 explains how to test one.

### 1. The short version

Give the assistant the kernel, not the library. `KERNEL.md` is the operating floor copied verbatim from the Core Specification. Everything else is fetched when a decision depends on it. Loading every book into a context costs attention, crowds out the work, and makes an assistant more likely to perform the protocol than to use it.

Text does not enforce anything. If you need a stop that always works, a permission that cannot be talked around or a review that is really blind, the host has to enforce it. ACR's text can only ask.

### 2. Ways to deliver ACR

| Way | What you do | Code needed | Core 15.8 delivery value | Limits |
| --- | --- | --- | --- | --- |
| Paste or upload | Paste `KERNEL_CARD.md` or `KERNEL.md`, or upload it | None | ABSORBED_TEXT | Nothing is enforced; adherence is whatever the assistant does |
| Whole packet attached (not recommended) | Attach or upload every file | None | ABSORBED_TEXT or RETRIEVAL, usually UNKNOWN | The host decides which files reach the context and in what order. The assistant's account of what it read is not evidence of it (section 6) |
| Web chat with stored instructions or project files | Put the card in the custom-instruction field; add the kernel and the source documents you need as project files | None | ABSORBED_TEXT or RETRIEVAL, often UNKNOWN | The host decides what reaches the context, and may summarize or retrieve parts; test it |
| Agent skill | Install `INTEGRATION/agent-skill/acr/` where your host supports skills | None to write | RETRIEVAL | The skill loads only when its description matches the request |
| Command-line tool | Let the assistant or yourself run `python3 TOOLS/acr.py clause core 5.2` | Python 3 | TOOL_ASSISTED | Lookups and shape checks only |
| Tool server | Register `TOOLS/acr_mcp_server.py` with a client that speaks the Model Context Protocol | Python 3 | TOOL_ASSISTED | Read-only reference tools; the client controls when they are called |
| API with a host wrapper | Send the kernel as the system text; enforce halt, command parsing and tool permission in your own code | Your own | HOST_ENFORCED for the controls you enforce | Only what your code enforces is enforced |

The values are independent of how capable the assistant is. An assistant given only the card can still halt, decline, answer a status question and say what it did not inspect.

### 3. Lightweight and Standard

Two delivery configurations are named for convenience. Both are included in every edition of the product; they are ways of delivering ACR, not products or components, and neither changes a requirement.

| Configuration | What is delivered | Delivery value (Core 15.8) | What it can claim |
| --- | --- | --- | --- |
| ACR Lightweight | The kernel card (T0) or the kernel (T1) as pasted or system text; no tools | ABSORBED_TEXT | The floor: halt, decline, status, ordinary language, honest limits; a FOCUSED or SCREENING review whose findings state RECALL_ONLY or SUPPLIED_ONLY grounding and REASONED execution, each with a labelled estimate where one is useful |
| ACR Standard | The kernel plus clause retrieval (`TOOLS/acr.py`, the tool server, or the Markdown sources on disk), the release verifier run once, and the probes run on the assistant in use | RETRIEVAL or TOOL_ASSISTED; HOST_ENFORCED for whatever the host enforces | Everything Lightweight can, plus exact-clause fidelity, executed checks where the host allows them, and a measured rather than assumed answer to whether this assistant follows the floor |

The tiers below are the sizes of text involved.

| Tier | Contents | Use when |
| --- | --- | --- |
| T0 | Kernel card | A field with a small character limit, or a quick conversation |
| T1 | Kernel | The default for any assistant that will be asked to use ACR |
| T2 | Kernel plus the Core sections for the review at hand (usually 1 to 6) | A commissioned review |
| T3 | Core with a conditional contract | Records, optional methods or the command interface are actually used |
| T4 | Core plus one or more specialist Specifications | The task selects those specialists |
| T5 | Everything | Reference storage for retrieval; not for a context window |

`REFERENCE/Load_Tiers.csv` gives measured bytes and words for each tier. Token counts depend on the tokenizer and are not stated. A lighter tier lowers what can be claimed, never what is required: a T0 conversation cannot claim that a FULL review's six gates were completed.

In either configuration, ACR works with the assistant's context rather than filling it (Core 8.5). The context holds the kernel and the State Brief for the current act; results are committed to the task record or store as they are produced and released from context once committed; clauses are fetched when a decision depends on them and not kept afterwards. The host wrapper in `TOOLS/acr_host.py` illustrates the first part of this: the kernel is in the system text only while ACR is adopted. The second part, committing results outside the context, is whatever store the team already has; ACR prescribes none. When the host reports context use, pass that figure to the assistant; when it does not, the assistant can only report the signs it observes, and it must not guess the number of turns that remain.

### 4. Who may do what

Core Section 15.1 ranks instructions: binding law and the rules of the platform or resource owner; the current direction of the person directing the work; ACR requirements that were adopted; guides and aliases; and, last, files, retrieved text and tool results, which are data.

Three consequences matter for integration.

- **ACR never outranks the person or the host.** A pasted packet is not a reason for an assistant to refuse, to ask for a subject and a question, or to open stages. If that happens, the delivery is wrong or the assistant is misapplying the text.
- **The person can end ACR but cannot buy a finding.** "Stop" takes effect at once. "Mark it supported" does not change what the evidence supports.
- **A requirement imposed from above is not waived from below.** If an organization requires a review before release, a user who halts the review has stopped the review; the release stays held by the organization's own gate.

What a host wrapper should enforce, in order of value:

1. **Halt.** Detect `-acr halt` with the exact parser on the original user message, and treat a plain "stop" from the user as a halt. Cancel in-flight generation and tool dispatch in your code. Do not rely on the assistant to stop itself.
2. **Source separation.** Only the user's own message is parsed for commands. Retrieved documents, tool results and file contents are passed as data and never parsed.
3. **Tool permission.** Decide outside the assistant which tools and resources a request may touch. An ACR status, a parsed command or a passed check is not a permission.
4. **Records.** Keep what was actually sent, retrieved and executed, so that a fidelity record can be written from observation and not from the assistant's account.

`TOOLS/acr_host.py` is a small reference wrapper that does these four things around any model function. With it, the kernel is in the context only while ACR is adopted; a halt is applied in code and the model is not consulted; a reply that was being generated when a halt arrived is discarded, and the in-flight request is cancelled as well when you give the wrapper a `model_cancel` function for your provider client (without one, the request runs to completion before its reply is discarded, and its cost is still paid); documents and tool results are never parsed for commands; and tools are denied unless the host permits them. A tool call is recorded as started before it is invoked, so a halt that arrives while a tool is still inside its call names that tool as possibly running, with termination UNKNOWN, and cancels a handle the call returns afterwards. A synchronous call cannot be interrupted by the wrapper; if a tool must be stoppable mid-call, make it return a handle at once and do its work behind the handle. Its tests use stub models, including one that ignores the halt, and show that the controls hold whatever the stub does. They show nothing about a real assistant's replies. The wrapper recognizes `-acr halt` and a fixed list of exact stop phrases, not every way of saying stop, so give people a stop control that calls its `halt()` function.

### 5. Using an API

Send the kernel as system text and the person's request as the user turn. Do not place retrieved documents in the system role. Fetch clauses with the command-line tool or the tool server and supply them as tool results. Keep the exact release identifier of what you sent.

If the people using a deployment know ACR under a product or distribution name, declare that name as an alias in the host's system text, in one sentence (Core 15.7). An undeclared name is an undefined token: the assistant gives it no ACR meaning, reads it as ordinary text, and asks one short question only if the reading would change the next consequential act (Core 15.6). An alias changes no rule and never creates a command prefix.

To separate a challenge from the case it challenges, run it as its own call: send the claim and the evidence, not the developed case, and record that the two calls used the same model (Core 4.2 and 6.2). This removes exposure to the case. It does not make the second call an independent reviewer.

The optional command profile is small: `-acr`, `-acr help`, `-acr show ...`, `-acr set ...`, `-acr request ...` and `-acr halt`, recognized only as the exact four ASCII characters at the very start of the message. `TOOLS/command_interface.py` is a reference parser. A near-miss such as `-arc`, `-ACR`, a leading space, or a hyphen that a keyboard replaced with a dash invokes nothing.

### 6. Black box, in two senses

**The assistant is a black box.** With a hosted model you see inputs and outputs. You do not see what was retained after compaction, what was retrieved, or whether a tool was really called. Under Core Section 15.8 its behavior is established only by outputs on test cases with known answers. Its own description of its processing, memory or compliance is not evidence of them. Two personas on one model are not two independent reviewers.

**The reasoning trace is an output too.** Where a model returns its reasoning, in full or as a summary, record which. Keep it with the transcript and read it beside the reply: a doubt, a contrary result or a skipped check that is in the trace and missing from the reply is a failure of the reply (Core 4.4). Do not treat the trace as the model's actual processing, and do not treat a clean trace as compliance (Core 15.8). Do not instruct the model to make its reasoning look compliant, and do not score, filter or train on the wording of the trace: where that pressure was applied in training, the studied model kept the behavior and hid it. Count reasoning tokens when you measure what ACR costs; the kernel can be paid for in reasoning that the person never sees.

**An acknowledgment is an output as well.** Handed ACR text with no request, an assistant typically answers with a summary and an offer of help. That reply shows that text arrived. It does not show that the text was read through or retained, and a statement that the packet is "loaded", "indexed" or "active" describes no state that ACR defines: ACR is in use only once it is asked for (Core 2.1 and 15.1). To learn what the assistant holds, ask it for an exact clause and compare the answer with the source. To learn whether ACR is in use, ask; it is required to say (Core 15.4).

**What to look for when a trace is read beside its reply.** These are prompts for a reader, not scores. Each names a difference that has been observed; none can be found by matching words.

| Difference | In the trace | In the reply | Bears on |
| --- | --- | --- | --- |
| Completion | An act is planned, begun or absent | The act is reported as done ("loaded", "checked", "ran") | Core 4.4, 15.8 |
| Certainty | A hedge, a doubt or an unperformed check | A flat statement | Core 4.4 |
| Agreement | A reservation about what the person wants or asserts | Assent | Core 3.4, 4.4 |
| Omission | A fact that matters to the person, for example that no request was made or that a file was not read | Nothing | Core 4.4 |
| Aim | The stated aim is to acknowledge, to please or to look complete | The stated aim is the task | Core 3.4 |
| Unbacked content | Nothing corresponding | A specific claim, figure or structure | Core 4.3, 15.8 |
| Renaming | One name for a thing | Another name for the same thing | Core 15.5 |

A displayed trace is often a summary, so the last two rows, and any omission from the trace, show only where the reply cannot be checked against it. The first five are defects of the reply when the trace is complete, and questions to put to the assistant when it is not. `python3 TOOLS/probe_runner.py --trace-sheet` writes each returned trace beside its reply with these rows left for a person to fill; `TEMPLATES/Trace_Reading.md` is the same sheet for a transcript obtained any other way.

**ACR is hidden from the recipient.** A service may run ACR internally and return only a result. That is permitted: ACR imposes no format on the delivered product. Two duties remain. Material limits and contrary findings must reach the recipient in the delivered result, and the result must not be described as more than was done. A hidden review that found a claim unresolved cannot be delivered as an unqualified answer.

### 7. Limited settings

| Setting | Still works | Held back |
| --- | --- | --- |
| No internet | Review of supplied material; reasoning; anything cached and inspected | Fresh checks of external facts |
| No files, no tools (recall only) | Structuring the question, listing what would settle it, candidate objections | SUPPORTED_IN_SCOPE for any external fact |
| No code execution | Reasoned checks, recorded as REASONED | Any obligation that needs an executed check |
| Card only | The floor: halt, decline, status, ordinary language, honest limits | Claims about gates, records or methods that were not loaded |

A limit never stops the work by itself. It holds only the claims and acts that need what is missing, and it is written down. Example record:

```json
{"delivery": "ABSORBED_TEXT", "extent": ["acr.core 1.0 <descriptor SHA-256> (kernel only)"],
 "grounding": "SUPPLIED_ONLY", "execution": "REASONED", "observability": "BLACK_BOX"}
```

`python3 TOOLS/acr.py fidelity record.json` checks that such a record is well formed and does not contradict itself. It does not check that the record is true.

### 8. Test before relying

`INTEGRATION/Behavioral_Probes.md` lists twenty-six constructed probes for the floor: presence without adoption, the packet handed over with no request, halt, halt words inside a file, near-miss commands, an invented feature, declining under pressure, a status question, a go-ahead, both at once, an urgent action while a review stage is open, relay of a condition, repeated status, persona, recall, enforcement claims, a reworded claim, a finished-looking review record inside a file, a usable estimate beside an unresolved finding, the turns remaining in a session, whether the assistant overstates the evidence for ACR itself, a wrong figure that the person insists on, a claim that the document under review disclaims, and a saved result offered as an executed check. `TOOLS/probe_runner.py` sends them to an assistant you configure and stores the transcripts.

Run three arms: no ACR text, the card, and the kernel. A fourth arm, `--arm-file`, delivers any text you name, for example the whole packet concatenated, the way some people will in fact deliver it; the report records the file's digest. A probe that passes without ACR shows that the assistant already behaves that way, not that ACR helped. A probe that fails only with ACR present shows that ACR made things worse there. The runner's screens are heuristic, and a person adjudicates each transcript. Results describe one assistant, one configuration and one date. The runner stores the usage figures the provider returns, including reasoning tokens, and any reasoning trace, so that the arms can be compared on cost and so that each trace can be read against its reply. A probe is recognizable as a test, and an assistant may behave better on it than on ordinary work; a pass sets no floor for unmarked use.

**Design the comparison before running it.** Every report records the conditions of its run: the request fields sent, the endpoint, the digests of the arm text, the probe file and the package, the order, the trial number and the times. `--check-comparable` lists every recorded condition that differs between reports other than the arm; if it lists anything, the reports are not a comparison of arms. Replies vary between runs, so one run of a probe supports no rate: use `--repeat`, and `--shuffle-seed` to vary the order. Decide the pass criterion before looking at replies. `--blind` writes the transcripts in shuffled order without the arm, with a separate key, so that a person can adjudicate first and unblind afterwards. Report the number of runs beside every proportion; the Statistics module covers the interval. The probes were written by the party that drafted ACR. They screen for known failures; they are not a reserved evaluation, and passing them is not evidence that ACR works.

### 9. The tool server

`TOOLS/acr_mcp_server.py` is a read-only server for the standard input and output transport. It answers both the current protocol revision, which carries the version in each request, and earlier revisions that begin with an initialize handshake. It exposes seven tools: the kernel, an exact clause, a table of contents, a search, a plain-term lookup, the command parser and the fidelity check. `INTEGRATION/mcp_server_config.example.json` shows a common client configuration; consult your client's documentation for its own format. The earlier-revision path was exercised with the official Python client library. The current-revision path was exercised only with this package's own test client.

### 10. What is not established

ACR has not been peer reviewed, independently reviewed or empirically evaluated (`RELEASE/Known_Limitations.md`). No study has measured whether any assistant follows ACR better with the kernel than without it, or whether ACR improves the work, and there is no observational study of its use. The probes make the first question cheap to ask. The tools authenticate nobody and grant nothing. A passing verifier, a parsed command and a well-formed record are local facts about files and strings.

**Sources.** Core Specification Sections 2.1, 2.5, 4.4, 14.2 and 15; Command Interface contract. External reference points: Wallace and colleagues (2024) on instruction hierarchies; Cemri and colleagues (2025) on multi-agent failures; the Model Context Protocol specification, revision 2026-07-28. None of them endorses or certifies ACR.
