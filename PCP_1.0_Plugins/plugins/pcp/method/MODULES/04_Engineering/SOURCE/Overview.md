# Adversarial Claim Review

# Engineering Overview - Version 1.0

**Packet:** ACR Version 1.0, Implementation  
**Component:** `acr.engineering`, Version 1.0  
**Required core:** `acr.core`, Version 1.0; Core descriptor SHA-256 `f15686b385002bf597c2625bc18e98a390531a21ce91f64bdb249f2fe04a86a7`  
**Creator:** Kirtus Justus  
**Date:** 11 November 2026, America/Vancouver

This is an informative guide. The Engineering Specification adds engineering requirements to the identified Core. Use the controlling text for an applicable requirement. Source identifiers N01-N19 refer to the Engineering source register and the Specification's reference appendix.

## 1. What this module is for

ACR Engineering supports development, improvement and examination of a particular engineering decision, candidate, disputed assumption, interface or handoff. The subject may be a product, structure, process, facility, component, service or change. The intended contribution is a clear connection between the question, the applicable configuration, the evidence, unresolved limitations and the people authorized to act on the result.

It fits inside the team's existing engineering work. Drawings, requirement registers, analyses, inspection records, hazard logs, test reports and change records remain useful evidence. Reference them rather than transcribing them into a second management system. If ordinary review already resolves the question adequately, continue that work.

A Review can be useful when a boundary is unclear: a test result is being applied to a different configuration; two teams interpret an interface differently; a simulation result is being treated as field evidence; a change may invalidate an earlier assessment; or a material unresolved condition has no acknowledged recipient. These are candidate uses, not established comparative benefits of ACR.

The module does not supply a design code, engineering competence, certification, professional appointment, risk-acceptance authority or operational control. Its scoped finding says what the review supports. Other decisions retain their actual owners and requirements.

### Choose the smallest useful intervention

| Situation | Proportionate approach |
| --- | --- |
| Authorized work has clear requirements, competent review and adequate records | Use the existing workflow. No Review is needed merely because this packet is present. |
| One material interpretation, change or handoff remains unresolved | Consider a FOCUSED review of that question, normally using Core G1, G5 and G6. |
| Several dependent issues need examination | Decompose where it helps; preserve the integration obligations and common assumptions. Additional Reviews are optional. |
| Applicable requirements demand specialist work or independent assessment | Perform that work with the required competence and separation. A short ACR procedure does not reduce the substantive obligation. |
| An urgent condition requires an established protective response | Use the authorized operational or emergency pathway. Do not insert a Review discussion into its time-critical path. |

FOCUSED is a way to reduce procedure, not a lesser standard of engineering evidence. FULL adds useful examination stages when the assignment warrants them. Neither profile replaces the team's development lifecycle. ISO/IEC/IEEE 15288's public scope explicitly accommodates iterative, concurrent and recursive work across a lifecycle without prescribing a particular methodology [N01].

## 2. Start from an actual assignment

Receiving the packet gives a participant reference material. A task and mandate still have to exist. A short authorized instruction can supply them: "Assess whether report R17 remains applicable to configuration C8 under operating envelope O3. Use the current change record and test evidence. Report unresolved conditions to the assigned decision owner; do not implement changes."

Core resolves the assignment's subject, question, authority, working basis and outcome. Existing instructions and records may already contain all of these. A participant does not ask the team to re-enter known information simply to satisfy a template. It retrieves the governing Core and the relevant Engineering clauses, resolves the necessary originals, and begins the authorized work when its prerequisites are satisfied.

The human-direction default and bounded child delegation remain those of Core. A participant assigned to direct a review does not thereby become the responsible engineer, asset operator, certifier or risk owner. A specialist's involvement is identified by their actual contribution, competence and authority. A role name expresses a duty, not competence; local vocabulary may use reviewer, analyst or another unambiguous alias.

### A compact engineering view

Use the existing task record. Add or reference only the engineering information that affects this question.

| Core portion | Engineering information that may be needed |
| --- | --- |
| Subject and question | Item or process; exact change or decision; intended use; relevant lifecycle activity and interfaces. |
| Mandate and limits | Permitted analysis and actions; competent decision owners; applicable requirements; required independent assessment; boundaries on equipment, data and disclosure. |
| Working basis | Requirement and configuration references; operating envelope; test or analysis evidence; material assumptions; hazards and controls; observation dates and uncertainty. |
| Result | Supported and unsupported conclusions; adverse evidence; outstanding conditions with recipients; decision or action still required; reuse limits and recheck triggers. |

The table above is a view of this information, not another mandatory form. A drawing reference can resolve configuration; a hazard-log entry can resolve an existing control and owner. A reference is sufficient only if the receiving participant can access and interpret what its next act needs.

If an inspection record cannot be opened, recover it through the available authorized path before concluding that the inspection was never performed. If recovery fails, report the access limit and its consequence for the dependent decision. A requirement to supply that record can remain unmet without establishing a physical defect. If the record is later recovered, correct the earlier access finding and inform affected recipients; do not carry it forward as a technical deficiency.

A new chat does not create a new assessment. Recover the current assignment, applicable basis and unresolved conditions. An unchanged file does not prove that equipment, materials, users or operating conditions are unchanged. When actual condition matters, identify the observation, inspection or other evidence supporting that condition.

## 3. Follow one review from question to finding

Consider a fictional review of whether an earlier assessment supports a changed operating envelope. The values below are invented, dimensionless fixtures. They are not design values or a recommended calculation for real equipment.

### Ground the question

The earlier assessment uses a constant capacity of 10 and explicitly checks only the finite load set {8, 9}, with no extrapolation. A proposal refers to the same report and quotes a nominal load of 9 for the changed use. The currently admissible finite load set is {9, 10, 11}; no probabilities are assigned, and the actual load is unknown. The review's question is whether the earlier report establishes capacity at least as large as every currently admissible load.

The relevant configuration and intended use are named. The report's unchanged digest identifies its bytes. It does not establish that its coverage includes the changed set. The review needs no new database or fourteen-person roster: a competent analyst and an appropriate check can use the existing record, subject to any required independence.

### Check the actual property

The nominal comparison, 9 less than or equal to 10, passes. The requested comparison over all admissible loads does not: the set permits 11, which exceeds 10. This defeats the proposed inference from the old report to the new envelope. It does not establish that a real item has failed, nor that the permitted upper value will occur.

The record therefore keeps the two statements distinct: the nominal comparison passes in the fixture; the submitted evidence does not establish the requested bound over the changed set. Possible authorized next work includes obtaining a justified narrower set or bound, changing the proposal or performing an appropriate new assessment. The Review does not invent an operating restriction or release permission outside its mandate.

### Deliver a useful finding

The delivery identifies the exact question, the input set, the checked inequality, the old report's applicability limit and the unresolved engineering decision. Its disposition follows the actual Claim. A claim that the inequality holds for every permitted value is refuted by 11; a broader claim about the real system may remain unresolved because its necessary evidence is absent.

The decision owner receives the limitation before dependent use. Where no acknowledgment or current access can be established, the record states the delivery limit. Administrative completion of the review does not mean that corrective work is complete or that the item is authorized to operate.

### Reuse what remains valid

If later evidence justifies the finite set {8, 9} under the same capacity assumption, the earlier enumerative coverage applies and the inequality holds for every member. That is a useful positive control. Other obligations, such as whether the capacity assumption applies, remain separate. Core's change and reuse rules preserve valid earlier work while rechecking affected conclusions.

The purpose of this bounded comparison is to show how the question, evidence and decision remain connected.

### Develop and compare candidates

The same record can support creation. Suppose an authorized team is exploring alternatives with a mandatory clearance of at least 5 invented units. It prefers a larger benefit-minus-cost score after that requirement is met. These are stipulated quantities, not real design values.

| Candidate | Clearance | Benefit minus cost | Eligible under the stated criterion? |
| --- | --- | --- | --- |
| A | 4 | 90 | No: the requirement fails. |
| B | 6 | 60 | Yes: this one criterion is met. |
| C | Unknown | 115 | Unestablished: the score cannot fill the evidence gap. |

A score-only selector picks C; discarding unknown values and then ranking still picks the nonconforming A. Applying the mandatory criterion first leaves B. This does not establish B's overall safety or optimality. It only answers the supplied constrained selection question. If no candidate meets the criterion, an empty selection is informative; the team need not pretend the best failing score is acceptable.

The team can continue authorized research on A or C. If evidence supports a revision A2 with clearance 6 and the same score of 90, it would outrank B under the declared rule. Preserve A's earlier failed result and identify that new evidence. The fixture stipulates A2's values; it does not produce engineering evidence for them. Selection for further investigation is not deployment approval. Check the actual acceptance boundary as well as plainly passing and failing candidates.

NASA's design guidance supports refinement of alternatives; its decision-analysis guidance treats mandatory criteria separately and examines uncertainty that can change a ranking [N17-N18]. Use the amount of comparison that the decision needs. A competent team can run this loop in its existing design or change record, reusing unaffected work without commissioning a new Review for every edit.

## 4. Separate verification, validation, risk and action

Several engineering decisions may use the same evidence without being equivalent.

The Specification distinguishes evidence assessment, deliverable acceptance, residual-risk acceptance and action authorization. Within the evidence assessment, verification and validation answer different questions:

| Judgment | Question it answers | What it does not supply by itself |
| --- | --- | --- |
| Requirement verification | Does the identified item satisfy the identified requirement under the checked conditions? | Adequacy of the requirement or suitability for the intended use. |
| Intended-use validation | Is there suitable evidence for the intended use in the relevant environment and human context? | Every required approval, or suitability for a different use or condition. |
| Residual-risk acceptance | Has the authorized accountable decision maker accepted the identified remaining risk under applicable criteria? | A missing technical result or a universal finding that the activity is safe. |
| Release or operating authorization | May the specified action proceed under the governing authority and conditions? | Evidence for unexamined properties or permanent authority after material change. |

NASA's handbook distinguishes verification against requirements from validation for intended use and environment [N03-N04]. Its risk-management directive illustrates a separate institutional accountability for risk acceptance, including implicit acceptance through consequential decisions [N15]. These are source-grounded distinctions; NASA's organizational rules are not universal rules for all engineering teams.

A requirement can be met and still be wrong for the intended purpose. A useful design can also fail an applicable requirement. Preserve both observations rather than force a single green status that hides one of them.

Likewise, a risk accepted by an authorized person does not become a technically resolved uncertainty. The rationale, remaining conditions and obligations still matter. Conversely, a negative finding does not automatically command physical shutdown. The actual operating response belongs to the authorized arrangements for that system and condition.

### Claims about standards

Name the applicable standard, edition, scope and evidence when claiming conformance. A reference to a standard's public abstract establishes neither access to its full clauses nor compliance with them. An approved deviation, where available under governing arrangements, remains a deviation with its own basis.

Status needs care during revisions. On 10 November 2026, IEC's public catalog lists IEC 61508-1:2010 as valid and the 2026 PRV as a Final Draft International Standard in its voting period. The module treats this as an example of why published requirements, draft previews and the project's adopted basis must be distinguished [N11]. Recheck the actual source when this status affects a later decision.

## 5. Examine harm, interfaces and change together

Engineering protection depends on the item in its actual setting. A control may be proposed, installed, tested, maintained and available at different times; those are different facts. An entry marked closed in a review system does not establish all of them.

Use the team's applicable hazard and risk methods. Trace a material hazard to the relevant condition, exposed parties or environment, controls, evidence that those controls work, dependencies and remaining obligations. Avoid unnecessary numeric scores. Where likelihood or dependence is unknown, describe the uncertainty; an unfilled estimate is not zero risk.

Engineers Canada's advisory guideline discusses risk reduction and continued attention to residual risk [N07]. HSE's human-factors guidance emphasizes actual tasks, workforce involvement, prevention and recovery, rather than reliance on procedures or training alone [N05]. ACR's contribution is to keep the relevant evidence and responsibility visible in a commissioned review. It does not replace those substantive methods.

### Components can share a failure

Two channels do not become independent because they have separate names, implementations or reviewers. They may share power, environment, maintenance, data, a supplier or an assumption. Integration can introduce effects that component-level evidence did not examine.

For example, two protections can each fail when their shared power source fails. Multiplying their separate failure probabilities then requires a dependence argument; different channel names do not supply one. Identify the relevant shared causes and use the appropriate reliability analysis.

### A local change can have distant consequences

A substitution, maintenance action, software change, revised operating procedure or altered environment can affect other interfaces and controls. HSE's plant-change guidance specifically warns that consequences can extend beyond the changed part [N06]. Assess the material dependency path before reusing an earlier result. Preserve unaffected evidence; do not re-run everything by habit.

Distinguish what was designed, built, tested, operated and maintained when those differ. A prototype's test evidence may depend on workmanship, tolerances, materials, environment or use conditions that production does not share. A simulation's credibility depends on its intended use and evidence, including relevant uncertainty [N09]. The missing bridge is an assessment obligation, not something a shared filename or polished summary supplies.

### Stopping and waiting can also create harm

A paused Review is an assessment state. It is not a physical safe state. Some protective functions require continued active support, while other conditions call for isolation or shutdown. The actual hazard, equipment, approved procedure and competent authority determine the response. A review label supplies none of those engineering facts [N16].

Do not wait for a final adjudication when an applicable procedure calls for a prompt response to a credible concern. Preserve its uncertainty while using the actual escalation or protective pathway. Conversely, a concern does not invent authority for an unsafe intervention. Evaluate review delays and shared workload before placing a Review on a response path. An apparently separate review can still interfere by consuming the same operator, processor, communications or attention. No example in this guide supplies a real shutdown procedure or response-time guarantee.

## 6. Use the modules together without duplicating them

Core owns entry, authority, records, findings, state, delivery and optional-method activation. Engineering adds the obligations relevant to an engineering decision. Mathematics addresses mathematical claims and calculations, Science scientific inference, and Cryptography cryptographic claims when selected for that work. The presence of calculations, experiments or encryption does not automatically select another module. Substantive engineering obligations remain applicable regardless of the module names chosen.

| Example assignment | Relevant contribution |
| --- | --- |
| Assess a changed operating envelope using existing evidence | Core plus Engineering; add further applicable specialist requirements from the team's governing practice. |
| Establish a mathematical bound used in a design decision | Mathematics can supply selected statement, proof or numerical-evidence obligations; Engineering retains applicability to the configuration and intended use. |
| Design an empirical study to support an engineering inference | Science can supply its selected inference obligations; Engineering retains intended-use, configuration and operational consequences. |
| Assess an authentication change in an engineered service | Cryptography can supply security-definition, implementation and key/state obligations; Engineering retains system effects, availability and change obligations. |
| Receive a signed inspection report | Core handles applicable delivery and trust conditions. The signature does not establish the report's substantive accuracy or the item's present condition. |

An imported result keeps its original property, assumptions, configuration and limits. A formally checked implication can establish that a consequence follows under stated conditions without establishing that those conditions hold in a deployed case. The application decision needs that additional bridge. No new Review, role or finding taxonomy is needed to express it.

Security and safety changes can interact. A credential expiry rule, recovery procedure or update restriction may affect availability or maintenance. Engineering evidence does not establish a cryptographic property; cryptographic evidence does not establish operational acceptability. Review the actual interfaces and applicable authority together when the decision crosses them.

### Automation stays bounded

An automated participant can retrieve accessible records, compare versions, run authorized checks, identify unresolved dependencies and prepare findings. A role name, Delegated Continuation label or method toggle does not authorize equipment control, hazardous testing, disclosure or release.

Optional ACR specialist methods retain Core's activation rules. Ordinary authorized engineering analysis and required safety work do not need a new ACR toggle. Controlled fault exercises need their actual isolation, authority and recovery conditions. This module adds no default daemon, database, language, scheduler or autonomous actuator.

If a team relies on the review as a consequential gate, the review process itself becomes part of the assessed dependency chain. Consider a wrong acceptance, a wrong block, omitted evidence, an unavailable service and delayed responses. Identify the actual fallback and any shared dependencies that could defeat both the original work and its check. The assessment can use existing assurance records; it does not require an endless succession of Reviews. FAA guidance is one scoped example of consequence-sensitive assurance and justified assumptions [N19]. Citing that guidance or passing the packet's examples establishes no aviation qualification.

## 7. Current pressures and where ACR should stop

Modern engineering often joins long-lived physical assets with changing software, data, suppliers and operating environments. The relevant question is which change can invalidate which conclusion. Configuration references, field evidence and explicit transfer assumptions help formulate that question; they do not remove the need for engineering expertise.

NIST's 2026 manufacturing digital-twin workshop report identifies interoperability, verification and validation with uncertainty, cybersecurity and workforce readiness as recurring challenges [N12]. Its separate digital-twin report addresses security and trust considerations [N14]. Engineers Canada's climate guidance addresses adaptation and mitigation in engineering decisions [N13]. These sources illustrate specific contemporary pressures; they do not rank all engineering problems or demonstrate ACR's effectiveness.

The useful response is to preserve a result's valid setting and make material changes visible. Avoid a universal checklist that expands every review into every field. Identify the current decision and the missing evidence, then use the appropriate competent method.

| Established practice | ACR's possible supporting role | Boundary |
| --- | --- | --- |
| Design and peer review | Resolve the exact disputed question and preserve material objections and follow-up. | Does not supply domain competence or an independent expert. |
| Requirement and configuration management | Bind the finding to existing controlled records and identify changed dependencies. | Does not replace the configuration system or observe physical condition. |
| Hazard analysis and safety assurance | Preserve control evidence, unresolved hazards and accountable recipients in the review. | Does not identify every hazard or accept residual risk. |
| Qualification, testing and validation | Check the relationship between the criterion, procedure, configuration and claimed result. | Does not extend finite tests to unexamined uses. |
| Independent assessment or certification | Deliver a clear evidence package to the actual assessor. | Does not grant that assessor's independence, accreditation or decision. |

Do not use ACR to delay required action, launder uncertainty through a vote, demand artificial opposition to settled evidence or hide missing competence behind roles. An objection can identify a missing load case, invalid assumption, incompatible interface or unreliable measurement without bringing a new executable script. Its relevance and support matter. A failed argument may defeat support without proving the engineering conclusion false.

## 8. Evaluate the intervention and deliver clearly

The constructed fixtures in this guide illustrate particular review distinctions. They do not replace equipment evidence, the team's actual methods or an evaluation of whether added procedure helps.

To evaluate usefulness, compare the team's ordinary competent review with the same workflow plus a specific ACR intervention at comparable total resources. Count preparation, record handling, prompting, checking, specialist time, integration and corrective follow-through. Preserve necessary evidence access and protection in both conditions. Do not measure agreement as accuracy when an independent answer is unavailable.

Useful outcomes include material issues found and missed, incorrect objections, quality of repairs, unresolved obligations, response delay, effort, and harm or disruption caused by the procedure itself. Distinguish issue detection from successful correction. Compare like tasks and record shared exposure when the same participants see related cases.

Retain added process when it protects an identified obligation or produces decision-relevant evidence unavailable from existing records. Remove duplicate summaries, role performances and empty approvals. High consequence can require more substantive assurance without requiring more ACR ceremony.

A useful final delivery says which decision was assessed, under which configuration and criteria, what the evidence establishes, what remains open, who has received the remaining obligations, and when the assessment needs reconsideration. It also distinguishes the Review's finding from any separately authorized engineering action. The team can then use the result without guessing what "review complete" means.

## Appendix A. Reading and execution map

| Need | Location |
| --- | --- |
| Governing shared rules and permissions | Core Specification and applicable conditional contracts. |
| Engineering requirements | Engineering Specification, Sections 1-9. |
| Compact optional review view | The table in Section 2 of this guide. |
| Constructed fixtures and boundaries | Sections 3 and 5 of this guide. |
| Evaluate a team intervention | Section 8 of this guide; Engineering Specification, Section 9. |
| Sources, status and inspected scope | The Specification's source appendix. |

## Appendix B. Selected source routes

**N01. ISO/IEC/IEEE 15288:2023.** Public scope of system lifecycle processes, including concurrent and recursive application. [Source](https://www.iso.org/standard/81702.html).

**N03-N04. NASA Systems Engineering Handbook, Product Verification and Product Validation.** Separate requirement and intended-use questions; tailored evidence and configuration. [Verification](https://www.nasa.gov/reference/5-3-product-verification/); [Validation](https://www.nasa.gov/reference/5-4-product-validation/).

**N05-N06. UK Health and Safety Executive.** Human factors in risk assessment and plant-change considerations. [Human factors](https://www.hse.gov.uk/humanfactors/topics/risk-assessment.htm); [Change](https://www.hse.gov.uk/comah/sragtech/techmeasplantmod.htm).

**N07, N13. Engineers Canada.** Advisory guidance on risk management and climate considerations. [Risk](https://engineerscanada.ca/guidelines-and-papers/public-guideline-on-risk-management); [Climate](https://engineerscanada.ca/guidelines-and-papers/public-guideline-principles-of-climate-adaptation-and-mitigation-for-engineers).

**N09. NASA-STD-7009B.** Use-specific credibility of analysis and simulation evidence. [Source](https://standards.nasa.gov/standard/nasa/nasa-std-7009).

**N11. IEC 61508-1 catalog.** Public scope and publication status, checked 10 November 2026. [2010 edition](https://webstore.iec.ch/en/publication/5515); [2026 PRV](https://webstore.iec.ch/en/publication/117296).

**N12, N14. NIST IR 8620 and IR 8356.** Manufacturing digital-twin workshop challenges and digital-twin security/trust considerations. [Workshop report](https://www.nist.gov/publications/digital-twins-workshops-summary-report); [Security report](https://csrc.nist.gov/pubs/ir/8356/final).

**N15. NASA NPR 8000.4C, Chapter 3.** Organizational responsibility and risk acceptance within NASA's applicable arrangements. [Source](https://nodis3.gsfc.nasa.gov/displayDir.cfm?Internal_ID=N_PR_8000_004C_&page_name=Chapter3).
