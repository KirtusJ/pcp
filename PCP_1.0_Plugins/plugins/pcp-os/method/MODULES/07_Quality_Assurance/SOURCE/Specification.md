# Adversarial Claim Review

# Quality Assurance Specification - Version 1.0

**Packet:** ACR Version 1.0, Implementation  
**Component:** `acr.quality_assurance`, Version 1.0  
**Required core:** `acr.core`, Version 1.0; Core descriptor SHA-256 `f15686b385002bf597c2625bc18e98a390531a21ce91f64bdb249f2fe04a86a7`  
**Creator and research direction:** Kirtus Justus  
**Specification assembly, source checks and constructed tests:** ChatGPT (OpenAI), assistant-origin; no independent professional validation or endorsement inferred.  
**Date:** 12 November 2026, America/Vancouver

This specialist module defines conditional Quality Assurance (QA) obligations for ACR use, on the same availability and task-selection terms as the other specialist modules, not a substitute for an organization's quality management system (QMS), product inspection, independent professional judgment, statutory duties or safety certification. Capitalized MUST / SHOULD / MAY express **normative requirements conditional on selection by an authorized task, Review commission or governing policy**; distributing this packet does not itself select them, amend Core or alter any released subject module. The Markdown source controls the component; its PDFs are informative reading copies. The sole required component is the exact Core identified above. A cross-module reference never silently adopts another component, standard or policy.

The module distinguishes **quality planning and assurance** (grounds for confidence that identified requirements will be fulfilled), **quality control and inspection** (tests or operations to determine or achieve conformity), **verification** (whether specified requirements are met), **validation** (whether intended use is fit), **safety assurance** (hazard-specific evidence), **epistemic warrant** (whether a claim is supported), **authorization** and **release**. None is an automatic consequence of another. Terminology may be mapped to the host's recognized disciplinary process when the substantive distinctions survive. [QA01, QA02, QA04]

## 1. Selection, entry and proportionality

1.1. Apply only to an identified quality-assurance assignment selected under the governing task, Review or policy. Possessing the packet, working on scientific results, or producing a numerical output does not automatically select this module, create a Review or authorize any action. Ordinary competent checking remains permissible without an ACR QA conformance claim.

1.2. Identify the quality-relevant subject: deliverable, process, service, information product, or particular effect boundary; its exact version and intended user/environment where material. Define what assurance is actually requested and which quality characteristics and governing acceptance criteria are relevant. A request for statistical inference does not alone require software QA, and a document review does not alone require aviation assurance.

1.3. Scale effort to consequence, complexity, reversibility, change risk, evidential uncertainty and expected checking benefit. Use the host's existing requirements, test plans, validation records, incident reports and version controls. This module mandates no new form, standing staff role, Review lifecycle, automatic second reviewer or duplicated record. Where scope and criteria are not known, do not convert UNKNOWN into NOT_APPLICABLE or assert success by vacuous passing.

## 2. Requirements, objectives and acceptance contract

2.1. Map material requirements and quality objectives to their actual source, edition or revision, applicability, authority, intended use, success criterion and evidence type. Differentiate laws and contracts, binding organizational policies, adopted standards, agreed product criteria, recommended methods and exploratory research desiderata. Cite a standard only for what was inspected. A purchased standard not examined clause-by-clause cannot be claimed to have been verified in full. [QA01-QA04]

2.2. For each conclusion-critical objective, establish a feasible, discriminating check or a reasoned competent assessment and the condition under which it would alter the disposition. Distinguish *demonstrated outcome* from mere presence of an activity, form, test name, or approval-looking token. A checklist is a navigation aid, not a proof of reliability. In particular, there is no universal scalar 'QA score' which certifies a result. [QA01, QA03, QA05]

2.3. Identify material interfaces, upstream inputs and downstream consumers. Where an acceptance criterion is missing or the requirements conflict, determine the affected claim or act and hold only that dependency; independently authorized unaffected work can continue. Do not silently invent pass thresholds, quality levels or the authority to waive them.

2.4. **Complete enough for the claimed purpose is not complete in principle.** Test whether specified acceptance objectives omit consequential quality dimensions, affected users, operating contexts, hazards, upstream suppliers or failure modes. The selection of a convenient test suite, a customer-supplied checklist or an inherited standard cannot itself establish completeness. Uninspected external rules and unidentified obligations remain unresolved rather than deemed nonexistent. Use the domain's actual requirements authority; QA invents no universal product criteria. [QA01, QA03, QA07, QA11]

2.5. **Quality tradeoffs and stopping criteria.** Where objectives compete (for example accessibility, latency, reliability, privacy or cost), identify the governing decision-maker and actual acceptance basis. A composite quality score MUST NOT conceal a separately binding critical requirement or convert a measured surrogate into the full objective. More checks, more severe findings, greater delay or more documentation are not automatically improvements. Proportionate stop conditions may permit a bounded unresolved result rather than either manufactured approval or indefinite review.

## 3. Evidence, coverage and assurance argument

3.1. For every conclusion-critical requirement, maintain a reconstructible link among the requirement, versioned item, claimed property, acceptance basis, verification or assessment method, actual execution/evidence, result, material exceptions and final scoped conclusion. An existing task record may hold all these meanings. If a required test has not run, record the actual state rather than treating its design as successful execution.

3.2. Check that the evidence *measures the claimed property*. A content hash checks byte identity, not provenance authenticity, semantic correctness or applicability. A passing unit test checks its chosen fixtures, not untested system behavior. Passing a reporting checklist does not certify design quality, causal identification, statistical calibration or safety. An inspection finding and an unread/unavailable inspection record are different claims. [QA04-QA06]

3.3. When risk or criticality warrants, distinguish requirement coverage, input/boundary coverage, operating-envelope coverage, adverse controls, regression after change, independence of the checking path, failure detection, timeliness and recovery. Evidence may be reused across requirements only if its checked property, version, conditions and inferential scope fit each. Do not equate percentage of requirements listed with completeness of the quality case.

3.4. A positive or negative finding MUST disclose materially relevant exclusions, untested conditions, uncertainty and common dependencies among tests. A reliable adverse witness can refute a universal acceptance claim even when only a narrow boundary was inspected. Unsupported failure speculation does not establish an actual nonconformity. Statistical estimates of risk require appropriate Statistics expertise or adopted procedures but are not the same as operating hazard controls.

3.5. **Statistical limits of assurance samples.** For test/inspection findings presented as prevalence, reliability or safety evidence, establish the sampled population, selection and exposure process, observation/defect definition, inspection sensitivity where relevant, independence or clustering and intended inferential scope. Zero recorded failures do not establish zero risk. A sample-size formula or nominal confidence limit conditional on iid trials is not transferable to selected or dependent repeats without a defensible bridge. QA may assess the evidence contract; Statistics and the governing domain own specialized inference and accepted safety criteria. When a broader QA rate is inferred, distinguish scheduled, executed, evaluable, passing, failed and inconclusive inspections where material, with their respective denominators; preserve exclusions and the effect of pooling critical and routine cases. An observed pass among tested items may remain valid even where broader assurance is unsupported. Do not manufacture counts, assign arbitrary pass thresholds or require subgroup estimates when their inferential contract is absent. [QA11, QA12]

3.6. **Requirement identity and aggregation.** Where requirements or test evidence are enumerated and machine-checked, a repeated identifier, overwritten version label or reused check result MUST NOT silently count as distinct satisfied obligations. Check identity uniqueness and version fidelity at the actual item/evidence granularity when a coverage or sign-off claim depends on them. A record that merely declares a stable revision number cannot substitute for a trustworthy link to the item actually inspected. This is a property to justify, not a mandatory file format.

3.7. **Assurance-claim continuity and escalation.** When findings are summarized, pooled, reissued, translated, incorporated into another report or passed to an LLM, retain the material acceptance basis, tested property, object/version, population or operating scope, evidence limits, unresolved hazards and any restrictions on downstream use. Repetition, agreement, sign-off-looking language or a passing quality gate cannot strengthen a narrow finding into a claim of safety, fitness, independent validation or certification. A faithful compact handoff may reference stable records; no new canonical JSON payload is mandated.

## 4. Competence, impartiality and independence

4.1. Resolve competence for tasks where it affects assurance, including domain knowledge, method choice and use of the relevant version of a standard. Role names, multiple model outputs and polished reports do not create professional qualifications. Disclosure of common provenance is required for consequential independence claims.

4.2. Assess independence and conflict of interest appropriate to the consequence and applicable sector rules. Separate participant identity, organization/provider, data and source provenance, model architecture/training, analysis design, implementation and true execution environment. Different model personas or prompts sharing one underlying assistant do not constitute independent validation. Independence is not mandatory for every routine check. [QA03, QA07]

4.3. If the same actor constructs and checks an artifact, label it self-review or internal checking. Such checking remains useful but should not be called external independent assurance. Evidence from another actor who relies on identical erroneous assumptions is likewise not independent confirmation of those assumptions. In high-consequence cases, identify which degree of independence is required and who has authority to attest it.

4.4. **Bias in quality judgments.** Where material, identify incentives and information flows that can cause false acceptance or false objection: management or reviewer pressure, premature closure, checklist completion targets, preferential selection of easy cases, confirmation bias, skeptical overreach, anchoring, automation bias, group consensus, suppressed contrary evidence and bias in who is heard. Require fair treatment of the original claim and both supporting and contradictory evidence. A reviewer's skepticism must not be taken as evidence of error, nor an organizational sign-off as evidence of truth. Record unresolved objections without inventing a misconduct finding; use the actual impartiality, appeal or escalation process where applicable. [QA03, QA13, QA14]

## 5. Verification, validation and fault-oriented checking

5.1. Select checks based on actual failure modes and use conditions, including normal valid cases, boundary cases and plausible adverse cases. Where useful and authorized, inject controlled defects or mutations to determine whether checking detects a specific known fault. Do not expose protected data or cause real-world hazards in the name of an adversarial exercise. No mandatory Resilience Exercise machinery or exhaustive test enumeration is imposed.

5.2. Distinguish requirements conformance (verification) from intended-user fitness (validation). For deployed or relied-upon tools, consider integration, accessibility and human use, robustness, security, latency, failure response, maintainability and operational monitoring when applicable. A passed small test does not imply reliable performance in untested environments. [QA02, QA04, QA06]

5.3. Assess known failure of the checker itself where material: false acceptance, false blocking, stale evidence, test-data contamination, incorrect oracle, ineffective mutations, hidden common cause, unreported failure and unreliable notification. A checker failing to detect an injected known fault is not 'PASS'; a checker wrongly rejecting a known-conforming case is likewise deficient. For each control, specify whether its expected outcome is fault detection/rejection or justified acceptance, so the labels 'positive control' and 'negative control' cannot reverse the intended polarity. Passing finitely many controls does not establish complete detection. Do not demand a checker that proves its own completeness by recursive QA.

5.4. **Checker and oracle limitations.** Treat a fixture-based gate reporting success from self-declared fields such as `relevant`, `independent_basis_verified` or `actual_execution` as structurally conditional: those flags do not authenticate underlying tests. If acceptance depends on an opaque or shared source, trace the source's limitations and common causes; where proportionate, challenge the oracle with independent alternative observations or controlled mutations. Counts of passing fixtures, independent-looking role labels and traceability edges are not measured sensitivity or specificity. Negative controls MUST be accompanied by legitimate positive controls when evaluating detection quality. [QA07, QA13]

## 6. Nonconformance, correction and continuous learning

6.1. Distinguish an **established nonconformity** against identified criteria, an **unestablished property** due to absent or inaccessible evidence, an **anomaly** needing diagnosis, a **corrected factual or measurement error**, and a **risk hypothesis**. Use Core's actual finding dispositions for commissioned Reviews rather than silently creating an alternative vocabulary with conflicting status meanings.

6.2. Identify the consequences and authorized protective response of a material defect. Separate immediate containment, correction of the particular item, causal analysis and corrective action intended to prevent recurrence. A proposed root cause is not an established root cause without support; a correction is not verified merely because it was made. [QA01, QA05]

6.3. Assess whether a corrective action works and whether it creates new regressions or misses upstream/downstream dependencies. Preserve enough provenance to reconstruct prior relied-upon findings without retaining data beyond lawful permissions. Disclose unresolved nonconformities or evidence limitations to recipients who depend on the result.

## 7. Change, delivery, effect and retirement

7.1. Changes to the item, requirements, evidence base, tool/LLM model, method, configuration, operating environment or applicable standard SHOULD trigger a scoped impact assessment when they can affect relied-on conclusions. Changes in LLM capabilities, access tier, instructions, context, tools or provider configuration may affect future checking fidelity, but a model label or tier is not a certified capability level. If an identifying fact is unavailable, report the limitation rather than inventing a model version or claiming continuity. A change does not *automatically* invalidate all earlier evidence; retain valid, independently checkable evidence where its tested property, configuration and intended use remain applicable. A model-name/version switch alone is neither proof of invalidity nor proof of equivalence. [QA02, QA04, QA06]

7.2. Preserve distinct records for designed checks, executed checks, observed outcomes, approved release and actual deployment. A valid assurance assessment is not release permission. Before a consequential external effect, resolve the governing destination's current authority, approval, identity and environment. A technically conforming artifact can still be unauthorized or unsafe to deploy for the new intended use.

7.3. Quality obligations may continue through operation, monitoring, feedback, maintenance, supplier change and retirement. A Review finding is bounded by its evidence and cutoff and does not imply completed future inspections, certification or continuously running monitoring. Identify triggers and responsibilities only when actually known or authorized. [QA01-QA04]

## 8. Cross-module composition and boundaries

8.1. **Core (the sole required component, as identified above)** governs the actual commission, permissions, roles if commissioned, provenance, obligations, scoped dispositions, handoff and changes. QA adds specialized quality-process and product-assurance checks; it does not change Core's rule hierarchy, certification semantics, or existing general evidence discipline.

8.2. **Engineering** already owns hazards, design and use-case assurance, concrete physical controls and lifecycle obligations. QA MUST NOT waive or replace those rules; selecting QA alone is not enough to claim engineering or regulated safety fitness. Engineering's own rule on reliance on the assessment process (at `acr.engineering` 1.0: Section 6.3; an informative pointer) remains binding when Engineering is selected.

8.3. **Science** retains empirical methods, design/exposure and scientific uncertainty. QA may assess the process and reporting, but a quality certificate-looking checklist cannot establish scientific truth or an observation law. Science's statistical safeguards remain binding even if Statistics is absent.

8.4. **Mathematics** retains proof validity, formalization and numerical soundness. QA may verify that proof checks were run, but it cannot infer proof correctness from packaging. **Cryptography** retains threat models, random source assurance and secure operation; passing generic QA cannot certify cryptographic security.

8.5. **ACR Statistics** (component `acr.statistics`, Version 1.0), a separately selectable module, is **not a required dependency** and is not adopted by this cross-reference. It governs specialist sampling, inferential guarantees, uncertainty, identification and predictive questions when independently selected or otherwise applicable. QA may examine whether suitable statistical checks were selected, executed and faithfully reported; a QA inspection cannot silently certify statistical inference, and withholding Statistics does not waive obligations already binding through Science, Engineering, a task policy or external law.

8.6. **Unassigned adjacent responsibilities.** QA examines evidence and delivery quality when selected; it does not automatically govern metric design, data operations or all communication. Where a property requires specialist evaluation not covered by selected competent work, preserve the unresolved dependency rather than inventing another ACR module or declaring compliance.

8.7. Where several selected modules govern the same work, required obligations compose under Core §14.1. Evidence may be shared with scoped attribution; no module withdrawal waives another independently binding obligation. A new module selection does not retroactively revise prior findings. Authority for an external standard derives from its real adoption or applicability, not from being listed here.

## 9. Evidence of ACR QA's own worth

9.1. Treat QA as an intervention subject to assessment, not an intrinsically beneficial layer. Compare with competent ordinary QA and the selected Core/domain-module controls on matched tasks, information, models, workers and resource ceilings. Include both correct and faulty outputs; otherwise always blocking can look excellent and always accepting can look efficient. Measure delivered completeness, supported conclusions, false acceptance, false rejection/obstruction, defect severity, time to useful work, rework and total human/tool cost. [QA01, QA05-QA08]

9.2. Independently adjudicate consequential cases where warranted, and record judge limitations and dependencies. Predeclare evaluation questions and criteria before looking at the comparison results where possible. Real-world quality improvement remains unproved until a suitable evaluation is executed; no finite constructed test establishes deployment efficacy.

9.3. Use the simplest useful QA plan for the actual project. A narrow checklist or direct test may suffice. Redundant audit rituals, recursion, ceremonial roles, extra forms and blanket mandatory approvals should be removed when they add no demonstrated protection. For high-consequence work, preserve genuinely required additional checks even if their cost is high.

9.4. **The cost of wrong assurance decisions is bidirectional.** A credible evaluation must score false acceptance and false rejection separately, including severity and delayed downstream effects, and ask whether the added QA layer changes actual user actions beneficially. An always-blocking, all-negative reviewer is not a safe or useful QA system. If independent adjudication is unavailable, report that limitation without manufacturing expert agreement. External certification, deployment suitability and causal improvement in outcomes remain unevaluated. [QA01, QA13]

9.5. **Community-benefit claims and assessor validity.** Benefits to experienced QA practitioners, novice users and LLM-assisted teams are distinct hypotheses. An improvement observed only against a weak baseline MUST NOT be advertised as an improvement over competent professional QA. Use task-specific independent adjudication when warranted and feasible, disclose judge dependencies, and report the distribution of consequential misses and unnecessary blocks alongside average scores. Prefer retaining the simpler practice if comparable evidence finds no acceptable net improvement.

## Appendix A. Reader caution (informative)

- QA is not a regulator, accreditation body, certification service, engineering signatory, statistical inference engine or provenance authenticator.
- Published standard edition and status must be checked for the actual date. A purchased standard not read cannot support a detailed claim of exact conformance.
- A citation, digest, attestation, checklist, test-suite pass or multiple agreeing LLM outputs each supports a different proposition; none is a general proof of correctness.
- In a high-risk setting, the host organization and competent domain professionals retain authority and duties set by applicable law and policy.
- A reviewer encountering a missing record should distinguish unavailable evidence from evidence that the required activity was never done.

## Appendix B. External reference ledger (informative)

**QA01.** ISO 9001:2026, *Quality management systems - Requirements*. ISO publication 16 September 2026. Publisher description and edition record, https://www.iso.org/standard/88464.html. **Published/paid full text not reviewed**; QMS reference, not an ACR certification basis.

**QA02.** ISO/IEC 25010:2023, *Systems and software Quality Requirements and Evaluation: Product quality model*, https://www.iso.org/standard/78176.html. Product-quality model, not a universal quality metric.

**QA03.** ISO 19011:2026, *Guidelines for auditing management systems*, published May 2026, https://www.iso.org/standard/19011. Auditing guidance, not itself certification. **Full normative text not inspected**.

**QA04.** IEEE 730-2026, *IEEE Standard for Software Quality Assurance Processes*, published 21 August 2026, https://standards.ieee.org/ieee/730/10854/. Software-specific SQA requirements; **full standard not reviewed**.

**QA05.** American Society for Quality (ASQ), *Quality Assurance vs Quality Control*, https://asq.org/quality-resources/quality-assurance-vs-control. Explains distinctions and overlaps; not itself binding governance.

**QA06.** NIST AI Risk Management Framework 1.0, https://www.nist.gov/itl/ai-risk-management-framework. Risk-oriented testing, measurement, independent review and uncertainty; voluntary cross-domain comparison unless adopted.

**QA07.** NASA, 5 November 2026 announcement of **draft** NASA-STD-8739.8C, https://sma.nasa.gov/news/articles/newsitem/2026/11/05/nasa-modernizes-software-assurance-guidance-with-updates-to-nasa-std-8739-8c-and-the-software-engineering-and-assurance-handbook. Describes outcome-oriented software assurance and 94 draft objective-based requirements; not an active adoption claim. NASA standards register still identified Revision B as active on inspection, https://standards.nasa.gov/standard/nasa/nasa-std-87398.

**QA08.** National Academies (2019), *Reproducibility and Replicability in Science*, https://www.nationalacademies.org/read/25303/chapter/3. Uncertainty, methods, analysis timing, and clear reporting.

**QA09.** TRIPOD+AI (2024), https://www.bmj.com/content/385/bmj-2023-078378, and CONSORT (2025), https://www.bmj.com/content/389/bmj-2024-081123. Reporting guidance; **neither is a general quality certificate**.

**QA10.** SAE ARP4754B (2023) and ARP4761A (2023), relevant to systems development and safety assessment in civil aviation. Proprietary full texts not accessed. FAA AC 20-115D recognizes DO-178C means of compliance in identified airworthiness contexts; none automatically applies to ACR.

**QA11.** NIST/SEMATECH e-Handbook of Statistical Methods, https://www.nist.gov/programs-projects/nistsematech-engineering-statistics-handbook. Established measurement, monitoring and reliability methods.

**QA12.** American Statistical Association, *Ethical Guidelines for Statistical Practice* (2022), https://www.amstat.org/your-career/ethical-guidelines-for-statistical-practice. Relevance of competence, inference limitations, conflicts, correction and stakeholder harm.

**QA13.** PCAOB, AS 1000, *General Responsibilities of the Auditor in Conducting an Audit*, https://pcaobus.org/oversight/standards/auditing-standards/details/as-1000--general-responsibilities-of-the-auditor-in-conducting-an-audit. Financial audit context only; both corroborating and contradictory evidence; management and auditor bias.

**QA14.** IAASB, *Embedding Professional Skepticism*, https://www.iaasb.org/focus-areas/embedding-professional-skepticism. Explains audit context, multiple cognitive biases and the importance of questioning evidence; not an ACR requirement unless separately adopted.
