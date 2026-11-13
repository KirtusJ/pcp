# PCP

**Parrot Council Protocol (PCP)** is the product. **Adversarial Claim Review (ACR)** is the method inside it: an epistemological protocol that specifies how a claim is examined and what its evidence is permitted to establish. The method's text names only itself and is the same bytes in every edition; the product is everything around it. *Evidence before agreement.*

This plugin delivers the method to an assistant as skills, subagents and the pinned method text. It is the lighter of the two PCP plugins: text only.

**Version:** 1.0.19 (PCP 1.0, build 19). **Edition:** stated in `edition/`. **Method release:** manifest `6b6d3a680f3fdec811ce7105dd2124e951e272c28a24608f073914f4155853c6`. `method/` holds the method's text, each file the packet's own bytes.

## Installing

This plugin is supplied inside a Claude Code marketplace folder, `PCP_1.0_Plugins`, named after your edition: `pcp-personal`, `pcp-commercial` or `pcp-enterprise`. In Claude Code:

```
/plugin marketplace add <path to the PCP_1.0_Plugins folder>
/plugin install pcp@pcp-personal
```

For another edition, put its marketplace name after the `@`. Install this plugin or the companion `pcp-os`, not both.

## Using it

Ask for PCP or ACR in your own words, or use the commands. There is no prefix to type.

| Command | What it does |
| --- | --- |
| `/pcp:review [what] [claim] [screening, focused or full]` | Commission and run a review |
| `/pcp:halt` | Stop ACR use at once |
| `/pcp:status` | Where things stand, in plain words |
| `/pcp:modules` | The modules, and how one comes to apply |
| `/pcp:clause <module> <section>` | The exact text of a clause |
| `/pcp:about` | What PCP and ACR are, and which edition this is |

Subagents: `challenger`, `checker`, `source-inspector`, `record-auditor`.

ACR is used only when you ask for it. Having the plugin enabled changes nothing about ordinary work.

## What is in the folder

| Path | What it is | Varies with the edition |
| --- | --- | --- |
| `skills/`, `agents/` | What the assistant reads when you ask | No |
| `method/` | The method's text from the ACR Implementation packet, each file unchanged: Specifications, Overviews, guides, kernel, and the lookup tool. Not here: the packet's other programs and its probes, which are in `ACR_1.0_Implementation.zip` in the edition | No |
| `themes/` | One terminal theme per module, dark and light (`/theme`) | No |
| `edition/` | The edition: `EDITION.json` for programs, `edition.md` for the assistant | Yes, and nothing else does |
| `.claude-plugin/` | The plugin's manifest and its icon, the product emblem | No |
| `MANIFEST.json` | Every file with its SHA-256 | Only through `edition/` |

## What this plugin is, and is not

It is text. It contains no program that runs by itself, no hook and no tool server, and it uses no network access or credential of its own. The one Python file, `method/TOOLS/acr.py`, is the method packet's lookup tool; the `clause` skill may ask the assistant to run it where a shell is available.

Because it is text, nothing enforces it: the assistant follows it or does not. The companion plugin `pcp-os` adds a register whose guards run outside the assistant's context. Install one of the two, not both.

## Status

Not peer reviewed, not independently reviewed, not evaluated in use. Validated as a package with Claude Code 2.1.322, and run in live sessions there as the release record describes. A handful of sessions shows that the plugin loads and can be followed; it supports no rate and no conclusion about effect. See `NOTICE.md` and `method/RELEASE/Known_Limitations.md`.
