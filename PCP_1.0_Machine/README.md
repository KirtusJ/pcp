# PCP 1.0 | The release as data

For programs and integrators. Nothing here is needed to use PCP, and nothing here restates a rule: the Markdown Specifications in the Implementation packet govern.

| File | What it is | Standard it follows |
| --- | --- | --- |
| `pcp.machine.json` | Every module (identifier, version, digest, what it requires, how it is selected), every numbered provision as an address with the SHA-256 of its exact text and its line range, the defined terms, the load tiers, the eight state machines as tables, the kinds of event, the exit codes, and which clause each guard cites | JSON (RFC 8259). Key words counted as BCP 14 defines them (RFC 2119, RFC 8174) |
| `schemas/register-event.schema.json` | The envelope of one line of a PCP OS register | JSON Schema 2020-12 |
| `schemas/edition-profile.schema.json` | `edition/EDITION.json` inside each plugin | JSON Schema 2020-12 |
| `design/pcp.tokens.json` | The design tokens: three edition themes, seven module profiles, and the 21 workspaces they make | Design Tokens Community Group format |
| `design/pcp.tokens.css` | The same as CSS custom properties | CSS |
| `design/pcp.tokens.audit.json` | Every colour pairing measured: contrast, and separation under simulated colour-vision deficiency | WCAG 2.2 (1.4.1, 1.4.3, 1.4.11) |
| `design/pcp.terminal.tsv` | Module plates as terminal colour codes | ECMA-48 SGR, 24-bit |
| `design/themes/` | Claude Code terminal themes, one per module, dark and light | Claude Code theme files |

## Why provisions are addresses and not rule records

A rule record would need, for each requirement, an identifier, a level and the condition under which it applies. Two of the seven Specifications (Statistics, Quality Assurance) number their requirements. The other five number headings only, many requirement sentences carry no key word, and conditions are written in prose. Turning those into records would mean someone deciding what each sentence requires, which is redrafting the method. So a provision here is its module, number and title, with the digest of its exact text: a program fetches the governing words from the pinned file, and can tell at once whether they are the words a record was made under.

## Design in one paragraph

Two codes, kept apart. The **edition** sets the page: a light, a middle and a dark field, told apart by lightness first, so that they survive greyscale and colour-vision deficiency. The **module** sets the hue: seven plates, each with a wing mark and a name. A **workspace** is a module shown on an edition's page: the module's hue, moved in lightness only as far as needed to reach 4.5 to 1 against that field. Hue alone does not separate every pair of modules for every viewer; the audit file gives the figures. That is why every colour is paired with a word or a mark and no colour is the only code. Colour decides nothing in a review.
