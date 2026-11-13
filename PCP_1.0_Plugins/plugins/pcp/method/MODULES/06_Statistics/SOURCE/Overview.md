# Adversarial Claim Review

# Statistics Overview - Version 1.0

**Packet:** ACR Version 1.0, Implementation  
**Component:** `acr.statistics`, Version 1.0  
**Required core:** `acr.core`, Version 1.0; Core descriptor SHA-256 `f15686b385002bf597c2625bc18e98a390531a21ce91f64bdb249f2fe04a86a7`  
**Creator and research direction:** Kirtus Justus  
**Contributors:** Specification compiled and checked by ChatGPT (OpenAI). This Overview drafted by Claude (Anthropic) at the creator's direction. No endorsement by either company is implied.  
**Date:** 11 November 2026, America/Vancouver

This guide explains how to use ACR Statistics when reviewing or producing statistical work. It is informative. The Statistics Specification defines the requirements, and the pinned Core governs the assignment, permissions, findings and delivery. Clause numbers in parentheses refer to the Statistics Specification. ST-prefixed citations resolve to its reference appendix. The numerical examples are constructed for instruction; they are not data and they establish nothing about any real study.

## 1. Begin with the statistical question

Ordinary competent statistical work is the default. The module applies only when an authorized task, a commissioned review or a governing policy selects it for identified statistical work (1.1). Having the file, or working on something that contains numbers, selects nothing. A deterministic calculation or an exact identity is not a statistical inference, and a qualitative description does not need a hypothesis test attached to it (1.2).

When the module is selected, apply only the obligations that matter to the actual claim and its intended use (1.3). A short descriptive answer may need one sentence on the data, the method and the limits. A consequential inference needs more. In both cases the work product stays in its own form; the module adds no dashboard, form or staged exchange.

Three habits carry most of the module:

| Habit | Question it answers |
| --- | --- |
| Name the target first | What quantity, in which population, under which conditions, is this claim about? |
| Match the guarantee to the claim | Does the stated interval, error rate or prediction cover what the conclusion says it covers? |
| Keep the denominator and the design | How were the units obtained, and what counts as one independent observation? |

## 2. Name the target before the method

Before a consequential claim, identify the estimand or other target, the population or system, the units, the time window and conditions, any comparator, and the decision the result is meant to inform (2.1). The target is not always a single effect size. It can be a distribution, a contrast, a rate, a set of values or a prediction target.

Five kinds of claim need to be kept apart, because evidence for one does not carry to the next (2.2):

| Claim | What it says | What it does not give |
| --- | --- | --- |
| Descriptive | What these data show | Anything about units that were not observed |
| Generalizing | What holds in a wider population | A cause, or performance on future data |
| Predictive | How well an outcome is forecast under stated conditions | That intervening on a predictor changes the outcome |
| Causal | What an intervention changes | That the action is permitted or worthwhile |
| Decision | What to do given costs and alternatives | Authority to do it |

A p-value or an interval does not by itself establish practical importance, equivalence or acceptability. If the commission or a governing body supplies a threshold, name its owner and scope. Do not invent one (2.3) [ST01, ST02].

## 3. A worked example: rows that were not independent

A team reports that 30% of patients met a target, "95% interval 26% to 34%", from 600 records. The records come from 12 clinics with 50 patients each. The review question is narrow: does the reported interval have the coverage it claims for the population of patients served by clinics like these?

The first thing to settle is the unit of replication (3.1, 3.4). Patients in one clinic share staff, protocols and local conditions, so their outcomes are likely to be correlated. Six hundred rows are not six hundred independent observations merely because they occupy separate rows.

The reported interval treats the rows as independent. Under that assumption the standard error of a proportion of 0.30 with 600 observations is about 0.0187, which gives the reported half-width of about 0.037. Suppose, as a stipulated illustration, that the within-clinic correlation is 0.05 and the clinics are equal in size. A standard approximation for that simple design multiplies the variance by 1 + (50 - 1) x 0.05 = 3.45. The standard error becomes about 0.0347, and the 600 rows carry roughly the information of 174 independent ones. With only 12 clinics, a reference distribution with 11 degrees of freedom is the more cautious choice, and the half-width becomes about 0.076: an interval from about 22% to 38%, twice as wide as reported.

What the review can and cannot say follows from the Specification:

- The adverse finding is specific. The reported interval's coverage claim is unsupported for the stated population, because the uncertainty argument does not refer to the actual design (4.5). The point estimate is not refuted.
- The corrected figure above is CONDITIONAL. It depends on a stipulated correlation and on equal clinic sizes. No design-effect formula is valid everywhere, and a correlation estimated from 12 clinics is itself uncertain (4.3, 4.5).
- A design-based, model-based or resampling analysis can each be appropriate. The module does not choose one (4.2).
- A descriptive statement about these 600 patients needs no interval at all. Whether the wider claim was needed is a question about the assignment (2.2).

The useful output is a short note in the team's own report: the unit of replication, the corrected analysis that was run, its assumptions, and the narrower claim that is supported.

## 4. Read a guarantee for what it covers

Most disputes about statistical conclusions are disputes about scope. The Specification asks the reviewer to state which of these is actually established (5.1, 5.2, 5.6) [ST06]:

| Distinction | Why it changes the conclusion |
| --- | --- |
| Estimate and target | The number computed is not the quantity of interest. |
| Confidence, credible and prediction intervals | They answer different questions. A credible interval depends on its prior; a prediction interval is about a future observation, not a parameter. |
| Pointwise and simultaneous | Twenty intervals that each cover 95% of the time do not jointly cover 95% of the time. |
| Finite-sample and asymptotic | An approximation needs its conditions; a nominal level is not an achieved one. |
| Fixed-horizon and anytime | A guarantee for one planned look does not survive repeated looks. |
| Statistical uncertainty and non-identification | More data narrows the first. It does not remove the second (5.4). |

Repeated looks, many comparisons and selective reporting have to be accounted for when they change the claimed error guarantee (5.3). A constructed illustration shows the size of the effect: twenty independent tests at the 5% level, with every null hypothesis true, produce at least one rejection with probability 1 - 0.95^20, about 64%. The remedy is not one mandatory correction. A prespecified sequential design, a selection-adjusted method, or simply a narrower claim can each be right. A correction should also not be imposed on descriptive or exploratory comparisons that make no protected claim (5.6).

A rejection is not proof of the alternative, and a failure to reject is not proof of the null. A p-value is not the probability that the null hypothesis is true (5.5) [ST01, ST11].

## 5. Zero failures is not zero risk

A team runs 300 trials, sees no failure, and proposes to report the system as safe. The Specification is direct on this point: zero recorded adverse events must not be read as zero hazard, reliability or certification (5.7).

If the 300 trials were independent and each had the same failure probability, the largest probability consistent with seeing no failures, at one-sided 95% confidence, is 1 - 0.05^(1/300), just under 1%. The familiar shortcut is three divided by the number of trials. That bound is the most the data can say, and only under those assumptions. Before relying on it, the review examines the denominator and the opportunities for failure, whether the trials resembled real use, whether a failure would have been detected and recorded, and whether trials were dependent or selected (5.7, 3.1). Moving from the bound to a deployment or safety threshold needs a separate, justified bridge, and the governing domain's rules keep priority.

Aggregates hide strata. An overall rate dominated by routine cases can mask a small group in which failures concentrate or matter most (5.8). Where a critical stratum cannot be observed, narrow the assurance claim. A sparse stratum should not be given precision it does not have, and a subgroup analysis is not required where its inferential basis is absent.

## 6. Prediction, causes and decisions

For a prediction claim, identify what was known at prediction time, how the model was selected and tuned, and whether evaluation data overlapped with fitting data through any path (7.1). A validation set is not clean because it has a different file name; tuning against it is exposure (7.4) [ST12]. Performance under one distribution does not transfer to a shifted one without an argument.

For a causal claim, state the intervention and the conditions that identify its effect: randomization, a confounding assumption, an instrument, a natural experiment or another valid design (7.2). A diagram can make the assumptions visible, and it is not required. Predictive accuracy does not justify an intervention.

For a decision, separate the model's validity from the decision rule, the costs of each kind of error, the alternatives, and the authority to act (7.3, 7.5). A score cannot authorize its own deployment. The module supplies no universal risk threshold, fairness metric or accuracy level.

## 7. Record what was seen before the analysis was chosen

Analysis choices made after seeing outcomes, diagnostics or scores are disclosed when they are informative: searches, stopping, exclusions, tuning and repeated comparisons (3.2). Exploration is legitimate when it is labelled as exploration. Prespecification is valuable when it happened and may not be claimed afterwards.

Exposure is wider than access to raw outcomes. Summary scores, subgroup tables, optimizer feedback and earlier model-generated suggestions can all inform a later choice and defeat a claim that a check was blind or fixed in advance (3.4) [ST13]. Core's exposure statuses apply unchanged, and under Core Section 15.8 a blind condition that nothing enforces is recorded as an intention.

## 8. Check, state the finding, and correct

Each conclusion-critical obligation is tied to a check or a competent assessment, with known-valid and known-invalid controls where they discriminate (8.1). A simulation establishes properties of the simulated model. Two scripts that share one wrong assumption are one check.

Findings use Core's dispositions without change (8.2). Some pairings recur:

| Situation | Disposition to consider |
| --- | --- |
| A calculation is correct given its model, and the model's fit to the data is not established | CONDITIONAL, or SUPPORTED_IN_SCOPE for the conditional relation itself |
| An estimate lacks support | UNRESOLVED; lack of support is not refutation |
| A model is shown not to pin down the target, with a witness | NOT_IDENTIFIED_IN_SCOPE |
| A checked counterexample meets the stated criterion | REFUTED_IN_SCOPE |

Review is balanced. The reviewer looks for evidence for and against the original claim, and an adverse-search brief is a method, not a conclusion (8.6). Unearned confirmation and unearned obstruction are both errors. Evidence that passes through more tools, roles or documents is not thereby corroborated (8.5, 8.8).

The statistical model and the language model reviewing it are different things (8.7). A change in the reviewing assistant's configuration, tools or context can affect later checking and does not undo evidence that was independently established. An assistant's own statement about its tier or accuracy is not a measurement.

Corrections name the earlier claim, the changed basis and the affected conclusions, and they travel in the user's own output (8.3). A favorable statistical assessment grants no data rights, approval or release permission (8.4).

## 9. Work with the other modules

Core is the only required component. It owns the assignment, authority, dispositions, context and delivery, including the operating floor of Core Section 15 (9.1). The other specialists remain independently selectable:

| Module | Keeps | Statistics adds, when selected |
| --- | --- | --- |
| Science | Questions, observation, approvals and its own statistical safeguards | Specialist checking of sampling, inference and uncertainty (9.2) |
| Mathematics | Proofs and rigorous numerical claims | Nothing about proof validity; a proved bound does not establish sampling premises (9.3) |
| Engineering | Hazards, controls and residual risk | Reliability estimates, which are not evidence that a barrier exists or works (9.4) |
| Cryptography | Threat models and entropy obligations | Nothing about unpredictability; randomness tests do not establish it (9.5) |
| Quality Assurance | Whether suitable checks were selected, run and reported | The inference itself, which QA cannot certify |

No module selects another. Evidence may be shared when its scope, version and interpretation fit each use (9.7).

## 10. Keep it proportionate, and test the module itself

Use existing plans, notebooks, repositories and tables. No canonical form, JSON serialization, multi-agent discussion or role performance is required (10.1).

Whether this module improves statistical work is a testable claim and is not established by this packet (10.4, 10.5). A fair test compares it with competent ordinary practice on the same tasks and resources, includes work that is correct as well as work that is flawed, and scores substantive errors, unsupported confidence, false blocking, completion and cost (10.2). If a simpler practice does as well, keep the simpler practice. The module is not a quality mark and does not replace a statistician, a regulated reviewer or a risk owner.

## Appendix A. Reader's glossary

| Term | Meaning in this guide |
| --- | --- |
| Estimand | The quantity a claim is about, defined before the method that estimates it. |
| Unit of replication | What counts as one independent observation under the actual design. |
| Design effect | A variance multiplier for a design relative to simple random sampling; an approximation tied to its assumptions. |
| Coverage | The long-run frequency with which a procedure's interval contains the target under stated conditions. |
| Exposure | Any information about outcomes or evaluation that could inform a later analysis choice. |
| Identification | Whether the target is determined by what can be observed under the stated assumptions. |

## Appendix B. Where to look

| Question | Specification |
| --- | --- |
| Does the module apply here? | 1.1 to 1.4 |
| What is the claim about? | 2.1 to 2.3 |
| How were the data obtained, and what was seen first? | 3.1 to 3.4 |
| Which model and uncertainty argument? | 4.1 to 4.5 |
| What does the guarantee cover? | 5.1 to 5.8 |
| Measurement and numerical assurance | 6.1 to 6.3 |
| Prediction, causation and decisions | 7.1 to 7.5 |
| Checking, findings and correction | 8.1 to 8.8 |
| Other modules | 9.1 to 9.7 |
| Proportion and evaluation | 10.1 to 10.5 |

## Appendix C. Reading for the examples

These two sources explain the constructed examples. They are informative and adopt no requirement.

- **Kish, L. (1965). Survey Sampling. Wiley.** The design effect for clustered samples used in Section 3. The expression holds for equal cluster sizes and an equal-probability design.
- **Hanley, J. A. and Lippman-Hand, A. (1983). If nothing goes wrong, is everything all right? Interpreting zero numerators. JAMA 249(13), 1743-1745.** The zero-numerator bound used in Section 5. [Source](https://doi.org/10.1001/jama.1983.03330370053031)
