# PCP OS 1.0 build-22: strict standard-value parsing

This is a standalone, read-only **behavioral regression contract** for [issue #25](https://github.com/KirtusJ/pcp/issues/25). It tests the Linux **hosted Rust `pcpos` CLI**, not the freestanding kernel. It does not update the package, change a real installation standard, or make an ACR conformance claim.

## Run

Extract the verified build-22 PCP OS Enterprise plugin and run:

```sh
python3 audit/build22-native-standard-values/test_standard_cli_values.py \
  --pcpos /absolute/path/to/pcp-os/servers/linux-x86_64/pcpos \
  --expect-fixed --json /tmp/pcp-standard-values.json
```

Every case initializes a **new temporary register** and issues one `standard ... CRITICAL` command. It reads the actual `STANDARD_SET` event, verifies the register, and checks that rejected inputs leave every register byte unchanged. Under `--expect-fixed`, exit **1** means at least one desired condition failed. Without that flag, exit 0 means observations were collected, **not that all tests passed**.

## What actually happened on the released binary

- Outer release ZIP SHA-256: `6007acc5b5fe43d4639330e17ef03f4948859f42df7d857e8f713aeca6ec73b0`.
- Hosted binary SHA-256: `c2c6795d36027c6e9041d63c5349f97434fe5709a6bcb649f4146faee9f03dcd`.
- Test script SHA-256: `e5e87e0d3039b12b5e305a52283720f6ca47d68620f315fcbee4ed9214a9416f`. Locally executed and committed Git blob: `ade44c0882053dbed26a8cff791ad1eb5b40b6b3`.

The exact script was syntax-checked and run twice. **Seven positive controls passed**, including an exact CRITICAL preset and six *intentional and valid* weaker settings. **Six malformed values were all accepted**, silently mapped to less strict settings, and written in `STANDARD_SET` events, with zero guard problems. Thus **7/13 desired checks passed, 6 failed** and fixed-behavior mode returned exit **1**.

The invalid examples were `human_adoption=tru`, `dual_authorization=treu`, `static_tasks=tru`, `offline_only=TRUE`, `method=NATIVE-ONLy` and `model_findings=MECHANICAL-ONLY`. The first four mapped to false, the method token to NATIVE_OR_PINNED, and the findings token to AS_METHOD. **None was explicitly the valid value selected in the output**. All test inputs were disposable; no real operator preference or third-party deployment was inferred.

## Acceptance

Validate enum and boolean values by exhaustive matching, with an informative refusal and zero event writes on an unrecognized value. Preserve legitimate explicit `false` and the documented alternative enum settings. Validate the entire command **before** the transaction changes any resource. Rerun the test on an actual recompiled publisher-side Rust host, along with the standard Rust test matrix.

The public `KirtusJ/pcp` default branch presently contains an **older packaged build-19 edition**, not the build-22 Rust publisher source. A test PR here is not an implementation repair. A successful local oracle on a future binary establishes only these parsed values under these conditions, not complete policy enforcement, safety certification, identity authentication, or ACR empirical benefit.
