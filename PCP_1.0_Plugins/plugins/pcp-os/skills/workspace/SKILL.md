---
name: workspace
description: Set or show the modules that every ACR review in this project uses - for example a science workspace, or science and statistics. Use when the person asks to make this a science (or other) workspace, to change or clear the project's modules, or asks which modules the project uses.
argument-hint: "[module ...]  e.g. science statistics; 'core' for Core only"
---

# Workspace

What they typed with the command, if anything: $ARGUMENTS

A workspace is this project's register, and its profile is the set of specialist modules its reviews use. The profile is the person's standing selection (Core 14.1 records each selected module by identifier, version and digest). It does not put ACR in use.

- **They typed this command with module names.** The host has recorded the profile itself, from what they typed, and says so. Do not record it again. Call `acr_modules`, and tell them in one or two sentences what the profile now is. If the host said a name is not a module, tell them the names that are.
- **They typed it with nothing.** Call `acr_modules` and say what the profile is and which modules exist.
- **They asked in their own words.** You cannot set the profile: it is recorded only from a command the person types or at a terminal. Tell them the command, for example `/pcp-os:workspace science`.

Each module has a colour profile, used wherever the workspace is shown: the status at a terminal names the workspace on the module's plate, and the plugin's themes (`/theme`, "PCP Science" and the others) carry the module's hue. The colour repeats what the words already say and decides nothing.
