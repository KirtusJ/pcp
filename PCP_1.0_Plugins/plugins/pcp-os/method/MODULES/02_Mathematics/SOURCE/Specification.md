# Adversarial Claim Review

# Mathematics Specification - Version 1.0

**Packet:** ACR Version 1.0, Implementation  
**Component:** `acr.mathematics`, Version 1.0  
**Required core:** `acr.core`, Version 1.0; Core descriptor SHA-256 `f15686b385002bf597c2625bc18e98a390531a21ce91f64bdb249f2fe04a86a7`  
**Creator:** Kirtus Justus  
**Date:** 11 November 2026, America/Vancouver

ACR Mathematics coordinates scoped mathematical exploration, construction, proof, computation and review. It applies across pure and applied mathematics, including discrete and continuous subjects. Mathematical methods and substantive judgment remain the team's responsibility.

This Markdown Specification is the normative module text; its PDF is the reading copy. Sections 1-9 are normative except labeled examples. Appendices A-C are informative terminology, cautions and sources. Capitalized requirement words have the governing Core's BCP 14 meanings. These are ACR coordination requirements; cited practices do not impose a universal research or publication procedure.

## 1. Scope and economical adoption

Apply this module when selected for an authorized mathematical assignment. Ordinary mathematical work remains the default. When a consequential statement, proof dependency, computation, interpretation or handoff needs structured checking, start with FOCUSED unless the mandate calls for another profile. Reuse adequate existing review. Neither routine calculation nor every lemma requires a Review.

The exact Core and applicable module requirements MUST be available for the assigned act. Module receipt supplies reference material, not a target or authority. The Core supplies onboarding, direction, permissions, assessment, delivery and change control; this module creates none of them again.

An assignment MAY pursue understanding, definitions, conjectures, examples, algorithms, proofs, bounds or revisions. It need not begin with a proved result. The target and useful next deliverable MUST nevertheless be clear. Existing notes, manuscripts, repositories, notebooks and proof projects SHOULD carry the evidence without parallel paperwork.

Ordinary authorized induction, contradiction, construction and conjecture exploration remain available without activating Core specialist methods M03 or M09. Their OFF settings do not ban mathematical practice or required checking.

Mathematical obligations can be selected alongside Science, Engineering or Cryptography for the same work. Selection preserves the existing assignment and any commissioned Review. This module is not a blanket dependency of those modules and does not supply empirical, safety or cryptographic deployment evidence.

## 2. Statement and mathematical basis

The assignment MUST identify the statement, construction, calculation or decision and its assessed revision. The question MUST distinguish what is being asked: for example, proving a universal statement, finding a witness, testing a conjecture, computing a bound or comparing methods. In commissioned Review work these are the Target and Claim; ordinary assignments need no Review records.

Preserve the material mathematical signature in the existing working basis; a Review may use its Basis Header:

| When material | Meaning to preserve |
| --- | --- |
| Objects and definitions | Domain, ambient structure, types, notation, exact definitions and referenced versions. |
| Logical scope | Quantifiers and their order; hypotheses; conclusion; existence or uniqueness obligations. |
| Boundary conditions | Parameter ranges, exclusions, endpoint conventions, regularity and admissibility conditions. |
| Quantitative conventions | Norms, scaling, units when applicable, error criterion, limits and approximation regime. |
| Dependencies | Results and assumptions actually used, their scope, unresolved steps and interpretation changes. |

Include only what the next dependent act needs, with resolvable references for detail. A digest or matching text does not establish mathematical equivalence, applicability or completeness. Material changes in definitions, domain or quantifiers require impact assessment under the Core.

A cited result MUST be checked against the statement and hypotheses actually needed. Distinguish a theorem in the source, a conjecture, an announced result, an informal explanation and a later correction. Novelty claims MUST retain search scope and date, and acknowledge relevant prior contributions [Q01].

## 3. Exploration, construction and revision

Authorized exploration MAY use heuristic reasoning, diagrams, analogies, examples, computation, conjectured lemmas and alternative definitions. Identify their evidential role. A conjecture can guide work without being accepted as a theorem. Experimental mathematics uses computation for insight, conjecture testing and proof development [Q03]; mathematical understanding is also a substantive outcome [Q04].

State what would change the next decision and use the existing resource and stopping limits. A useful result can be a failed approach, discriminating example, repaired statement or clearer obstruction. Do not require speculative work to meet the eventual proof obligation before it can be investigated.

When revising a candidate or conjecture, retain the earlier statement and relevant adverse findings. A counterexample may motivate a narrower result; it MUST NOT disappear through silent restatement of the original claim. Local iterations within the mandate need no new Review. Reassess affected dependencies and reuse unaffected work.

Comparative claims MUST identify the comparator and material conditions: mathematical problem, assumptions, accuracy or correctness criterion, instance family, resources and implementation where relevant. Complexity, measured running time, practical usefulness and explanatory value are different claims. A selected set of favorable examples does not establish unrestricted superiority.

## 4. Proof review and adverse cases

A claimed proof MUST support its exact conclusion under its stated hypotheses. Preserve the argument, substantive dependencies and unresolved obligations. Review the steps capable of changing the conclusion, including case coverage, admissibility, circular dependence and any unjustified change of representation or limiting operation. A published reference or familiar technique is not a substitute for a missing applicability argument.

A proof outline or assumed lemma MAY guide further work but MUST NOT be reported as a completed proof when its unresolved step is essential. An invalid derivation defeats that support path; it does not by itself prove the conclusion false. An objection may identify a missing argument without constructing a rival theory or executable witness.

A counterexample MUST satisfy the original hypotheses and defeat the stated conclusion. Verify that it lies in the relevant domain and uses the required conventions. A changed hypothesis or excluded boundary point can expose a different problem without refuting the original theorem. A reductio MUST identify the added supposition and establish the contradiction without silently importing an incompatible extra premise.

Core requirements for executed mechanical checks apply when the decisive obligation has a suitable available and authorized checker. Mathematical review need not be replaced by universal formalization. Choose evidence appropriate to the claim; neither agreement among participants nor a generated derivation substitutes for that evidence.

## 5. Formal proofs and trusted computation

A formal-proof claim MUST identify the exact formal statement, proof artifact, definitions and dependencies, checker/version/configuration and actual outcome. Assess correspondence with the intended statement, including coercions, overloaded notation and domain restrictions. Checking a formal expression and checking its intended meaning are distinct obligations [Q05].

Resolve the axioms, admitted results, external computations and other trusted components material to the claimed assurance. A successful build MUST NOT conceal an incomplete dependency, an unexpected axiom or a weakened theorem. Proof-assistant checks operate within their logic and trust boundaries; for example, Lean documents axiom inspection and the additional trust introduced by native evaluation [Q05-Q06]. Use tool-specific validation appropriate to the actual risk and required assurance, rather than imposing one checker on every assignment.

Exploratory axioms MAY be used explicitly. Declared foundations and hypotheses specify the mathematical question; they are not empirical claims that must be re-established for every theorem. Known inconsistency, unintended axioms or a claim extending beyond those foundations MUST be reported where material. A derivation from contradictory hypotheses does not establish existence of an object satisfying them.

For a generated certificate, distinguish generation from checking. Record what the checker establishes and how the certificate connects to the claim. A failed search or rejected certificate need not show that no valid certificate exists. Treat proof projects and their build steps as executable artifacts under Core handling rules; a proof-looking file does not confer execution permission.

## 6. Computation and numerical assurance

Computational evidence MUST identify the input interpretation, method, exact artifacts and relevant execution conditions. Preserve actual outputs, unsuccessful cases and coverage. Reproducibility allows an execution to be examined; it does not independently establish its correctness. LMS publication policy provides an example of explicit computational roles and inspectable supporting code [Q02].

| Evidence used | Additional obligation when decisive |
| --- | --- |
| Exact arithmetic or symbolic transformation | Preserve the domain and side conditions; justify the identity, algorithm or certificate used. Exact arithmetic does not validate an incorrect argument. |
| Exhaustive finite verification | Establish coverage of every required case or a justified reduction; account for exclusions and checker behavior. |
| Approximate computation | State precision, stopping and error criteria; distinguish numerical agreement from a proved bound. |
| Certified enclosure | Establish input containment, applicable operations and rounding/error guarantees; propagate the relevant error sources. |
| Sampled or randomized investigation | State generation, sampling, stopping and coverage; attach a probabilistic guarantee only when its assumptions and derivation support it. |

Preserve indeterminate results. A symbolic query that returns unknown, an unfinished search or a numerical enclosure crossing a decision boundary MUST NOT be converted into a decisive positive or negative conclusion without the evidence that conclusion requires. Symbolic simplification depends on assumptions; SymPy's documentation explicitly distinguishes unresolved predicates from false ones [Q10].

Correct rounding of an operation is not a bound on every later conclusion. MPFR specifies operation-level rounding; interval and ball methods propagate enclosures [Q07-Q08]. Establish the required input, truncation, discretization and accumulation bounds when they matter. More precision can reduce arithmetic error without resolving uncertain inputs or an inappropriate approximation. A library's supported functions and actual version matter; mpmath distinguishes ordinary and interval contexts and documents interval-support limitations [Q09].

Existence, uniqueness, conditioning and algorithmic stability MUST remain distinguishable. A unique solution can be highly sensitive to small input changes. A small residual or backward error needs appropriate conditioning information before supporting a forward-error claim [Q12]. A computed estimate of a bound MUST NOT be represented as a certified enclosure without justification.

## 7. Findings, foundations and applications

Use Core dispositions for commissioned Review findings. Ordinary results need no ACR status vocabulary; any chosen canonical disposition retains its meaning and evidential guards for the precise question. Descriptions such as conjecture, theorem, counterexample and numerical observation describe mathematical content; they do not replace a selected disposition.

A proved statement of the form "for every admissible object, H implies C" MAY be SUPPORTED_IN_SCOPE as that implication. Its hypotheses are part of the statement. Applying it to a particular object requires evidence that the object satisfies H. If an acceptance-critical application premise remains assumed, that application retains CONDITIONAL or UNRESOLVED treatment under the Core. Do not downgrade every theorem merely because its statement has hypotheses, or promote the theorem into an unconditional application result.

Separate failure to find a proof, a proved negation, algorithmic undecidability and independence relative to an axiom system. A claim of undecidability or independence needs its own exact problem or statement, formal system, metatheoretic argument and any consistency assumptions. Failure to find a proof alone establishes none of those conclusions. A justified complete decision procedure or finite reduction may establish the relevant claim; a defined class in which no solution exists requires a corresponding impossibility argument or complete applicable verification.

NOT_IDENTIFIED_IN_SCOPE applies only when its Core criterion is met by a checked ambiguity or non-uniqueness result for the stated inferential task. It is not a synonym for an unproved conjecture, an undecidable statement or failure to discover a discriminator.

For an application, identify the map between mathematical objects and the claimed external quantities, evidence for required premises and limits of the transfer. A correct theorem does not itself establish calibration, measurement, physical suitability or operational authority. Select the applicable companion obligations when those matters enter the assignment; bounded mathematical work can proceed while the application remains unresolved.

## 8. Delivery, correction and reuse

Deliver the exact assessed statement or construction, sufficient supporting argument or artifacts, actual checks, material assumptions and remaining limitations. Reference existing supporting work. Distinguish a checked theorem, an application assessment and a proposed next step. The packet SHOULD let a receiving worker locate the decisive evidence without reconstructing the entire conversation. Distinguish an inspected mathematical gap from an inability to retrieve or inspect its evidence under Core Section 4.3; the latter does not by itself establish that an argument is absent or invalid.

Bind computational and formal results to their actual inputs, source and relevant dependencies. Changes in a theorem statement, definition, library, encoding or numerical procedure require reassessment of affected claims. A matching identifier cannot repair a changed meaning. Preserve adverse results and corrections under Core revision rules.

Publication and external disclosure follow their actual authority and venue requirements. Resolve attribution, confidentiality, coauthor responsibilities, required disclosure of automated assistance and applicable competing-interest or recusal rules for publication and review. Apply the venue's participation and recusal rules; resolve uncertainty with its responsible authority. Technical separation and disclosure alone do not establish eligibility. EMS guidance addresses these obligations and timely correction of erroneous work [Q01]. An ACR role does not authorize uploading a confidential manuscript or certify its mathematical correctness.

## 9. Customization and evaluation

Teams MAY use local terminology, specialist methods and established tooling while preserving applicable Core and module meanings. No particular proof assistant, programming language, notebook, database or representation is mandatory merely through adoption. Missing decisive evidence remains missing when a local template omits its field.

Evaluate the smallest intervention against competent ordinary mathematical work at comparable total cost and access. Assess correct progress, material defects, false objections, reproducibility, useful revisions and coordination overhead. Do not score conjecture volume, participant agreement or record count as mathematical achievement. The constructed examples in the Overview illustrate specific distinctions; they do not establish that ACR improves research.

## Appendix A. Working glossary

| Term | Meaning here |
| --- | --- |
| Mathematical signature | Material definitions, objects, logical scope and conventions needed to interpret a task. |
| Conjecture | A proposed mathematical statement whose proof is not established in the stated account. |
| Hypothesis | An explicit condition within a theorem or argument; distinct from evidence that it holds in an application. |
| Proof obligation | A proposition or justification needed by the particular argument being assessed. |
| Formalization | An explicit representation in a formal system, with a correspondence to the intended mathematical content. |
| Trusted computing base | Components whose correct behavior the specified assurance relies on. |
| Certificate | An artifact checked against a stated verification rule; its meaning depends on that rule and the claim binding. |
| Certified enclosure | A set proved to contain the claimed value under specified input and computational conditions. |
| Conditioning | Sensitivity of the mathematical answer to changes in the input, under stated scales and norms. |
| Algorithmic stability | How an algorithm's error relates to the mathematical problem and its perturbations. |
| Relative independence | Neither a statement nor its negation is derivable in the specified formal theory, under the stated metatheoretic assumptions. |

## Appendix B. Cautions and reading discipline

| Code | Caution |
| --- | --- |
| MA01 | Agreement, fluent explanations and intact records do not establish a proof. |
| MA02 | Changing a domain, quantifier, definition or convention can change the problem. |
| MA03 | A verified implication does not establish its hypotheses for an external application. |
| MA04 | A formal check retains statement, axiom and trusted-component boundaries. |
| MA05 | Exact arithmetic, high precision and certified enclosure are different assurances. |
| MA06 | A passed finite prefix alone does not establish a universal positive claim. A valid counterexample can refute it; a justified complete reduction can prove it. |
| MA07 | An impossible or contradictory premise can make an implication vacuous; existence is separate. |
| MA08 | Extra review can consume the resources needed for mathematical progress. Use existing adequate evidence. |

Read the assignment and relevant Core obligations, then this module's applicable clauses and the substantive mathematics. Preserve material constraints during handoffs. Role names describe duties held by fallible participants; they are not mathematical credentials or an invitation to roleplay.

## Appendix C. Primary sources

Source identifiers are local to this module. Sources were checked on 10 November 2026; software documentation remains version-dependent. References ground mathematical practice and tool boundaries, not ACR's effectiveness.

**Q01. European Mathematical Society.** Code of Practice for Mathematical Publication, approved 19 March 2025. [Source](https://euromathsoc.org/code-of-practice).

**Q02. London Mathematical Society.** Computer Aided Proofs, updated November 2024. [Source](https://www.lms.ac.uk/publications/policies/computeraidedproofs).

**Q03. Bailey and Borwein.** Experimental Mathematics in the Society of the Future, 2016; author-hosted manuscript. [Source](https://www.davidhbailey.com/dhbpapers/expmath-society.pdf).

**Q04. Thurston.** On proof and progress in mathematics, 1994. [Source](https://arxiv.org/abs/math/9404236).

**Q05. Lean project.** Validating a Lean Proof; official evolving documentation. [Source](https://lean-lang.org/doc/reference/latest/ValidatingProofs/).

**Q06. Lean project.** Axioms; official evolving documentation. [Source](https://lean-lang.org/doc/reference/latest/Axioms/).

**Q07. MPFR project.** GNU MPFR 4.2.2 manual; specified arithmetic and rounding semantics. [Source](https://www.mpfr.org/mpfr-current/mpfr.html).

**Q08. Johansson.** Arb: Efficient Arbitrary-Precision Midpoint-Radius Interval Arithmetic, 2017; author preprint 2016. [Source](https://arxiv.org/abs/1611.02831).

**Q09. mpmath project.** Contexts, version 1.3.0 documentation; arithmetic modes and interval-support limitations. [Source](https://www.mpmath.org/doc/current/contexts.html).

**Q10. SymPy project.** Assumptions, version 1.14.0 documentation. [Source](https://docs.sympy.org/latest/guides/assumptions.html).

**Q11. Hales and colleagues.** A formal proof of the Kepler conjecture, 2017; author preprint 2015. [Source](https://arxiv.org/abs/1501.02155).

**Q12. LAPACK project.** Users' Guide, Standard Error Analysis; conditioning and backward error. [Source](https://netlib.org/lapack/lug/node78.html).
