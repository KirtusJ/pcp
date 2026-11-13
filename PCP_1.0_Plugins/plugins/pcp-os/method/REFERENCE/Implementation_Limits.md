# Implementation and assurance limits | ACR 1.0

This package is **one Version 1.0 distribution**: seven module directories with two source documents each, three conditional Core contracts, a kernel, guides, integration files and optional local tools. There are no separate component archives, hidden controllers or bundled audit packets.

**What the tools do.** All are standard-library Python and read-only with respect to the package.

| Tool | Does | Does not |
| --- | --- | --- |
| `TOOLS/acr.py` | Prints the kernel, an exact clause, a table of contents, search hits, defined terms, load-tier sizes and the derived clause index; checks the shape of a fidelity record | Interpret a clause, decide applicability, verify that a record is true |
| `TOOLS/command_interface.py` | Parses one message with the exact ACR-TEXT-2 profile and flags near-misses | Decide source eligibility or permission; apply anything |
| `TOOLS/acr_mcp_server.py` | Serves the same lookups to a Model Context Protocol client over standard input and output | Authenticate a client, write files, call a network |
| `TOOLS/acr_host.py` | Wraps a model function and enforces in code: kernel only while adopted, halt (with cancellation of the in-flight request when the integrator supplies a cancel function), command parsing on the person's message only, tool permission | Authenticate anyone, recognize every phrasing of stop, cancel a provider request by itself, or make a model's replies follow ACR |
| `TOOLS/probe_runner.py` | Sends constructed probes to a provider the holder configures, screens the replies, and lays each returned reasoning trace beside its reply | Certify an assistant, or compare a trace with a reply; the screens are heuristic and a person adjudicates |
| `TOOLS/selection_preflight.py` | Checks the shape of a caller-declared module selection | Select modules, authenticate anyone, authorize effects |
| `TOOLS/verify_release.py` | Checks inventory, hashes, pinned identities and derived cross-file relationships | Authenticate the publisher or validate meaning |

**Core pin.** Each specialist module names its required Core (`acr.core`, Version 1.0) and a Core descriptor SHA-256. That value is the SHA-256 of the bytes of `RELEASE/Core_Descriptor.json`, which lists the four Core definition files (Overview, Specification and three conditional contracts) with their SHA-256 digests. The verifier recomputes it.

**Kernel.** `KERNEL.md` consists of marked extracts that are byte-identical to passages of the Core Specification, with a short frame around them. The verifier checks the identity. `KERNEL_CARD.md` is a hand-written summary with section references; it is informative.

**Clause index.** `REFERENCE/Clause_Index.csv` is derived from the seven Specifications: every numbered or appendix heading and every numbered requirement paragraph. Each row is marked `INDEXED_NOT_SEMANTICALLY_VERIFIED`. It is a finding aid and not a list of audited obligations.

**Status labels.** `RELEASE/Release_Status.json` records this packet's release, licensing and evidence status. `RELEASE/Components.json` records the exact identities of its constituent sources. Neither creates a separate product version. Actual host permissions, data rights and domain obligations remain independently binding.
