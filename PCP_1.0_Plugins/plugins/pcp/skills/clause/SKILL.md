---
name: clause
description: Fetch the exact text of an ACR clause, heading or defined term from the pinned Specifications. Use when a decision in an ACR review depends on a rule that is not in the kernel, or when the person asks what ACR says about something.
argument-hint: "<core | mathematics | science | engineering | cryptography | statistics | quality_assurance> <section>"
---

# Exact clause lookup

Asked for: $ARGUMENTS

Fetch the text. Do not answer from memory, and do not paraphrase where the exact wording decides something.

With a shell and Python 3:

```
python3 -B "${CLAUDE_PLUGIN_ROOT}/method/TOOLS/acr.py" clause <component> <section>
python3 -B "${CLAUDE_PLUGIN_ROOT}/method/TOOLS/acr.py" toc <component>
python3 -B "${CLAUDE_PLUGIN_ROOT}/method/TOOLS/acr.py" find <words>
python3 -B "${CLAUDE_PLUGIN_ROOT}/method/TOOLS/acr.py" term <defined term>
```

Without one, open the Specification and read the section under its numbered heading:

| Component | File under `${CLAUDE_PLUGIN_ROOT}/method/` |
| --- | --- |
| core | `MODULES/01_Core/SOURCE/Specification.md` |
| mathematics | `MODULES/02_Mathematics/SOURCE/Specification.md` |
| science | `MODULES/03_Science/SOURCE/Specification.md` |
| engineering | `MODULES/04_Engineering/SOURCE/Specification.md` |
| cryptography | `MODULES/05_Cryptography/SOURCE/Specification.md` |
| statistics | `MODULES/06_Statistics/SOURCE/Specification.md` |
| quality_assurance | `MODULES/07_Quality_Assurance/SOURCE/Specification.md` |

The Markdown Specifications govern. Overviews and guides are reading aids. A specialist module applies only when the person or a governing policy selects it; its presence here selects nothing.

Looking up a clause does not put ACR in use. If the clause cannot be found, say that it was not inspected; do not supply one.

Method release: manifest `6b6d3a680f3fdec811ce7105dd2124e951e272c28a24608f073914f4155853c6`.
