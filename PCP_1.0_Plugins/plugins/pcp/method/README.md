# ACR | Version 1.0 | Implementation packet

**Adversarial Claim Review (ACR)** is an epistemological protocol: it specifies how a claim is examined and what its evidence is permitted to establish. In practice it is a method for reviewing a claim, a change or a piece of work: fix the subject and the question, check the decisive points, and report what the evidence supports and what it does not. This packet is the implementation: one packet, seven modules, two source documents per module, with the kernel, tools, probes and release records. Every document, term and tool in it uses ACR vocabulary and no other name. The companion Readers packet carries the typeset reading copies and the commercial product identity under which ACR is sold; nothing in it is needed to use ACR. The license terms are supplied with the edition of that product under which this packet was obtained.

Open **`START_HERE.md`** to begin. For each applicable module, the **Overview** helps orientation and the **Specification** supplies the requirements. The Markdown Specification and any applicable conditional Core contract control when a reading copy differs.

- `KERNEL.md`, `KERNEL_CARD.md` - the small part meant to be held in an assistant's context. The kernel is copied verbatim from the Core Specification.
- `MODULES/` - fourteen source documents, an Overview and a Specification for each module.
- `GUIDES/` - Entry Card, module map, Safety Handbook and Integration Guide (informative).
- `SUPPLEMENTS/Core_Conditional/` - three conditional Core contracts.
- `INTEGRATION/` - an agent skill, a tool-server configuration example and behavioral probes, the means of testing an assistant against ACR.
- `TEMPLATES/` and `REFERENCE/` - working aids (a task record, a compact review record and a sheet for reading a reasoning trace beside its reply), defined terms, load tiers, path crosswalk and source indexes.
- `TOOLS/` - optional local programs: clause lookup, command parser, tool server, reference host wrapper, probe runner and release verifier. No test grants real-world permission.
- `RELEASE/` - component and source records, release status, and the evidence status and known limits (`Known_Limitations.md`).
- `NOTICE.md` - the rights in this packet.

The six specialists are available, **not automatically activated** by distribution. Ordinary authorized work does not require a commissioned review or the FULL procedure. ACR provides protocol materials, not third-party LLM access, hosting, regulatory approval or professional certification.

**Status.** Proprietary: Copyright (c) 2026 Kirtus Justus, all rights reserved; use requires a license from the rights holder (`NOTICE.md`). Untested: ACR has not been peer reviewed, independently reviewed or evaluated in use, and there is no observational evidence of its effect (`RELEASE/Known_Limitations.md`).

This packet contains no files other than Markdown, JSON, CSV and Python. `python3 TOOLS/verify_release.py` checks the file inventory, the pins and the cross-file relationships; a pass is a local fact about these files and authenticates nobody.
