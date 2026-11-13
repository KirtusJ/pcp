---
name: clause
description: Fetch the exact text of an ACR clause, numbered requirement or appendix from the pinned Specifications. Use when a decision in an ACR review depends on a rule that is not in the kernel, or when the person asks what ACR says about something.
argument-hint: "<core | mathematics | science | engineering | cryptography | statistics | quality_assurance> <section>"
---

# Exact clause lookup

Asked for: $ARGUMENTS

Call `acr_clause` with the module and the section's number (`15.2`, `4.5`, `Appendix A`). The server reads the Specification itself and returns the provision's exact text with its digest. Without a section it returns the module's headings. No interpreter and no shell are needed.

Do not answer from memory, and do not paraphrase where the exact wording decides something. If the tool says there is no such provision, say that it was not inspected; do not supply one.

The Markdown Specifications govern. Overviews and guides are reading aids. A specialist module applies only when the person or a governing policy selects it; looking one up selects nothing, and does not put ACR in use.

Method release: manifest `6b6d3a680f3fdec811ce7105dd2124e951e272c28a24608f073914f4155853c6`.
