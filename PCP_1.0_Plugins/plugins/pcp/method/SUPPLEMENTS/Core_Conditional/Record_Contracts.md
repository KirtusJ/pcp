# ACR Record Contracts

**Conditional attachment to `acr.core`, Version 1.0 / Kirtus Justus**

This conditional normative attachment maps core meanings to records. It applies only where the corresponding activity or boundary exists. An implementation may combine fields, reuse exact references and map existing host identifiers. It must document the mapping, make it available to authorized consumers as needed, and preserve required meaning; these contracts do not prescribe separate forms or databases.

## 1. Compact record and exact references

The compact record combines subject/question, mandate/limits, working basis and result. Preserve the actual requested deliverable, intended use or recipient and material inherited output requirements; Review-specific fields apply only to the corresponding commissioned work. An Entry Card, State Brief, Basis Header, access view and continuity anchor may be projections of it. None requires a separate file or an onboarding status flag.

A PinnedRef resolves object identity, kind, immutable version and a digest when byte integrity is claimed. Declare unavailable bytes explicitly. A filename, mutable head or supplied digest alone does not establish the referenced version or origin.

Canonical exchange identities have the form acr:<kind>:<uuid>. The UUID is lowercase hexadecimal in 8-4-4-4-12 groups, version digit 4 and RFC UUID variant digit 8, 9, a or b. Kind is one of participant, review, session, target, claim, scope, evidence, artifact, packet, event, receipt, decision, policy or run. A local profile may instead use its declared stable identity mapping. Allocation verifies uniqueness within the declared namespace.

An authoritative record carries its exact profile/version. Parsers reject conflicting duplicates, unknown critical fields, incorrect types, nonfinite values where numeric facts are required, excessive size/nesting and unmapped critical identities. Integer fields reject booleans and implicit string conversion. The profile defines numeric bounds, absent-value semantics and bounded error handling.

## 2. Commission and work

The Charter resolves the exact components (identifier, version and digest) and profile, Review and initial Session, Target/whole/Claims, criteria, direction, assignments, actual authority, inputs, resource limits, protection, exposure and completion conditions. Required parent, Observer Channel, recurring-service and optional-method fields apply only to those features.

Where modules apply, the existing task, commission or policy binds their exact selected definitions, required components, scope and effective basis. Ordinary authorized work uses its existing subject, question, basis and checking record; module adoption does not create Review-only objects, gates or lifecycle fields. A later selection change identifies its authorizing basis, effective revision and affected obligations under core Section 14.1; historical findings retain their original rule basis. Subject classification, packet inclusion, receipt and task adoption remain separate meanings. No additional record kind or universal module field is required.

A creation operation binds exact commission, Review/initial Session, Target/Charter and original commissioning basis. Current retry actor/permission is separate. Preserve coherent replay, unused-identity guards, original creator and receipt, allocation accounting and current Session pointer under the core commissioning rules.

A task binds run, responsible actor/duty, exact assessment basis, applicable parent token, inputs, permissions, method/resource/exposure constraints, dependencies and work state.

A result binds actual work and output identity, original basis, source/assumption lineage, execution outcome, proposed finding, checks, uncertainty, relevant cost and interventions. A compatibility assessment references that immutable result and the proposed current acceptance basis.

## 3. State, projection and Basis Header

An authoritative event identifies event ID, Review/Session, ordering domain, expected prior revision, actor/duty, action, current authority, exact relevant payloads, checked guards, resulting state and timestamp/timezone. Ordering is defined by the authority mechanism rather than wall-clock time alone.

A State Brief binds source cutoff, snapshot/projection rule and permitted recipient view. It resolves current task, relevant state/authority, necessary inputs, restrictions, objections, unknowns, deadline, blocked acts and next permitted action. An acknowledgment binds the exact received view and consequential meaning assessment when needed.

Its projection identifies the controlling meanings needed for the next act and the basis on which jointly required facts are compatible. Exact references may defer supporting detail, but do not replace active restrictions or needed inspection. Core Section 8.1 governs this boundary; no additional record is required.

For a module change, carry the applicable rule differences, resolved dependencies, affected task/parent obligations, conflicts and remaining unknowns needed by the next act. Reuse compatible prior context. Acknowledgment names what was actually checked; receipt of a component does not establish adoption, understanding or permission.

A delta identifies its exact prior view and changes; reliance requires reconstructing the necessary current view. Missing bases require recovery rather than treating omissions as unchanged. Content equality does not restore a previous control revision, authority generation, allowance, exposure or obligation.

Its Basis Header resolves source basis, Target/Claim, selected scope, intended acceptance property, relevant input/output meanings, representation conventions, boundaries, required invariant references, permitted variation and unresolved obligations. Exact inherited records may supply these meanings. The mapping includes the declared equality or refinement relation and any applicability assessment; a copied header cannot erase a missing condition.

An access view records permitted, reachable, retrieved, integrity_verified and actually_inspected separately with YES, NO or UNKNOWN, evidence and cutoff. NOT_APPLICABLE requires a reason. Cached inspected bytes may remain usable when an endpoint is unreachable under the governing freshness and access rules.

Where ACR is relied on for consequential work, the access view also carries the fidelity settings of Core Section 15.8 as delivery (ABSORBED_TEXT, RETRIEVAL, TOOL_ASSISTED, HOST_ENFORCED or UNKNOWN), extent (exact components available, by identifier, version and digest), grounding (EXTERNAL_INSPECTED, SUPPLIED_ONLY, RECALL_ONLY, NONE or UNKNOWN), execution (EXECUTED, REASONED or UNKNOWN) and observability (INSPECTABLE, BLACK_BOX or UNKNOWN). Where it matters to reliance, the view also states whether the host exposes the participant's reasoning trace (FULL, SUMMARY, NONE or UNKNOWN); a trace is recorded as an output, never as an inspection of processing. The settings state what could be established. UNKNOWN is not replaced by an assumed value. A setting waives no requirement and blocks no work by itself. No record carries a character or persona field.

A freeze identifies affected fields or acts, governing authority and amendment/release conditions. A seal identifies the preserved artifact and basis, including whether it is an assessment seal. An implementation lock/lease identifies resource, holder, enforcing destination, release/expiry and failure rules. These meanings do not require another Review state or separate record type.

## 4. Canonical context fields

| Field or group | Type and rule |
| --- | --- |
| protocol_version; core_descriptor_sha256; schema_profile | Nonempty strings identifying the protocol version, the exact Core text (the digest of `RELEASE/Core_Descriptor.json`) and the serialization profile. |
| review_ref; session_ref; target_ref; charter_ref | Pinned references for active assessment. The canonical charter_ref uses kind policy and subtype CHARTER. A continuing mandate may have no active Session; no active-assessment authority is inferred from that absence. |
| whole_ref; selection; intended_extent | Exact whole/boundary and selection; TOTAL or PARTIAL. |
| claim_refs; scope_ref; criteria_ref | Nonempty mapped Claims and exact assessment scope/criteria. Each Claim relates to the Target or identified arm. |
| objective; opening_expectation_ref | Purpose and preserved opening expectations; NO_DIRECTIONAL_EXPECTATION is valid. |
| procedure_profile; required_gates | SCREENING, FOCUSED or FULL; unique ordered subset of G1-G6 containing G1, G5 and G6. FULL requires all six. |
| lifecycle; stage; passed_gates | Session lifecycle from the Specification; stage UNSTARTED or G1-G6; completed gates form an ordered prefix of required_gates with evidence. |
| control_revision; authority_term | Nonnegative revision and positive authority generation, integers excluding booleans, monotonic in the declared scope. |
| actor_ref; role_code; authority_ref | Actual participant, duty and current authority context. Role does not create permission. |
| governance_mode; participation_ref | HUMAN_DIRECTED, AUTOMATION_DIRECTED or JOINT_DIRECTED; planned/observed human participation and coverage. |
| parent_binding | ROOT with reason or exact Parent State Token and coordinating relationship. Peer/audit relations are separate. |
| task_ref; dependency_refs; budget_ref | Work, required/optional/context dependencies, resource units, reservations, reserves, deadline and residual liability. |
| method_config_ref; exposure_ref | Exact optional-method settings/activation and protected set, enforcement and known exposure. |
| blocked_actions; permitted_actions | Applicable acts under current policy and all necessary authority families. |
| observer_channel_mode | CLOSED, READ_ONLY or CONTRIBUTIONS_ENABLED with actual audience, intake cutoff and activated submission policy where needed. |
| closing_account_ref | NOT_CLOSED before closure; otherwise opening comparison, examined extent, evidence, cost, access, participation, deviations and remaining obligations. A parent's incomplete or aborted ending retains missing contributions, unfinished integration and child/resource liabilities without treating them as complete. |

Role codes are DIRECTOR, COORDINATOR, AUTHOR, CASE_DEVELOPER, CHALLENGER, SOURCE_REVIEWER, RESILIENCE_TESTER, INTERPRETER, CHECKER, ASSESSOR, COURIER, RECORDER, MONITOR and OBSERVER. Actor kind is HUMAN, AUTOMATED or UNKNOWN. Candidate exploration (M09) is recorded against AUTHOR.

Permission outcome is PERMIT, DENY or INDETERMINATE. It is separate from evidence disposition. Identity or authority required for an effect cannot be replaced with UNKNOWN. For other unknowns retain their cause and impact.

Optional M01-M11, WATCHED_INGESTION, AUTO_RECHECK, AUTO_REASSIGN, AUTO_PUBLISH, OBSERVER_SUBMISSION and DELIVERY_ENCRYPTION use OFF/ON with activation reference when ON. A pinned default policy resolves omitted optional settings to OFF. Unknown or empty values do not mean ON. Required controls have no disabling switch.

| Standing automation setting | Behavior governed |
| --- | --- |
| WATCHED_INGESTION | Retrieve newly detected inputs through a commissioned monitoring channel and apply its intake rules. Intake does not itself admit a finding. |
| AUTO_RECHECK | Dispatch rechecking in response to a declared event without a new task instruction. |
| AUTO_REASSIGN | Replace or redistribute assignments under declared scheduling conditions without a new task instruction. |
| AUTO_PUBLISH | Release an eligible exact output under a declared standing trigger and release rule without a new release instruction. |

These settings do not prohibit execution of steps and bounded retries already included in an authorized current assignment. A rule subscribed to future source, scheduling or release events remains standing behavior even when written in the current task; the same authorized instruction may supply its scoped activation. Ordinary conditional steps do not become a standing subscription merely because they react to their own results. Activation, current permission, release eligibility and actual runtime capability remain separate.

A Delegated Continuation setting selects no feature implicitly. Its execution-policy reference resolves the assignment, triggers, grants, bounds, checks, active settings, stop path, exception handling and runtime defined in core Section 12.2; existing records may supply them.

Where retries apply, that policy identifies their owner or equivalent shared limit, attempt/time/resource bounds, relevant recovery condition and handling of uncertain effects. A finding, permission outcome and work state remain separate. Exception handling does not create communication rights or release residual resource liability.

## 5. Interpretation, checking and admission

A meaning receipt binds source/version, reader, readback, assessor, method, outcome MATCH/MISMATCH/UNRESOLVED and limitations. A permitted same-actor assessment is labeled SELF_CHECK.

A verification record binds intended criterion, checked property, inputs/outputs, method/version/configuration, assumptions, coverage, execution status, actual result, diagnostics and assessment of applicability. Execution status is distinct from PASS/FAIL or another procedure-specific result.

An admission record binds the proposed result, original basis, receiving assessment basis, current authority, exact performed checks, unresolved dependencies and decision. Compatibility refers to an assessment linking original and current dependencies rather than a free-standing assertion.

A finding binds Claim, scope, Review/Session, rule, supporting evidence, checks, objections, limits, lifecycle and supersession. Evidence dispositions are SUPPORTED_IN_SCOPE, CONDITIONAL, REFUTED_IN_SCOPE, NOT_IDENTIFIED_IN_SCOPE, DISPUTED, UNRESOLVED and INCOMPARABLE. Evidence lifecycle ACTIVE/SUPERSEDED/WITHDRAWN and recheck status RECHECK_REQUIRED are separate. Where a Claim was narrowed, re-scoped or made conditional after evidence was in (Core Section 5.2), the finding for the substitute references the original Claim and that Claim's own disposition. A best estimate is recorded apart from the disposition, labelled as an estimate, with its basis. A record uses only the defined values for status codes and settings. A distinction that has no defined value is written in ordinary words; it is not coined as a code.

For a material absence claim, the existing source/coverage and finding fields identify what was inspected or otherwise established, any applicable requirement, and access or search limits. A correction links the prior assessment, changed basis and affected current views or consumers. Core Sections 4.3-4.4, 8.2 and 12.1 govern assessment, recovery and communication; no new record kind is required. Field presence, a valid schema or a digest does not establish that a reported act occurred.

## 6. Trial and release

A constructed trial resolves question, construction assumptions, exact inputs/procedure, assessment criterion, applicable controls, resource/stopping limits, execution record, actual results, deviations, failures and transfer scope. Resolve alternatives, selection/enumeration/sampling design, quantitative measures, reference sets, denominators, weighting and uncertainty as required by the trial's design or claims.

A release resolves actual result, coverage, evidence, limits, participation, current authority and audience. A local result may remain in the versioned task record. Where the chosen transfer profile uses a detached manifest, a transferred packet additionally resolves exact payload/dependency identities, sizes/digests, manifest and profile-required receipts. Distinguish required, optional and contextual dependencies.

A logical operation is a run subtype EFFECT_OPERATION; its immutable binding identifies receiver, action, approved content and effect context. Delivery-attempt and envelope/representation references are separate. Same-operation different-binding is rejected. Current request and disclosure authority still apply to retrieving a prior receipt.

## 7. Security and delivery mapping

A concrete delivery format maps the following meanings to exact authenticated inputs, authorized configuration or explicitly inapplicable values. It defines protected versus visible metadata and avoids circular digests.

| Group | Meaning |
| --- | --- |
| security_profile_ref | Exact path, policy, approving authority and revision. |
| protected_assets; threat_basis | Protected content/effects, considered adversaries/failures, trusted components, boundaries and exclusions. |
| recipient_binding; data_policy_ref | Audience/projection, disclosure and retention, plaintext processors and metadata exposure. |
| origin_authentication | Checked principal, mechanism, trust anchor/enrollment, intermediaries and producer mapping. |
| transport_binding | Actual endpoints, protection/termination, negotiated properties when relevant, or justified local inapplicability. |
| origin_basis; effect_contract; delivery_authorization | Immutable result provenance, approved logical effect and current delivery context; original parent basis remains intact. |
| logical_operation; representation_refs | Stable operation binding with separate attempt, envelope and plaintext/ciphertext artifacts. |
| protected_context | Relied-on principal, action, audience, Review/Session, basis/authority, payload and dependency bindings. |
| delivery_encryption | OFF/ON, activation/policy, concrete format/suite, implementation, keys and no-fallback rule. |
| key_policy_ref | Custody, enrollment/use, rotation/revocation, recovery, compromise and validation cutoff; references contain no secrets. |
| freshness_and_replay | Ordering domain, duplicate/conflict rule, expiry/clock, rollback floor, restoration and bounded offline authority. |
| input_policy_ref | Formats, field/numeric/size/nesting/path limits, processing boundary, network destinations and separate execution permission. |
| acceptance_record_ref | Applicable positive/negative checks, actual environment/cutoffs, failures, exclusions and unresolved requirements. |

Security check status is PASS, FAIL, NOT_CHECKED or justified NOT_APPLICABLE for a named check. Encryption activation, attempted execution and delivered representation are separately recorded.

## 8. Method and exercise mapping

A method activation binds card/version, purpose, task/Session, inputs/parameters, applicable authority, interactions, resources, stop rule, exposure and assessing actor. Deactivation resolves in-flight work.

A Resilience Exercise is a run subtype RESILIENCE_EXERCISE under M10. Its record resolves purpose; environment/assets/owners; isolated/live authorization; allowed effects; actual controller and adversary privileges; observer and role overlap; sampling; resource and stop bounds; provenance/reveal; execution observations; and closure.

Exercise phases are PLANNED, ARMED, RUNNING, STOPPING and CLOSED under the catalog transition guards. Separately record stop-requested, dispatch-blocked, effect-fenced, execution-stopped and recovery-verified values for affected destinations.

Closure is COMPLETE, INCOMPLETE or ABORTED with restoration evidence and residual obligations. Before closure use NOT_CLOSED. A planned but unexecuted case is NOT_RUN; an unobserved outcome is UNKNOWN. Stop/recovery has its own bounded mandate and does not restore injection permission.
