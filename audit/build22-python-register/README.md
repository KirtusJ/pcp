# Build-22 Python PCP OS register consistency checks

**Scope:** standalone regression contracts for the Python compatibility implementation supplied with the 13 November 2026 release. These are not release fixes, nor do they add the proprietary build-22 source to the older build-19 `pcp/master` edition.

**Original source:** `PCP_1.0_Source.zip`, SHA-256 `bbee36c4ee05f70f5062e396a8b033a80e3b3465da176c0efed3e5e5fc4f040b`. These tests import and execute whichever local source folder is explicitly supplied; only run with a trusted original/candidate copy.

## Usage

```sh
python3 audit/build22-python-register/test_register_contracts.py \
  --python-os /absolute/path/to/PCP_1.0_Source/PCP_OS_Python
```

All files, links, synthetic events and locks are created under newly allocated temporary directories. No repository register, real deployment or network service is used.

## Requirements tested

1. A normal register appends and reads one event, with a single-link regular file.
2. An existing symlink or hard link on `register.jsonl` is rejected before append, leaving the controlled external target unchanged. See [issue #14](https://github.com/KirtusJ/pcp/issues/14).
3. A register repair cooperates with the writer lock. Under a constructed two-thread schedule, a writer fsyncs an incomplete line's valid remainder while holding the lock; repair must not replace the register from its stale partial snapshot and erase the completed event. See [issue #12](https://github.com/KirtusJ/pcp/issues/12).

## Executed RED/GREEN evidence

Against an independently extracted original build-22 Python source, these three tests produced **three failures** (one repair failure and two link subtest failures), exit 1. The regular-append control passed. Against a locally hardened candidate, the same original local test file produced **three passing tests**, exit 0. The candidate's full Python discovery suite separately reported **117 tests, four skipped**, with the declared environment. The test file as committed in this PR was copied from the locally executed contract; after publication it should be executed from a fresh GitHub checkout before any acceptance claim.

Candidate source patch `PCP22_Python_Hardening_Candidate.patch`, SHA-256 `78866e6fd30254fcadb856d66d685cb47cf807304d01445e32add9546d45307f`, is **not included** in this PR and has not been incorporated into a released edition. The candidate's pathname checks and no-follow leaf opens are not a complete protection against same-user concurrent filesystem substitution, hostile parent renames, or compromised platform privileges. An adequate production fix requires a deliberate OS-specific filesystem trust boundary.

## Relationship to the existing work

This PR is stacked on [#13](https://github.com/KirtusJ/pcp/pull/13), which tests different build-22 method and object-store filesystem cases. The two test suites are separate. Merging either PR alone only adds tests, not remediation. Keep the earlier edition and original release SHA records unchanged.

*All test results are single-operator controls under Kirtus Justus's project direction, not external security certification or independent peer review.*
