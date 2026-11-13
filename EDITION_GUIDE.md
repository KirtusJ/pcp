# PCP 1.0 | Enterprise Edition Guide

**INFORMATIVE.** This guide explains how the Enterprise Edition is meant to be used. It adds no requirement to ACR and no term to the license. The Core Specification governs the method, `LICENSE.md` governs what is permitted, and `EVIDENCE_STATUS.md` states what has and has not been established about the product.

## What the organization holds

- `ACR_1.0_Implementation.zip`: the method. Sources, the kernel, tools, probes and release records. It is named ACR throughout and is the only part that is integrated or given to an AI assistant.
- `PCP_1.0_Readers.zip`: typeset reading copies of every document, for people, and the brand identity.
- `PCP_1.0_Plugins/`, `PCP_1.0_Machine/` and `PCP_1.0_OS/`: the two plugins for Claude, the release as data with the design profiles, and the PCP OS documents. `README.md` describes each. With Claude Code, a plugin is the shorter path than this guide.
- `LICENSE.md` (the License Conditions that form part of the signed Agreement), `NOTICE.md`, `PRICING.md`, `EVIDENCE_STATUS.md` and this guide.

The Implementation packet is the same in every edition, byte for byte, and carries no edition marker. Its identity is its release fingerprint and the Core descriptor digest. A finding made in an integrated system therefore rests on the same rules as a finding made anywhere else.

## Integrating ACR

1. **Pin the identity.** Record the Implementation packet's release fingerprint and the Core descriptor digest in the integration's own configuration. Run `TOOLS/verify_release.py` in the build. Compare the fingerprint with one obtained from the Licensor through a separate channel; the verifier cannot authenticate its own publisher.
2. **Enforce in the host what text cannot.** Halt, separation of instructions from data, tool permission and records are enforced only where the host enforces them (Core Section 15.1; Integration Guide, section 4). `TOOLS/acr_host.py` is a reference for the four controls, including cancellation of an in-flight model request. It is a reference, not a product.
3. **Identify the principal for each session.** The operating floor ranks the host and the principal above ACR. A multi-user platform has to bind each message to the person entitled to direct that work and to halt it (Core Sections 15.1 and 15.2).
4. **Deliver the kernel, retrieve the rest.** Keep the kernel in context only while ACR is adopted, and fetch clauses when a decision depends on them. Commit findings and controlling conditions to a store outside the model's context (Core Section 8.5).
5. **Apply the security profile that fits.** Where findings or effects cross a trust boundary, Core Section 11 states what a repository, a delivery path and an input boundary have to resolve.
6. **Test, and test again on change.** Run the behavioral probes on the deployed model and configuration in three arms, with human adjudication. Treat a model, version or prompt change as a reason to rerun them. A probe is recognizable as a test; sample unmarked production transcripts as well where your own policies allow it.
7. **Record the reasoning channel as an output.** Log whether the model returns its reasoning in full, as a summary or not at all, and log reasoning tokens. Read traces against replies for a dropped doubt, an unperformed check or an act reported as done that the trace does not show (Core Section 4.4); `TOOLS/probe_runner.py --trace-sheet` lays the two side by side. Do not treat a trace as the model's processing, and do not score, filter or train on its wording (Core Sections 14.2 and 15.8; Integration Guide, section 6).
8. **Claim only what was demonstrated.** A statement that a host supports the operating floor names the sections demonstrated by test and the settings (Core Section 14.2). It is not a certification, and the evidence status travels with it.
9. **Declare the alias if people will say PCP.** One sentence in the host's system text; the Readers packet's `README.md` gives it. The Implementation packet itself never names the product.

## Internal distribution

Where the Agreement allows distribution to affiliates, distribute the two sealed packets and the documents of this edition together, with every notice in place (`LICENSE.md`, sections 3 and 4).

## What remains the organization's responsibility

The choice of model and provider, the enforcement of every control, the testing, and every decision made with the results. PCP supplies protocol materials. It supplies no model, no hosting and no assurance.
