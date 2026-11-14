# Cross-archive release-identity regression

This is a **read-only, standard-library-only test contract** for [PCP issue #1](https://github.com/KirtusJ/pcp/issues/1). It does not change or redistribute a release. The public repository default branch carried the older build-19 packaged edition at the time of this work; the tested source was supplied by the rights holder as the build-22 release ZIP.

## Run on an actual release

```sh
python3 audit/build22-release-identity/check_cross_archive_identity.py \
  '/absolute/path/to/PCP_1.0_Release.zip' \
  --json /tmp/pcp-build-identity-result.json
```

Exit 0 means all **tested** outer archive hashes and cross-package build labels match; exit 1 identifies mismatched recorded hashes or build labels; exit 2 means the input could not be evaluated. The checker reads the ZIPs in memory and writes only the requested JSON report. It intentionally does not execute bundled release programs.

Run the independent synthetic test-oracle controls:

```sh
python3 audit/build22-release-identity/test_identity_oracle.py
```

The positive synthetic fixture has eight intact outer archive hashes, 24 matching identity fields and zero problems. The negative synthetic fixture also has eight intact outer hashes, but its Enterprise edition records build 21 under a build-22 outer index; the checker reports two mismatching fields. These fixtures prove the checker distinguishes identity drift from archive corruption; they do not prove the release itself is correct.

## Executed on the owner-supplied build-22 archive

Outer ZIP SHA-256: `6007acc5b5fe43d4639330e17ef03f4948859f42df7d857e8f713aeca6ec73b0`.

```
checked_archives:      8
hashes_passed:         8
build_labels_checked: 24
build_labels_matched: 12
problems:             12
exit:                  1
```

Every Personal, Commercial and Enterprise inner edition has `EDITION.json` and `MANIFEST.json` recording build **21**, while each matching plugin-only archive has `PLUGINS.json` and `MANIFEST.json` recording build **21**. Outer `RELEASE.json` records build **22**. The included `pcp` and `pcp-os` Claude manifests record plugin version `1.0.22` and match the outer plugin-version field in all six archives. The source, record, three edition ZIPs and three plugin-only ZIPs all match their *outer* recorded SHA-256 digests.

That result is a reproducible **cross-package identity inconsistency**, not byte corruption or a finding about PCP methodology, licensing authority, empirical efficacy, PDF/UA, or the kernel.

## Acceptance contract

Either (A) intentionally distinguish wrapper/product build from edition/plugin build and explicitly specify an exact, unambiguous, machine-readable relationship, including its rationale, or (B) make the labels agree and regenerate every affected manifest and ZIP. This initial checker applies the simple **same-build** interpretation until a separately specified split-build schema is adopted. If the split is intentional, update this check against the *approved mapping*, not by suppressing mismatches.

Keep the earlier released ZIP immutable. A local digest is not publisher authentication, and a passing regression is not certification of release fitness.
