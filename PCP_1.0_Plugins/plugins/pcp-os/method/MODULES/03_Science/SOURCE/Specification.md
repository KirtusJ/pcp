# Adversarial Claim Review

# Science Specification - Version 1.0

**Packet:** ACR Version 1.0, Implementation  
**Component:** `acr.science`, Version 1.0  
**Required core:** `acr.core`, Version 1.0; Core descriptor SHA-256 `f15686b385002bf597c2625bc18e98a390531a21ce91f64bdb249f2fe04a86a7`  
**Creator:** Kirtus Justus  
**Date:** 12 November 2026, America/Vancouver

ACR Science is a broad, generic module for scientific inquiry across disciplines. It adds requirements for examining scientific questions, methods, evidence and conclusions, using the Core's authority, evidence and delivery rules, with its Review and Session structure where commissioned. The scientific team supplies the substantive methods and applicable research governance.

This Markdown Specification is the normative Science text; its PDF is the corresponding reading copy. The component catalog binds their exact versions. Sections 1-9 and Appendix A are normative, except explicitly labeled examples. Appendices B-C are interpretive guidance and references. Capitalized requirement words have the governing core's BCP 14 meanings.

## 1. Scope and entry

### 1.1 Apply the module to identified work

Science applies when selected by an authorized task, commission or applicable policy. Ordinary authorized research remains the default. A team SHOULD begin with a FOCUSED review when a specific disagreement, consequential uncertainty, handoff or governing requirement calls for structured assessment.

The exact core definition and applicable scientific rules MUST be resolved for the assigned act. A compact instruction or State Brief may carry controlling obligations while exact supporting records remain available through an authorized path. An unavailable prerequisite blocks its dependent commitment; separately authorized preparation or provisional investigation may continue.

Preserve the existing authorized task. For commissioned Review work, applying Science MUST preserve the assigned Review and reuse its applicable active assessment Session under core guards. A continuing Review may have no active assessment between commissioned cycles. Applying the module creates no assessment, Director or additional permission. Session renewal, role succession and material changes follow the core.

Mathematics MAY be selected alongside Science for mathematical claims, derivations or calculations. Scientific inference and empirical premises retain this module's obligations; a mathematical implication does not establish their applicability. The modules do not require one another, and later selection follows the Core's change and context requirements.

### 1.2 Reuse the team's working record

A **Study** is the scientific investigation associated with the review. It may have no Review or several bounded reviews. The responsible **Research Owner** is identified under actual governance; this is an accountability reference, not another mandatory participant role.

Use existing notebooks, plans, repositories or task records. Add or reference only the scientific meanings relevant to the assignment:

| Core record portion | Scientific meaning |
| --- | --- |
| Subject and question | Study reference; exact question and object assessed; population, material or setting; intended inference and review boundary. |
| Mandate and limits | Research Owner; decision responsibility; applicable protection and approval references; resources and scientific stopping requirements. |
| Working basis | Plans and input versions; design and assumptions; current scientific activity; actual information exposure; relevant checks and unresolved concerns. |
| Result | Finding and uncertainty; assessed scope; deviations and contrary evidence; remaining obligations and permitted disclosure. |

Known information MUST be reused without redundant transcription. Missing material information MUST remain unresolved rather than being inferred from a role label or expected result. The core Entry Card and Basis Header can present these meanings; this module adds no form requirement.

## 2. Scientific question and inherited meaning

The question MUST identify what the offered evidence is intended to establish. It MUST also state what observation or result would count against the claim, and whether that was fixed before the evidence was seen. The assessed subject can be a proposed design, measurement procedure, dataset, analysis, interpretation or conclusion. Commissioned Review work binds it as the Target. Total coverage is always relative to a named whole. Reviewing an entire script does not establish the adequacy of an entire Study.

For quantitative work, resolve the quantity of interest and domain, together with units, relevant population or system, comparison, observational unit and sampling or allocation unit where applicable. Distinguish repeated readings and subsamples from independent units. For qualitative work, resolve the question, setting, sampling rationale, methodological orientation, analytic process, evidential links and transfer limits; include researcher positioning where material [S15].

The working basis and inherited references MUST preserve material quantifiers, representation conventions, assumptions, criteria, exposure and unresolved conditions. Structured identity, type and inheritance checks apply under the core when a suitable authorized checker is available. A compact view MUST retain or resolve constraints needed for the next act.

An exact artifact identity binds a particular representation. An assessed compatibility relation establishes permitted reuse. Equivalent transformations MAY reuse prior work when their mapping and limits are documented. An already authorized narrower scope MAY be examined without amending the parent claim; its result remains restricted to that scope, and remaining parent obligations stay recorded.

Replacing the parent question, weakening a criterion outside permitted variations or extending a conclusion beyond its assessed scope MUST follow the applicable core change procedure. A new header cannot make an old result current without a justified relation between their actual bases.

**EXAMPLE:** converting centimetres to millimetres can preserve a length. Replacing "every item" with "the average item" changes the acceptance property. An authorized review of three items does not complete a four-item review.

## 3. Accountability and research protections

The record MUST identify responsibility for the assigned research decisions, required expertise and applicable human or institutional involvement. Automated direction MAY be delegated under core authority. It MUST NOT displace responsibilities assigned by research governance [S02]. A human title or automated role does not establish competence.

Before dependent actions, resolve applicable requirements for participants, animals, hazardous work, field access, protected information, data rights, communities, funders and publication. Use relevant institutional and disciplinary practice; this module prescribes no universal approval body. Existing valid approvals MAY be referenced. Mandatory protections cannot be disabled through optional-method settings.

An unavailable approval blocks actions requiring it; it does not itself refute a scientific hypothesis. A favorable assessment supplies neither consent nor permission to disclose. Unknown protection applicability MUST be resolved before the affected consequential action.

Collect and expose only the information needed for the authorized task. Restricted details may remain in protected records. Retention, correction and deletion obligations apply to observations, identifiers, prompts and derived records. Provenance requirements do not authorize indefinite retention of prohibited material.

Observer participation follows the core's access and submission rules. An observer's material exposure MUST be carried forward if that person later performs an assessment requiring concealment. Community members or participants who hold substantive governance rights retain them regardless of any Observer role. CARE provides relevant principles for Indigenous data governance where applicable [S18].

## 4. Methods, plans and exposure

### 4.1 Select methods for the scientific question

Scientific inquiry has common evidential commitments and diverse methods [S01]. This module MUST NOT impose a null hypothesis, intervention, numerical effect estimate, p-value or fixed sample size on every investigation.

Framing, design, acquisition, analysis, interpretation, reporting and follow-up may overlap or recur. They describe scientific activity, not a second Review lifecycle. Completion of an assigned analysis and support for its conclusion remain separate.

| Activity | Material controls to address when applicable |
| --- | --- |
| Experimental | Allocation and independent units; controls; concealment or blinding; breaches; intervention fidelity; sample-size or precision rationale; exclusions and stopping. |
| Observational | Sampling and selection; measurement; missingness; temporal order; confounding; adjustment rationale; identification and sensitivity for causal claims. |
| Measurement | Measurand, units, references, calibration, uncertainty, systematic effects, operating conditions and fitness for use [S10]. Where a measure stands for something it does not observe directly: what it is taken to indicate, the support for that reading, its reliability, and whether an outcome is a surrogate. |
| Statistical | Target quantity, dependence, assumptions, multiplicity, selection, interim looks, uncertainty, diagnostics and practically relevant magnitudes [S03]. |
| Predictive | Predicted outcome or object, conditions of use, available information at prediction, relevant horizon and performance evidence; fitting, selection and information reuse where material [S32]. |
| Qualitative | Methodological coherence, context, sampling rationale, analytic decisions, evidential interpretation, reflexivity and divergent cases where relevant [S15]. |
| Mixed methods | Relations among components and their evidence; integration where claimed; support for the combined inference, material discrepancies and shared dependencies [S33]. |
| Evidence synthesis | Search and eligibility, duplicate reports, extraction, risk of bias, synthesis choices, missing evidence and certainty [S14]. Whether the conclusion rests on one study or on a body of evidence; inconsistency, indirectness and imprecision across studies; funding and sponsor interests in the evidence relied on. |
| Computational or theoretical | Exact premises and inputs, derivation or algorithm, implementation checks, numerical error or convergence, sensitivity and empirical applicability. |

For each activity the assessed work includes, each listed control MUST be addressed or recorded as inapplicable with a reason. Existing scientific protocols and specialist standards MAY provide the controls. Do not replace unresolved methodological questions with an unsupported applicability flag.

### 4.2 Preserve timing and adaptation

Scientific purpose, plan timing, actual exposure and inferential warrant MUST remain distinguishable. A registered exploratory search remains exploratory. A valid analysis of selected results does not make its question prospective.

A prospective record SHOULD precede the decisions or exposure it is intended to govern. For existing data, disclose relevant access and prior analysis. Where preregistration is used, bind the exact plan and relevant timing boundary [S04]. Registered Reports additionally involve pre-outcome review and conditional in-principle acceptance under the outlet's rules [S05].

A consequential amendment MUST record what changed, why, when, under whose authority and with what information available. Identify affected inferences, approvals and reuse. Apply the core's material-change rules; ordinary arrival of in-scope evidence does not itself create a new Session.

A frozen plan MUST NOT exclude relevant adverse observations from the record. An authorized amendment or successor preserves actual prior exposure; it does not make a retrospective choice prospective. Delegated continuation, including any Delegated Continuation policy, follows core authority. Automatic repetition, selection and stopping remain part of the actual scientific procedure and MUST satisfy its applicable inferential conditions.

Selection-aware and sequential procedures MAY support adaptive analysis under their stated assumptions [S06-S07]. Claimed statistical guarantees MUST account for actual multiplicity, selection, dependence, interim inspection and stopping. If a guarantee does not apply, revise the procedure or narrow the claim. A Review deadline supplies no statistical justification.

Reserved observations and first passes retain their actual exposure history. Feedback containing outcomes, scores or other informative derivatives may compromise a reservation even when raw records remain hidden. The protection applies to the information, not merely its file location.

## 5. Scientific objections and decisive checks

### 5.1 Assess the concern

An objection MUST identify an affected claim or obligation, the specific concern, its material consequence and available evidence or missing required information. Grounds may include inspected sources, observations, study-design limitations, measurement defects, qualitative evidence, explicit inference errors or reproducible counterexamples.

Apply the Core Section 4.3 distinction between a source omission and an inspection limitation. A missing-method objection identifies the applicable requirement and inspected material; an unread appendix or unsuccessful retrieval does not establish that the method was unspecified. Resolve the dependent assessment only as far as the available evidence supports. An unmet required check still limits the dependent conclusion. PRISMA separates reports that were not retrieved from retrieved reports excluded on eligibility [S14].

An objection MUST NOT be dismissed solely because it lacks a new script, measurement or formal counterexample. A critic need not prove a rival conclusion to identify inadequate support. Distinguish an inquiry, a supported concern and a checked adverse finding. A speculative possibility is not an established refutation.

Assessment MUST address the assigned claim. Additional work extending the Study requires a reason beyond a reviewer's preference. COPE distinguishes investigations needed to support existing claims from work that extends their scope [S25]. Participants may withdraw positions; no scientific duty requires performed opposition or a predetermined result.

Before a published source is relied on, its status MUST be recorded: preprint, peer-reviewed article, secondary report or other; and whether a retraction, correction or expression of concern was looked for, where and on what date. A status that was not checked is recorded as not checked.

### 5.2 Connect each decisive obligation to a check

Every obligation decisive to the assigned conclusion MUST be connected to the property actually assessed. For commissioned Review work, this is part of G5. Reuse existing checking records for inputs, method, configuration, assumptions, actual outputs, diagnostics, coverage and dependencies.

For each mechanically checkable obligation with an available, authorized and suitable procedure, obtain an executed checking record. Where such a procedure does not apply, identify the appropriate substantive assessment. An essential unresolved check limits the dependent conclusion; a narrower finding may be reported when it has support within its declared scope.

Assess the translation from the scientific criterion to the checked property. Use valid and invalid controls when they discriminate relevant failures. Execution success, output agreement or one incidental check of another kind cannot substitute for coverage of the decisive obligations.

Preserve material contrary evidence and common dependencies among observations, sources, implementations and interpretations. An independence claim MUST name the dimensions actually separated and relevant dependencies or unknowns. Different participants, providers or prompts alone do not establish independence.

### 5.3 Numerical results

When relevant to the conclusion, distinguish approximation, stability checking, exact calculation and rigorous enclosure. An enclosure claim MUST identify the encoded quantity, input bounds, operation semantics and caller-supplied approximation or truncation bounds.

The complete enclosure MUST support the stated comparison. An interval crossing a decision boundary is inconclusive for that comparison even when its midpoint lies on the desired side. Agreement at greater precision is a stability observation unless an applicable error guarantee supports more.

The mpmath documentation distinguishes ordinary arbitrary-precision calculations from interval contexts and notes limits of precision-based error checks [S26-S27]. Ball-arithmetic inclusion semantics supply a relevant enclosure contract for applicable operations [S28]. Incorrectly encoded inputs or missing approximation bounds still affect the scientific conclusion. Tool choice and numerical assurance MUST remain distinct from measurement validity and empirical interpretation.

### 5.4 Identification and empirical uncertainty

For quantitative bounds or set-valued inference, the finding MUST identify the reported object and interpretation. Population identified sets, their sample estimates, sensitivity sets, numerical enclosures, confidence regions, credible regions and prediction regions have different meanings. An identified set is the set of target values compatible with the population observation law and admitted assumptions; replacing that law with an empirical estimate does not by itself supply a coverage guarantee.

A reported probabilistic region MUST state its interpretation and assumptions. A frequentist coverage claim MUST state its covered object and quantifiers, distinguishing coverage of each admissible parameter separately from simultaneous coverage of the entire identified set [S29]. Identify whether the guarantee is finite-sample or asymptotic; pointwise at each fixed observation law or uniform over a declared class [S30]; and valid at a fixed analysis time or across the reported sequence. Selection and repeated inspection remain subject to Section 4.2. Bayesian credible probability and sensitivity ranges retain their own interpretations.

Material measurement corrections, calibration uncertainty, dependence and drift MUST be represented in the uncertainty assessment for the conditions of use [S31]. A stipulated bound, estimated bound and bound supported at a stated confidence level are different inputs. A chosen distance, uncertainty radius, penalty or worst-case objective needs a claim-specific justification; none automatically supplies sampling coverage. A numerical outer approximation must preserve the relevant inclusion guarantee and be labeled as an outer approximation.

An empty computed or sample-derived set MUST be interpreted through its procedure and diagnostics. Sampling variation, incompatible assumptions, an incomplete search or numerical failure can have different consequences; emptiness alone does not establish population refutation or NOT_IDENTIFIED_IN_SCOPE. Reuse the existing method and finding records, with a method appropriate to the particular claim.

## 6. Inference and dispositions

Use Core dispositions for commissioned Review findings. Ordinary results need no ACR status vocabulary; any chosen canonical disposition retains its meaning and evidential guards. Scientific scope, assumptions and uncertainty MUST remain explicit. CONDITIONAL applies when an essential condition is assumed but remains unresolved by the review. Definitions and justified scope restrictions are not automatically unresolved factual premises.

A non-significant result MUST NOT automatically be reported as no effect. Statistical significance does not establish importance, truth or replicability [S03]. Evidence of absence, equivalence, prediction, description and causation require criteria suited to those different questions.

A causal conclusion MUST identify its target contrast, information and identifying assumptions. When admissible mechanisms induce the same observable-data law under the declared information design but disagree on the target quantity, that information does not identify the quantity within that assumption class [S08, S30]. For a deterministic observation map, the corresponding condition is equality of its observable output. Agreement on a realized finite record, equal likelihood at that record or failure to reject a difference does not establish equality of the observable-data laws. NOT_IDENTIFIED_IN_SCOPE requires a checked ambiguity witness for the declared information and assumptions, not merely unsuccessful analysis. Report justified bounds or information needed to resolve the question where available.

Theoretical derivation establishes a consequence of stated premises under the applicable reasoning rules. Application to a scientific system requires a supported correspondence between those premises and the system. An exact computation or counterexample retains its own scope.

Use the following distinctions for repeated work, following the National Academies terminology [S09]. Defined field-specific terminology MAY be used.

| Work performed | Report |
| --- | --- |
| Same-input computational rerun | Reproduction attempt, comparison criterion and actual outcome, including failures or partial agreement. |
| New data addressing the same scientific question | Replication attempt, design differences, uncertainty and assessed consistency. |
| Existing data analyzed differently | Reanalysis or robustness check, with shared evidence and changed method identified. |
| Same claim checked with another implementation | Additional implementation check; separate what changed from common inputs or assumptions. |
| Reporting checklist completed | Items reported; methodological adequacy and inference remain assessed through their applicable criteria. |

An attempt does not imply success. Same-data work MUST NOT be labeled new-data replication. For the core's separated-checking method, specify the actual separation rather than importing a scientific replication claim.

## 7. Simplified investigations and optional methods

### 7.1 Method use

The core owns optional methods, their OFF defaults, permissions, resource bounds and activation records. Scientific requirements add interpretation and protection conditions.

A reductio identifies premises, inference rules and the contradiction; it does not establish the empirical truth of a rival. Multiscale work identifies the relations between scales and the limits of transfer. Adaptive numerical resolution requires a suitable representation, error or convergence criterion, refinement strategy and stopping rule. More numerical resolution does not create more empirical observations.

A Resilience Exercise MUST follow Core Section 10.4, including initial isolation and the specific live grant and supported containment required for live assets. Applicable research protections remain in force. Injected artifacts retain controller-visible provenance and remain segregated from original measurements, participant records, blinded allocations and ordinary released research results. An exercise's detection outcome concerns the tested workflow, not the underlying scientific phenomenon.

### 7.2 Construction and delivery

A simplified investigation, including a toy model, simulation or finite counterexample, MUST state its purpose, generating assumptions or premises, target property and interpretation boundary. Distinguish stipulated, generated, observed and computed quantities.

Specify the procedure, inputs, design factors, comparisons and outcome measures needed for its purpose. For statistical simulation, ADEMP organizes aims, data-generating mechanisms, estimands, methods and performance measures [S11]. A small exact counterexample need not become a large performance benchmark.

Retain enough information to inspect or reproduce the claimed result: procedure or derivation, material inputs and dependencies, actual outputs, failures and deviations. Include code, parameters, random-number method, seed strategy, repetitions and enumeration bounds where used. Sampled performance estimates MUST report relevant Monte Carlo uncertainty. Exact finite enumeration has no Monte Carlo sampling error, while its specification and implementation still require checking.

Include valid controls alongside adverse cases when evaluating a discriminator. Identify planted faults, their coverage and assessors' exposure to them. For claims of added value, use a relevant ordinary workflow or simpler comparator and report outcome quality, false objections, unresolved cases and total relevant cost. State tuning, evaluation, exclusions, stopping and budget censoring.

Reported counts, rates, proportions and aggregate measures MUST identify the reference set, denominator or weighting basis needed for their interpretation. Reported probabilities MUST identify their events and any conditioning. A constructed failure establishes that failure's possibility under its conditions; an observed frequency pertains to the specified sampling procedure. Generalization and optimality require their own arguments.

## 8. Records, sharing and scientific delivery

### 8.1 Version the scientific basis

Keep protocol releases distinct from Study plans, data, procedures, environments, outputs and interpretation versions. A suitable repository, notebook, data service or disciplined versioned-folder practice MAY supply the necessary history [S16]. Capture material untracked changes and external inputs.

A version-control commit does not identify every input automatically. Git author and committer dates are configurable; local dates alone do not independently establish that a plan preceded outcome access [S19]. Use suitable timing and access evidence for the claim made.

A delivery MUST resolve the exact basis necessary to assess the stated result, subject to legitimate access limits. Distinguish a general identifier, particular version and exact content. Apply the core's binding, handoff and recipient-access requirements. Science adds no separate transport receipt.

### 8.2 Share under actual rights and responsibilities

FAIR permits access through authenticated or authorized procedures; accessible does not mean unrestricted [S17]. Applicable community governance, including CARE principles where relevant, remains binding [S18].

Restricted records MAY be represented by an authorized description, access route and limitation. Filenames, identifiers, hashes and small summaries can themselves reveal sensitive information. A synthetic substitute MUST be labeled and cannot establish exact reproduction of an unavailable original.

Use reporting guidance suited to the Study and output. PRISMA, SRQR and CONSORT have defined scopes [S14-S15, S24]; completing their reporting items does not replace appraisal of design and inference. Authorship, disclosure rights and approvals follow applicable governance.

### 8.3 Report the result and its basis

A finding MUST connect its conclusion to evidence and assessments, state uncertainty and coverage, preserve material contrary findings, identify deviations and report remaining obligations. Null, adverse and incomplete results MUST be included when material to the question.

Disclose consequential AI assistance and verification under applicable research policies [S02]. Retain relevant system or tool versions, inputs, consequential instructions, outputs and checks when needed for assessment or reproduction. Hidden private deliberation and every incidental prompt are not required. Verify generated citations against inspected sources.

Correct released scientific errors through the appropriate versioning and dissemination process. Core correction rules also apply to an erroneous review finding: correct the current assessment and affected dependent findings, while retaining the history rather than repeating a settled access limitation as a present defect of the Study. Automated checks MAY examine files, data properties, reruns or numerical regressions; report the property checked. A continuing scientific monitor additionally needs a defined detection target, uncertainty or error criteria, and interpretation limits under the core's continuous-operation contract.

Applicable research and review governance MUST resolve material financial and nonfinancial competing interests, required disclosures and participation or recusal decisions [S02]. Use the existing responsibility or review record. Disclosure alone does not establish independence or authorize participation; apply the rule to the actual duty.

## 9. Working methodology and proportionate use

Use scientific expertise and suitable existing tools. The core duties may be combined when permitted; a role roster is not a staffing quota. Resolve a bounded question through direct checking when that suffices.

| Core work | Scientific contribution |
| --- | --- |
| Grounding | Question, design, exposure, applicable protections and intended inference. |
| Faithful case and challenge | Evidence-to-claim argument, assumptions, material validity threats and discriminating adverse cases. |
| Examination | Authorized inquiry, actual results, deviations, failed attempts and unexpected findings. |
| Checking and judgment | Criterion coverage, design, measurement, uncertainty, identification and warranted scope. |
| Findings and release | Result, basis, limits, disclosure conditions and remaining obligations. |

This mapping adds no gates or mandatory research sequence. A compact review performs the relevant obligations using the core's selected procedure profile.

For a team adopting structured review, identify the specific gap and compare a small intervention with competent ordinary practice. Measure useful corrections and valid conclusions retained, as well as false objections, elapsed time, participant and tool effort, and disruption. Preserve open disagreements and cases the evidence cannot settle. Simplify or stop when added coordination fails to justify its cost.

## Appendix A. Scientific glossary

| Term | Meaning |
| --- | --- |
| Study | Scientific investigation associated with a review; distinct from the Review. |
| Research Owner | Person or organization holding responsibilities under actual research governance. |
| Estimand | Quantity an analysis aims to estimate, with population and conditions specified. |
| Measurand | Quantity intended to be measured, sufficiently specified for its purpose. |
| Independent unit | Unit at which the applicable sampling, allocation or independence argument holds. |
| Inferential warrant | Evidence and assumptions supporting the move to a stated conclusion. |
| Identifiability | Whether admitted information and assumptions uniquely determine the target quantity. |
| Identified set | Target values compatible with a population observation law and admitted assumptions. |
| Confidence region | Data-dependent region with a stated repeated-sampling coverage target and guarantee under specified assumptions. |
| Sensitivity set | Values obtained over declared alternative assumptions or inputs; no sampling coverage follows from that description alone. |
| Exposure | Information available before a consequential research or review decision. |
| Prospective plan | Plan preceding the decisions or exposure it is intended to govern. |
| Reproduction | Same-input computational repetition, with an assessed outcome. |
| Replication | New-data investigation of the same scientific question, with assessed consistency. |
| Rigorous enclosure | Set guaranteed under stated conditions to contain the specified exact result. |
| Simplified investigation | Deliberately restricted construction for examining a mechanism, method or limit. |
| ADEMP | Aims, data-generating mechanisms, estimands, methods and performance measures. |

## Appendix B. Interpretation and cautions

| Concern | Interpretation |
| --- | --- |
| Protocol completion | Records satisfaction of the stated process requirements. Scientific support and approvals retain their own criteria. |
| Shared dependencies | Separate roles or repeated computations may retain common data, sources, assumptions or implementation errors. |
| Scope and uncertainty | Exact calculation, reproduction, measurement fitness, identification and generalization address different questions. |
| Selection and exposure | Search, interim inspection, amendments and feedback affect the inference and independence that can be claimed. |
| Accountability | Automation retains the governing research responsibilities, permissions and protections. |
| Constructed evidence | Finite examples establish their stated properties; estimates of prevalence or comparative benefit require an appropriate investigation. |
| Opportunity cost | Review effort competes with research effort. Use existing records and stop unproductive repetition. |

ACR Science conformance describes the applicable protocol requirements fulfilled for a stated scope. Professional accreditation, ethical approval, institutional authorization and external endorsement require their own evidence. References support the particular distinctions for which they are cited.

## Appendix C. Sources

Source identifiers are local to this module.

**S01.** National Academies (2019). *Reproducibility and Replicability in Science*, scientific methods. https://www.nationalacademies.org/read/25303/chapter/5

**S02.** ALLEA (2023). *The European Code of Conduct for Research Integrity*. https://allea.org/code-of-conduct/

**S03.** Wasserstein and Lazar (2016). *The ASA Statement on p-Values*. https://doi.org/10.1080/00031305.2016.1154108

**S04.** Center for Open Science. *Preregistration*. https://www.cos.io/initiatives/prereg

**S05.** Center for Open Science. *Registered Reports*. https://www.cos.io/initiatives/registered-reports

**S06.** Fithian, Sun and Taylor. *Optimal Inference After Model Selection*. https://arxiv.org/abs/1410.2597v4

**S07.** Howard et al. (2021). *Time-uniform, nonparametric, nonasymptotic confidence sequences*. https://doi.org/10.1214/20-AOS1991

**S08.** Pearl (2009). *Causal inference in statistics: An overview*. https://doi.org/10.1214/09-SS057

**S09.** National Academies (2019). Computational reproducibility and replication. https://www.nationalacademies.org/read/25303/chapter/6

**S10.** NIST. *Metrological Traceability: Frequently Asked Questions and NIST Policy*. https://www.nist.gov/metrology/metrological-traceability

**S11.** Morris, White and Crowther (2019). *Using simulation studies to evaluate statistical methods*. https://doi.org/10.1002/sim.8086

**S14.** Page et al. (2021). *The PRISMA 2020 statement*. https://doi.org/10.1136/bmj.n71. [Expanded checklist, item 16a](https://www.prisma-statement.org/s/PRISMA_2020_expanded_checklist-yc78.pdf).

**S15.** O'Brien et al. (2014). *Standards for Reporting Qualitative Research*. https://doi.org/10.1097/ACM.0000000000000388

**S16.** Wilson et al. (2017). *Good enough practices in scientific computing*. https://doi.org/10.1371/journal.pcbi.1005510

**S17.** Wilkinson et al. (2016). *The FAIR Guiding Principles*. https://doi.org/10.1038/sdata.2016.18

**S18.** Global Indigenous Data Alliance. *CARE Principles for Indigenous Data Governance*. https://www.gida-global.org/careprinciples

**S19.** Git project. *git-commit*, commit information and dates. https://git-scm.com/docs/git-commit

**S24.** Hopewell et al. (2025). *CONSORT 2025 statement*. https://doi.org/10.1136/bmj-2024-081123

**S25.** COPE Review (2017). *Ethical guidelines for peer reviewers*, version 2. https://doi.org/10.24318/cope.2019.1.9

**S26.** mpmath 1.3.0 documentation. *Precision and representation issues*. https://mpmath.org/doc/current/technical.html

**S27.** mpmath 1.3.0 documentation. *Contexts*. https://mpmath.org/doc/current/contexts.html

**S28.** Arb documentation. *Using ball arithmetic*, inclusion semantics and input representation. https://arblib.org/using.html

**S29.** Imbens and Manski (2004). *Confidence Intervals for Partially Identified Parameters*. https://doi.org/10.1111/j.1468-0262.2004.00555.x

**S30.** Romano and Shaikh (2010). *Inference for the Identified Set in Partially Identified Econometric Models*. https://doi.org/10.3982/ECTA6706

**S31.** JCGM (2020). *Guide to the expression of uncertainty in measurement — Part 6: Developing and using measurement models*. https://doi.org/10.59161/JCGMGUM-6-2020

**S32.** Shmueli (2010). *To Explain or to Predict?* https://doi.org/10.1214/10-STS330

**S33.** American Psychological Association (2024). *Mixed Methods Article Reporting Standards*, JARS-Mixed Table 1. https://apastyle.apa.org/jars/mixed-table-1.pdf
