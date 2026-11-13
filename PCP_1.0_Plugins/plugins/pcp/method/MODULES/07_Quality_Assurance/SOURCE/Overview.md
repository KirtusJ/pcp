# Adversarial Claim Review

# Quality Assurance Overview - Version 1.0

**Packet:** ACR Version 1.0, Implementation  
**Component:** `acr.quality_assurance`, Version 1.0  
**Required core:** `acr.core`, Version 1.0; Core descriptor SHA-256 `f15686b385002bf597c2625bc18e98a390531a21ce91f64bdb249f2fe04a86a7`  
**Creator and research direction:** Kirtus Justus  
**Contributors:** Specification assembled and checked by ChatGPT (OpenAI). This Overview drafted by Claude (Anthropic) at the creator's direction. No endorsement by either company is implied.  
**Date:** 11 November 2026, America/Vancouver

This guide explains how to use ACR Quality Assurance when planning, performing or reviewing assurance work. It is informative. The Quality Assurance Specification defines the requirements, and the pinned Core governs the assignment, permissions, findings and delivery. Clause numbers in parentheses refer to the Quality Assurance Specification. QA-prefixed citations resolve to its reference ledger. The numerical example is constructed for instruction and describes no real product.

## 1. Begin with the assurance that was asked for

Ordinary competent checking is the default. The module applies only when an authorized task, a commissioned review or a governing policy selects it for an identified assurance assignment (1.1). It does not replace an organization's quality management system, an inspection, professional judgment, a statutory duty or a certification.

The first step is to say what is being assured and for whom: the deliverable, process or service, its exact version, and its intended user and environment (1.2). The second is to say which kind of statement is wanted, because the words are often used loosely:

| Term | Question it answers |
| --- | --- |
| Quality assurance | Are there grounds for confidence that identified requirements will be met? |
| Quality control, inspection | Does this item conform, as tested or examined? |
| Verification | Were the specified requirements met? |
| Validation | Is it fit for the intended use? |
| Safety assurance | Is there hazard-specific evidence for the stated safety claim? |
| Epistemic warrant | Is this particular claim supported? |
| Authorization and release | May it be released, and has someone with authority decided so? |

None of these follows automatically from another [QA01, QA02, QA04, QA05]. A team may use its own names for them as long as the distinctions survive.

Effort scales with consequence, complexity, reversibility and the benefit expected from checking (1.3). Reuse the requirements, test plans, validation records and version controls that already exist. The module mandates no form, standing role, second reviewer or duplicate record.

## 2. Write the acceptance contract

Each material requirement is traced to its real source: the law or contract, the binding policy, the adopted standard with its edition, the agreed product criterion, or a recommendation (2.1). They have different authority. A standard is cited only for what was actually inspected; a purchased standard that nobody read clause by clause cannot be reported as verified in full.

For each conclusion-critical objective there is a discriminating check or a reasoned competent assessment, and a stated condition under which the result would change the disposition (2.2). The contract distinguishes a demonstrated outcome from the presence of an activity, a form, a test name or an approval-looking token. No single quality score certifies a result.

Two further questions keep the contract honest. Is it complete enough for the claimed purpose, or does it leave out a user group, an operating context, a supplier or a failure mode that matters (2.4)? And where objectives compete, who decides the trade, and what stopping rule permits a bounded unresolved result in place of either manufactured approval or endless review (2.5)? A missing criterion holds only the claim or act that depends on it (2.3). Thresholds and the authority to waive them are never invented.

## 3. A worked example: a suite that passed

A release note says "test suite passed, 94%". The review question is what that sentence supports.

The team's records give four different counts (3.5):

| Stage | Count | Meaning |
| --- | --- | --- |
| Scheduled | 120 | Checks the plan required |
| Executed | 104 | Checks that actually ran; 16 never ran |
| Evaluable | 97 | Runs that produced a usable result; 7 failed for environment reasons |
| Passed | 91 | Evaluable runs that met their criterion; 6 did not |

The "94%" is 91 of 97. Against the plan it is 91 of 120, about 76%, with 16 required checks unrun and 7 inconclusive. Neither figure is wrong. They answer different questions, and a report that gives one without its denominator invites the reader to assume the other. The six failures and the 23 checks without a result are the first things a dependent reader needs.

The second question is about the checker (5.3, 5.4). The team seeds ten known defects and the suite flags seven. It also runs twenty items known to conform and the suite rejects two. On these controls the suite missed three of ten seeded defects and wrongly blocked two of twenty good items. Those are observations about these thirty cases. They are not a measured detection rate for unseen defects, and passing a finite set of controls does not establish complete detection. They do show that a clean pass from this suite is weaker evidence than the release note implied, and that both kinds of checker error are present.

What the review reports:

- The 91 passes stand as passes of those checks on that version (3.2, 3.4).
- The claim "the release meets its requirements" is UNRESOLVED for whatever the 23 checks without a result were meant to establish, and it fails for the six checks that did not pass.
- The suite's sensitivity is partly characterized, by controls with stated polarity: seeded defects were expected to be rejected, conforming items to be accepted (5.3).
- Release remains a separate decision by whoever holds that authority (7.2).

Nothing in the example needs a new form. The four counts, the control results and the scoped conclusion fit in the existing test report.

## 4. Make the evidence measure the claimed property

Each conclusion-critical requirement keeps a reconstructible link: requirement, versioned item, claimed property, acceptance basis, method, actual execution, result, exceptions and scoped conclusion (3.1). A designed test that has not run is recorded as not run.

The central check is whether the evidence measures what the claim says (3.2):

| Evidence | What it supports | What it does not |
| --- | --- | --- |
| A matching content hash | The bytes are the same | Who produced them, or that they are correct |
| A passing unit test | Its fixtures behave as asserted | Untested behavior of the system |
| A completed reporting checklist | The listed items were reported | Design quality, calibration or safety |
| Several agreeing model outputs | Those outputs agree | Independent confirmation of a shared assumption |
| An inspection record that cannot be read | Nothing yet | That the inspection found no defect |

Coverage has several dimensions: requirements, inputs and boundaries, operating envelope, adverse cases, regression after change, and independence of the checking path (3.3). A percentage of requirements listed is not completeness of the case. Identifiers and versions are checked at the granularity the claim depends on, so that a repeated identifier or a reused result is not counted as two satisfied obligations (3.6).

When a finding is summarized, pooled, translated or handed to another assistant, its acceptance basis, tested property, version, scope and limits travel with it (3.7). Repetition and sign-off language do not turn a narrow finding into a claim of safety, fitness or certification. Core Section 15.5 states the same rule for every relay.

## 5. Competence, independence and bias

Competence is resolved where it affects the assurance: domain knowledge, method choice and the correct edition of a standard (4.1). Role names, multiple model outputs and polished reports confer no qualification.

Independence is assessed to the degree the consequence and sector rules require, and it is not required for every routine check (4.2) [QA03, QA07]. The dimensions are separate: who the participant is, which organization or provider, which data and sources, which model and training, which analysis design, and which execution environment. Different personas or prompts on one underlying assistant are not independent validation. When one actor builds and checks an item, the check is labelled self-review. It is still useful, and it is not external assurance (4.3).

Quality judgments are exposed to pressure in both directions (4.4) [QA13, QA14]. Schedule pressure, completion targets, anchoring, automation bias and consensus push toward false acceptance. Skeptical overreach and a habit of objecting push toward false rejection. A reviewer's skepticism is not evidence of a defect, and an organization's sign-off is not evidence of truth. Unresolved objections are recorded without inventing a finding of misconduct. Core Section 15.3 protects the reviewer who declines to sign as well as the author who declines to concede.

## 6. Verification, validation and the checker itself

Checks are chosen from actual failure modes and conditions of use: normal cases, boundary cases and plausible adverse cases (5.1). Seeding a controlled defect to see whether checking finds it is useful where it is authorized and safe. No Resilience Exercise machinery or exhaustive enumeration is required.

Verification asks whether requirements were met. Validation asks whether the thing is fit for its intended user and use, which can bring in integration, accessibility, robustness, security, latency, failure response and monitoring (5.2). A passed small test says nothing about untested environments.

The checker is also an object of assurance (5.3). It can accept what it should reject, block what it should accept, use stale evidence, apply a wrong oracle or fail without reporting. A gate that reports success from self-declared fields has authenticated nothing (5.4). Counts of passing fixtures and traceability links are not sensitivity or specificity. Negative controls are paired with positive ones. The module does not ask for a checker that proves its own completeness.

## 7. Nonconformity, correction and learning

Five things are kept apart (6.1): an established nonconformity against identified criteria, a property that is unestablished because evidence is missing, an anomaly that needs diagnosis, a corrected factual error, and a risk hypothesis. In commissioned reviews, Core's dispositions are used and no rival vocabulary is introduced.

For a material defect, containment, correction of the item, causal analysis and action to prevent recurrence are separate steps (6.2). A proposed root cause is not an established one. A correction is not verified because it was made; its effect and its side effects are checked (6.3). Recipients who depend on the result are told about unresolved nonconformities and evidence limits.

## 8. Change, delivery and release

A change to the item, the requirements, the evidence, the tool or assistant, the configuration, the environment or the applicable standard triggers a scoped impact assessment when it can affect a relied-on conclusion (7.1). A change does not automatically invalidate earlier evidence, and a model name or tier is neither proof of equivalence nor proof of invalidity. If an identifying fact is unavailable, the limitation is reported.

Designed checks, executed checks, observed outcomes, approved release and actual deployment are distinct records (7.2). A sound assessment is not release permission. Quality obligations can continue through operation and retirement, and a finding is bounded by its evidence and cutoff (7.3).

## 9. Work with the other modules

Core is the only required component and supplies the assignment, authority, dispositions and the operating floor (8.1). The boundaries with the other specialists are firm:

| Module | Keeps | What QA may and may not do |
| --- | --- | --- |
| Engineering | Hazards, design assurance, physical controls, lifecycle duties | May check that the work was done and reported; may not waive or replace it (8.2) |
| Science | Empirical method, design and uncertainty | May assess process and reporting; a checklist cannot establish a scientific result (8.3) |
| Mathematics | Proof validity and numerical soundness | May verify that proof checks ran; may not infer correctness from packaging (8.4) |
| Cryptography | Threat models, entropy and secure operation | Generic QA cannot certify security (8.4) |
| Statistics | Sampling, inference and uncertainty | May check that suitable analyses were chosen, run and reported; may not certify the inference (8.5) |

Where a property needs specialist evaluation that no selected work covers, the dependency is recorded as unresolved. QA does not invent another module or declare compliance (8.6). Obligations from several modules compose under Core, and withdrawing a module waives nothing that another authority imposed (8.7).

## 10. Proportion, and evidence of the module's own worth

Use the simplest plan that serves the project. A narrow checklist or one direct test is often enough. Redundant audit rituals, recursion, role performance and blanket approvals are removed when they add no demonstrated protection, and checks that are genuinely required are kept even when they are costly (9.3).

Whether ACR Quality Assurance improves outcomes is not established by this packet (9.1, 9.2). A fair evaluation compares it with competent ordinary QA on matched tasks and resources, includes correct outputs as well as faulty ones, and scores false acceptance and false rejection separately, with severity and downstream effects (9.4). A reviewer that blocks everything is not safe, and one that accepts everything is not efficient. A gain measured only against a weak baseline is not reported as a gain over professional practice, and if a simpler practice does as well, the simpler practice is kept (9.5).

## Appendix A. Reader's glossary

| Term | Meaning in this guide |
| --- | --- |
| Acceptance contract | The requirements, their sources and authority, and the checks and criteria that decide acceptance. |
| Evaluable | A check that ran and produced a usable result, whether pass or fail. |
| Oracle | The rule or reference by which a check decides pass or fail. |
| Positive and negative control | A case with a known expected outcome, with the expected outcome stated, used to test the checker. |
| Nonconformity | An established failure to meet an identified criterion; not an unverified suspicion. |
| Self-review | Checking by the actor that produced the item. |

## Appendix B. Where to look

| Question | Specification |
| --- | --- |
| Does the module apply, and to what? | 1.1 to 1.3 |
| What are the requirements and acceptance criteria? | 2.1 to 2.5 |
| Does the evidence measure the claim, with what coverage? | 3.1 to 3.7 |
| Who checked, and how independent were they? | 4.1 to 4.4 |
| Which checks, and how good is the checker? | 5.1 to 5.4 |
| What kind of defect, and what was done about it? | 6.1 to 6.3 |
| What changed, and who may release? | 7.1 to 7.3 |
| Other modules | 8.1 to 8.7 |
| Is the module worth its cost? | 9.1 to 9.5 |
