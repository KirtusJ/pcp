# ACR 1.0 | Known limitations and boundaries

This packet holds the ACR documents in human-readable form with optional local tools; typeset reading copies are distributed separately in the Readers packet. It is not an LLM service, a regulated safety certification or a grant of host authorization.

## Evidence status

As of 12 November 2026:

1. **Not peer reviewed.** No part of ACR has been submitted to or accepted by a peer-reviewed venue, and no standards body has reviewed or adopted it.
2. **Not independently reviewed.** Every review of these materials was performed by the party that drafted them or by AI systems working at the creator's direction. No independent expert, auditor or institution has examined them.
3. **Not empirically evaluated.** No controlled evaluation, pilot, field trial or other prospective study of ACR in use has been conducted. No assistant, model or host has been tested against ACR under conditions that support a conclusion. The behavioral probes in this packet were run on 12 November 2026 in uncontrolled sessions only: by the party that drafted ACR, with assistants of one provider, most probes once or twice, with screens that are text patterns and replies read by that same party. Those runs show that the probes can be delivered and screened. They support no rate and no conclusion about effect, and they are not the evaluation this item says is missing.
4. **No observational evidence of effect.** There is no retrospective or post-deployment study, and no outcome data about what ACR's use changed. Two single uncontrolled instances have been examined, each under conditions that were not recorded. In one, an assistant produced a review in ACR's format that departed from ACR's rules: it attributed to its subject a claim the subject disclaims, reported execution it did not demonstrate, and used status codes ACR does not define. In the other, an assistant handed the whole packet with no request reported it as loaded and indexed and summarized it with a structural error. Two instances support no rate and no conclusion about effect. They show that ACR's format and vocabulary can be reproduced without its substance.
5. **What the release checks are.** The verifier, the tool tests and the fault-injection runs verify these files and reference programs against their own specification. That is verification of the artifacts. It is not validation that ACR achieves its purpose.
6. **What the cited sources are.** The sources in each register support individual design choices in the settings those sources studied. None of them evaluates ACR, and together they do not validate it.

ACR's statements about what a participant must do are therefore specifications of intended behavior, and its expected benefits are untested hypotheses. Nothing in this packet may be described as validated, proven, certified or peer reviewed. A holder who needs evidence has to produce it: `INTEGRATION/Behavioral_Probes.md`, `TOOLS/probe_runner.py` and Core Section 14.2 describe how. The probe screens were checked only against constructed good and bad replies.

## Other limits

**Text enforces nothing.** Halt, permission, blindness and source separation are enforced only where a host enforces them. The reference tools do not enforce them.

**Reading copies.** The Readers packet holds a PDF generated from each Markdown source here; its own record states what was compared. The Markdown sources in this packet govern.

**Host wrapper.** `TOOLS/acr_host.py` was tested only with stub models. Those tests show that its halt, source separation and tool permission hold in code. They do not show that any assistant's replies follow ACR, and the wrapper's stop-phrase list is a fixed set of exact phrases. Cancellation of an in-flight model request happens only through a `model_cancel` function that the integrator supplies; it was exercised with a stub, not with any provider's client. A tool that is inside a synchronous call when a halt arrives cannot be interrupted by the wrapper: it is reported as possibly running with termination UNKNOWN, and a handle it returns afterwards is cancelled then. An earlier build reported that nothing was running in that case; the defect was found by an external review, not by this packet's own tests.

**Probe runner.** The runner records the conditions it sent, not what the provider did with them: it cannot show that a provider served the same model or defaults to each arm. The probes were written by the party that drafted ACR and are not a reserved evaluation. The sheet written by `--trace-sheet` places each returned trace beside its reply for a person to read; it compares nothing by itself.

**Reasoning and reply.** ACR's text reaches an assistant's reasoning as well as its reply, and nothing has measured what it does there: whether it improves the reasoning, consumes it with protocol administration, or changes only how the reply is worded. An assistant's reply can differ from its reasoning, and a displayed reasoning trace can differ from its processing. ACR places its duties on the reply and cannot detect a divergence by itself; a host that records the trace can look for one, and should record whether the trace is complete or a summary. An assistant's acknowledgment that it has loaded or understood ACR is a reply like any other and establishes neither. Probe results may overstate ordinary behavior, because an assistant can recognize a probe as a test.

**Single-model review.** One assistant that develops a case and then challenges it has performed a self-check. Running the two in separate calls removes exposure to the case and nothing else. The packet supplies no independent reviewer.

**Tool server.** The initialize-handshake path of `TOOLS/acr_mcp_server.py` was exercised with the official Python client library. The per-request-metadata path of revision 2026-07-28 was exercised only with this package's own test client.

**Verifier.** `TOOLS/verify_release.py` checks the file inventory and hashes, the pinned content identities, and the cross-file relationships it derives from the sources. It also runs the tools' own tests. A pass does **not** authenticate the publisher, verify natural-language statements, establish LLM behavior or grant any qualification. Anyone who can rewrite the package can rewrite the verifier; compare the printed release fingerprint with one obtained from the publisher through a separate channel.

**Component-local paths.** The Core names its three conditional contracts by component-local paths. `REFERENCE/Path_Crosswalk.csv` maps each to its packaged location. The source registers printed in each Specification's appendix are complete in themselves.

**Licensing.** The packet is proprietary and is supplied only under license (`NOTICE.md`). It contains no license terms: those are supplied with the edition of the commercial product under which the packet was obtained, and possession of the packet alone grants no rights. Any real deployment requires separately designed and tested permissions and domain-specific controls.
