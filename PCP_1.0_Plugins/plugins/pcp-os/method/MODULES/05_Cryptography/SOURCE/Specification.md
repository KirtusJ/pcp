# Adversarial Claim Review

# Cryptography Specification - Version 1.0

**Packet:** ACR Version 1.0, Implementation  
**Component:** `acr.cryptography`, Version 1.0  
**Required core:** `acr.core`, Version 1.0; Core descriptor SHA-256 `f15686b385002bf597c2625bc18e98a390531a21ce91f64bdb249f2fe04a86a7`  
**Creator:** Kirtus Justus  
**Date:** 11 November 2026, America/Vancouver

ACR Cryptography governs scoped cryptographic investigation, construction and review. It supplies a compact evidence contract for questions, constructions, implementations and deployments. Teams retain their established cryptographic methods, specialist expertise, security governance and operational controls.

This Markdown Specification is the normative module text; its PDF is the corresponding reading copy. Sections 1-9 are normative, except labeled examples. Appendices A-C provide terminology, cautions and sources. Capitalized requirement words have the governing core's BCP 14 meanings.

## 1. Scope, adoption and economy

The module applies when selected by an authorized task, commission or adopted policy. Ordinary authorized work remains the default. Teams SHOULD use a FOCUSED review for an identified disagreement, consequential uncertainty, composition boundary or handoff that needs structured assessment. Reuse an adequate existing review rather than commissioning a duplicate.

The exact core and applicable module obligations MUST be available for the assigned act. A compact instruction or State Brief MAY carry the controlling requirements while supporting records remain accessible through an authorized path. Missing prerequisites block only dependent commitments; independently authorized preparation may continue.

Adoption preserves the existing authorized task, authority and duties; commissioned Review work retains its Review and applicable assessment Session. It creates no Director, target, permission, additional role or lifecycle. Mathematics, Science and Engineering are independently selectable for their applicable obligations. Topical grouping under Mathematics does not make that module a required dependency; cryptographic work also has implementation, operational and empirical obligations. Module receipt alone commissions no review.

Existing issue records, proof repositories, security analyses, test reports and deployment records SHOULD supply the evidence. Conformance records performance of the specified review; it MUST NOT be represented as cryptographic security, regulatory approval, implementation validation or permission to deploy.

## 2. Claim, adversary and inherited basis

The task MUST identify the artifact or decision and its exact assessed version. The assessment question MUST state the property being assessed, relevant scope and what would count as contrary evidence. Commissioned Review work resolves these meanings through its Target and Claim. A claim such as "secure" is insufficient without its intended meaning and setting. Threat analysis SHOULD use established security practice [C01].

Add or reference only the material meanings in this table within the core task record. No separate form is required.

| Record portion | Cryptographic meaning when relevant |
| --- | --- |
| Subject and question | Construction, implementation, configuration or deployment; intended security property; decision and review boundary. |
| Working basis | Exact specification and parameters; assumptions; adversary access; interfaces; relevant environment, evidence and unresolved obligations. |
| Mandate and limits | Responsible decision owner; needed expertise; permitted testing, access, disclosure, resources and governing requirements. |
| Result | Checked property and evidence; applicability; contrary findings; limitations; remaining obligations and recheck conditions. |

Resolve adversary capabilities material to the claim: passive observation, active messages, chosen inputs, concurrent sessions, compromise, insider access, physical or side-channel access, and classical or quantum computation. State relevant resources, confidentiality or authenticity lifetime and allowed failure probability where the claim uses them. An omitted capability MUST NOT silently become an established absence.

The working basis MUST preserve material conventions and assumptions across handoffs, using the Core Basis Header or an equivalent existing record. These can include parameter sets, encodings, algorithm modes, key roles, security definitions, oracle access, trust anchors, compromise timing and state rules. Exact references MAY carry detail; the receiving worker MUST be able to resolve what its act needs.

Claims can concern several layers. Distinguish construction/security analysis, implementation behavior, operational deployment and standards conformance. Evidence for one layer MUST NOT be silently promoted to another. A narrower authorized investigation retains its boundary; a change to the parent property follows core change control.

## 3. Analysis, proofs and composition

A claimed security analysis MUST identify its security notion, assumptions, adversary setting, assessed construction and material parameter or resource bounds. Resolve distinctions such as single-user versus multi-user, one execution versus concurrent use, and classical versus quantum adversaries when they affect the conclusion. A named primitive or familiar proof technique does not supply an omitted argument.

For proof-based evidence, preserve the exact theorem or proposition, premises, proof artifact and checked conclusion. A formal check MUST record the statement actually checked, relevant tool/version/configuration, trusted dependencies and execution outcome. Review the translation between the intended property and the formal statement. Prose review and successful tool execution establish different facts.

A supported implication does not establish its premises for a deployment. Apply the Core's evidence rules to the actual operational claim, preserving acceptance-critical premises and the argument connecting the proof to that use.

Composition requires an argument for the actual interfaces, context binding, key use, negotiation and adversary setting. Individually assessed components do not automatically establish the combined property. KEM use, for example, requires application-specific treatment of authentication and subsequent key use [C03]. A hybrid construction MUST identify its combiner and required assumptions; the word "hybrid" supplies no security guarantee.

**EXAMPLE:** RFC 9180 describes HPKE's security properties and limits. Its specified modes do not provide general replay prevention, automatic downgrade prevention or recipient-compromise forward secrecy; applications also supply a wire encoding. An HPKE-based delivery therefore needs evidence for the surrounding properties it claims [C02].

### 3.1 Research and construction

An authorized assignment MAY develop ciphers, other primitives, protocols, implementations, security arguments or cryptanalytic methods. State the intended contribution and relevant alternatives: additional functionality, an attack, stronger evidence, weaker assumptions or a cost improvement. A novelty claim MUST retain the search scope and date. Established cryptographic design and cryptanalysis remain the substantive methods [C21-C22].

The candidate MUST have an identifiable revision and a specification sufficient for the assigned check. Preserve material algorithms, interfaces, encodings, parameters, input domains, randomness, state and failure behavior. Distinguish functional correctness from the security property. Apply Section 2's adversary and scope requirements to the actual candidate; state success criteria, resource and query limits and advantage convention when used. A full security reduction is not a prerequisite to exploratory work. Identify what is conjectured, argued, proved or observed.

Attacks and negative searches MUST identify the attacked object, methods, parameters, resources and coverage. Distinguish full constructions from reduced instances or internal components; transfer between them requires an argument. An internal distinguisher or reduced-round attack need not defeat the full claimed construction [C22].

Revisions MAY proceed within the existing mandate. Preserve the changes relevant to earlier findings, known attacks and unresolved obligations. A repair does not erase an earlier failure. Reassess affected evidence and reuse unaffected evidence; changes to the commissioned property or authority follow the core. Iteration does not require a new Review for each candidate.

Comparative claims MUST identify the baseline and material comparison conditions: functionality, security basis, parameters, implementation, platform, workload and protective measures. Report measured costs and uncertainty separately from estimated security. Different assumptions, protection costs or optimization maturity MUST NOT be hidden in a general superiority claim. Public cryptanalytic review and reproducible comparisons are relevant evidence, not substitutes for the actual argument [C21-C22].

Deliver the smallest sufficient candidate description, evidence and unresolved limitations under Section 8. A failed candidate, new attack or narrower result can be a useful research outcome. Research findings confer no deployment or disclosure authority. Responsible experts retain the substantive judgment appropriate to the decision.

## 4. Implementation and execution evidence

An implementation claim MUST resolve the code and dependencies, build or executable identity, relevant configuration and platform sufficient to interpret or reproduce the check. Include compiler, optimization, hardware or runtime details when they affect the property. Use the team's established language and tooling where suitable; this module prescribes no programming language or database.

Select checks that can expose failure of the claimed property. Depending on the assignment, evidence may include specification vectors, known adverse inputs, differential checks, fuzzing, formal verification, integration tests, resource-limit tests or measurements. Reuse maintained suites where their coverage fits; Wycheproof supplies tests for known cryptographic weaknesses, not a complete security proof [C10].

Where a decisive obligation is mechanically checkable and an appropriate authorized checker is available, perform the check under the core. No universal tool or witness format is required. An unavailable check leaves its dependent conclusion unresolved or narrower; it does not prohibit other useful authorized analysis.

The evidence MUST distinguish planned, attempted and completed checks. Record the criterion, exact inputs or input-generation procedure, execution conditions, outputs and relevant diagnostics. Preserve failures, exclusions and non-reproducible outcomes. A positive control or known failing case SHOULD establish that a negative-result procedure can detect the failure class it claims to examine.

Functional correctness, memory safety, timing behavior and physical leakage are distinct properties. Claims relying on formal verification MUST respect its specified coverage, trusted compilation path and caller preconditions [C09]. Claims about leakage or fault resistance MUST identify the observation or fault capability and tested setting. Absence of observed leakage is bounded by the procedure's sensitivity and coverage. KyberSlash illustrates why specification-level security and implementation timing require separate assessment [C11].

A small example, reduced instance or simulated adversary MUST identify simplifications, the demonstrated result and the missing transfer argument. A successful demonstration cannot establish untested parameter sizes, platforms or deployment conditions.

## 5. Randomness, keys, state and identity

Address the following obligations when the claim depends on them; existing assessed mechanisms and records MAY supply the evidence.

| Dependency | Assessment needed |
| --- | --- |
| Randomness | Required unpredictability or distribution; source and generator; initialization, reseeding, failure handling and relevant fork/restore behavior. |
| Key lifecycle | Generation or enrollment; principal/purpose binding; custody and allowed operations; use limits; rotation, compromise, recovery, revocation and destruction. |
| Stateful use | Uniqueness and allocation across writers; exhaustion; crash, retry, backup, restore, cloning and transfer behavior. |
| Identity and context | Trusted enrollment; message/protocol context; recipient and purpose binding; key confirmation or peer authentication when required. |

Random output appearance or statistical tests alone MUST NOT be presented as establishing secret entropy. NIST's SP 800-90 series distinguishes entropy sources, deterministic generators and their construction; use applicable guidance for the actual source and system [C05]. Key-management requirements follow the relevant security setting and adopted governance [C04].

Nonce and key-use conditions MUST be assessed across the complete relevant execution, including recovery. A valid ciphertext or signature does not establish freshness. A retry that reproduces an existing object differs from a new cryptographic operation. The selected scheme's exact requirements govern both. RFC 8439 illustrates the consequences of repeating a nonce with the same key [C06].

For stateful signatures, key availability and prevention of state reuse are separate obligations. Apply the selected scheme and governing profile to backup and migration. NIST SP 800-208 restricts its approved use; RFC 10033 describes additional operational patterns, some beyond those restrictions. Do not infer compliance with one source from following another [C07-C08].

Core delivery, credential and protection requirements remain controlling. Keep secret material outside prompts and ordinary evidence packets; use mediated operations and protected records where applicable. Module adoption does not activate DELIVERY_ENCRYPTION. Its OFF setting cannot waive protection required by the actual path or policy.

## 6. Deployment, standards and transition

A deployment assessment MUST connect the claimed protection to the actual endpoints, trust boundaries, configuration, available algorithms, identity path, retained data and recovery procedures that matter to the claim. Transport, object storage, authentication and durable signatures can have different security lifetimes and transition requirements.

A migration assessment SHOULD begin from the relevant cryptographic inventory and dependencies, then evaluate interoperability, performance, failure behavior, downgrade resistance, operations and recovery. Existing inventories and management tools SHOULD be reused. Cryptographic agility includes maintaining security and operation while changing mechanisms; adding negotiation choices alone is insufficient [C17].

Selection MUST identify the applicable specification, parameter set, implementation/version, source status, review date and material errata or advisories. Do not silently equate a draft, selection announcement, proposed correction or vendor assertion with a final standard or assessed deployment. Monitor the sources relevant to the decision; no continuous service is required unless commissioned.

The following status snapshot is informative and MUST NOT replace a current check for a consequential selection or change:

| Source | Status verified 10 November 2026 |
| --- | --- |
| FIPS 203 / 204 / 205 | Final, 13 August 2024. FIPS 203 and 204 have published potential-update notices [C13-C15]. |
| NIST IR 8547 | Final, 27 October 2026; post-quantum transition guidance [C16]. |
| RFC 10024 / RFC 9954 | TLS 1.3 hybrid mechanisms: Proposed Standard, August 2026; construction framework: Informational, July 2026 [C18-C19]. |
| SP 800-57 Part 1 | Revision 5 is final; Revision 6 is an initial public draft [C04, C20]. |
| CSWP 39upd1 | Final update, 29 June 2026; supersedes CSWP 39 [C17]. |

Post-quantum claims MUST name the property and components covered. An improved key-establishment path does not establish the security of every authentication, signature or stored object. Standards are applied within their actual scope and relevant governance; this module imposes no universal jurisdictional compliance regime.

Where validation or certification is claimed, resolve the issuing program, certificate status, exact component/version, operating environment and conditions. An algorithm certificate alone does not establish FIPS 140 module validation; a module validation does not assess every surrounding application decision. FIPS 140 validation does not assess supply-chain or supplier risk; assess those separately when the selection decision depends on them [C12].

## 7. Objections and authorized adverse testing

An objection MUST identify the disputed claim, relevant assumptions or boundary, supporting reasoning or evidence, and the consequence if sustained. Evidence may be a proof defect, applicable attack, counterexample, measurement, implementation failure, unsupported assumption or missing required check. An objection need not contain executable code to be material.

Distinguish a failure within the stated claim from an assumption variation or a threat outside scope. An out-of-scope threat can still reveal that the claim is unsuitable for the intended decision; record that applicability issue without changing the original claim silently. Unsupported rhetorical opposition supplies no contrary evidence.

A suspected vulnerability MUST be distinguished from a validated failure and from an assessment-access limitation. Apply the Core evidence-access rules before treating an unread specification, unavailable test or failed retrieval as an omission in the assessed construction. NIST SP 800-115 describes validation of suspected findings and warns that different tools can repeat the same false positive [C25].

Use only authorized systems, access, inputs and disclosure paths. Core permissions and containment govern fault injection, compromised-state simulations, fuzzing, adversarial traffic and other disruptive work. Specialist testing follows a suitable commissioned method; ordinary authorized checks need no additional ceremony. Production evidence, keys or operation MUST NOT be covertly altered for a Resilience Exercise.

A controlled demonstration SHOULD use disposable material and an isolated setting where feasible. State its threat, preconditions, expected discriminating result, resource limits, containment and recovery relevant to the action. A test result supplies no permission to apply the procedure elsewhere.

## 8. Findings, release and recheck

Use Core dispositions and lifecycle states for commissioned Review work. Ordinary results need no ACR status vocabulary; any chosen canonical disposition retains its meaning and evidential guards. A finding MUST distinguish the property assessed, evidence obtained, assumptions accepted, applicable scope and unresolved obligations. Do not replace these with vote totals, a successful parser result or a generic security score.

REFUTED_IN_SCOPE requires contrary evidence meeting the original criterion. A failed proof can remove support without refuting its conclusion. NOT_IDENTIFIED_IN_SCOPE requires a checked ambiguity or nonselection witness establishing insufficiency of the permitted information, as defined in core Section 5.2; failure to discover an attack does not establish it. UNRESOLVED is appropriate when necessary evidence, access, clarity or effort is missing. CONDITIONAL applies as defined by the core, with the implication distinction in Section 3.

Release the smallest reproducible evidence package appropriate to the claim and disclosure limits. Exact references MAY supply large or restricted artifacts. Separate public findings from protected reproduction material. Disclosure, remediation and deployment follow their actual authority; review completion authorizes none of them automatically. Route material findings and corrections through the Core correction and handoff rules to the affected authorized recipients. A local correction alone does not establish that a recipient stopped relying on the earlier finding.

Identify recheck triggers material to continued reliance: changed assumptions, security definitions, code/builds, dependencies, platform, key handling, compromise information, standards status or deployment conditions. Reuse unaffected evidence through a justified compatibility assessment. A historical result remains historical when its applicability has not been re-established.

## 9. Customization and module evaluation

Teams MAY use local vocabulary, templates, tools and review procedures while preserving the controlling meanings and safeguards. Apply only relevant obligations. An inapplicability decision MUST have a substantive basis; UNKNOWN cannot be relabeled inapplicable to complete a form.

Use the core's permission and change mechanisms for customization and delegated continuation. No blanket permission arises from a cryptographic role, expert title or automated session. Preserve existing decision accountability and any required specialist participation.

When evaluating whether the module helps a team, compare with its ordinary expert process at comparable total cost and access. Identify the task mix, review criteria, defects or unresolved issues found, false objections, remediation quality and coordination overhead. Include review and record-preparation effort. Use the results to narrow, simplify or discontinue an intervention that adds no useful protection.

## Appendix A. Working glossary

| Term | Meaning here |
| --- | --- |
| Security claim | A stated property of an identified target under declared conditions and adversary capabilities. |
| Security notion | The formal or operational meaning of a property, including the relevant experiment, interfaces and success criterion. |
| Construction | A specified mechanism or composition of mechanisms whose properties are assessed. |
| Security parameter | A parameter governing a construction's claimed security or resource scale; distinct from a protocol version. |
| Evidence boundary | The property, artifacts, environment and assumptions actually covered by a result. |
| Cryptographic agility | Ability to change cryptographic mechanisms while maintaining the required security and operation. |
| Use limit | A bound or condition on a key, nonce, state or operation required by the selected mechanism and setting. |

## Appendix B. Cautions and reading discipline

| Code | Caution |
| --- | --- |
| CC01 | Consensus, role labels and polished explanations supply no cryptographic evidence. Read the claim and its actual support. |
| CC02 | A proof, test, measurement, certification record and deployment observation support different conclusions. Preserve their boundaries. |
| CC03 | Exact identity and authenticated records can preserve an incorrect assessment. Evaluate meaning and applicability as well as bytes. |
| CC04 | Recovery, concurrency and compromise can invalidate assumptions that held in an isolated successful run. |
| CC05 | A restricted demonstration or negative attack search establishes only its stated coverage; neither establishes universal security. |
| CC06 | A review packet may contain sensitive methods or artifacts. Follow its actual access and disclosure controls. |

Read the authorized task and relevant core instructions first, then this module's applicable clauses, then the referenced substantive methods. Preserve material assumptions in compact context. Request missing information only where the next dependent act requires it; continue authorized unaffected work.

## Appendix C. Primary sources

Source status was checked on 10 November 2026. These sources substantiate technical practice; ACR requirements are stated in Sections 1-9.

**C01. IETF/IAB. RFC 3552, BCP 72.** Security goals, threat analysis and security considerations. [Source](https://www.rfc-editor.org/rfc/rfc3552.html).

**C02. IRTF. RFC 9180, Hybrid Public Key Encryption.** Informational, 2022; construction, security properties and application obligations. [Source](https://www.rfc-editor.org/rfc/rfc9180.html).

**C03. NIST SP 800-227.** Final, 18 September 2025; recommendations for KEM use. [Source](https://csrc.nist.gov/pubs/sp/800/227/final).

**C04. NIST SP 800-57 Part 1 Rev. 5.** Final, 4 May 2020; key-management guidance. [Source](https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final).

**C05. NIST SP 800-90C.** Final, 25 September 2025; random-bit-generator constructions. [Source](https://csrc.nist.gov/pubs/sp/800/90/c/final).

**C06. IRTF. RFC 8439.** Informational, 2018; ChaCha20-Poly1305 and nonce-use constraints. [Source](https://www.rfc-editor.org/rfc/rfc8439.html).

**C07. NIST SP 800-208.** Final, 2020; stateful hash-based signature schemes and restrictions. [Source](https://csrc.nist.gov/pubs/sp/800/208/final).

**C08. IETF. RFC 10033.** Informational, September 2026; hash-based signature state and backup management. [Source](https://www.rfc-editor.org/rfc/rfc10033.html).

**C09. HACL*/EverCrypt documentation.** Verification coverage and client obligations. [Verification](https://hacl-star.github.io/Overview.html); [Caller preconditions](https://hacl-star.github.io/General.html).

**C10. C2SP. Project Wycheproof.** Maintained adverse test vectors for cryptographic implementations. [Source](https://github.com/C2SP/wycheproof).

**C11. Bernstein and colleagues. KyberSlash.** Research paper, ePrint 2024/1049; implementation timing vulnerabilities. [Source](https://eprint.iacr.org/2024/1049).

**C12. NIST. CMVP validated modules.** Program guidance and scope of module validation. [Source](https://csrc.nist.gov/Projects/cryptographic-module-validation-program/validated-modules).

**C13. NIST FIPS 203.** Final, 13 August 2024; ML-KEM; potential-update notice dated 17 November 2025. [Source](https://csrc.nist.gov/pubs/fips/203/final).

**C14. NIST FIPS 204.** Final, 13 August 2024; ML-DSA; potential-update notice dated 31 July 2026. [Source](https://csrc.nist.gov/pubs/fips/204/final).

**C15. NIST FIPS 205.** Final, 13 August 2024; SLH-DSA. [Source](https://csrc.nist.gov/pubs/fips/205/final).

**C16. NIST IR 8547.** Final, 27 October 2026; transition to post-quantum standards. [Source](https://csrc.nist.gov/pubs/ir/8547/final).

**C17. NIST CSWP 39upd1.** Final update, 29 June 2026; crypto-agility strategies and practices. [Source](https://csrc.nist.gov/pubs/cswp/39/upd1/considerations-for-achieving-crypto-agility/final).

**C18. IETF. RFC 10024.** Proposed Standard, August 2026; specific PQ/traditional hybrid TLS 1.3 mechanisms. [Source](https://www.rfc-editor.org/rfc/rfc10024.html).

**C19. IETF. RFC 9954.** Informational, July 2026; hybrid key exchange in TLS 1.3. [Source](https://www.rfc-editor.org/rfc/rfc9954.html).

**C20. NIST SP 800-57 Rev. 6.** Initial Public Draft, 5 December 2025; proposed key-management revision. [Source](https://csrc.nist.gov/pubs/sp/800/57/pt1/r6/ipd).

**C21. NIST IR 8610.** Final, May 2026; additional-signature candidate evaluation, cryptanalysis, comparative criteria and revisions. [Source](https://csrc.nist.gov/pubs/ir/8610/final).

**C22. NIST IR 8454.** Final, June 2023; lightweight cryptographic construction evaluation, attack scope, candidate changes and benchmarking limits. [Source](https://csrc.nist.gov/pubs/ir/8454/final).

**C23. IRTF. RFC 8032.** Informational, January 2017; EdDSA signature schemes, including Ed25519, and test vectors. [Source](https://www.rfc-editor.org/rfc/rfc8032.html).

**C24. NIST FIPS 186-5.** Final, February 2023; Digital Signature Standard, including EdDSA; publication page identifies potential corrections. [Source](https://csrc.nist.gov/pubs/fips/186-5/final).

**C25. NIST SP 800-115.** Technical Guide to Information Security Testing and Assessment, 2008. Sections 7.3 and 8.2 address finding validation, false positives and reporting to appropriate recipients. [Source](https://csrc.nist.gov/pubs/sp/800/115/final); [Full text](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-115.pdf).
