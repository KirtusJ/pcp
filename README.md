# Parrot Council Protocol (PCP) 1.0 | Enterprise Edition

*Evidence before agreement.*

**Parrot Council Protocol (PCP)** is the product. **Adversarial Claim Review (ACR)** is the method inside it: an epistemological protocol that specifies how a claim is examined and what its evidence is permitted to establish.

This is the whole Enterprise Edition, build 19 of Version 1.0, dated 12 November 2026.

## What PCP does

You give an assistant a claim and the thing the claim is about: "this function works for any list", "this study shows sleep improves scores", "this proof is complete". Under ACR the assistant fixes exactly what is being claimed and what would count for and against it before it looks, inspects the thing itself instead of a description of it, runs what can be run, records what it did and did not examine, and reports what the evidence supports. It does not report more certainty than its work reached, and it says so when a conclusion rests on memory.

ACR is used only when you ask for it. At all other times the assistant works normally.

## Why two names

| | PCP | ACR |
| --- | --- | --- |
| What it is | The product: everything in this folder | The method: the rules of a review |
| Where it appears | Covers, licenses, plugin names, PCP OS | The Specifications, the kernel, every review record |
| Varies with the edition | Yes: license, roles, page theme | Never: the same bytes in every edition |
| Identified by | Version 1.0, build 19 | The digest of its release: `6b6d3a680f3fdec811ce7105dd2124e951e272c28a24608f073914f4155853c6` |

The method is written to stand alone. Its text names only itself, so a review can say exactly which rules it was held to, and those rules do not change with what you paid or which program delivered them. The product is everything that may differ around the method. Asking an assistant for "PCP" or for "ACR" gets the same thing.

## This edition

Licensed to the organization named in a signed Enterprise License Agreement, including integration into its own systems as that Agreement provides. There is no published price: the fee and terms are in your signed Agreement.

The organization assigns roles and groups and may set a floor that every installation meets. An installation may be stricter than the floor and never laxer. Whoever administers does not assess, and an auditor writes nothing.

The three editions hold the same method, the same programs and the same documents. They differ in the license, in who may take part and in which roles, and in the colour of the page.

## What is in the folder

| Item | What it is | For |
| --- | --- | --- |
| `README.md` | This overview | Reading first |
| `EDITION_GUIDE.md` | How to use the method as text in any assistant | People |
| `LICENSE.md`, `NOTICE.md`, `PRICING.md` | What is permitted, who owns it, the fixed price schedule | People |
| `EVIDENCE_STATUS.md` | What has and has not been established | Reading before relying on anything |
| `ACR_1.0_Implementation.zip` | The method: Specifications, Overviews, guides, kernel, tools, probes. Named ACR throughout; no product name, no edition | Assistants and programs |
| `PCP_1.0_Readers.zip` | Typeset reading copies of every document in this edition's theme, and the brand identity | People |
| `PCP_1.0_Plugins/` | Two plugins for Claude: `pcp` (text only) and `pcp-os` (with a recorded register). Install one | Claude Code |
| `PCP_1.0_Machine/` | The release as data: every module and provision by address and digest, the state machines, schemas, design tokens | Programs and integrators |
| `PCP_1.0_OS/` | PCP OS: its Overview and Specification, each as text and as a typeset reading copy, the requirements as data, and the default backgrounds for every workspace | People; programs |
| `THIRD_PARTY_LICENSES.md` | Notices for the open-source components compiled into the PCP OS program | People |
| `EDITION.json`, `MANIFEST.json`, `verify_edition.py` | Identity, inventory and a local check | Programs |

## Three kinds of document, kept apart

| Kind | What it is | Where |
| --- | --- | --- |
| **Specification** | The rules. Precise and normative; the only text that binds | `MODULES/*/SOURCE/Specification.md` in the Implementation packet; as data in `PCP_1.0_Machine/pcp.machine.json` |
| **Overview** | Plain language, start to finish. Explains; requires nothing | `MODULES/*/SOURCE/Overview.md`; this file, for the product |
| **Guide** | How to do a particular thing | `GUIDES/` in the Implementation packet; `EDITION_GUIDE.md`; each plugin's `README.md` |

The Specifications, Overviews and guides of the method are the same in every edition. What is written per edition is this overview, the edition guide, the license and `EDITION.json`.

## The modules

Core applies whenever ACR is in use. A specialist module applies only when you select it; nothing selects one for you.

| Module | Use it for | Colour |
| --- | --- | --- |
| Core | Any claim, change or piece of work. Always applies | Navy `#10283F`, plain wing |
| Mathematics | Proofs, derivations, computations claimed to be exact | Burgundy `#701A32`, two concentric arcs |
| Science | Studies, experiments, measurements and what they are said to show | Sky blue `#A5E7F5`, ring with a centre dot |
| Engineering | Designs, requirements, hazards and whether a system meets them | Orange `#D05D29`, two stacked chevrons |
| Cryptography | Security claims about schemes, protocols and their implementations | Violet `#34214F`, keyhole |
| Statistics | Estimates, tests, models and what the numbers support | White `#FFFFFF`, three rising bars |
| Quality Assurance | Whether a product or process was checked against what it was meant to meet | Lime `#B5D94B`, check mark |

Each module has a colour profile, used wherever a workspace of that module is shown. `PCP_1.0_Machine/design/` holds the profiles; the Readers packet's `RELEASE/Brand_And_Book_Identity.md` explains the cover design.

## Starting

**With Claude Code.** Add the plugin folder as a marketplace and install one plugin:

```
/plugin marketplace add <path to this folder>/PCP_1.0_Plugins
/plugin install pcp-os@pcp-enterprise
```

Then ask for a PCP review in your own words, or type `/pcp-os:review <what> "<the claim>"`. For a science project, type `/pcp-os:workspace science` first. `pcp` is the lighter plugin: the same method as text, with no program and no record. `PCP_1.0_Plugins/README.md` says what each does on your computer. Extract this archive with a tool that keeps file permissions (`unzip` does); `verify_edition.py` tells you if the program lost its permission to run.

**With any other assistant.** Follow `EDITION_GUIDE.md`: extract the Implementation packet and give the assistant `KERNEL.md`.

## Checking this folder

`python3 verify_edition.py` checks every file against `MANIFEST.json`, that the packets and plugins are the ones `EDITION.json` names, that the method text inside each plugin is the Implementation packet's own, file for file, and runs each packet's own verifier. A pass is a local fact about these files. It authenticates nobody and certifies nothing.

## Status

Proprietary; all rights reserved; supplied under license only. Copyright (c) 2026 Kirtus Justus.

Not peer reviewed, not independently reviewed, not evaluated in use. `EVIDENCE_STATUS.md` is the full statement, and nothing here may be described as validated, proven or certified. This is a pre-publication build. The price schedule is fixed.
