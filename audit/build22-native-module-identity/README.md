# Build-22 PCP OS module-name identity regression

This directory contains a **test-only, standard-library-only** regression for [issue #23](https://github.com/KirtusJ/pcp/issues/23): `pcpos module remove` can change the name supplied by the operator and then delete a *different*, correctly installed module. It does not install a new host, fix the publisher's private Rust source, change a released ZIP, or touch any real PCP register.

## Reproduce

Supply the verified Linux x86-64 `pcpos` executable and its matching ACR method folder. Every test creates its own temporary register and synthetic modules, automatically deleted afterward.

```sh
python3 audit/build22-native-module-identity/test_native_module_names.py \
  --pcpos /absolute/path/to/pcp-os/servers/linux-x86_64/pcpos \
  --method /absolute/path/to/pcp-os/method \
  --json /tmp/pcp-module-identity.json \
  --expect-fixed
```

**Exit status:** `--expect-fixed` returns exit 1 if any condition fails. Without that switch, the script returns 0 in evidence-only mode and prints `REGRESSION_RED` or `ALL_PASS`; evidence-mode exit 0 is **not** a pass. An input/tool failure returns an error rather than silently counting as a successful test.

## Observations against actual build 22

- Supplied outer release ZIP SHA-256: `6007acc5b5fe43d4639330e17ef03f4948859f42df7d857e8f713aeca6ec73b0`
- Hosted Linux x86-64 binary SHA-256: `c2c6795d36027c6e9041d63c5349f97434fe5709a6bcb649f4146faee9f03dcd`
- Method manifest SHA-256: `7ff72eed9162e2c11fc62f6681c4afbc29524bfa96b87d45a455423d027d4707`
- This script SHA-256: `564868147be6a590407db95966a8414dd6d50c9ba1e007a09412c53bfd346857`; Git blob `dc4cdc3000cbece3b8330506d0341c4d1f254ddc`

The exact script was syntax-checked and executed twice, including `--expect-fixed`. On the unmodified binary it produced:

| Case | Fixed-behavior expectation | Observed |
|---|---|---|
| `plain` | Remove `local.plain` | **PASS** |
| `alpha-beta` alongside `alpha_beta` | Delete hyphen module only | **FAIL:** underscore module deleted |
| `Upper` | Delete installed `local.Upper` | **FAIL:** refused |
| `Alpha` alongside `alpha` | Delete uppercase module only | **FAIL:** lowercase module deleted |
| `local.Mixed` | Delete installed `local.Mixed` | **FAIL:** refused |
| `acr.marker` while only `local.marker` is installed | Reject reserved-namespace target, no deletion | **FAIL:** local module deleted |

**1 of 6** exact-identity expectations passed, **5 failed**; fixed-behavior exit code **1**. The other module names and their exact bytes are checked after removal. Every resulting register was replayed successfully. This demonstrates **wrong-target deletion and ledger attribution** with a formally intact hash chain, not an OS privilege escalation, remote attack, or kernel exploit.

## Source cause and acceptance

The distributed build-22 publisher source `PCP_OS_Rust/crates/pcpos-host/src/pcpos.rs`, `module_command` remove arm, rewrites `what` with `to_ascii_lowercase().replace('-', "_")` and strips both `acr.` and `local.`. Installation preserves case and punctuation. The removal command must instead resolve **one exact canonical module identity**, refuse a requested `acr.*` release-module identifier, then confirm the target really is installed under the exclusive register lock *before* deleting anything. Keep separate obligations for unexpected directories, race handling, path confinement and write-to-ledger crash consistency ([issues #17](https://github.com/KirtusJ/pcp/issues/17), [#4](https://github.com/KirtusJ/pcp/issues/4), [#5](https://github.com/KirtusJ/pcp/issues/5), [#8](https://github.com/KirtusJ/pcp/issues/8)).

**Boundary:** the public default branch is still the packaged Enterprise build-19 release, not the separately supplied build-22 Rust publisher source. These tests cannot by themselves repair the native binary. A future fixed build must be compiled from the actual publisher source and pass this regression plus the wider native suite before any issue is closed.
