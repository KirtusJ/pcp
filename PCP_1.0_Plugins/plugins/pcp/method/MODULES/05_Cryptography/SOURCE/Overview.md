# Adversarial Claim Review

# Cryptography Overview - Version 1.0

**Packet:** ACR Version 1.0, Implementation  
**Component:** `acr.cryptography`, Version 1.0  
**Required core:** `acr.core`, Version 1.0; Core descriptor SHA-256 `f15686b385002bf597c2625bc18e98a390531a21ce91f64bdb249f2fe04a86a7`  
**Creator:** Kirtus Justus  
**Date:** 11 November 2026, America/Vancouver

ACR Cryptography helps a team investigate, construct and examine cryptographic work while carrying its conditions into dependent decisions. This guide explains how to use the module. The Cryptography Specification defines its requirements; the pinned core supplies authority, scope, assessment, findings and delivery. C-prefixed citations resolve to the module's source register and the Specification's reference appendix.

## 1. Start with a consequential question

A team has an encrypted delivery service. Its tests encrypt and decrypt successfully. A reviewer asks whether an old valid delivery can be replayed to apply an operation twice. The encryption test and the review question concern different properties. Both can be answered correctly while the service still has a defect.

This is a useful place for a focused ACR review: identify the promised property, the mechanism supposed to provide it, the evidence actually checked and the decision that follows. Security review already uses explicit goals and adversary assumptions. ACR coordinates that work; it does not replace established cryptographic analysis [C01].

Use ordinary expert review when it already handles the issue clearly. A Review becomes useful when a contested assumption, a consequential change or a handoff leaves responsibility or evidence unclear. The default commissioned procedure is FOCUSED. It can be one existing issue, one exact target and the people or tools needed to settle it. No standing service, database, full role roster or separate cryptographic Review is required.

| Review question | Useful intervention | Existing work to reuse |
| --- | --- | --- |
| Does a candidate improve a specified limitation? | State the intended contribution, relevant alternatives, security conditions and decisive comparisons. | Candidate specification, design rationale, cryptanalysis and benchmark artifacts. |
| Does this proof cover the adversary the application faces? | Map the application's capabilities to the security definition and identify exclusions. | Security argument, design review and proof artifacts. |
| Does the deployed caller satisfy a library's requirements? | Check the interface, build and state conditions used by that caller. | Code review, library documentation and release evidence. |
| Can recovery reuse a nonce or signing state? | Exercise the relevant restart, concurrency and restore paths in an authorized test setting. | Operational design, key-management procedure and recovery tests. |
| Does a migration protect the claimed information? | Separate key establishment, authentication, retained objects and signatures. | Cryptographic inventory and migration plan. |

An unevidenced concern is not a demonstrated attack. A supported objection can still be decisive without a working exploit: for example, a proof excludes compromise of the very party whose compromise the application promises to tolerate. The relevant task is to resolve that mismatch, not to stage an argument.

Choose alternatives for the actual function: authenticated encryption, hashing, key establishment, signatures or another explicitly identified purpose. For example, a signature assignment can assess Ed25519 under RFC 8032 and the applicable EdDSA requirements of FIPS 186-5 [C23-C24]. Specify the property and usage conditions before comparing candidates.

## 2. Receive the module and begin without ceremony

Receiving this module supplies reference material. It does not appoint a Director, activate a Review or authorize experiments. Apply the module when the actual instruction or adopted policy selects it for identified work. If a current assignment already supplies the target, authority, limits and required inputs, use them without asking for another form.

Applying this module requires the exact governing Core. A cryptographic assignment needs the relevant core rules and this module's applicable requirements in context. Mathematics can add selected obligations for mathematical exploration, proofs and calculations; Science for scientific inference; Engineering for engineering decisions. These are separate selections, not automatic imports. Cryptography is a specialized subject with mathematical foundations and implementation, operational and empirical aspects. A navigation label placing it under Mathematics does not require that module for every cryptographic assignment. Selected modules preserve the existing task; commissioned Review work retains its assigned Review and assessment.

For a new Review, the core's authorized human-direction default applies. A delegated participant can direct a justified child assessment within its grant. A role name describes a duty; it supplies no cryptographic expertise. The reviewer responsible for a consequential security judgment needs the appropriate competence, evidence and authority.

A resumed session first recovers the exact assignment and current relevant basis. A compact view should preserve the security property, adversary assumptions, excluded capabilities, implementation or deployment version, unresolved objections and next act. A fresh conversation does not erase prior exposure or make an expired grant current.

Do not paste private keys, recovery secrets or live credentials into a task record. Use nonsecret identifiers and authorized references. When sensitive evidence cannot be exposed to a participant, preserve that limitation and route the affected check to a permitted setting. A packet cannot confer access that the platform or key custodian has not granted.

## 3. Walk through one focused review

### The question and its boundary

An authorized team asks: "Can release R accept the same signed result twice and apply its consequence twice after a worker restarts?" The target is the exact receiver and its declared persistence behavior. The claim is limited to repeated delivery of the same logical operation; it does not claim confidentiality, resistance to every signer compromise or complete service availability.

The existing task record can carry the following concise account. These are example meanings, not a mandatory new schema.

| Portion | Example account |
| --- | --- |
| Subject and question | Receiver R; duplicate acceptance across the specified restart boundary; one logical effect per operation. |
| Mandate and limits | Authorized local fixture, synthetic credentials, two attempts and one restart; no external publication. |
| Working basis | Exact signed content, enrolled test key, operation identity, current permission rule and persistence contract. |
| Result | Observed accept/reject decisions, applied-effect count, retained state, checked cases and untested crash points. |

### The decisive adverse case

Send a valid result, record the applied effect, restart the receiver and send the identical result again. Its signature can verify both times. Signature verification answers whether the covered bytes match the test key; it does not remember that the operation already took effect. If the receiver applies a second effect, the scoped replay claim fails even though the cryptography behaved as specified.

The repair must address the actual effect boundary: persistent operation identity, appropriate transaction or recoverable procedure, current authority and an unambiguous association with the result. Checking a nonce in memory and clearing that memory on restart does not settle the commissioned question. Re-encrypting or re-signing the same logical operation also must not create a new effect identity under the core rules.

### The positive control and the finding

Confirm that an authorized new operation still succeeds. A receiver that rejects every message passes a superficial replay test while failing its intended function. Test the relevant crash and recovery points where the claimed guarantee depends on them; otherwise state that coverage remains missing.

A useful finding says which target and conditions were checked, what failed or passed, what was changed and what remains open. It does not turn a successful replay check into a judgment about the whole service. The implementation and its actual state transition need examination; a conversation in which participants agree that persistence exists supplies no substitute.

Suppose the persistence specification cannot be opened. That supports a narrower statement: the reviewer has not established the persistence contract. It does not show that the receiver has no persistence. Try the available authorized recovery path; if it remains inaccessible, identify the dependent conclusion left unestablished. If the assignment separately requires a readable specification to be delivered, assess that delivery obligation on its own basis. A later recovery can settle the access issue without any repair to the receiver. Correct the earlier finding and route the correction to affected recipients.

This is part of checking an objection, not an instruction to ignore suspected defects. NIST guidance calls for validation of suspected vulnerabilities and cautions that multiple tools can share a false positive [C25]. An observed duplicate effect under the valid stated procedure remains contrary evidence even if an unrelated document is unavailable.

## 4. Keep the evidence layers connected

Cryptographic work can concern a construction, a protocol, an implementation or an operating deployment. An assignment may cover one layer or several. Moving a conclusion between layers requires a justified connection, not a stronger adjective.

| Evidence | What it can establish in its stated scope | Question still requiring attention |
| --- | --- | --- |
| Security argument or checked proof | The specified implication under the named definitions, assumptions and trusted checking base. | Are those definitions and assumptions appropriate for the intended use? |
| Known-answer test | The tested implementation produces the expected result on specified inputs. | What untested inputs, misuse, build paths or leakage remain? |
| Adversarial input suite | Selected malformed and edge inputs produce the checked outcomes. | Does the suite cover the relevant threat, and are its expected outcomes justified? |
| Leakage analysis or measurement | The stated property or measured behavior under its analysis and observation conditions. | Which platforms, inputs, sensitivities and leakage channels are excluded? |
| Operational recovery exercise | The observed recovery trace under the exercise's configuration. | Does it cover the actual failure and restoration paths relied upon? |
| Validation certificate | The recorded validation scope, version, environment and status. | Does the deployed configuration fall within that scope? |

Verified cryptographic software can supply much stronger evidence than a collection of examples, but its specification, caller requirements and trusted toolchain still matter. The HACL*/EverCrypt documentation describes distinct functional, memory and secret-independence properties; identify which guarantee is being used [C09]. An approved algorithm, an algorithm test and a validated cryptographic module are different claims. The CMVP record and its security policy define the relevant validation scope [C12].

A conditional theorem may be established as a theorem: "If assumptions A hold, property P follows." That does not establish that A holds in a deployment. Review the theorem and its application as distinguishable claims. This preserves useful theoretical results without concealing unresolved operating assumptions.

LLM assistance can help locate missing assumptions, propose adverse inputs, compare artifacts and organize a review. A generated proof, plausible reference or predicted tool output remains a proposal until checked against the actual source or authorized execution. Multiple participants may share the same mistaken premise. The core's evidence and lineage rules apply unchanged.

## 5. Construct, compare and revise

For an authorized construction assignment, identify the intended contribution and relevant alternatives. Preserve the candidate's exact revision, security definition, assumptions and interfaces. Develop the strongest supported case for that candidate while looking for discriminating failures. A useful outcome may be an improved construction, an attack, a weaker required assumption or a precise limit on an attempted design.

Compare like properties under declared conditions. A faster configuration may rely on a different security assumption or omit protective measures. NIST's signature and lightweight-cryptography evaluations illustrate why security, implementation and performance need separate attention [C21-C22]. Candidate revision can continue under the existing mandate; retain the earlier result and reassess the changed dependencies.

| Development question | What the review should connect |
| --- | --- |
| Does the construction work as specified? | Functional behavior and its checked domain. Correct recovery of a message alone does not establish confidentiality. |
| Does the argument support the intended security property? | Security definition, assumptions, adversary capabilities and the actual conclusion. |
| Does the implementation preserve that argument's conditions? | Interfaces, encodings, platform behavior, randomness and key/state use. |
| Does the operating arrangement preserve those conditions? | Concurrency, recovery, trust, compromise and authorized maintenance. |
| Does the revision improve the intended tradeoff? | Comparable functionality, security basis, protection costs, workload and uncertainty. |

A faithful account does not remove an adversary capability or narrow a claim merely to make it defensible. Such a change can be a useful candidate revision, but it remains a different claim. Judge the original and the proposed revision under their respective conditions. Neither a request to prove security nor a request to find a break supplies the result.

Small constructed illustrations of correctness without confidentiality, authenticated context, nonce reuse, state restoration and application guarantees can clarify a current issue; constructing or executing every such illustration is unnecessary for ordinary module use.

## 6. Review current migration decisions carefully

The following status notes were checked on 10 November 2026. They orient a review; they are not a universal deployment prescription. Resolve later changes, applicable errata, organizational requirements and implementation support before a consequential decision.

| Topic | Current reference | Review consequence |
| --- | --- | --- |
| Post-quantum transition | NIST IR 8547, Final, October 2026 [C16]. | Inventory what information and operations need protection, for how long and under which transition requirements. |
| Cryptographic agility | NIST CSWP 39upd1, June 2026 [C17]. | Plan inventory, replacement, interoperability and operational continuity without silently weakening security policy. |
| Hybrid TLS key establishment | RFC 10024, Standards Track, August 2026; RFC 9954 describes the underlying hybrid construction [C18-C19]. | Bind the exact negotiated mechanism and implementation. Key establishment does not describe every authentication or retained-data property. |
| Key-management guidance | SP 800-57 Part 1 Rev. 5 is final; Rev. 6 remains an initial public draft [C04, C20]. | Distinguish adopted final requirements from proposed changes. |
| PQ algorithms and updates | FIPS 203, 204 and 205 are final standards; the 203 and 204 publication pages also identify potential updates [C13-C15]. | Pin the actual version, parameter set, implementation and relevant corrections. A pending update is not a replacement final standard. |

Cryptography is more than choosing an algorithm. A migration can change message sizes, latency, certificates, hardware support, recovery procedures and fallback behavior. A theoretically suitable construction may not be suitable for every constrained deployment. Evaluate the consequences that matter to the assigned decision and retain the ordinary team's existing evidence.

Optional delivery encryption is governed by the core. Activating this module does not encrypt a packet or activate a new delivery channel. Conversely, leaving optional object encryption OFF does not waive transport protection, secret handling or other applicable requirements. A live key exchange, a stored object and a long-lived signature can have different security requirements.

## 7. Use checks at their actual scope

A local instructional check that calls an installed cryptographic library on fixed synthetic inputs establishes only what it checks. Its record should identify the source digest, dependency and backend versions, actual observations, expected outcomes and limits. Inspect the source and dependency needs before an authorized run.

Public test vectors and synthetic inputs demonstrate selected primitive and application boundaries. They do not exercise a production ACR transport or key service. Select checks for the actual assignment; no fixed example list is a required suite for every review.

The release verifier in the Implementation packet (`TOOLS/verify_release.py`) has a different job: comparing local files and component bindings against the supplied manifest. It does not authenticate that manifest's publisher. If an attacker replaces both the payload and its digest in an untrusted manifest, a matching local hash is expected; a trusted external binding is required when provenance authentication matters. This module does not turn a checksum utility into a security boundary.

CI can rerun suitable checks after changes to the target, its dependencies or its required environment. Bind results to the exact artifacts. Reusing a prior result is reasonable when its relevant basis remains applicable; a changed compiler, provider, parameter or trust policy can require reassessment. A green job only establishes what that job actually checks.

Standing monitoring and Delegated Continuation remain core capabilities with explicit scope, permissions, budgets and recheck triggers. They create no background process by themselves. Keep ordinary bounded work simple. A cryptographic key's retirement, revocation or state exhaustion must not be treated as a prompt preference that an automated participant can waive.

## 8. Evaluate the module before expanding it

Start with one question, reuse current evidence and check the decisive adverse condition. Keep the finding within the work's scope. Before expanding the process, compare representative tasks under ordinary work and the smallest relevant ACR intervention. Keep access, expertise and total effort comparable, including setup, tools, review and integration. Select acceptance criteria before inspecting outcomes; related examples are not independent replications of an efficiency claim.

Measure correctly identified material defects, resolved objections, false objections, appropriate repairs and total effort. Assess missed defects where a suitable reference exists and retain inconclusive outcomes. Extra records alone show no advantage.

Evaluation should examine claim coverage, demanding implementation and recovery cases, and proof applicability. Add a step for a demonstrated gap; remove or simplify it when existing evidence is adequate or it contributes no relevant protection.
