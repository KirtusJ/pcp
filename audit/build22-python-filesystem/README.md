# Build-22 Python PCP OS filesystem regression contract

These are **standalone negative/positive tests**, not a copy of the proprietary PCP OS source or a corrected release. They are based on the supplied 13 November 2026 build-22 source archive `PCP_1.0_Source.zip`, SHA-256 `bbee36c4ee05f70f5062e396a8b033a80e3b3465da176c0efed3e5e5fc4f040b`. The accompanying ACR Implementation ZIP has SHA-256 `c7310f55b34ec7705b48363b95fc0839e7df96dd044c41bfd9b3183edf21abe4`.

## Run

```sh
python3 audit/build22-python-filesystem/test_guard_contracts.py \
  --python-os /absolute/path/to/PCP_1.0_Source/PCP_OS_Python \
  --method-zip /absolute/path/to/ACR_1.0_Implementation.zip
```

Only synthetic files and disposable temp workspaces are created. Importing the selected Python source executes that code with the caller's permissions: use a trusted copy, **not** an arbitrary downloaded module.

The wrapper checks the method ZIP's SHA-256 before loading the supplied Python code. On Windows, a host that denies symbolic-link creation with error 1314 explicitly skips the three symbolic-link fixtures. An otherwise passing run with those skips covers five tests. A complete run requires a host that can create the links.

## Required properties

- Replacing an object uses an exclusive, unpredictable temporary file and does not follow a planted `.tmp<PID>` link.
- Sealed method installation refuses pre-existing linked packet subdirectories before writing beyond the selected destination.
- Workspace object storage refuses symlinked `objects` directories leading outside the workspace.
- `put_bytes` and `put_file` reject a digest-named object whose bytes do not match the digest, rather than silently reporting storage success.
- Ordinary installation, replacement and storing already-correct objects continue to work.

The tests should **fail on the original vulnerable build-22 Python source** and **pass on a corrected implementation**. They exercise controlled *pre-existing* files and links. Passing them does **not** establish resistance to concurrent directory substitution, OS-level hostile permission changes, or malicious code already running with the same rights.

### First executed RED/GREEN result (13 November 2026)

An independently extracted original build-22 source produced four failing tests out of eight on the first corresponding test suite. A locally modified candidate (`base.py`, `method.py`, `store.py`) produced 8/8 passes. A subsequent complete standard discovery log reported 113 total tests: 109 passes, four feature/environment skips. Targeted original suites also passed independently under optimized Python; no complete optimized aggregate is claimed. The candidate patch, `PCP22_Python_Filesystem_Hardening.patch`, SHA-256 `70cb4c826bc03acfe7ac4d5c4df33c798c35ab3cf219fbae975e59c7bc8386b8`, was provided privately for review; **this branch does not include or publish the proprietary source patch**.

Issues: [#6](https://github.com/KirtusJ/pcp/issues/6), [#7](https://github.com/KirtusJ/pcp/issues/7), [#11](https://github.com/KirtusJ/pcp/issues/11). Do not mark these issues fixed until the repaired source, its tested binary/package, and the released identities are updated.

The current `pcp/master` is an older packaged edition, so these tests are intentionally external to its verifier. No existing edition or release artifact is modified by this PR.
