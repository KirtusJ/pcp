# Adversarial Claim Review

# Engineering Specification - Version 1.0

**Packet:** ACR Version 1.0, Implementation  
**Component:** `acr.engineering`, Version 1.0  
**Required core:** `acr.core`, Version 1.0; Core descriptor SHA-256 `f15686b385002bf597c2625bc18e98a390531a21ce91f64bdb249f2fe04a86a7`  
**Creator:** Kirtus Justus  
**Date:** 11 November 2026, America/Vancouver

This Specification defines the engineering module of Adversarial Claim Review (ACR). It adds decision-specific engineering obligations to the governing Core. This Markdown Specification is normative; its PDF is the corresponding reading copy. Sections 1-9 are normative except labeled examples. Appendices provide terminology, cautions and sources. Capitalized requirement words have the Core's BCP 14 meanings.

## 1. Scope, entry and proportionate use

The module applies to identified engineering work when selected by an authorized task, commission or adopted policy. It supports development, improvement and assessment of engineered systems, components, processes, facilities and their interactions across relevant lifecycle activities. It does not establish a professional credential, engineering code, certification scheme or permission to construct, energize, operate or retire anything.

Ordinary competent engineering work remains the default. Teams SHOULD use a FOCUSED review for a material uncertainty, disputed requirement, consequential change or evidence handoff that benefits from structured assessment. An adequate existing design review, verification activity or change procedure SHOULD be reused. Routine work does not require a new Review.

Preserve the existing authorized task. For commissioned Review work, Engineering MUST use the assigned Review, applicable Core assessment Session, authority and dispositions. Module selection creates no new lifecycle, Director or permission. The applicable Core and Engineering requirements MUST be available for the assigned act; a compact task context MAY carry controlling requirements with authorized access to supporting records. Missing material information blocks dependent commitments, not unrelated authorized preparation.

The team's engineering lifecycle may be iterative, concurrent, recursive or otherwise suited to its work. ACR gates organize a commissioned review; they do not impose a replacement development sequence. ISO/IEC/IEEE 15288:2023 describes lifecycle processes without prescribing a particular lifecycle model or methodology [N01]. NASA applies systems engineering through development, operation, maintenance and disposal within its institutional scope [N02].

Mathematics, Science and Cryptography are independently selected modules. Mathematical derivation, scientific inference, cryptographic assurance or other specialist obligations MUST be addressed when material; selection of Engineering does not automatically select every module. Existing lawful, competent engineering methods continue under their actual authorization. An optional ACR method being OFF never disables required testing, hazard analysis, inspection or professional duties.

## 2. The engineering decision and its basis

The task MUST identify the engineering issue, assessment question and decision or handoff it is intended to inform. Commissioned Review work resolves these meanings through its Target and Claim. A review of a component, calculation or document MUST NOT silently become a finding about the whole installed system. The assessed lifecycle activity, intended use and operating conditions MUST be clear enough to determine what evidence is relevant.

Reuse the Core's four portions and the team's established records. Information MAY be linked rather than transcribed. Include only the detail material to the assigned decision.

| Existing record portion | Engineering meaning to resolve |
|---|---|
| Subject and question | Item or system boundary; configuration; intended use; interfaces; decision and acceptance criteria. |
| Mandate and limits | Actual responsible authorities; applicable obligations; permitted work and exposure; budget and stopping conditions. |
| Working basis | Requirements, assumptions, relevant hazards and controls; drawings, analyses, observations and tests; material unknowns and dependencies. |
| Result | Criterion-specific findings; evidence coverage; unresolved conditions; decision owner; permitted handoff and required follow-up. |

The working basis MUST distinguish the recorded configuration from the physical or operational configuration it claims to describe. Resolve as-designed, as-built, as-tested, as-operated or as-maintained differences when they affect the question. A document identifier or matching digest establishes which record was used, not that the installed item still matches it. State the relevant observation, inspection or configuration-control basis and its time.

Material constraints MUST survive compacting, delegation and session transition. These can include units, coordinate conventions, tolerances, loads, environment, service duration, degradation, interfaces, human capabilities and excluded conditions. Preserve their authoritative references and assessed meaning through the Core Basis Header or equivalent existing record. Exact text equality cannot establish that a constraint is complete or applicable.

A baseline identifies a controlled basis for assessment. It MUST NOT suppress contrary observations or prevent an authorized change. New evidence that can alter the decision MUST be routed for impact assessment; dependent findings use the Core's recheck and supersession rules. Expanding the intended use, changing a critical assumption or accepting a new configuration requires assessment of the resulting evidence gap.

## 3. Applicable obligations and accountable decisions

Before a dependent commitment, resolve the relevant jurisdiction, contractual requirements, adopted codes or standards, organizational procedures and competent decision authority. Reference existing applicability decisions. Do not invent a universal approval body or require every available standard for every task.

For a standards-based claim, identify the publication, edition, applicable scope and relevant amendments or approved departures. Distinguish adopted requirements from informative guidance, draft revisions and catalogue abstracts. A newer publication does not silently replace a project's applicable basis. The public scope of ISO 12100 concerns machinery safety; IEC 61508 concerns specified electrical, electronic and programmable electronic safety-related systems [N10, N11]. Neither is a universal engineering code.

The record MUST distinguish four acts: assessing evidence, accepting a deliverable, accepting residual risk where that decision is permitted, and authorizing an external action. One person may hold more than one applicable duty, but performing one act does not establish the others. Any required independent assessment or concurrence MUST be retained.

ACR role assignment MUST NOT be represented as professional competence, statutory authority or delegated engineering responsibility. Competence and accountability are determined by the actual work and governing practice. Professional engineering guidance emphasizes public protection, qualified practice and truthful technical reporting [N08]. NASA's risk-management directive illustrates an explicit allocation of risk-acceptance accountability; its institutional rules are not imposed on other organizations by this module [N15].

A finding MAY identify a technically supported option without authorizing its implementation. A budget limit, majority opinion or Director instruction cannot waive an obligation outside that Director's authority. When a required specialist, inspection, concurrence or approval is absent, identify the specific dependent decision that remains unavailable and continue other authorized work.

Resolve material competing interests and applicable disclosure, participation or recusal obligations for the actual professional duty [N08]. Technical independence, a role title or disclosure alone does not establish eligibility for a decision. This requirement does not impose a universal ban on interested technical contributors.

## 4. Requirements, assumptions and interfaces

Each acceptance-critical criterion MUST be connected to its source or justified decision basis and to evidence capable of assessing it. Identify ambiguities, missing criteria and incompatible requirements before treating the finding as supported. Avoid copying a full requirements register into the Review record when exact relevant references suffice.

Requirements conformance and suitability for intended use MUST remain distinguishable. A precisely implemented requirement can still express the wrong need. NASA's verification guidance assesses conformity to specified requirements; its validation guidance assesses intended use and the intended environment [N03, N04]. One test MAY serve both purposes when its design and results support both obligations.

For material interfaces, assess compatibility of the connected items, including relevant ranges, units, tolerances, timing, physical connections, failure behavior and responsibility boundaries. Component acceptance alone MUST NOT establish system acceptance. Integration claims require evidence for the relevant interactions and operating conditions.

Assumptions MUST be identified as assumptions rather than hidden in a calculation, supplier statement or default setting. Record their source, justification, applicability and consequences of failure when material. A valid conditional analysis does not establish that its conditions hold in the actual installation. Unresolved acceptance-critical premises retain the Core's conditional or unresolved treatment.

Reused or purchased items MUST be assessed for the proposed use to the extent material to the decision. Prior service, a supplier certificate or an unchanged part number does not establish compatibility with changed loads, environment, manufacture, installation or maintenance. Preserve relevant qualification limits and unresolved provenance or substitution concerns.

### 4.1 Development and comparison of alternatives

An authorized assignment MAY develop or improve a design, process or method. State the intended improvement, relevant baseline and criteria for the present development decision. Distinguish mandatory constraints from preferences. An exploratory candidate MAY be studied before it meets acceptance requirements, but a selection or readiness finding MUST NOT treat an unestablished constraint as satisfied or compensate for a failed mandatory criterion through a weighted score. A change to a controlling requirement requires the applicable authority and impact assessment.

Identify candidate revisions and the evidence supporting their material characteristics. Compare relevant alternatives under declared conditions, including the existing approach where it is a viable comparator. Preserve the reasons for narrowing the search and any uncertainty capable of changing the recommendation. A numerical ranking MUST retain its scales, weights and material assumptions; it is not evidence of an unrestricted optimum. NASA's design guidance examines alternatives through successive refinement, while its decision-analysis guidance distinguishes mandatory criteria from preferences and considers uncertainty in rankings [N17, N18].

Candidates MAY be revised within the existing mandate without creating a Review for each iteration. Reuse unaffected evidence, retain adverse findings against the assessed revision, and recheck affected interfaces and obligations. A prototype, failed alternative or narrower result can be a useful development outcome. Selection for further investigation MUST remain distinct from approval to construct or use it.

## 5. Hazards, controls and human use

The review MUST identify the hazards material to its assessed subject and affected interfaces, or reference an adequate existing assessment. Define the relevant harm, exposure, circumstances and affected parties or environment. A partial review MUST identify which broader hazard obligations it does not assess; exclusion from the review does not remove those obligations from the responsible project.

Hazard identification, risk estimation, selection of controls and acceptance of residual risk MUST remain distinguishable. An unknown likelihood is not zero. A risk score or category is not evidence that a control works, and this module defines no universal numerical threshold for acceptable risk. State the chosen assessment method, material uncertainty and governing acceptance basis.

For each control relied upon by the finding, resolve its intended effect, implementation, relevant dependencies, effectiveness evidence and continuing obligations. A proposed control, an installed control and a demonstrated effective control are different evidence states. Reuse the hazard log or safety case rather than creating a competing register.

Consider feasible hazard elimination or reduction at source before relying exclusively on warnings, procedures or personal protective measures. Engineers Canada's risk-management guidance organizes controls by inherent design, passive and active engineering measures, and procedural measures [N07]. The applicable discipline and hazard determine the appropriate analysis and controls; ACR does not mandate one analysis technique for every system.

Claims relying on multiple barriers, redundant channels or independent checks MUST examine material shared causes. Shared power, environment, sensing, maintenance, assumptions or control logic can defeat several protections together. Multiplying individual failure probabilities requires a justified dependence treatment. Protective functions can also require continued utilities or active action; removing power is not universally safe [N16].

Human contributions MUST be assessed in the actual task context where material: users and maintainers, workload, access, displays, communication, time pressure, foreseeable mistakes and recovery. Do not treat training or a written instruction as sufficient evidence of reliable performance. HSE guidance supports proportionate assessment involving the workforce and attention to how work is actually performed [N05].

Evidence of immediate danger, loss of a required protection or a condition requiring prompt response under applicable procedures MUST be routed through the established emergency, stop-work or escalation pathway without waiting for Review discussion or disposition. Participants MUST follow their actual responsibilities and authorized procedures. A Review pause, fence or closure is not a physical safe state. ACR MUST NOT be used to invent a shutdown action or bypass a protective function.

## 6. Verification, validation and evidence quality

### 6.1 Plan and interpret the decisive checks

The assessment MUST link each decisive obligation to a suitable check and its result, coverage and limitations. In commissioned Review work, this is part of G5. Use actual authorized engineering methods: inspection, measurement, analysis, demonstration, testing and competent review as appropriate. A generated explanation or repeated agreement does not replace the evidence required by the criterion.

Before relying on a test, resolve the tested item and configuration, procedure, conditions, instrumentation, calibration status where relevant, acceptance criteria and observed outcomes. Distinguish a test-design problem, execution anomaly and actual nonconformance; uncertainty about the cause MUST remain visible. Preserve material contrary results and deviations. Do not retroactively change criteria to relabel a failure as a pass.

Apply the Core evidence-access rules when a record cannot be inspected: an assessment-access limitation MUST NOT be reported as an absent control, missing inspection or physical defect without the evidence for that further claim. A required verification can remain unestablished, and any actual record-delivery obligation is assessed separately. Credible concerns requiring prompt protective response retain Section 5's actual escalation and authority arrangements.

The claimed operating envelope MUST be supported by the assessed coverage. Sampling a few nominal conditions cannot establish performance at untested limits without a justified argument. Units, tolerance, numerical precision and measurement uncertainty MUST be treated when they can change the conclusion. Margins must have an identified basis; the module supplies no universal safety factor.

Validation MUST address the intended use, relevant environment and material human or system interactions. Qualification of a design, acceptance of a particular delivered item and authorization to put that item into service MUST be identified separately when relevant. Evidence for one is not automatically evidence for all.

### 6.2 Analysis, simulation and reduced investigations

For an analysis or simulation used in a consequential decision, identify its intended use, assumptions, inputs, relevant implementation and assessed domain. Separate correct execution of the method from adequacy of its representation of the engineering situation. NASA-STD-7009B provides a use-specific credibility framework and requires communication of uncertainty characterization or its unavailability within its scope [N09].

A simplified calculation, prototype, bench test or digital twin MUST state what it represents, what it omits and which observations could challenge its intended inference. Transfer to a different scale, configuration, environment or service duration requires a stated bridge and evidence adequate to the resulting claim. A successful demonstration does not supply that bridge by itself.

The Core's required executed checks remain mandatory when an acceptance-decisive obligation is mechanically checkable with a suitable available and authorized verifier. Additional checks MAY be used when useful. Required engineering verification also remains required. A formally checked expression or reproducible execution does not independently verify material properties, manufacturing quality, input measurements or physical representativeness.

A credible concern MAY arise from an inspection, incident, expert observation, missing requirement or untested interaction without an executable counterexample. Evaluate its relevance and evidence needs. Dismiss rhetorical opposition that adds no material issue, while preserving unresolved substantive concerns. The Core's Resilience Exercise rules (Section 10.4) apply when such an exercise is commissioned; ordinary authorized engineering tests are not automatically Resilience Exercises.

### 6.3 Reliance on the assessment process

Where the review or its tools are relied upon as a consequential gate or protective function, their contribution MUST be included in the applicable assurance assessment. Address material false acceptance, false rejection, omitted evidence, delayed or unavailable responses, and common dependencies with the work being checked. Identify the actual fallback, authority and response constraints; a safe fallback cannot be assumed from a pause label. Assess this reliance at the relevant use and change boundary, without requiring recursive Reviews.

Repeatable execution, passing examples and separate participant names do not establish tool suitability or independent assurance. Apply any governing qualification, validation or independent-check obligations to the actual use. FAA system-design guidance illustrates consequence-sensitive development assurance, common-cause analysis and justification of assumptions [N19]. Its aviation-specific applicability is not extended by citing it here. ACR conformance does not qualify a tool or establish suitability for a safety-critical function.

## 7. Change, service and retirement

Changes MUST be assessed for material effects on the evidence and obligations supporting the relevant decision. This includes physical modification, replacement, changed duty, software or security changes, altered procedures, supplier changes, environmental change, ageing and service-life extension. Reuse the established management-of-change process; an administrative label such as minor or replacement-in-kind cannot establish technical equivalence by itself.

The impact assessment MUST consider affected interfaces and controls beyond the changed item, required rechecks, temporary arrangements, restoration and updated instructions. A correction must be checked for material adverse interactions with previously accepted behavior. HSE plant-change guidance addresses effects across the plant and the continuity of engineering review, maintenance and authorized changes [N06].

Where continued performance depends on inspection, proof testing, maintenance, calibration, monitoring, competence or utility availability, the finding MUST identify those dependencies and the responsible operational records. Review closure MUST NOT be represented as completion of future obligations. A periodic or event-triggered review may remain appropriate without an always-running Review or new infrastructure.

Changed conditions, incidents, near misses, unexpected degradation, new evidence or relevant standards changes SHOULD trigger the established reassessment pathway when they can invalidate a relied-upon basis. The trigger does not itself determine the result or authorize an action. For exposed long-lived assets, consider whether historical environmental assumptions remain appropriate over the intended service period [N13].

Handover, decommissioning and retirement MUST address relevant residual hazards, stored energy or materials, disposal constraints, retained records and responsibility transfer. The record's completion state does not establish the physical condition of the asset. Apply the relevant competent procedures rather than a generic instruction to stop, disconnect or discard it.

## 8. Findings and engineering handover

Use Core dispositions and lifecycle rules for commissioned Review work. Ordinary results need no ACR status vocabulary; any chosen canonical disposition retains its meaning and evidential guards. The finding MUST identify the assessed question, configuration, criteria, supporting evidence, significant objections, uncertainty and exclusions. Acceptance-critical unestablished premises MUST remain visible in the finding; an informative limitation must not be used to disguise a failed mandatory requirement.

For a consequential handover, the recipient MUST be able to determine what is established, what remains conditional, which configuration and use are covered, and what further decision or action is authorized. Use the Core handoff and meaning-check process at the relevant boundary. No duplicate receipt is required where an existing record carries the required meaning and authority.

An unresolved item MUST have a stated consequence for the dependent decision and a responsible follow-up route where one exists. Do not fabricate an owner, approval or closure. Expiry of the review budget may yield an incomplete finding; it does not make an unsafe or nonconforming condition acceptable.

Material findings and corrections MUST be routed to the authorized decision or follow-up recipient under Core's reporting and correction rules. A corrected access error is not retained as an open technical defect solely on that superseded basis. An unresolved delivery remains distinguishable from successful receipt. Objective reporting includes relevant information and acknowledgment of errors under the applicable professional duty [N08].

External release MUST preserve the distinction between an ACR review outcome, an engineering recommendation, a formal acceptance and an authorized implementation. A positive finding MUST NOT be described as a general safety, reliability or regulatory certification beyond the evidence and actual issuing authority.

## 9. Customization and usefulness

Teams MAY map terminology to their established professional vocabulary, link existing tools and records, and select the smallest sufficient review arrangement. Required meanings and applicable protections MUST survive the mapping. Add detail when it resolves a material decision need; remove duplicate transcription and unused ceremony.

Evaluate the intervention against the team's ordinary competent process at comparable total cost and access. Assess material issues detected and missed, false objections, corrective-action quality, decision delay and record-preparation effort. A completed checklist or successful educational trial does not establish improved engineering outcomes. Narrow or discontinue a Review arrangement that adds no useful protection.

## Appendix A. Working glossary

| Term | Meaning in this module |
|---|---|
| Acceptance criterion | Stated condition and assessment basis for the decision under review. |
| Configuration | Relevant physical, functional and informational characteristics of the identified item at a stated basis or time. |
| Intended use | Purpose, users, operating circumstances and conditions for which the finding is claimed. |
| Material | Capable of changing the assessed decision, its conditions or a relevant protection obligation. |
| Verification | Assessment of conformity to identified requirements. |
| Validation | Assessment of suitability for identified intended use and conditions. |
| Hazard | A potential source or situation of harm. |
| Risk | Characterization of possible adverse consequences and their likelihood or uncertainty in the assessed context. |
| Residual risk | Risk remaining after the assessed controls; its existence does not establish acceptance. |
| Common cause | A shared condition or mechanism capable of defeating multiple items or protections. |
| Decision authority | Actual authority for a specified engineering decision; not created by an ACR role. |
| Evidence transfer | Justified use of evidence from one configuration or circumstance for another. |
| Mandatory criterion | A controlling condition that must be met for the particular acceptance decision; a preference score cannot waive it. |
| Development candidate | An identifiable proposed solution under investigation; its existence or selection for study does not establish acceptance readiness. |

## Appendix B. Cautions and reading discipline

**EN01 - Record and reality.** A controlled record may accurately preserve an incorrect or obsolete description. Confirm the physical basis when the decision depends on it.

**EN02 - Scope and composition.** Passing component checks, satisfying selected requirements or supporting a conditional analysis does not settle system suitability or overall safety.

**EN03 - Authority and control.** Findings inform decisions. Credentials, risk acceptance, emergency response and physical actuation retain their actual governance.

**EN04 - Exposure and uncertainty.** Untested conditions, common causes and unknown likelihoods remain limitations; agreement cannot eliminate them.

**EN05 - Review burden.** Excess ceremony can consume the attention and time needed for engineering. Reuse existing evidence and focus on consequential questions.

Read the authorized assignment and applicable Core instructions first, then the relevant Engineering clauses and substantive engineering sources. Preserve material constraints in compact context. Role names identify duties held by fallible participants; professional conduct and evidence determine the work.

## Appendix C. Primary sources

Source identifiers are local to this module. Public catalogue abstracts are not substitutes for the actual applicable standards. Status was checked on 2026-11-10.

**N01. ISO/IEC/IEEE 15288:2023.** System life cycle processes. Public scope; full standard not inspected. [Source](https://www.iso.org/standard/81702.html).

**N02. NASA NPR 7123.1D, Change 2.** Systems Engineering Processes and Requirements. NASA-specific directive. [Source](https://nodis3.gsfc.nasa.gov/displayDir.cfm?Internal_ID=N_PR_7123_001D_&page_name=Chapter1).

**N03. NASA.** Systems Engineering Handbook, 5.3 Product Verification. [Source](https://www.nasa.gov/reference/5-3-product-verification/).

**N04. NASA.** Systems Engineering Handbook, 5.4 Product Validation. [Source](https://www.nasa.gov/reference/5-4-product-validation/).

**N05. HSE.** Human factors in risk assessment. UK regulator guidance. [Source](https://www.hse.gov.uk/humanfactors/topics/risk-assessment.htm).

**N06. HSE.** Plant modification / Change procedures. Process-sector guidance. [Source](https://www.hse.gov.uk/comah/sragtech/techmeasplantmod.htm).

**N07. Engineers Canada.** Public guideline on risk management. Advisory professional guidance. [Source](https://engineerscanada.ca/guidelines-and-papers/public-guideline-on-risk-management).

**N08. NSPE.** Code of Ethics for Engineers. Professional code. [Source](https://www.nspe.org/career-growth/nspe-code-ethics-engineers).

**N09. NASA-STD-7009B.** Standard for Models and Simulations, 2024. [Source](https://standards.nasa.gov/standard/nasa/nasa-std-7009).

**N10. ISO 12100:2010.** Safety of machinery. Public scope and status; full standard not inspected. [Source](https://www.iso.org/standard/51528.html).

**N11. IEC 61508-1.** Public scope and status: 2010 edition and 2026 FDIS pre-release. Full texts not inspected. [2010](https://webstore.iec.ch/en/publication/5515); [pre-release](https://webstore.iec.ch/en/publication/117296).

**N12. NIST IR 8620.** Digital Twins Workshops Summary Report, 2026. Manufacturing workshop findings. [Source](https://www.nist.gov/publications/digital-twins-workshops-summary-report).

**N13. Engineers Canada.** Principles of climate adaptation and mitigation for engineers. Advisory guidance. [Source](https://engineerscanada.ca/guidelines-and-papers/public-guideline-principles-of-climate-adaptation-and-mitigation-for-engineers).

**N14. NIST IR 8356.** Security and Trust Considerations for Digital Twin Technology, 2025. [Source](https://csrc.nist.gov/pubs/ir/8356/final).

**N15. NASA NPR 8000.4C.** Agency Risk Management Procedural Requirements, Chapters 1 and 3. NASA-specific responsibilities. [Source](https://nodis3.gsfc.nasa.gov/displayDir.cfm?Internal_ID=N_PR_8000_004C_&page_name=Chapter1).

**N16. HSE.** Control systems; independence and dependence on utilities. [Source](https://www.hse.gov.uk/comah/sragtech/techmeascontsyst.htm).

**N17. NASA.** Systems Engineering Handbook, 4.4 Design Solution Definition. [Source](https://www.nasa.gov/reference/4-4-design-solution-definition/).

**N18. NASA.** Systems Engineering Handbook, 6.8 Decision Analysis. [Source](https://www.nasa.gov/reference/6-8-decision-analysis/).

**N19. FAA AC 25.1309-1B.** System Design and Analysis, 2024. Advisory guidance for its stated aircraft-certification scope. [Source](https://www.faa.gov/documentLibrary/media/Advisory_Circular/AC_25.1309-1B.pdf).
