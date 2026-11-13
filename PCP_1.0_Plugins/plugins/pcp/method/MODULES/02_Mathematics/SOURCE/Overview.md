# Adversarial Claim Review

# Mathematics Overview - Version 1.0

**Packet:** ACR Version 1.0, Implementation  
**Component:** `acr.mathematics`, Version 1.0  
**Required core:** `acr.core`, Version 1.0; Core descriptor SHA-256 `f15686b385002bf597c2625bc18e98a390531a21ce91f64bdb249f2fe04a86a7`  
**Creator:** Kirtus Justus  
**Date:** 11 November 2026, America/Vancouver

This guide explains how to use ACR Mathematics for exploration, construction and assessment. The Mathematics Specification defines its requirements; the pinned Core governs the assignment, permissions, findings and delivery. Q-prefixed citations resolve to the module's source register and the Specification's reference appendix. The examples below are instructional mathematical constructions, not a study of ACR's effectiveness.

## 1. Begin with the mathematical work

A mathematician wants to explore a pattern. A collaborator needs a lemma whose assumptions differ slightly from those in a manuscript. A team has a numerical bound but cannot tell whether rounding could reverse the final inequality. These are different tasks. Each needs a clear question and suitable evidence; none automatically needs a large review procedure.

Ordinary competent mathematical work is the default. Use ACR where a statement, dependency, computation or handoff needs coordination that the existing process is not supplying. A focused check can fit into one research note or repository issue. It needs no permanent database, extra staff or transcription of the entire argument into administrative records.

| Immediate goal | Useful output | Additional work before a stronger claim |
| --- | --- | --- |
| Explore a conjecture | Examples, patterns, failed approaches and a sharper question. | A proof or admissible counterexample for the chosen statement. |
| Construct an object or method | Exact definition, intended properties and checked cases. | Evidence for each claimed property and comparison. |
| Review a proof | Checked statement, dependencies, decisive steps and remaining gaps. | Resolution of essential gaps before claiming a completed proof. |
| Obtain a numerical bound | A calculation with a stated error treatment. | Justification that the required value is enclosed tightly enough. |
| Apply a theorem | Mapping of its hypotheses to the proposed object or situation. | Evidence for application premises and any external interpretation. |

Computation can generate insight and suggest proof strategies before a proof exists [Q03]. Understanding why a definition or argument works is also useful mathematical progress [Q04]. ACR should preserve that freedom while keeping the resulting claims accurate.

## 2. Receive the packet and identify the assignment

Receiving this guide does not invent a problem or start a Review. Use the actual instruction and the governing Core. If the target and limits are already clear, work from them. If a necessary statement or input is missing, identify that dependency while continuing useful authorized preparation.

The team can ask for exploration rather than proof. For example: "Investigate whether this proposed bound survives its endpoint cases; return a counterexample, a justified repair, or the remaining obstacle within the assigned budget." That is a specific deliverable even when the eventual theorem is unknown.

Use the mathematical content that matters now: statement, domain, hypotheses, definitions, convention-sensitive quantities and unresolved dependencies. A summary can point to a long proof instead of reproducing it. Before a dependent step, the worker must inspect the needed material. A hash does not communicate the meaning of an unread definition.

A resumed session recovers the current assignment and affected basis. It does not restart the proof from a new memory of the problem, erase exposure to earlier answers or replace the parent's conditions. Ordinary induction, proof by contradiction, construction and conjecture exploration remain available under the assignment; specialist toggles being OFF do not prohibit those methods.

Mathematics may be selected alongside Science, Engineering or Cryptography for shared work. The same result can need a mathematical proof, an empirical premise check and a deployment decision. Those are complementary obligations under one governing assignment, not an invitation to create competing Directors or automatic module dependencies.

## 3. Follow a conjecture through failure and repair

Consider the polynomial `p(n) = n^2 + n + 41`. An exploratory calculation finds prime values for every integer from 0 through 39. The researcher proposes that every nonnegative integer gives a prime.

### Keep the observation and conjecture separate

The observed finite statement concerns 40 inputs. The conjecture concerns infinitely many. The fact that the calculation used exact integers does not turn the finite observation into an unrestricted proof. Exactness answers how the tested values were computed, not whether every required case was covered.

Checking those 40 values exactly and then examining `n = 40` gives `1681 = 41^2`, which is composite. This is an admissible counterexample to the stated universal conjecture. It does not invalidate the correctly checked finite statement.

### Make the failure useful

The original universal statement retains its adverse finding. The team may investigate why the initial range behaves as it does, test a revised statement or use a different construction. It need not defend the conjecture because it generated it, or open a new Review for every local iteration.

The revised goal might be finite: verify the proposed range and explain its boundary. It might be theoretical: derive conditions under which a related expression is composite. Those are new or refined mathematical questions. They should be labeled as such rather than presented as if the original universal conjecture survived.

### Deliver the part that was established

A concise delivery identifies the exact polynomial, integer domain, tested range, checking method and counterexample. It separates the finite result from the refuted extrapolation and gives the next authorized step. A failed conjecture can improve the research direction without producing a new theorem.

The same discipline applies to graphs, sequences, geometric constructions and numerical experiments. A picture, search or sample can guide discovery. A universal conclusion requires the appropriate argument or a complete justified reduction. Conversely, a complete finite argument can prove a genuinely finite claim; finite computation is not automatically weaker than prose.

## 4. Preserve the question across people and tools

### Quantifier order changes the task

Let the domain be the three numbers `{-1, 0, 1}`. The statement "for each x there is a y with x + y = 0" is true: choose `y = -x`. The statement "there is one y that works for every x" is false. The same symbols appear in both, but the permitted dependence of y on x has changed.

Both finite statements can be checked by enumeration over the three values. This is why a handoff must preserve quantifiers, not merely a list of variable names. Similar care is needed for a uniform bound versus a separate bound for each instance, or an existence result versus a method that finds an object under specified resource limits.

Definitions and domains matter just as much. With ordinary partial rational division, `(x^2 - 1)/(x - 1)` is undefined at `x = 1`; simplifying it to `x + 1` does not make the original expression defined there. A formal system may use a different totalized operation. The encoding and the intended mathematics must be reconciled explicitly.

### A theorem and its use are separate claims

Suppose the premises are `x + y = 3` and `x - y = 1`. Adding half of each equation gives `x = 2`. This small rational linear-combination certificate can be checked exactly; so can the facts that `(x,y) = (2,1)` satisfies the premises, while `(3,0)` violates one premise and the conclusion.

The implication remains valid. Its use at `(3,0)` fails. A Review can support the implication as the theorem it actually proves while refusing the unsupported application. Mathematical hypotheses do not need to be empirically proved for every theorem; evidence that a particular application satisfies them is a different obligation.

There is another separation: from the incompatible premises `x = 0` and `x = 1`, subtraction yields `0 = 1`. A checker can verify that derivation without establishing that any x satisfies both premises. The task must say whether it asks for an implication, existence, or both. The supplied certificate is an elementary finite checker example, not a proof-assistant kernel verification.

### What an unsuccessful search means

If a search finds no proof, report its actual limits. Failure to find a proof alone does not show that the statement is false, independent of a chosen axiom system or part of an algorithmically undecidable problem. Those are separate mathematical claims requiring their own arguments. A justified complete decision procedure or finite reduction can support a decisive result; an unsuccessful bounded search without such justification cannot.

Core NOT_IDENTIFIED_IN_SCOPE is reserved for its stated criterion, such as a checked non-uniqueness result for an inferential question. It is not a general label for difficult mathematics. A budget-exhausted investigation may simply leave the mathematical question unresolved.

## 5. Choose the computational assurance the conclusion needs

An exact integer calculation, a symbolic identity, a decimal approximation and a rigorous enclosure provide different kinds of evidence. Select the relevant method rather than choosing a tool name and assuming that every output has the same assurance.

Symbolic systems also track assumptions. For example, a simplification valid for a positive real variable may not be valid for an arbitrary complex variable. SymPy documents both assumption-dependent simplification and predicates that remain undecided [Q10]. Preserve such results instead of treating an unknown answer as true or false.

### Decimal agreement is not an enclosure

Compare two exact rational numbers, `1.41423999` and `1.41424001`. Both display as `1.4142` when rounded to four decimal places, yet they lie on opposite sides of the threshold `1.41424`. The display alone cannot decide the comparison.

The same construction gives a rational bracket for the positive square root of 2: `[1.414213, 1.414214]`. Exact squaring verifies that the lower endpoint is below the root and the upper endpoint above it. Because the whole bracket is below `1.41424`, it settles that strict comparison.

A coarser enclosing interval, `[1.4142, 1.4143]`, crosses the threshold. Its midpoint, `1.41425`, is above the threshold even though the root is below it. This is an inconclusive enclosure with a misleading midpoint, not evidence that the root is above the threshold. The positive control is the narrower bracket that actually resolves the question.

Correctly rounded arithmetic such as MPFR and enclosure methods such as Arb have different contracts [Q07-Q08]. Their assurance depends on the operations, input interpretation and error treatment actually used. Merely importing mpmath does not select interval arithmetic; its documentation distinguishes contexts and warns about incomplete interval support [Q09]. The rational example above executes none of these external libraries.

### Uniqueness does not guarantee numerical robustness

Consider a diagonal linear map with diagonal entries 1 and a positive parameter `epsilon`. It is invertible for every tested positive value. An error in the second output is nevertheless amplified by `1/epsilon` during inversion.

At `epsilon = 1/1000000`, a residual of `1/1000000` can accompany a solution error of 1 in the constructed case. Exact invertibility and a small residual are therefore insufficient for the stronger accuracy claim. The LAPACK guide distinguishes conditioning from backward error and explains their role in estimating forward error [Q12]. The fixture is an exact rational demonstration; it does not test LAPACK or estimate the performance of a numerical algorithm.

Arithmetic error is only one possible limitation. Truncation, discretization, input uncertainty and an inappropriate mathematical representation can remain after increasing precision. A useful finding identifies which source of error it controls and which it does not.

## 6. Use formal proofs without losing their meaning

A proof assistant checks an explicit formal statement using a particular logic, definitions, dependencies and trusted implementation. That can provide strong evidence. The formal proof of the Kepler conjecture is a substantive example using HOL Light and Isabelle [Q11]. It is not evidence that every other proof project, translation or tool run is correct.

Before relying on a formal result, identify the statement actually checked. A proof of a weaker bound, an altered definition or a theorem over an unintended domain does not settle the requested statement. Review that correspondence separately from successful execution.

Lean's official validation guidance describes different checks for a proof and its dependencies, and distinguishes validity of the formal theorem from its intended meaning [Q05]. Its axiom documentation explains that added axioms and native computation change what is being trusted [Q06]. Use the checks appropriate to the actual tool version, imports and assurance need. The module does not require one prover or a full formalization of every argument.

This matters for automated assistance. Generated proof text can suggest a route, while a reported successful build still needs an actual inspected execution. A proof project can also run code during loading or building. The Core's authorized artifact-handling rules continue to apply. Role names and a second assistant repeating the argument confer no additional mathematical guarantee.

Current practical challenges include maintaining large dependency chains, aligning informal and formal statements, preserving computational evidence and distinguishing numerical evidence from certification. These are places to test whether a small ACR intervention helps. They are not reasons to replace competent mathematical practice with a universal workflow.

## 7. Finish, hand over and revise efficiently

The receiver should be able to answer: What was asked? Which statement and definitions were used? What was actually established? Where is the decisive argument or execution? What remains open, and what can happen next?

For a short proof, the delivery may be the proof and a few lines of context. For a large computation, it may point to a versioned repository, exact inputs, a compact certificate and a checked result. The LMS computer-aided-proof policy illustrates the importance of exposing a calculation's role and making its supporting artifacts inspectable [Q02]. The actual team and venue determine applicable disclosure requirements.

Preserve a corrected or withdrawn argument and its effects on dependent claims. Reuse evidence that remains applicable. A notation change may be harmless; a hidden change of domain may require rechecking several results. Version control preserves revisions, while substantive review determines which conclusions survive them.

Attribution and responsibility remain with the people responsible for the work. The EMS Code addresses originality, credit, corrections, confidentiality and disclosure of automated assistance [Q01]. A Review receipt is neither authorship consent nor permission to upload a confidential manuscript to another service.

## 8. Evaluate the intervention, including reasons to stop using it

The five constructions in this guide show five exact distinctions. They do not test a proof-assistant kernel, a symbolic algebra system, interval software or a deployed ACR runtime. Nor do they show that a research team makes better decisions after adopting the module. Their purpose is to make the claim boundaries inspectable.

For a useful pilot, compare ordinary competent mathematical work with the same work plus a targeted intervention. Keep the task, expertise, evidence access and total resources comparable. Count preparation, communication, tool execution, checking, integration and correction time. Assess progress appropriate to the assignment: a justified theorem, informative counterexample, well-defined obstruction, useful construction or reliable computational result.

A review that generates many objections can be harmful if they are irrelevant, repeat known limits or prevent authorized exploration. Measure false objections and unnecessary delay as well as discovered defects. Preserve cases where the ordinary workflow is faster or sufficient. Where independent correctness cannot be established, report that limitation rather than using agreement as the score.

Start with one actual friction point and reuse existing mathematical records. Retain added process when it addresses that problem; simplify or discontinue it when it consumes effort without useful protection or progress.
