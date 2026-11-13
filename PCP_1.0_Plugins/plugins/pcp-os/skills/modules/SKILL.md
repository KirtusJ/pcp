---
name: modules
description: List the modules of ACR - Core and the specialist modules - with what each is for and where its text is, and explain how a module comes to apply to a review. Use when the person asks which modules exist, asks for a science, mathematics, engineering, cryptography, statistics or quality assurance review, or asks how to select a module.
---

# Modules

Core applies whenever ACR is in use. A specialist module applies to a review only when the person directing the work, or a policy they set, selects it. Having a module here selects nothing, and you do not select one for them. If they ask for a kind of review that a module covers, say which module that is and ask whether to apply it, once.

| Module | Identifier | Role | Specification | Overview | Words |
| --- | --- | --- | --- | --- | --- |
| Core | `acr.core` 1.0 | Core | `MODULES/01_Core/SOURCE/Specification.md` | `MODULES/01_Core/SOURCE/Overview.md` | 18058 |
| Mathematics | `acr.mathematics` 1.0 | Specialist | `MODULES/02_Mathematics/SOURCE/Specification.md` | `MODULES/02_Mathematics/SOURCE/Overview.md` | 2832 |
| Science | `acr.science` 1.0 | Specialist | `MODULES/03_Science/SOURCE/Specification.md` | `MODULES/03_Science/SOURCE/Overview.md` | 4840 |
| Engineering | `acr.engineering` 1.0 | Specialist | `MODULES/04_Engineering/SOURCE/Specification.md` | `MODULES/04_Engineering/SOURCE/Overview.md` | 3959 |
| Cryptography | `acr.cryptography` 1.0 | Specialist | `MODULES/05_Cryptography/SOURCE/Specification.md` | `MODULES/05_Cryptography/SOURCE/Overview.md` | 3602 |
| Statistics | `acr.statistics` 1.0 | Specialist | `MODULES/06_Statistics/SOURCE/Specification.md` | `MODULES/06_Statistics/SOURCE/Overview.md` | 4034 |
| Quality Assurance | `acr.quality_assurance` 1.0 | Specialist | `MODULES/07_Quality_Assurance/SOURCE/Specification.md` | `MODULES/07_Quality_Assurance/SOURCE/Overview.md` | 3470 |

Paths are under `${CLAUDE_PLUGIN_ROOT}/method/`. The Specification governs; the Overview is a reading aid. Read a selected module's Specification before the first step that depends on it. No module requires another specialist module.

In this plugin a selection is in the register. `acr_modules` shows the list above as the server finds it, and the modules this workspace's reviews use. The person sets those with `/pcp-os:workspace <module ...>`; the host records what they typed, and you do not record it for them. Commission each review with those modules in `modules`.

Listing modules does not put ACR in use.
