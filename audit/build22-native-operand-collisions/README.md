# Build-22 native CLI operand identity regression

This test-only regression is for [pcp issue #27](https://github.com/KirtusJ/pcp/issues/27). It is specifically about **positional operands being discarded when they have the same text as a flag's value**, not about invalid enum/boolean coercion (issue #25).

Run against the **build-22 Linux x86-64 hosted** `pcpos` executable and the matching ACR method directory:

```sh
python3 audit/build22-native-operand-collisions/test_cli_flag_operand_collisions.py \
  --pcpos /absolute/path/to/pcpos \
  --method /absolute/path/to/pcp-os/method \
  --expect-fixed --json /tmp/pcp-flag-collision.json
```

Every case creates its own temporary register, makes one terminal `standard` or `workspace` call, reads the actual event and verifies the resulting register. With `--expect-fixed`, exit 1 means a reported mismatch; without it the script reports observations and exit 0 does **not** establish a pass.

**Observed on supplied build 22:** executable SHA-256 `c2c6795d36027c6e9041d63c5349f97434fe5709a6bcb649f4146faee9f03dcd`, method fingerprint `7ff72eed9162e2c11fc62f6681c4afbc29524bfa96b87d45a455423d027d4707`. Three ordinary controls passed. Three valid collision cases failed: principal `CRITICAL` requesting `CRITICAL` recorded BASELINE; principal `science` requesting Science recorded no specialist; principal `mathematics` requesting Mathematics likewise recorded no specialist. Each register was internally valid. The submitted test code's Git blob `85a42a5ffe1d7c5caf4716b59365368a003c8a6b` matches the locally executed source.

**Acceptance:** consume flag values by **position**, not by equality with unrelated positional strings. Reject missing or unknown flags. Retain one-to-one user-supplied module identities, regardless of actor names. Execute again on a recompiled Rust host. These tests do not modify the native implementation; that source is separately available in [KirtusJ/pcp-os](https://github.com/KirtusJ/pcp-os).
