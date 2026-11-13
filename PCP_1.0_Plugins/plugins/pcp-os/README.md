# PCP OS

**Parrot Council Protocol (PCP)** is the product. **Adversarial Claim Review (ACR)** is the method inside it: an epistemological protocol that specifies how a claim is examined and what its evidence is permitted to establish. The method's text names only itself and is the same bytes in every edition; the product is everything around it. *Evidence before agreement.*

This plugin delivers the method over the native core of PCP OS: an append-only, hash-chained register whose guards check every event before it is written, in a program outside the assistant's context.

**Version:** 1.0.19 (PCP 1.0, build 19). **Edition:** stated in `edition/`. **Method release:** manifest `6b6d3a680f3fdec811ce7105dd2124e951e272c28a24608f073914f4155853c6`. `method/` holds the method's text, each file the packet's own bytes.

## Installing

This plugin is supplied inside a Claude Code marketplace folder, `PCP_1.0_Plugins`, named after your edition: `pcp-personal`, `pcp-commercial` or `pcp-enterprise`. In Claude Code:

```
/plugin marketplace add <path to the PCP_1.0_Plugins folder>
/plugin install pcp-os@pcp-personal
```

For another edition, put its marketplace name after the `@`. Install this plugin or the lighter `pcp`, not both. The program must be able to run: keep the files' permissions when you extract the archive (`unzip` does), or see `servers/README.md`.

## Using it

Ask for PCP or ACR in your own words, or use the commands. There is no prefix to type.

| Command | What it does |
| --- | --- |
| `/pcp-os:review [what] [claim] [screening, focused or full]` | Commission and run a review, recorded in the register |
| `/pcp-os:adopt` | Put ACR in use without starting a review; recorded by the host from what you typed |
| `/pcp-os:halt` | Stop ACR use at once; recorded by the host from what you typed |
| `/pcp-os:status [register]` | What the record says now: attention items, reviews, tasks |
| `/pcp-os:verify [register]` | Check the chain, replay the guards, print the head digest |
| `/pcp-os:workspace [module ...]` | The modules every review in this project uses, e.g. `science statistics`; recorded by the host from what you typed |
| `/pcp-os:modules` | The modules, and how one comes to apply |
| `/pcp-os:clause <module> <section>` | The exact text of a clause |
| `/pcp-os:system` | The operating system itself: kernel, state machines, what exists |
| `/pcp-os:about` | What PCP and ACR are, and which edition this is |

Subagents: `challenger`, `checker`, `source-inspector`, `record-auditor`. While ACR is in use, each subagent the session starts is recorded as a task, and its end is recorded from what the host observed.

ACR is used only when you ask for it. With no register in the project, the plugin's programs write nothing and say nothing.

The first time the assistant uses a register tool, Claude Code asks your permission. To allow them all at once, add `mcp__plugin_pcp-os_pcp` to the allowed tools in your settings.

## What is in the folder

| Path | What it is | Varies with the edition |
| --- | --- | --- |
| `skills/`, `agents/` | What the assistant reads when you ask | No |
| `hooks/`, `.mcp.json`, `servers/` | The program, and how the host starts it | No |
| `method/` | The method's text from the ACR Implementation packet, each file unchanged. Not here: the packet's Python programs and its probes, which are in `ACR_1.0_Implementation.zip` in the edition | No |
| `themes/` | One terminal theme per module, dark and light (`/theme`) | No |
| `edition/` | The edition: `EDITION.json` for programs, `edition.md` for the assistant | Yes, and nothing else does |
| `.claude-plugin/` | The plugin's manifest and its icon, the product emblem | No |
| `MANIFEST.json` | Every file with its SHA-256 | Only through `edition/` |

## What runs on your machine

| Part | What it does | When |
| --- | --- | --- |
| Tool server (`servers/pcpos mcp`) | Reads and appends to register files under the project directory; reads a file there, or keeps text it is handed, when asked to record it as an artifact; reads the method text in this plugin to list modules and fetch clauses. Nowhere else | While the plugin is enabled |
| Hook: session start | If a review is open, gives the assistant the record's status; after a compaction or clear, records that the assistant's context was reset | Each session start |
| Hook: prompt | Keeps a prompt you typed only if it is one of this plugin's commands or contains PCP or ACR as a word, in `.pcp/observed.jsonl` in clear text, so that an adoption can be tied to your own words. This happens whether or not ACR is in use; delete the file to discard them. Records `/pcp-os:review`, `/pcp-os:adopt`, `/pcp-os:halt` and `/pcp-os:workspace` itself | Each prompt |
| Hook: subagent start and stop | Records the task and its observed end | While ACR is in use |
| Hook: before a file write | Refuses a write by the assistant's file tools into the register's folder | Each file write |
| Hook: after a shell command | While ACR is in use, keeps what the host saw of each shell command the assistant ran: the command in clear text, its exit status and the SHA-256 digests of its output, never the output, in `.pcp/observed_tools.jsonl`, the newest 200. A check recorded with `acr_check` is taken from there, so that it is the host's observation and not the assistant's report. Outside ACR use nothing is kept; delete the file to discard them | Each shell command, while ACR is in use |

No network access and no credential is used, and no interpreter: the program is one Rust executable, and nothing in this plugin needs Python. The programs run with your rights. The programs supplied are for Linux, on x86_64 and on 64-bit ARM, each one file that needs no library from the system it runs on; `servers/README.md` says how they were built and tried. On macOS and on Windows this plugin's programs do nothing: use the `pcp` plugin there.

## Settings

Nothing needs to be set. Each of these can be changed with an environment variable in the shell that starts Claude Code, so that the tool server and the hooks see the same value.

| Variable | Default | Meaning |
| --- | --- | --- |
| `PCPOS_REGISTER` | `.pcp/register.jsonl` | The register, relative to the project directory |
| `PCPOS_PRINCIPAL` | the one person the register records as directing the work, else `principal` | The label of the person directing the work |
| `PCPOS_ACTOR` | `assistant` | The label under which the assistant's events are written |

At a terminal a person can act as themselves: `pcpos init`, `pcpos adopt`, `pcpos halt`, `pcpos standard`, `pcpos workspace`, `pcpos status`, `pcpos verify`, `pcpos repair`, `pcpos modules`, `pcpos module` (run `servers/pcpos` with no arguments for the forms). `pcpos status` names the workspace on its modules' colour plates where the terminal takes colour; `NO_COLOR` turns that off.

## Adding a module of your own

The plugin ships Core and six specialist modules and nothing else. A further module is added by a person, at a terminal, and stands beside the register in `.pcp/modules/`:

```
servers/pcpos module add .pcp/register.jsonl <folder or Specification.md> --by <your label>
servers/pcpos module list .pcp/register.jsonl
servers/pcpos module remove .pcp/register.jsonl <name> --by <your label>
```

Its Specification begins as the shipped ones do, with a line ``**Component:** `local.<name>`, Version <n>``; identifiers beginning `acr.` belong to the modules of the method. The program records the addition with the digest of that text, lists the module as `ADDED`, serves its clauses, and lets a workspace or a review select it by that digest. An added module never replaces a module of the method: an identifier the method already has is refused, and an identifier that two folders claim is served from neither. The assistant's file tools cannot write there. An added module is your text; it is not part of ACR and nothing here has reviewed it.

## What is enforced, and what is not

- **Enforced against the assistant's tool calls:** the mechanical rules of the method (order of gates, what a finding must cite, what may follow a halt); that the assistant cannot choose its actor, adopt ACR as a person (only a command you type is recorded as your own act; a request in your own words is recorded as relayed by the assistant), set a standard or the workspace's modules, or write halt, system, task and extension events of its own shaping; that a register is never reached through a link or outside the project; that two writers cannot extend the same head.
- **Checks.** A check recorded with `acr_check` is what the host reported to this program about a shell command run after the review was commissioned: that it ran, how it exited, and the digests of the output as the host passed it on, which a host may shorten when it is long. A run from before the review, or from an earlier review, is not taken. A check the assistant submits itself is recorded as its report, and a finding that rests only on such reports is marked `execution: UNKNOWN`. Neither kind shows that the command tests the claim, and the guards cannot tell a claim that a procedure settles from one that reading settles: the assistant declares the kind, and `acr_status` shows, for every finding, whether a check was run and who saw it.
- **Where material came from.** While a review is open, words the assistant hands over are recorded as its own (PRODUCED) unless the host saw you type them, a file written since the review was commissioned is recorded as PRODUCED, and the assistant cannot record material as SUPPLIED on a digest alone. A finding cannot rest only on what the review itself produced. This is bookkeeping, not proof of authorship: a file's date can be set by any program running as you.
- **The observations file is not authenticated.** `.pcp/observed_tools.jsonl` is an ordinary file. The assistant's file tools are refused there; a shell command is not, and a line written into it by hand is taken for the host's. "The host saw it run" means the host's hook reported it to this program on a computer where nothing is signed.
- **Not enforced:** whether any finding is right. Who a participant really is: labels are fixed per session and are not authentication. Anything that writes the register file without going through the tools, which on an ordinary operating system is any program running as you, including a shell command the assistant runs. The hash chain makes such a rewrite detectable only to someone who kept the head digest. The same program run from a shell with made-up hook input writes an ordinary, valid event: the record cannot tell that from the host.
- **Not a safety mechanism.** A halt stops ACR use. It is not a physical or external safe state, and a request to stop a task is not a stop.

Install this plugin or the lighter `pcp` plugin, not both.

## Status

Not peer reviewed, not independently reviewed, not evaluated in use. The program's tests passed where it was built, the plugin was validated as a package with Claude Code 2.1.322, and it was run in live sessions there as the release record describes. A handful of sessions shows that the plugin loads, that the hooks fire and that an assistant can follow it; it supports no rate and no conclusion about effect. See `NOTICE.md` and `method/RELEASE/Known_Limitations.md`.
