# Parrot Council Protocol (PCP) 1.0 | Enterprise Edition | Plugins for Claude

**Parrot Council Protocol (PCP)** is the product. **Adversarial Claim Review (ACR)** is the method inside it. This folder is a Claude Code marketplace named `pcp-enterprise` that holds the two PCP plugins. Version 1.0.19: PCP 1.0, build 19.

## Two plugins. Install one.

| Plugin | What it is | Where it runs |
| --- | --- | --- |
| `pcp` | The method as skills, subagents and the pinned method text. Text only: no program, no hook, no tool server. Nothing enforces it; the assistant follows it or does not. | Claude Code. On claude.ai and in Cowork, skills load and themes do not; not tried there. |
| `pcp-os` | The same method over the native core of PCP OS: a hash-chained register whose guards check every event in a program outside the assistant's context, module workspaces, a task view, and hooks that record what the host itself observes. | Claude Code on a computer where the program can run. The programs supplied are for Linux, on x86_64 and on 64-bit ARM; on macOS and on Windows use `pcp`. A local program does not run on claude.ai. |

Both carry the ACR 1.0 Implementation packet unchanged (manifest `6b6d3a680f3fdec811ce7105dd2124e951e272c28a24608f073914f4155853c6`), the same bytes as `ACR_1.0_Implementation.zip` in the Enterprise Edition and in every other edition.

## Installing

Extract the archive with a tool that keeps file permissions (`unzip` does): `pcp-os` starts a program, and a program that has lost its permission to run does not start. Then, in Claude Code:

```
/plugin marketplace add <path to this folder>
/plugin install pcp-os@pcp-enterprise
```

or `pcp@pcp-enterprise` for the lighter plugin. Claude Code reads the plugins from this folder where it stands, so keep the folder. To move to a later build, replace the folder and run `/plugin marketplace update pcp-enterprise`. Then ask for a PCP review in your own words, or type `/pcp-os:review` or `/pcp:review`. Each plugin's own `README.md` lists its commands and says exactly what it does on your computer.

## How the edition is kept apart

Inside each plugin, the folder `edition/` is the edition: `EDITION.json` for programs and `edition.md` for the assistant. Every other file of a plugin is the same bytes in every edition, and the build refuses to finish otherwise. A plugin therefore cannot behave differently by edition except through that one folder, and the method cannot differ at all.

## Versions

The product is Version 1.0. Each build of it has a number, and the plugins carry both as `1.0.19`, so that Claude Code can tell a corrected build from the one it replaces. Two builds are the same only if their digests are the same.

## What the license covers

`LICENSE.md`, supplied beside this folder, names these plugins and the PCP OS program among the licensed Materials. The plugins are part of the Enterprise Edition whether they reach you inside the edition's archive or in the plugins archive `PCP_1.0_Plugins_Enterprise_Edition.zip`; the plugins archive is not a separate product and carries no separate license. Nothing in this folder is legal advice.
