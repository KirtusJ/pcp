# Build-22 native PCP OS host regression contract

This test-only folder exercises **five known native-host filesystem / evidence-integrity defects** and **two valid controls** using the actual Linux x86-64 `pcpos` binary. It does not include proprietary Rust source or replace a released program.

**Evidence identities (13 November 2026):**

- Owner-supplied outer `PCP_1.0_Release(8).zip`: SHA-256 `6007acc5b5fe43d4639330e17ef03f4948859f42df7d857e8f713aeca6ec73b0`.
- Binary: `c2c6795d36027c6e9041d63c5349f97434fe5709a6bcb649f4146faee9f03dcd`.
- `pcp-os/method/MANIFEST.json` bytes: SHA-256 `7ff72eed9162e2c11fc62f6681c4afbc29524bfa96b87d45a455423d027d4707`.
- Committed test program SHA-256: `3524fbf3e4cd3b7bed84aa036e2508b709d468127e8ca5fb144913f564cbd234`; Git blob SHA `69ba4c836f3f0e4e1adf22b02ba051961c11ab62` was checked against the locally executed program.

## How to run

Extract the Enterprise edition's build-22 `pcp-os` plugin to a trusted location and run:

```sh
python3 audit/build22-native-host/native_host_contract.py \
  --pcpos /absolute/path/to/pcp-os/servers/linux-x86_64/pcpos \
  --method /absolute/path/to/pcp-os/method \
  --rounds 3 \
  --expect-fixed \
  --json /tmp/native-host-regression.json
```

The script creates synthetic, disposable temporary directories, registers, and exterior sentinel files. Its `--expect-fixed` mode returns **exit 1 if any check fails**. With the vulnerable build it should fail, so the expected historical RED result is exit 1. Without `--expect-fixed`, it returns exit 0 and writes observations for an evidence-gathering run; that exit status is not a conformance result.

## Controls and targets

| Case | Property | Issue |
| --- | --- | --- |
| `normal` | A normal module is added; a sequential duplicate is refused; chain remains sound | Positive control |
| `race` | Concurrent proposals for the same module ID cannot append multiple accepted additions; the installed Specification must match the sole recorded digest | [#4](https://github.com/KirtusJ/pcp/issues/4) |
| `module_symlink` | A prelinked module folder must not cause exterior writes | [#8](https://github.com/KirtusJ/pcp/issues/8) |
| `failed_remove` | Failed register append must not leave a module physically removed without a recorded transition | [#5](https://github.com/KirtusJ/pcp/issues/5) |
| `repair_symlink` | A prelinked fragment sidecar must not overwrite an exterior file | [#9](https://github.com/KirtusJ/pcp/issues/9) |
| `artifact_hardlink` | Text artifact storage must not overwrite an exterior hard-linked inode | [#10](https://github.com/KirtusJ/pcp/issues/10) |
| `artifact_read` | In-root ordinary artifact readable; symlink, parent link, traversal and exterior absolute path refused | Positive control |

## Actual executed outcomes

The byte-identical script was syntax-checked with `python -m py_compile` and executed against the pinned released host.

- Evidence mode, two racing rounds: **6/8** and **6/8** duplicate module installs accepted, with corresponding events and intact register verification. All four other adverse cases reproduced; both positive controls passed.
- `--expect-fixed` mode, two more racing rounds: **5/8** and **5/8** accepted. Exited **1** with `REGRESSION_FAIL: race, module_symlink, failed_remove, repair_symlink, artifact_hardlink`. The two positive controls again passed.
- Additional refreshed two-round run with the strengthened on-disk identity oracle: **4/8** and **7/8** accepted, matching 4 and 7 recorded addition events while the register verified. The installed-file digest and sole-event comparison correctly failed. A finite collision-free race test after a fix cannot prove the absence of races. Repeat it and inspect transaction ordering; include interruption points and real filesystem snapshots.
- The file-size injection is POSIX-specific, and these controls have not been run against a repaired binary, on real hardware, or on another host OS.

## Important boundaries

A successful hash-chain replay **does not** establish that external filesystem state matches what the ledger says. No privilege escalation was demonstrated. The host runs under the operating system's existing permissions; only controlled synthetic exterior files were modified.

This folder is a **regression contract** for the current deficits, not an OS assurance certificate. The actual build-22 Rust source is not in `pcp/master`, which remains the older packaged build-19 distribution. Preserve the historical release, publish a corrected source/binary separately, and rerun the checks before changing the issue statuses. External expert review and empirical effectiveness assessment remain unperformed.
