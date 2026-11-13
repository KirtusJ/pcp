# Event bodies, in the order a review uses them

Every body below was offered to the guards when this plugin was built, in this order, and accepted. Write events with `acr_submit` (`kind`, `body`). The server sets the actor. Fields the guards compute (ids, digests of text, relation, grounding observed, coverage) are filled in for you: leave them out.

Replace what is specific to the example: digests, labels, texts. A digest is the SHA-256 of the exact bytes, in lower-case hexadecimal. Labels are letters, digits, `.`, `_` and `-`.

Your participant label is `assistant` unless `acr_status` shows another. The person directing the work is `principal` unless it shows another.


## 1. Tell the record you hold the method text

`DELIVERY_STATE`

```json
{
  "agent": "assistant",
  "event": "DELIVER",
  "text": "01bf42c8c662fa0d9d42e50e40eebd422f50ff8298680bcc71144a339e2e29de"
}
```

`text` is the SHA-256 of `method/KERNEL.md` as you read it. After a context reset, deliver again.


## 2. Put the target in the record

`ARTIFACT_ADDED`

```json
{
  "sha256": "bd9043cb35aa5fbd89bc3ae21ec026ec0b6bbd3c41ab9793198571f9a3fbfb53",
  "size": 15,
  "origin": "SUPPLIED",
  "name": "target",
  "filename": "proof.md",
  "stored": false
}
```

Prefer `acr_artifact`, with the file's `path`, or with `text` for words given only in the conversation: the server then computes this digest itself. For a directory, pin a tree instead: kind `TREE_PINNED`, body `{"name": ..., "manifest": <SHA-256 of its manifest>, "origin": "SUPPLIED"}`.


## 3. Commission the review

`REVIEW_COMMISSIONED`

```json
{
  "label": "R1",
  "title": "Is the proof complete",
  "target": {
    "t": "artifact",
    "sha256": "bd9043cb35aa5fbd89bc3ae21ec026ec0b6bbd3c41ab9793198571f9a3fbfb53"
  },
  "extent": "TOTAL",
  "procedure": "FOCUSED",
  "director": "principal",
  "claims": [
    {
      "label": "A",
      "text": "Every step of the proof in proof.md follows from the steps before it.",
      "origin": "COMMISSIONER",
      "kind": "DERIVATION",
      "criterion": "Supported if each step is checked and follows; refuted if one step is shown not to follow."
    },
    {
      "label": "B",
      "text": "The test suite passes.",
      "origin": "COMMISSIONER",
      "kind": "MECHANICAL_CHECK",
      "criterion": "The suite exits 0."
    },
    {
      "label": "C",
      "text": "The lemma used in step 4 is a published result.",
      "origin": "TARGET_TEXT",
      "kind": "EXTERNAL_FACT",
      "criterion": "Supported if the publication is retrieved and states it."
    }
  ]
}
```

The claim's words are the person's or the target's, not yours. `author` names the participant that wrote the target, when that is known; your check of your own work is then recorded as a self-check. `modules` lists selected specialist modules by digest.


## 4. Say how much of an item you read

`INSPECTION_DECLARED`

```json
{
  "ref": {
    "t": "artifact",
    "sha256": "bd9043cb35aa5fbd89bc3ae21ec026ec0b6bbd3c41ab9793198571f9a3fbfb53"
  },
  "extent": "all of it, lines 1 to 212"
}
```

Without this, a basis that cites the item is refused unless the basis itself gives an extent.


## 5. Commit G1

`GATE_COMMITTED`

```json
{
  "review": "R1",
  "gate": "G1"
}
```

G1 needs no evidence reference. Every later gate does: a basis or a note of what was done.


## 6. Record a check you ran

`CHECK_RAN`

```json
{
  "argv": [
    "cargo",
    "test"
  ],
  "exit": 0,
  "expect_exit": 0,
  "timeout": false,
  "stdout": "d367a494a1f42c203ab4f4e02edb39df73e9ce42729a079f1dd3200e341b42a5",
  "stderr": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
}
```

The guards number it `K1`. Prefer `acr_check`: with the review commissioned, run the command with the shell tool, then call `acr_check` with the same command text, and the server records what the host itself saw, as `observed: HOST_OBSERVED_TOOL`. A check written with `acr_submit`, as here, is recorded as `observed: REPORTED_BY_PARTICIPANT`, whatever its body says, and a finding that rests only on such checks is marked `execution: UNKNOWN`. Record a check only if you ran it and saw the result. `stdout` and `stderr` are SHA-256 digests of the output.


## 7. Raise an objection

`OBJECTION_RAISED`

```json
{
  "review": "R1",
  "claim": "A",
  "text": "Step 7 divides by a quantity that step 3 allows to be zero."
}
```

Numbered `O1`.


## 8. Resolve it, or record it open

`OBJECTION_RESOLVED`

```json
{
  "id": "O1",
  "resolution": "OPEN_RECORDED",
  "how": "The proof does not exclude the zero case; the objection stands."
}
```

An objection that stands is recorded open. It is not made to disappear.


## 9. A finding that the evidence does not support the claim as posed

`FINDING_RECORDED`

```json
{
  "review": "R1",
  "claim": "A",
  "disposition": "UNRESOLVED",
  "basis": [
    {
      "ref": {
        "t": "artifact",
        "sha256": "bd9043cb35aa5fbd89bc3ae21ec026ec0b6bbd3c41ab9793198571f9a3fbfb53"
      }
    }
  ],
  "left_open": "Step 7 for the zero case. Steps 1 to 6 and 8 to 12 were checked and follow."
}
```

Lack of support is not refutation. REFUTED_IN_SCOPE needs `contrary`: checked contrary evidence.


## 10. A finding supported by an executed check

`FINDING_RECORDED`

```json
{
  "review": "R1",
  "claim": "B",
  "disposition": "SUPPORTED_IN_SCOPE",
  "basis": [
    {
      "ref": {
        "t": "check",
        "id": "K1"
      }
    }
  ]
}
```

A mechanical claim is supported only by an executed check that met its expectation.


## 11. A finding about an external fact that rests on recall

`FINDING_RECORDED`

```json
{
  "review": "R1",
  "claim": "C",
  "disposition": "CONDITIONAL",
  "grounding_declared": "RECALL_ONLY",
  "conditions": [
    "The lemma is as stated in the cited publication, which was not retrieved."
  ],
  "estimate": "Probably a standard result; not checked against the source.",
  "left_open": "Retrieve the publication and read the statement of the lemma."
}
```

Recall supports nothing by itself. Retrieve the source (`ARTIFACT_ADDED` with origin RETRIEVED), inspect it, and record a new finding; the new one supersedes this.


## 12. Commit G5

`GATE_COMMITTED`

```json
{
  "review": "R1",
  "gate": "G5",
  "basis": [
    {
      "ref": {
        "t": "check",
        "id": "K1"
      }
    }
  ],
  "note": "Each claim has a finding; one objection is recorded open."
}
```

Refused while a claim has no finding.


## 13. Pause before a limit

`REVIEW_PAUSED`

```json
{
  "review": "R1",
  "reason": "The session is near its end."
}
```

A paused review accepts no step until it is resumed. `brief` may cite an artifact that holds your notes.


## 14. Resume

`REVIEW_RESUMED`

```json
{
  "review": "R1",
  "note": "Status read; delivery recorded again."
}
```

Read `acr_status` first.


## 15. Commit G6

`GATE_COMMITTED`

```json
{
  "review": "R1",
  "gate": "G6",
  "note": "Findings reported to the person with the open objection and what was not examined."
}
```


## 16. Close

`REVIEW_CLOSED`

```json
{
  "review": "R1",
  "lifecycle": "CLOSED_COMPLETE",
  "examined_extent": "TOTAL"
}
```

CLOSED_COMPLETE needs every required gate and a finding for each claim. Otherwise close as CLOSED_INCOMPLETE with the coverage the guards compute. A closed session is not reopened: renewed assessment is `SESSION_OPENED` with a reason.



## Values the guards accept

- **Disposition:** SUPPORTED_IN_SCOPE, CONDITIONAL, REFUTED_IN_SCOPE, NOT_IDENTIFIED_IN_SCOPE, DISPUTED, UNRESOLVED, INCOMPARABLE.
- **Procedure:** SCREENING, FOCUSED, FULL. **Gates:** G1 to G6; `required_gates` may name an ordered subset that contains G1, G5 and G6.
- **Claim origin:** COMMISSIONER, TARGET_TEXT, REVIEWER_CONSTRUCTED. **Claim kind:** UNSPECIFIED, EXTERNAL_FACT, MECHANICAL_CHECK, DERIVATION.
- **Artifact origin:** SUPPLIED, PRODUCED, RETRIEVED (a retrieved artifact carries `source` with where and when).
- **Grounding declared:** NONE, RECALL_ONLY, SUPPLIED_ONLY, EXTERNAL_INSPECTED; never above what the record holds as inspected.
- **Objection resolution:** RESOLVED, WITHDRAWN, OPEN_RECORDED. **Closing lifecycle:** CLOSED_COMPLETE, CLOSED_INCOMPLETE, ABORTED. **Examined extent:** NONE, PARTIAL, TOTAL, UNKNOWN.
- **`basis` and `contrary` are lists of references**, each written `{"ref": {...}}`, never text. Say in `left_open` or a note what the evidence showed.
- **References** in a basis: `{"t": "artifact", "sha256": ...}`, `{"t": "member", "tree": ..., "path": ...}`, `{"t": "check", "id": "K1"}`, `{"t": "finding", "id": "F1"}`.

## What the guards will refuse, so you need not try

- A review step while ACR is not in use, or in a review that is closed or paused.
- A finding before G1; SUPPORTED_IN_SCOPE or REFUTED_IN_SCOPE on a claim with no criterion; REFUTED_IN_SCOPE without contrary evidence; CONDITIONAL without its conditions.
- SUPPORTED_IN_SCOPE for a claim about an external fact on recall; for a mechanical claim without an executed check that met its expectation. REFUTED_IN_SCOPE for a mechanical claim without an executed check that ran to its end.
- REFUTED_IN_SCOPE whose contrary evidence is only text this review produced, or SUPPORTED_IN_SCOPE that cites nothing else: an artifact recorded as PRODUCED after the review was commissioned, a subagent's returned message included. The disposition without a check or inspected material is UNRESOLVED.
- `acr_check` with no review open; for a command the host did not see run, or saw before the open review was commissioned, or saw and already recorded.
- `ARTIFACT_ADDED` with origin SUPPLIED through `acr_submit` while a review is open: the server did not read it. Use `acr_artifact`.
- A basis that cites something not in the record, or an item with no inspection recorded and no extent given.
- A gate out of order; G5 with a claim that has no finding; CLOSED_COMPLETE with a gate or a finding missing.
- ADOPTED, HALTED, STANDARD_SET, the workspace's modules, system events, task events and extension events through `acr_submit`. Those are a person's or the host's; use `acr_adopt` and `acr_halt`.
- More than 64 reviews open at once.
