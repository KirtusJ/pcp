# Adversarial Claim Review

# Science Overview - Version 1.0

**Packet:** ACR Version 1.0, Implementation  
**Component:** `acr.science`, Version 1.0  
**Required core:** `acr.core`, Version 1.0; Core descriptor SHA-256 `f15686b385002bf597c2625bc18e98a390531a21ce91f64bdb249f2fe04a86a7`  
**Creator:** Kirtus Justus  
**Date:** 11 November 2026, America/Vancouver

ACR Science is the broad, generic scientific-inquiry module of ACR. It helps organize a bounded examination of scientific support: which question is being answered, which evidence bears on it, what the checks establish and what remains unresolved. The governing Core supplies the shared protocol. The Science Specification defines the additional requirements; this guide explains their use across scientific disciplines.

## 1. Begin with the scientific work

Continue ordinary authorized research when an appropriate calculation, source inspection, discussion or expert assessment can settle the issue. Consider a Review when a particular disagreement, consequential uncertainty, handoff or governing requirement needs structured examination.

For example, a team may agree about an analysis result but disagree about whether its sampling unit supports the reported uncertainty. That is a clear review target. "Review all of our science" leaves too many choices unresolved unless the whole and its acceptance criteria are carefully bounded.

Identify the Research Owner under the team's existing governance. Preserve existing direction and permission arrangements. Delegated automated direction may conduct the review; scientific responsibilities remain with those assigned by actual governance. Existing valid approvals and task permissions do not need to be reissued merely because a scientific module is selected.

Start from the core entry route and the authorized assignment; use the Overviews for orientation as needed. Resolve applicable core and Science requirements for the next act. Its instruction or State Brief can carry controlling obligations, with exact supporting records available as needed. This module alone does not supply missing core context.

For commissioned Review work, the same Review continues to own the assignment. A new conversation can resume its active assessment after the required reconciliation. A completed assessment remains sealed; renewed assessment follows the core's successor rules. A module does not create a second Director or parallel state machine.

Mathematics can be added for a mathematical claim within the work, without replacing the scientific question or starting another Review. The proof of an implication and the evidence for its empirical premises remain distinct. Select the relevant obligations through the Core's current-basis rules; receiving another PDF does not retrospectively assess earlier work.

A FOCUSED review is the recommended starting procedure for a bounded issue. The relevant duties can be combined under core rules. A notebook, task record or repository may already hold everything needed; no new database, daemon or programming language is required.

## 2. Make the assignment small and answerable

Use the core's four connected record portions. For scientific work, an entry can be as short as the following constructed example:

| Portion | Example content |
| --- | --- |
| Subject | Assess whether the stated per-item criterion holds for the four identified reference items. |
| Mandate | Existing research lead; permitted inspection and calculation; no new acquisition or external disclosure. |
| Basis | Exact table and criterion; stipulated references; no population inference; current core and Science rules. |
| Result | Item-level differences, criterion outcome, adverse item if any, and the limit of the finding. |

Known references can supply these facts. The participant should identify its next authorized act rather than recite the rulebook.

The working basis preserves scientific meanings that are easy to lose during handoff: units, domain, quantifiers, assumptions, exposure and acceptance criteria. A Review can use its Basis Header. Some constraints can be checked mechanically; others require substantive interpretation.

Permitted narrowing is useful. A child assignment may inspect one section or one subset while the parent retains all remaining obligations. Its scope need not equal the parent's whole. The finding must say which part it covers. Changing a conclusion about every item into a conclusion about an average changes the question.

## 3. A check that answers the wrong question

### 3.1 The constructed measurement example

The values below are invented, and the references are stipulated exactly. The task is arithmetic on this finite table. Real measurement work would additionally examine its design, references, uncertainty and fitness for purpose [S10].

The claim is: **For each reference item, the absolute difference between its observed mean reading and its stipulated reference is at most two units.**

| Item | Reference | Three readings | Mean | Difference |
| --- | --- | --- | --- | --- |
| R1 | 100 | 100, 101, 102 | 101 | +1 |
| R2 | 200 | 200, 201, 202 | 201 | +1 |
| R3 | 300 | 300, 301, 302 | 301 | +1 |
| R4 | 400 | 404, 405, 406 | 405 | +5 |

The average of the four absolute item differences is **2**. An average-only test passes. The claim requires every item to satisfy the bound, and R4 fails with a difference of **5**.

The calculation can be perfectly reproducible while checking the wrong property. The decisive step is to connect the actual claim to the property being calculated.

### 3.2 Resolve the disagreement

Correct an agreed error directly. If interpretations conflict, identify who explains the support, examines the quantifier and checks the arithmetic. These attributable duties require no separate conversations or staged argument.

A useful readback identifies one item's mean outside the bound as an adverse case. A single reading outside the bound need not defeat the criterion if that item's mean still satisfies it.

Calculate every item. R4 supports REFUTED_IN_SCOPE for the all-four assertion. Replacing "each" with "average" or excluding R4 changes the question and requires the applicable change handling.

Twelve readings concern four reference items. This finite calculation needs no confidence interval; inference about future items requires a suitable design and uncertainty assessment.

## 4. Choose the method for the question

Scientific inquiry uses shared evidential principles with different methods [S01]. Description, experimentation, qualitative interpretation, formal derivation and evidence synthesis do not all follow one fixed sequence.

| Question | Focus of review |
| --- | --- |
| What was observed? | Material or setting, selection, representation, context and limits; measurement and uncertainty where used. |
| What changed under an intervention? | Allocation, independent units, controls, adherence, measurement and the causal contrast. |
| What causal conclusion can observational data support? | The information available and assumptions connecting it to the causal quantity [S08]. |
| What can be predicted in the intended setting? | Information available at prediction, relevant horizon and evidence for the stated performance [S32]. |
| What supports an interpretation? | Context, sampling rationale, methodological orientation, analytic evidence and transfer limits [S15]. |
| What does combining methods add? | Relations among components, integration where claimed, discrepancies and support for the combined inference [S33]. |
| What does a synthesis establish? | Search, eligibility, duplicate reports, appraisal, synthesis choices and missing evidence [S14]. |
| What does a calculation establish? | Premises, exact inputs, implementation, numerical conditions and the relation to the scientific question. |

Reporting standards make work inspectable within their scope. PRISMA concerns systematic-review reporting; SRQR addresses qualitative reporting; CONSORT addresses randomized-trial reporting [S14-S15, S24]. Use suitable conduct and appraisal methods as well.

For a constructed example, a team examines selected field notes to describe how a practice was organized. Review the selection, context and links between passages and interpretation. This question needs neither an intervention effect nor a numerical denominator. If the team instead claims that most sites use the practice, the added prevalence claim needs an appropriate reference population and evidential basis. The review follows the claim actually made.

An objection can identify a missing support step without producing a new experiment. If an analysis treats repeated observations on one unit as independent units, a specific methodological objection may be enough to require rechecking the uncertainty calculation. COPE similarly distinguishes essential support from requests to extend the work [S25].

Vague suspicion is not a refutation. A useful contribution identifies the affected claim, concern, consequence and available support or missing information. The assessment determines its status.

If the reviewer cannot open an appendix, the supported report is an inspection limitation, not "the method was unspecified." Follow the Core recovery rule within the existing authority and budget. Required evidence may still be unavailable for acceptance; that limits the dependent finding without establishing a defect in uninspected work. If the detail is recovered, update the current assessment and affected recipients rather than carrying the earlier limitation forward unchanged.

## 5. Preserve planning and exposure

Suppose a team searches existing observations, notices a pattern and then writes a detailed plan. That plan can govern later work. It cannot retroactively precede the observations already inspected.

Keep four questions distinct: What is the scientific purpose? When was the plan established? What information was available? What justifies the inference actually made?

Preregistration records specified plans prospectively relative to declared decisions or exposure. A planned exploratory search remains exploratory. Registered Reports add a publication process with pre-outcome review and conditional in-principle acceptance [S04-S05].

An unexpected observation may justify an amendment or a new question. Record the change, reason, timing, available information and affected inference. Valid selective or sequential methods can support some adaptive procedures under their assumptions [S06-S07]. Adaptation is not universally forbidden, and registration does not automatically validate the analysis.

A frozen plan still admits adverse observations into the record. Changing the plan or opening a successor does not erase what the team has seen. The core's optional Delegated Continuation policy may govern delegated execution; it cannot make repeated outcome inspection a fixed-sample procedure or turn a retrospectively selected analysis into a prospective one.

The same principle applies to protected first passes and reserved evaluation material. A participant who sees a summary, score or informative feedback may have gained relevant exposure even without opening the raw file. A later session anchor preserves that fact.

Scientific protections remain active throughout. A participant with community governance rights retains them regardless of any Observer role. An Observer's access does not authorize public release of restricted observations or allocations [S18].

## 6. Check the decisive obligation

A useful assessment maps each acceptance-critical obligation to its actual check. In commissioned Review work this is part of G5. If a suitable mechanical check is available and authorized for a checkable obligation, run it. For obligations requiring source inspection, observation or expert assessment, identify the assessment used and its limits.

For numerical work, state whether the output is an approximation, a stability observation, an exact calculation or an enclosure. More precision can improve a calculation without proving the requested error bound. The mpmath documentation describes limitations of precision-based checks and distinguishes arithmetic contexts [S26-S27].

If a certified interval for a quantity spans a decision threshold, its midpoint does not settle which side contains the true value. Ball arithmetic provides an inclusion contract for applicable operations, but correct input representation and any caller-level approximation bounds still matter [S28].

Statistical and measurement uncertainty ask additional questions. A population identified set describes the values compatible with an observation law and assumptions. An interval estimated from a finite sample need not contain that set with a stated probability. A confidence region for each possible true parameter and a region covering the entire identified set have different coverage events [S29-S30]. State which result is claimed. Calibration corrections and time-dependent changes also need appropriate uncertainty treatment [S31]; numerical precision cannot supply missing measurement information.

Repeated work also needs a precise description. Recomputing the same inputs can test computational reproducibility. New data addressing the same question can constitute a replication attempt. Reanalysis with another method may explore robustness without providing new observations [S09].

State what was separated: data acquisition, implementation, sources, assessors or prior exposure. Two implementations can catch different programming errors while sharing the same biased measurements. An accurate account of that separation is more useful than counting agreeing participants.

## 7. Deliver a scientific finding

A compact finding connects its conclusion to evidence and checks, states uncertainty and scope, retains material contrary evidence, and names remaining obligations. Use the team's existing plan, data, code, environment and interpretation versions. A code commit alone need not include every input.

Version control helps track changes. Because Git author and committer dates can be supplied, a local commit date alone does not independently establish prior registration or absence of outcome exposure [S19]. Appropriate external records may supply additional timing evidence.

Use reporting guidance relevant to the output and disclose consequential AI assistance under applicable research policy [S02]. Retain the information needed to inspect the contribution and its verification. Publishing every routine prompt or private deliberation is unnecessary.

Sharing follows actual rights. FAIR allows authenticated and authorized access [S17]. A general packet can identify a permitted access route and a restriction without copying confidential records. Metadata, filenames and small summaries also need appropriate protection. Community authority remains relevant [S18].

The core handles delivery, receipt and current authority. Scientific delivery adds the exact Study basis, exposure consequences and interpretation limits. A recipient should be able to locate the specified inputs and result through the permitted route.

## 8. Keep review proportionate

Choose a concrete scientific gap and the smallest useful intervention. Existing expert review, direct checking, prospective design review or a suitable publication process may already address it.

For a comparison, include valid cases, material errors and questions that available evidence cannot settle. Set outcome criteria before inspecting results, use evaluation cases distinct from development examples when appropriate, and conceal the review condition from assessors where feasible.

Measure useful corrections and valid conclusions retained alongside false objections, unresolved cases, time, participant effort, tool cost and disruption. Planted errors and genuine open questions have different answer bases and should not be pooled into an unexplained correctness score.

A simplified investigation can examine a procedure without representing a real population. State its assumptions, controls, procedure, results, deviations and transfer limits. Sampled estimates need relevant simulation uncertainty; exact finite examples still need specification and implementation checks [S11].

Stop repeated examination when the bounded question is settled or further work lacks an adequate reason. Preserve incomplete or identification-limited findings when those accurately describe the evidence.

## 9. Boundaries worth examining

The worked measurement review above shows how the protocol fits an assignment. The following boundaries recur in scientific review. Each can be examined with a small constructed case of the team's own, with parameters chosen for the question at hand rather than taken as ACR defaults.

| Boundary to examine | Constructed case |
| --- | --- |
| A search across candidates changes the error question. | Multiplicity. |
| Repeated looks change the procedure being assessed. | Sequential inspection. |
| Discovery and independent follow-up have different exposure histories. | Candidate selection and confirmation. |
| Available observations may leave a target unidentified. | Observational ambiguity. |
| Identification bounds and sampling coverage are distinct. | Identified-set coverage. |
| Equal likelihood at one record need not mean equal observable laws. | Identification scope. |

Use a case to clarify a specific distinction. A constructed case establishes its stated properties only; it does not establish that ACR improves scientific work.

## Appendix. Reader's glossary

| Term | Meaning |
| --- | --- |
| Study | The scientific investigation, which may exist without a Review. |
| Estimand | Precisely defined quantity to be estimated. |
| Measurand | Quantity intended to be measured under specified conditions. |
| Inferential warrant | Evidence and assumptions supporting a conclusion. |
| Identification | Whether admitted information and assumptions determine the target quantity. |
| Identified set | Target values compatible with the population observation law and admitted assumptions. |
| Confidence region | Random region with a stated sampling guarantee for a specified parameter or set. |
| Prospective plan | Plan established before the decisions or exposure it governs. |
| Reproduction | Same-input computational repetition with an assessed outcome. |
| Replication | New-data investigation of the same question with assessed consistency. |
