# Native method manifest-membership regression

[Issue #21](https://github.com/KirtusJ/pcp/issues/21) demonstrates that the build-22 Rust host accepts an unlisted `acr.*` specialist alongside a completely unchanged official method manifest. This directory contains **test code only**, not a modified released method or binary.

Run against the exact method folder and native host binary you intend to check:

```sh
python3 audit/build22-method-identity/native_unlisted_module_contract.py \
  --pcpos /absolute/path/to/pcpos \
  --method /absolute/path/to/pcp-os/method \
  --json /tmp/method-identity-results.json
```

Add `--expect-fixed` to return exit **1** if the release fingerprint still appears complete or the unlisted module can still be classified, served, or selected as an official specialist. The script copies the method into a temporary directory, adds a single **synthetic** `acr.synthetic` Specification outside the unchanged manifest, and uses a new temporary register. It leaves the supplied method and any live register untouched.

**Actual build-22 RED result:** unmodified control passes; the mutated method reports the same fingerprint, discovers the unlisted specialist, serves its clause, permits a principal-labelled workspace selection, and verifies the register. All four negative predicates fail; `--expect-fixed` exited 1. The distributed Linux host SHA-256 is `c2c6795d36027c6e9041d63c5349f97434fe5709a6bcb649f4146faee9f03dcd`. The committed source Git blob `b8ccb62cdeda6f34c12c72719b675765a62db57d` is byte-identical to the executed local script.

The full ACR implementation's Python verifier rejects the corresponding extra file, demonstrating the narrower Rust/Python difference. This is a local method-directory integrity check, not an authenticated-provider assertion or proof of remote exploitation. A real fix belongs in the matching unpublished build-22 Rust publisher source; only a rebuilt and pinned binary can be declared fixed.
