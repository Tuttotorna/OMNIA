# Projection Fidelity: A Decision-Validity Criterion for Projections

## Abstract

This note states the operational core of OMNIA in its shortest defensible form.

A projection is valid only for the decisions it preserves.

The point is not that every projection is false.

The point is stricter:

a projection becomes invalid when it is used for a decision whose required distinctions it does not preserve.

This gives a decision-validity criterion for aggregates, benchmarks, KPIs, models, representations, classifications, frames, scores, and visible outputs.

The theorem does not depend on the examples.

The examples only show where the theorem becomes visible.

Reference field:

https://github.com/Tuttotorna/OMNIA

Law of Totality:

https://github.com/Tuttotorna/LAW-OF-TOTALITY

DOI:

https://doi.org/10.5281/zenodo.20700914

---

## 1. The Absolute Constraint

Let Omega_infinity denote the total field as primary.

Every finite form x_f appearing within the total field satisfies:

for every x_f in Omega_infinity:

x_f is not equal to Omega_infinity

and

x_f is not independent from Omega_infinity.

In symbolic form:

forall x_f in Omega_infinity:

(x_f != Omega_infinity) and not (x_f independent from Omega_infinity)

A finite form is not false because it is finite.

A finite form becomes structurally false when it is treated as autonomous, complete, or total.

This is the absolute constraint.

It does not yet solve a decision.

It prevents a finite form from claiming totality.

---

## 2. The Operational Problem

Real decisions are not made on Omega_infinity directly.

They are made on accessible fields, projections, measurements, scores, aggregates, maps, models, representations, frames, and classifications.

Therefore the practical question is not:

Is the projection complete?

No finite projection is complete.

The practical question is:

Does the projection preserve the decision being made from it?

This is the operational core.

---

## 3. Definitions

Let Omega be the accessible field, generative structure, or full model available at the level of analysis.

Let P be a projected space.

Let pi: Omega -> P be a projection, reduction, metric, benchmark, aggregation, measurement, model, representation, frame, score, visible output, or classification.

Let A be the decision space, answer space, classification space, or judgement space.

Let D: Omega -> A be the decision, inference, classification, property, or judgement required on the accessible field.

The question is:

Can D be validly determined from pi alone?

---

## 4. Projection Fidelity Condition

The projection pi is faithful with respect to D if and only if there exists a function:

d: P -> A

such that:

D = d composed with pi

Equivalently:

D(omega) = d(pi(omega))

for every omega in Omega.

In words:

the decision must factor through the projection.

If D factors through pi, the projection preserves the decision.

If D does not factor through pi, the projection does not preserve the decision.

---

## 5. Equivalent Fibre Condition

The factorization condition is equivalent to:

for every omega1, omega2 in Omega:

if pi(omega1) = pi(omega2), then D(omega1) = D(omega2).

In symbols:

pi(omega1) = pi(omega2) implies D(omega1) = D(omega2)

This is the decisive test.

If two states become identical under the projection but require different decisions, then the projection cannot support that decision.

---

## 6. Failure Condition

Projection failure occurs when there exist omega1 and omega2 in Omega such that:

pi(omega1) = pi(omega2)

and

D(omega1) != D(omega2)

In that case, the projection collapses states that the decision must keep distinct.

Therefore no decision based only on pi can be valid for D over Omega.

The conclusion is not weak.

It is not a matter of style.

It is not merely that context is missing.

The decision cannot be founded on that object.

---

## 7. Theorem

A projection is decision-valid if and only if the required decision factors through the projection.

Equivalently:

A projection is valid only for the decisions it preserves.

---

## 8. Proof

Assume that D factors through pi.

Then there exists d: P -> A such that:

D = d composed with pi.

Let omega1 and omega2 be elements of Omega such that:

pi(omega1) = pi(omega2).

Then:

D(omega1) = d(pi(omega1))

and:

D(omega2) = d(pi(omega2)).

Since pi(omega1) = pi(omega2), it follows that:

d(pi(omega1)) = d(pi(omega2)).

Therefore:

D(omega1) = D(omega2).

So every pair of full states collapsed by pi has the same decision value under D.

Now assume the converse:

for all omega1 and omega2 in Omega,

pi(omega1) = pi(omega2) implies D(omega1) = D(omega2).

Define d on the image of pi by:

d(p) = D(omega)

for any omega such that pi(omega) = p.

This definition is well-defined because if two possible choices omega1 and omega2 have the same projection p, then D(omega1) = D(omega2).

Therefore d exists and:

D(omega) = d(pi(omega))

for every omega in Omega.

Thus D factors through pi.

This proves the theorem.

---

## 9. What This Does Not Claim

This does not claim that every projection is invalid.

This does not claim that every finite model is false.

This does not claim that every incomplete representation is useless.

This does not claim to produce missing data.

This does not claim to solve every problem automatically.

The theorem only states the validity condition:

a projection can support only the decisions it preserves.

Outside that preserved domain, the projection is the wrong object for the decision.

---

## 10. What This Does Claim

If a decision D does not factor through a projection pi, then D cannot be validly founded on pi alone.

If a benchmark score does not preserve the deployment decision, then the benchmark score cannot found that decision.

If an aggregate does not preserve the treatment or rollout decision, then the aggregate cannot found that decision.

If a KPI does not preserve the system distinctions relevant to action, then the KPI cannot found that action.

If a representation does not preserve the property being asserted, then the representation cannot found that assertion.

If words do not preserve the originating frame, then word preservation cannot found frame fidelity.

This is not interpretation.

This is the consequence of non-factorization.

---

## 11. Decision Error Function

Define:

E_D(Omega, pi) = 1

if and only if there exist omega1 and omega2 in Omega such that:

pi(omega1) = pi(omega2)

and

D(omega1) != D(omega2).

Otherwise:

E_D(Omega, pi) = 0.

So:

E_D(Omega, pi) = 1

means the projection is not decision-faithful.

E_D(Omega, pi) = 0

means the projection preserves the decision.

---

## 12. Public Translation

The public sentence is:

Correct answers to the wrong object are not solutions.

The mathematical sentence is:

D must factor through pi.

If D does not factor through pi, the answer may be correct inside the projection, but the projection is not faithful to the decision.

---

## 13. Examples

### 13.1 Aggregates

Omega = conditioned or stratified structure.

pi(Omega) = aggregate.

D = treatment decision, rollout decision, or causal judgement.

If two different conditioned structures collapse into the same or misleading aggregate while requiring different decisions, then D does not factor through pi.

Therefore the aggregate is not the decision object.

### 13.2 Benchmarks

Omega = real task-solving and deployment field.

pi(Omega) = benchmark score.

D = model-selection or deployment decision.

If two systems have the same score but differ in reliability, cost, safety, recoverability, or actual task completion, then D does not factor through pi.

Therefore the benchmark score is not the deployment object.

### 13.3 Leaderboards

Omega = model, environment, verifier, task set, runtime constraints, infrastructure, repeated evaluation.

pi(Omega) = leaderboard score.

D = stable ranking decision.

If two models can swap order under environment change, noise, task selection, or verifier instability, then D does not factor through pi.

Therefore the leaderboard score is not a valid ranking object.

### 13.4 KPIs

Omega = operational system with dependencies, costs, externalities, incentives, and future fragilities.

pi(Omega) = KPI.

D = management action.

If two systems have the same KPI but require different actions, then D does not factor through pi.

Therefore the KPI is not the system.

### 13.5 Numerical Representations

Omega = numerical object-field.

pi(Omega) = base-expression, notation, or digit string.

D = identity with the object or a property not preserved by the representation.

If the representation does not preserve the property being asserted, then D does not factor through pi.

The notation is valid as notation.

It is not sovereign as object.

### 13.6 Frame Fidelity

Omega = originating frame.

pi(Omega) = preserved words or topic.

D = judgement of frame-faithful response.

If two different frames can preserve similar words but require different answers, then D does not factor through pi.

Therefore word preservation is not frame fidelity.

---

## 14. Relation to Law of Totality

The Law of Totality states:

a finite local form becomes structurally false when it is treated as autonomous, complete, or total.

Projection Fidelity gives the operational test:

a finite projection becomes invalid for a decision when it collapses states that require different decisions.

The absolute level is:

the finite does not coincide with the total field and is not independent from it.

The operational level is:

the projection is valid only for the decisions it preserves.

---

## 15. Relation to Wrong Object Test

The Wrong Object Test asks:

Is the answer correct for the object actually required by the decision?

Projection Fidelity sharpens this:

the object is correct for D only if D factors through the projection being used.

If not, the answer is attached to the wrong object.

---

## 16. Limits

The theorem does not identify Omega automatically.

It does not identify D automatically.

It does not recover missing data automatically.

It does not decide the problem when the necessary field is absent.

It does not turn insufficient information into sufficient information.

Its role is stricter:

it determines whether the object being used can logically support the decision being made.

If it cannot, the conclusion must be rejected, suspended, or reformulated on a richer object.

---

## 17. Final Form

The core is not:

context matters.

The core is:

a decision is valid through a projection only if the decision factors through that projection.

In shortest form:

A projection is valid only for the decisions it preserves.

In public form:

Correct answers to the wrong object are not solutions.\n