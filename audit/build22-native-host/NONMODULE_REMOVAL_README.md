# Native module-removal provenance regression

This test adds a separate build-22 contract for [issue #17](https://github.com/KirtusJ/pcp/issues/17), independent of the five native-host cases in the parent PR.

Run on a **trusted, explicit** Linux x86-64 host executable and matching method folder:

```sh
python3 audit/build22-native-host/native_nonmodule_contract.py \
  --pcpos /path/to/pcpos \
  --method /path/to/pcp-os/method \
  --json /tmp/nonmodule-evidence.json
```

Append `--expect-fixed` to require all cases to pass. The test creates only disposable temporary roots. It checks a legitimate installed module that can be removed, an unrelated directory containing a synthetic note, and a directory containing a malformed `Specification.md`. For either invalid directory, a correct module-removal command must **refuse** without deleting the note, changing any register bytes, or appending a fictitious `MODULE_REMOVED` event.

Exact distributed executable tested: SHA-256 `c2c6795d36027c6e9041d63c5349f97434fe5709a6bcb649f4146faee9f03dcd`. Its normal-module control **passed**. The two invalid-directory cases **failed** as expected, both in evidence-only mode and under `--expect-fixed` (which exited 1). The submitted Python test has Git blob SHA `59d1bac928adea56809921b23552e9d8a3557816`, the same blob as the locally executed test.

This is a test-only addition, not a fix to a Rust host, kernel, or release binary. The public repository's default branch does not contain the corresponding build-22 publisher source. The test does not validate actor authority or arbitrary hostile filesystems.
