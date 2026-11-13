# Adversarial Claim Review

# Statistics Specification - Version 1.0

**Packet:** ACR Version 1.0, Implementation  
**Component:** `acr.statistics`, Version 1.0  
**Required core:** `acr.core`, Version 1.0; Core descriptor SHA-256 `f15686b385002bf597c2625bc18e98a390531a21ce91f64bdb249f2fe04a86a7`  
**Creator and research direction:** Kirtus Justus  
**Compilation and internal checks for this version:** ChatGPT (OpenAI). Assistant-origin construction. No independent professional assessment, independent release approval, or regulatory certification is claimed.  
**Date:** 12 November 2026, America/Vancouver

This is the **version 1.0 text** of a separately selectable ACR specialist module, under the same selection rules as the other specialist modules. Its MUST / SHOULD / MAY terms have their ordinary protocol meanings **only when this exact component is adopted for identified work under governing authority**: MUST is mandatory when its premise applies; SHOULD may be departed from for a defensible, disclosed reason; MAY is permitted but not required. This module is available in the seven-component collection on the same terms as other specialist modules. Availability, download or distribution does not select it for any task; an authorized task or governing policy resolves actual applicability. This module does not amend Core or any other specialist module. Core and any independently binding obligations retain precedence whether or not this specialist is selected. No example, PDF, package check or version label certifies a statistical conclusion, production safety, or permission to deploy.

The module is about **ACR's use and review of statistical work**, not a claim to contain the discipline of statistics. It does not prescribe a universal philosophy of inference or infer that all numerical, scientific, predictive, or analytics work is statistical. Statistical correctness, useful evidence, policy permission and ACR conformance remain separate properties.

## 1. Entry, applicability and proportionality

1.1. Statistics applies **only** when an authorized task, Review commission or governing policy selects the exact module for identified statistical work. Availability, installation, topic labels or obtaining this file do not select it, commission a Review, create roles or grant permissions. Statistics requires only exact Core by component definition. No other specialist module is an implicit dependency. No independent Review lifecycle, default roleplay or standing JSON form is created. Existing competent statistical work remains permissible under its governing requirements without an ACR Statistics conformance claim.

1.2. Intended scope includes statistical design, data acquisition, descriptive characterization, sampling, estimation, testing, uncertainty assessment, predictive assessment, causal inference where statistically claimed, measurement and calibration when statistically claimed, and statistical information supporting decisions. A purely deterministic proof or exact numerical identity does not become a statistical inference solely because it contains numbers. Qualitative or descriptive work must not acquire an artificial hypothesis test.

1.3. Apply only obligations material to the actual claim and intended use. An inapplicability finding must be supported by the work; UNKNOWN must not be relabeled INAPPLICABLE. An unestablished prerequisite limits the dependent conclusion, not independently authorized preparation. A useful short answer, artifact or analysis should not be replaced with protocol administration. Reuse the host task, source material, working evidence and existing records.

1.4. Where a statistical question is materially unresolved, identify an expert or authoritative reference suitable to the particular work if needed. Module activation does not create competence or constitute independent peer review; no universal requirement for an extra reviewer follows solely from applying this module. Distinguish personnel expertise from actual scope of an assessed claim.

## 2. Target, estimand and decision meaning

2.1. Before making a consequential statistical claim, establish the relevant target: quantity or estimand, population or system, observational and sampling units, conditions and time window where relevant, interventions/exposure if claimed, comparator, decision use, and the exact statement the analysis is supposed to support. An estimand is not always a single point effect; it may be a distribution, contrast, functional, identified set, rate or prediction target. Do not import a treatment-effect estimand into work for which it is irrelevant. [ST03]

2.2. Separate **descriptive observation**, **population/generalization**, **predictive performance**, **causal/interventional inference**, and **decision recommendation**. A correct summary of a provided finite dataset does not by itself justify a population, future, causal or safety claim. A valid statistical result does not supply permission for consequential actions or establish that a utility or loss model is appropriate.

2.3. Define the intended reference or comparison class, consequential difference or margin when relevant. A p-value or confidence interval cannot alone establish practical importance, equivalence, clinical benefit, engineering fitness, or regulatory acceptance. If an acceptance threshold comes from the commission or governance, identify its owner and scope; do not silently invent a threshold. [ST01, ST02]

## 3. Data-generating process, design and exposure

3.1. Identify material origins and acquisition conditions: frame, selection, inclusion and exclusion, units, missingness, censoring, clustering, correlation, temporal/spatial structure, measurement and annotation, calibration, linkage, transformations, and any restrictions on lawful use. Distinguish raw samples, repeated readings and independent replicates. No universal iid assumption is permitted; iid methods are admissible where justified for the actual procedure. [ST04, ST05]

3.2. Disclose materially informative analysis choices made after seeing outcomes, diagnostics or evaluation feedback, including searches, stopping, exclusions, tuning and repeated comparisons. Prespecification and preregistration are useful when actually performed, but may not be retroactively asserted. Purely exploratory work remains legitimate when labeled and interpreted as exploratory.

3.3. Where random allocation, weighting, stratification, nonresponse corrections, intervention or controls are material, assess their actual implementation and limitations. A model-based statistical analysis cannot silently repair deficient design, confounding, dependent errors or changed operating conditions. External approvals and data rights remain governed by their actual authorities.

3.4. Treat information *exposure* as wider than raw outcome access. Optimization feedback, evaluation scores, subgroup summaries, analytic choices, stopping information and earlier model-generated proposals can inform later choices and invalidate a claimed blind or fixed-procedure check. Identify the actual unit of replication and dependence structure. Pseudoreplicated readings MUST NOT be counted as independent sampling units merely because they occupy separate rows. Preserve validated survey/design-based alternatives rather than mandating an iid correction for all designs. [ST02, ST12, ST13]

## 4. Statistical models and estimation contracts

4.1. For each relied-on procedure, identify the input data, statistic/estimator, target, population model or design-based randomization, assumptions, fitting or training, uncertainty and diagnostics necessary for the claim. A computational implementation is not the inferential model. A valid formula under its assumptions does not establish those assumptions for the actual data.

4.2. Choose finite-sample, asymptotic, Bayesian, robust, simulation-based, randomization-based, likelihood-based, nonparametric, semiparametric or other justified approaches according to their claims and conditions. **No mandatory preference for finite-sample bounds, significance tests, Bayesian estimators, test martingales, identified-set projection or other named technique.** Exact results are preferable only when their assumptions and target match and the cost/precision tradeoff is justified. Asymptotic approximations remain admissible when their use conditions and limitations are warranted.

4.3. Report uncertainty sources material to the claim: sampling or allocation, model specification, nuisance estimation, measurement and calibration, numerical computation, dependence, sensitivity to assumptions and external validity as appropriate. Do not add incompatible uncertainty quantities mechanically. When uncertainty cannot be adequately bounded, communicate that limitation rather than invent precision.

4.4. Missing data and selected samples require an explicit account of observed versus unobserved targets, assumptions needed for generalization and feasible sensitivity analysis where material. Model diagnostics and goodness-of-fit can reveal limitations, but passing diagnostics alone does not prove a model correct.

4.5. When observations are clustered, weighted, longitudinal or dependent, the recorded uncertainty argument MUST refer to that design and the actual unit of replication. Model-based, design-based and resampling approaches can be appropriate under different assumptions. No effective-sample-size formula or cluster correction is universally valid; a label such as "robust standard error" is not proof that the particular dependence or number of clusters supports its claimed guarantee.

## 5. Statistical inference, guarantees and scope

5.1. Distinguish, as applicable: an estimate versus true target; a **population identified set** versus its sample estimate; **point coverage** versus simultaneous coverage of an entire identified set; pointwise versus uniform guarantees; finite-sample versus asymptotic properties; fixed-horizon versus time-uniform validity; confidence versus credible versus prediction intervals; interval enclosure versus stochastic coverage. Report the interpretation actually established. [ST06]

5.2. A confidence or error-control claim MUST identify its model, quantifiers, actual procedure, sampling/exposure conditions and relevant selection process. A named nominal level (e.g. 95%) alone is not evidence of achieved coverage. A Bayesian posterior or credible interval must be interpreted under its prior and likelihood and must not be advertised as having frequentist coverage unless separately established. A prediction interval is not automatically a confidence interval for a parameter.

5.3. Repeated looks, adaptive decisions, multiplicity, selected reporting and data-dependent stopping MUST be accounted for **when they change the claimed error guarantee**. Legitimate controls may include prespecified sequential boundaries, alpha spending, time-uniform methods, selection-adjusted inference, appropriate conditional analysis, properly justified simulation, or an appropriately narrowed claim. One tool or correction is not required everywhere. A fixed-time error guarantee must not be silently promoted to anytime validity.

5.4. Partial identification and observation-equivalent models must not be presented as point identification. Statistical uncertainty and *structural* nonidentification are separate questions. An empty empirical compatibility region is not by itself proof that the population model is contradictory. A set-valued result must state which set and inferential notion it represents. [ST06]

5.5. A test rejection is not a proof of the alternative hypothesis; a failure to reject is not proof of the null. A p-value is not the probability that the null is true. Report effect/precision and substantive context when material. Neither a positive nor a negative result is a performance target. [ST01, ST02]

5.6. Where a conclusion concerns multiple targets, comparisons, time points, selected subgroups or a *whole set*, the inferential guarantee MUST match that joint scope. Individually valid intervals or tests do not automatically provide simultaneous coverage or familywise control. Conversely a global adjustment must not be imposed on every descriptive or exploratory comparison without a clearly stated protected claim. [ST01, ST06, ST11]

5.7. **Rare-event and safety-related claims.** When a statistical result is offered as evidence of low hazard probability, audit the actual denominator, opportunities for failure, sampling unit, censoring/ascertainment, dependency, adverse exposure and detection sensitivity. In particular, zero recorded adverse events or zero detected defects MUST NOT be interpreted as zero hazard, universal safety, operational reliability or safety certification. Any confidence or credible upper bound is conditional on its explicit data and observation model, and its transfer to a deployment or safety threshold requires a separately justified bridge. This provision does not prescribe a universal probability-of-failure threshold, an iid model or any particular estimator; domain safety rules retain priority. [ST02, ST04, ST15, ST17]

5.8. **Aggregation and critical-stratum evidence.** For a conclusion that extrapolates an aggregate rate or model score to consequentially different groups, operating modes, exposures or failure types, assess material heterogeneity and whether small, safety-critical strata are masked by dominant routine observations. Preserve the denominator, sampling contract, detection capability and uncertainty for any asserted stratum-level conclusion. A subgroup analysis is not universally mandatory, and a sparse or selected stratum cannot be assigned unjustified precision. Where relevant strata cannot be observed, narrow the assurance claim rather than treating aggregate performance as proof of universal acceptability. [ST02, ST04, ST15] 

## 6. Measurement, calibration and numerical assurance

6.1. If a claim depends on instrument or measurement accuracy, identify the measurand, relevant reference and calibration data, response model, stability, uncertainty, correlations and operating range. Treat estimated nuisance and calibration quantities with appropriate uncertainty when they materially affect inference. [ST04]

6.2. A required joint uncertainty guarantee can be established using a suitable confidence region, validated propagation, likelihood, Bayesian model, bootstrap, conservative bounds or other justified procedure **only within its applicable assumptions**. Joint projection is an available technique, **not universally mandated**. Data whose instrument sensitivity is effectively zero may support weak or no identification; do not assume a positive gain floor from an unstable estimated denominator.

6.3. A statistical sampling statement is distinct from rounding error, numerical stability, rigorous numerical enclosure and deterministic mathematical proof. Reuse Mathematics and Science checks when separately applicable; one check may support several obligations only when its checked property and limits actually fit each. Cross-implementation agreement alone is not independent proof of an unverified assumption.

## 7. Prediction, causal claims and operational decisions

7.1. For prediction, identify the target/horizon, information actually available at prediction, selection and fitting history, dataset overlap, leakage mechanisms and validation environment. Examine out-of-sample evidence or another justified predictive performance argument when relied on. Distribution drift and subgroup limitations are relevant when they could change the action. No universal exchangeability assumption is required; any such assumption must be justified when used.

7.2. For causal claims, declare the intervention/exposure and identifying conditions: randomization, confounding assumptions, instruments, natural experiments, structural restrictions, temporal order or other valid design where appropriate. A directed acyclic graph may clarify assumptions but is **not mandatory for all causal inference**. Prediction accuracy does not by itself justify a causal intervention.

7.3. For consequential decisions using statistical outputs, distinguish model validity, decision rule, loss/utility assumptions, alternatives, error consequences, required professional or regulatory judgment, authorization and operational fallback. A score cannot authorize its own deployment. Risk thresholds are task- and governance-dependent; no module-wide numerical aviation or enterprise safety limit is supplied.

7.4. When consequential predictive or algorithmic claims concern real users or changing environments, assess material transport, dataset shift, subgroup performance, outcome-label quality, and feedback effects, as applicable. A validation dataset is not clean solely because it has a separate filename; tests contaminated by selection, tuning, or exposure require a defensible claim-specific account. Neither a single fairness metric nor a universal accuracy threshold is prescribed. [ST07, ST12, ST14]

7.5. **Decision consequences and bias.** For materially safety-affecting use, distinguish statistical error rates from harm severity, detection and reporting processes, human response, available protective controls and authority to act. Identify who bears false-positive and false-negative costs where material, and whether selected populations, missing subgroups or institutional incentives could distort claimed benefit, fairness or safety. A point estimate or nominal risk threshold is not a safety argument. Do not impose universal fairness metrics or demand demographic analyses where they would be inapplicable or prohibited; use competent, lawfully justified, context-specific evaluation. [ST02, ST07, ST16, ST17]

## 8. Checking, disposition and correction

8.1. Connect each conclusion-critical obligation to a check or competent assessment. Include known-valid and known-invalid controls where they discriminate relevant defects. Preserve design, relevant code/data versions and provenance without requiring prohibited data retention. Different scripts sharing one defective assumption do not supply independent external confirmation. A simulation establishes only properties of the simulated model and procedures under its stated conditions.

8.2. Use Core §5.2 dispositions unchanged. In particular: a valid conditional probability calculation can be supported **as a conditional calculation** without establishing that its model applies; an unsupported estimate is not necessarily `REFUTED_IN_SCOPE`; observed nonidentification requires a witness, not simply the absence of a found estimator; failure of a test to reject is not a verified negative effect.

8.3. Material correction, changed data law, revised code, discovered selection, exposure, new calibration or changed model calls for impact assessment on affected claims. Preserve earlier provenance and exact analysis basis; no retrospective adoption or concealed hypothesis switch. Communicate limitations and corrections through the user's required output rather than replacing it with a protocol dashboard.

8.4. A favorable statistical assessment does not establish data access rights, human-subject approval, cryptographic secrecy, engineering safety, regulatory conformity or release permission. If an activity is prohibited by binding law, governance or current authorization, module applicability does not waive the prohibition.

8.5. State evidentiary provenance with appropriate granularity: an original source, one assistant's self-generated review, separately provided collaborators' submissions, reproduced execution, independent reconstruction under shared premises, and external independent assessment are distinct. Agreement among outputs sharing hidden assumptions is not a counted number of independent confirmations. An uninspected source cannot be used to claim source-specific contents absent from the public metadata. [ST02, ST13]

8.6. **Balanced adversarial review.** Seek both evidence that could support the original proposition and evidence that could refute it. An adverse-search brief is a method for finding weaknesses, not a prior that the claim is false. An objection MUST identify the affected proposition, evidence or necessary missing information, and material effect; absence of inspection cannot be silently converted to observed absence. Keep legitimate positive controls and unresolved cases, including very small effects when relevant. Undeserved confirmation and undeserved obstruction are both review errors. [ST02, ST13]

8.7. **Statistical model versus reviewing LLM.** Distinguish a statistical model/procedure from any language model or tool generating, reviewing, or interpreting it. Known material changes in the latter's configuration, capabilities, prompts, source access or context SHOULD receive a targeted impact assessment for unverified claims and future actions; retain unaffected, independently established evidence. If host configuration is unknown, disclose that fact without claiming a downgrade or verified equivalence. A self-report, tier label or independent-looking persona is not a quantitative guarantee of reviewing accuracy. [ST02, ST16]

8.8. **Assurance escalation and reviewer incentives.** Any broader conclusion drawn from an earlier computation, QA pass, independent-looking review, or statistical report MUST have its own justified inference and applicability bridge. The reviewer SHOULD consider incentives to approve, reject, delay, or conceal uncertainty, and test for both unsupported acceptance and unjustified obstruction when material. The same evidence cannot be counted as fresh independent corroboration merely because it passes through more tools, roles or documents. This clause adds no new release authority and does not require a standing QA module. [ST02, ST07, ST13] 

## 9. Cross-module composition

9.1. **Core (required)** owns general evidence discipline, authority, roles when commissioned, correct claims, permissions, the selected assessment procedure, context and delivery. Statistics adds statistical-specific checking. Internal Core sections are not replaced or weakened by this module.

9.2. **Science (independently selectable)** retains scientific questions, hypothesis/observation grounding, approvals, empirical applicability and its own statistical obligations (at `acr.science` 1.0: Sections 4.2 and 5.4; an informative pointer). Adding Statistics does not migrate, delete or waive them. Science's result need not depend on Statistics being selected; a task policy MAY separately require Statistics for declared statistical claims. Unresolved conflicts are handled under Core §14.1, not by module load order.

9.3. **Mathematics** retains formal deductions, proof domains, rigorous numerical claims and computational checking. Statistics may require mathematical proof of an inferential guarantee; Mathematics is not automatically selected merely because statistical methods use mathematics. Conversely a formal bound alone does not prove sampling premises.

9.4. **Engineering** retains hazard analysis, lifecycle assurance, requirements, actual controls and residual-risk authority. A statistical reliability estimate is not evidence that an engineering safety barrier exists or works; an engineering obligation may trigger statistical work without automatically requiring an additional ACR Review.

9.5. **Cryptography** retains threat models, entropy-source obligations, key/state management and security claims. Randomness tests do not establish cryptographic unpredictability. Statistical assessment cannot supply cryptographic authorization or defeat required secrecy controls.

9.6. **Unassigned adjacent responsibilities.** Data processing, communication and presentation remain governed by the actual task and independently applicable Core or specialist obligations. This component does not invent another module, transfer an existing responsibility, or make a communication or data-tooling activity automatically statistical.

9.7. Shared check evidence can be reused only with explicit scope, version and interpretation. A new module selection uses the existing task or Review; it cannot silently reopen or rewrite an assessment or redefine another module's required Core.

## 10. Proportionality and evaluation

10.1. Normal descriptive analysis may require only a short statement of data, method and limitations. Extensive experimental analyses require an appropriate trace of sampling, fitting, uncertainty, multiple selection and checking. Use existing plans, notebooks, repositories, tables and native work products. This module mandates no separate canonical form, forced JSON serialization, automatic multi-agent discussion or performed roles.

10.2. Evaluate a future Statistics implementation against competent ordinary work and relevant existing Science/Engineering/Mathematics/Cryptography work. Include accurate descriptive tasks, correct inference, undercoverage, dependent sampling, genuine missing inputs, partial identification, false-positive and false-negative objections, and procedures that perform well without this module. Score substantive errors, unsupported confidence, false blocking, completion, cost and reviewer common dependencies. Keep performance and significance thresholds predeclared and appropriate to the task. [ST07, ST08]

10.3. For high-consequence uses, apply governing domain-specific standards and independent assurance as required. This module is not a certifiable safety plan; an aeronautical standard is not incorporated as a binding requirement merely by being cited. Evaluate traceability, change impact, test coverage, independence where required, configuration control and operational feedback in the actual deployment. [ST09, ST10]

10.4. A contribution to statistical practice is a *testable claim*, not a consequence of good intentions. When ACR is evaluated as a checking or teaching instrument, predeclare appropriate baseline comparators and evaluation criteria, include domain-competent adjudicators and deliberately valid cases, assess false objection and false acceptance rates, and disclose completion cost and limits on generalization. A protocol framing or a machine-readable record is not by itself a new statistical inferential method. [ST02, ST13]

10.5. **Release-use boundary.** A task-specific implementation may truthfully claim conformance only to the exact applicable and actually checked obligations, with identified gaps. The module itself is not a quality mark or a substitute for a competent statistician, regulated reviewer, or risk owner. A professional-community benefit claim requires an externally adjudicated comparison against appropriate existing practice; absence of that comparison means that benefit remains unestablished. 

## Appendix A. Interpretive safeguards (informative)

- Distinguish *descriptive accuracy*, *statistical inference*, *scientific truth*, *decision usefulness*, *process conformance* and *authority*. None entails all others.
- Use an adverse-search brief without adopting a preference for an adverse result. A one-sided search declares its coverage.
- Distinguish a source not inspected from a method demonstrated absent. Treat claims about checks as evidence-dependent.
- If a tool reports `exit=0`, identify precisely the property checked; that return code does not certify its subject-matter correctness.
- For long analyses use exact sources and a compact, reconstructible state reference; don't repeatedly dump whole conversation JSON.
- An externally published guideline is not binding unless adopted by the applicable task or authority; report when its content was not fully inspected.

## Appendix B. External reference basis (informative; no automatic standard adoption)

**ST01.** American Statistical Association. *The ASA Statement on p-Values: Context, Process, and Purpose* (2016), https://doi.org/10.1080/00031305.2016.1154108. Used for interpretation and limitations of p-values.

**ST02.** American Statistical Association. *Ethical Guidelines for Statistical Practice* (approved 2022), https://www.amstat.org/your-career/ethical-guidelines-for-statistical-practice. Used for method/data fitness, competence, transparency, stakeholder responsibilities and correction.

**ST03.** ICH E9(R1) estimands and sensitivity analysis, FDA/EMA final guidance, https://www.fda.gov/regulatory-information/search-fda-guidance-documents/e9r1-statistical-principles-clinical-trials-addendum-estimands-and-sensitivity-analysis-clinical. A domain-specific example, not a mandate for every statistical task.

**ST04.** NIST/SEMATECH e-Handbook of Statistical Methods, https://www.nist.gov/programs-projects/nistsematech-engineering-statistics-handbook. Used for assumptions, measurement, calibration, monitoring and engineering statistics.

**ST05.** SAMPL statistical reporting guidance, https://www.equator-network.org/wp-content/uploads/2013/07/SAMPL-Guidelines-6-27-13.pdf. Reporting reference, not independent proof of inferential validity.

**ST06.** Guido W. Imbens and Charles F. Manski (2004), *Confidence Intervals for Partially Identified Parameters*, Econometrica, https://doi.org/10.1111/j.1468-0262.2004.00555.x. Supports the need to distinguish pointwise parameter coverage, whole-set coverage, and uniformity conditions. Later correction literature qualifies exact technical claims; this citation does not assert all methods are universally valid.

**ST07.** NIST AI Risk Management Framework 1.0, https://www.nist.gov/itl/ai-risk-management-framework. General risk-governance comparison, not an automatic standard applied to ACR.

**ST08.** CONSORT 2025 reporting guidelines, https://www.bmj.com/content/389/bmj-2024-081123. Domain-specific reporting reference; not a statistical validity certification or quality score.

**ST09.** FAA AC 20-115D, [FAA advisory circular listing](https://www.faa.gov/regulations_policies/advisory_circulars/index.cfm/go/document.information/documentID/1032046). Recognizes DO-178C and associated assurance guidance as an acceptable means in specified aviation regulatory contexts; not universal ACR certification.

**ST10.** SAE ARP4754B (2023) and ARP4761A (2023), https://saemobilus.sae.org/standards/arp4754b-guidelines-development-civil-aircraft-systems and https://doi.org/10.4271/ARP4761A. Used for the separation of systems development and safety assessment. Full paid standards were **not** accessed.

**ST11.** ASA President's Task Force on Statistical Significance and Replicability (2021), https://magazine.amstat.org/blog/2021/08/01/task-force-statement-p-value/. Contextual use of properly interpreted p-values and significance tests remains legitimate; a 2019 editorial against dichotomized significance is not blanket ASA policy.

**ST12.** Kapoor and Narayanan (2023), *Leakage and the reproducibility crisis in machine-learning-based science*, Patterns, https://doi.org/10.1016/j.patter.2023.100804. Empirical and conceptual examples of leakage; not proof that all studies are affected.

**ST13.** National Academies of Sciences, Engineering, and Medicine (2019), *Reproducibility and Replicability in Science*, https://www.nationalacademies.org/read/25303/chapter/3. Research transparency, analytical timing, uncertainty, and reproducibility.

**ST14.** TRIPOD+AI (2024), https://www.bmj.com/content/385/bmj-2023-078378. A clinical prediction *reporting* guideline, not a quality-appraisal or prediction-method certification instrument.

**ST15.** NIST/SEMATECH e-Handbook of Statistical Methods: reliability, process/product monitoring and measurement characterization, https://www.nist.gov/programs-projects/nistsematech-engineering-statistics-handbook. Established handbook, not proof that a given inspection sample is representative.

**ST16.** NIST, *Towards a Standard for Identifying and Managing Bias in Artificial Intelligence* (SP 1270, 2022), https://doi.org/10.6028/NIST.SP.1270. Distinguishes systemic, statistical/computational and human biases; applies to AI examples, not to all statistical tasks universally.

**ST17.** ISO 14971:2019, *Medical devices - Application of risk management to medical devices*, https://www.iso.org/standard/72704.html. Current standard status checked in public ISO summary; full proprietary standard not read. Medical-device example, not an ACR or general statistical certification requirement.

