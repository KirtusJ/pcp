# ACR

**Version 1.0**  
One packet. Seven modules. Two source documents per module.

Adversarial Claim Review (ACR) is an epistemological protocol, a method for reviewing a claim, a change or a piece of work: fix the subject and the question, check the decisive points, and report what the evidence supports and what it does not. ACR is the only name used in this packet; the commercial product it is supplied under is named in the Readers packet.

Ordinary work is the default. Receiving this packet changes nothing: ACR is not in use, no review exists and no module is selected until the person directing the work asks for ACR.

## Choose how you will use it

| You want to | Use | Size |
| --- | --- | --- |
| Give an assistant the essentials in one paste or a custom-instruction field | `KERNEL_CARD.md` | about 1.5 kB |
| Give an assistant the operating floor verbatim | `KERNEL.md` | see `REFERENCE/Load_Tiers.csv` |
| Run a commissioned review in full | `KERNEL.md`, then the Core Specification sections you need | retrieved as needed |
| Apply a specialist module | The above, plus that module's Specification | retrieved as needed |
| Read as a person | `MODULES/01_Core/SOURCE/Overview.md`, then other Overviews (typeset copies are in the Readers packet) | - |
| Integrate with a tool, an API or a host | `GUIDES/Integration_Guide.md` and `INTEGRATION/` | - |

Loading every document into an assistant's context is the least effective way to use ACR. Load the kernel, and fetch exact clauses when a decision depends on them (`python3 TOOLS/acr.py clause core 5.2`).

## Where to start

1. Identify the work already requested, its sources, what is uncertain, and the next permissible act. Receiving ACR does not commission anything.
2. For a commissioned review, establish the **Target** (subject) and **Claim** (question), with the scope, evidence and authority. Choose one of three procedures: **SCREENING**, **FOCUSED** or **FULL**. Only FULL runs all six gates.
3. Select only specialists relevant to the assignment. Their presence in this package does not activate them.
4. To stop, say so. A halt takes effect at once (Core Specification, Section 15.2).

## Find the source documents

Each `MODULES/` folder has an **Overview** and a **Specification** as Markdown under `SOURCE/`; typeset copies are in the Readers packet.

| Module | Location |
| --- | --- |
| Core | `MODULES/01_Core/` |
| Mathematics | `MODULES/02_Mathematics/` |
| Science | `MODULES/03_Science/` |
| Engineering | `MODULES/04_Engineering/` |
| Cryptography | `MODULES/05_Cryptography/` |
| Statistics | `MODULES/06_Statistics/` |
| Quality Assurance | `MODULES/07_Quality_Assurance/` |

The Markdown Specifications and the applicable conditional Core contracts govern. Overviews, guides, the kernel card and the typeset copies in the Readers packet are reading aids. No coding or installation is needed to read and apply the documents.

This packet supplies protocol materials, **not** external LLM services or computing. An ACR document does not grant host permissions or certify the safety of a real system.

## When the packet is handed to an assistant

An assistant given these files with no request has been given reference material. An accurate acknowledgment says what arrived and what was actually opened, and asks what is wanted. "Loaded", "indexed", "installed" and "active" name no state that ACR defines, and an acknowledgment, however detailed, does not show what was read. To find out, ask for an exact clause and compare it with the source.

## Status

ACR is untested and has not been peer reviewed; read `RELEASE/Known_Limitations.md` before relying on a result. The packet is proprietary; `NOTICE.md` states the rights in it.
