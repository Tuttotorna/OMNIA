# Projection Fidelity Theorem

## Purpose

This document formalizes the mathematical core of OMNIA in its strongest operational form.

The public sentence is:

A correct answer can answer the wrong object.

The mathematical sentence is:

A projection is valid only for the decisions it preserves.

This formulation removes the purely conceptual weakness of saying only:

the fragment is not the whole.

The rigorous question is not whether a projection is useful.

The rigorous question is whether the projection preserves the decision, inference, classification, property, or calculation being made on it.

## Objects

Let:

Omega be the accessible total field, generative structure, or complete model available at the level of analysis.

P be a reduced projected space.

pi: Omega -> P be a projection, reduction, measurement, representation, aggregation, compression, framing, or visible terminal form.

A be the decision space, answer space, classification space, or value space.

D: Omega -> A be the decision, inference, classification, property, or calculation that is actually required on the full field.

The question is:

Can D be computed from pi alone?

## Projection Fidelity Condition

The projection pi is faithful with respect to D if and only if there exists a function:

d: P -> A

such that:

D = d composed with pi

In symbols:

D(omega) = d(pi(omega))

for every omega in Omega.

This means that D factors through pi.

If D factors through pi, then the projection preserves everything needed for that decision.

If D does not factor through pi, then the projection has destroyed information required by the decision.

## Equivalent Condition

The condition above is equivalent to:

for all omega1, omega2 in Omega,

if pi(omega1) = pi(omega2), then D(omega1) = D(omega2).

In symbols:

forall omega1, omega2 in Omega:
pi(omega1) = pi(omega2) implies D(omega1) = D(omega2)

This is the decisive test.

If two different full states become identical under the projection, but require different decisions, then the projection is not faithful for that decision.

## Projection Failure Condition

Projection failure occurs when there exist omega1 and omega2 in Omega such that:

pi(omega1) = pi(omega2)

but:

D(omega1) != D(omega2)

In symbols:

exists omega1, omega2 in Omega:
pi(omega1) = pi(omega2) and D(omega1) != D(omega2)

When this happens, no decision based only on pi can be valid for D over Omega.

The projection has collapsed distinct decision-relevant states into one visible object.

## OMNIA Error Function

The OMNIA decision error can be written as:

E_D(Omega, pi) = 1

if and only if:

exists omega1, omega2 in Omega:
pi(omega1) = pi(omega2) and D(omega1) != D(omega2)

Otherwise:

E_D(Omega, pi) = 0

when:

for all omega1, omega2 in Omega:
pi(omega1) = pi(omega2) implies D(omega1) = D(omega2)

## Core Theorem

A projection is decision-valid if and only if the required decision factors through the projection.

Equivalently:

A projection is valid only for the decisions it preserves.

## Proof

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

for all omega1, omega2 in Omega,

pi(omega1) = pi(omega2) implies D(omega1) = D(omega2).

Define d on the image of pi by:

d(p) = D(omega)

for any omega such that pi(omega) = p.

This definition is well-defined because if two possible choices omega1 and omega2 have the same projection p, then by assumption D(omega1) = D(omega2).

Therefore d exists and:

D(omega) = d(pi(omega))

for every omega in Omega.

Thus D factors through pi.

This proves the theorem.

## Interpretation

The projection itself is not the error.

Every finite system needs projections.

The error begins when a projection is used for a decision it does not preserve.

Projection is allowed.

False totalization is not.

A reduced object is valid only for the invariants, decisions, or properties that survive the reduction.

## Relation to the Law of Totality

The Law of Totality states:

a finite local form becomes structurally false when it is treated as autonomous, complete, or total.

The Projection Fidelity Theorem gives the operational mathematical test:

a finite projection becomes structurally invalid for a decision when it collapses states that require different decisions.

Reference:

https://github.com/Tuttotorna/LAW-OF-TOTALITY

Public threshold release:

https://github.com/Tuttotorna/LAW-OF-TOTALITY/releases/tag/v0.1.2

DOI:

https://doi.org/10.5281/zenodo.20700914

## Relation to Wrong Object Test

The Wrong Object Test says:

OMNIA detects when a correct answer is answering the wrong object.

The Projection Fidelity Theorem sharpens this:

the object is wrong for decision D exactly when D does not factor through the projection being used.

So the public question:

Is this the right object?

becomes the mathematical question:

Does the required decision factor through this projection?

## Examples

### Monty Hall

Omega is the full game structure:

car placement, initial choice, host knowledge, host rule, opened door, and conditional information.

pi(Omega) is the terminal visible projection:

two closed doors remain.

D is the optimal switching decision.

The terminal projection does not preserve the decision-relevant generative information.

Therefore D does not factor through pi.

The error appears when the terminal projection is treated as the full stochastic model.

### Simpson's Paradox

Omega is the conditioned data structure.

pi(Omega) is the aggregate.

D is the treatment decision.

If different subgroup structures can produce the same or misleading aggregate while requiring different treatment decisions, then D does not factor through the aggregate.

The aggregate is not decision-faithful.

### AI Frame Fidelity

Omega is the originating frame.

pi(Omega) is the visible wording.

D is the judgement of frame-faithful response.

If two different frames can preserve similar words while requiring different responses, then D does not factor through the words.

Word preservation is not frame fidelity.

### Numerical Representation

Omega is the numerical object-field.

pi(Omega) is a base-expression or digit string.

D is identity with the numerical object.

A base-expression does not preserve total numerical identity.

Therefore identity does not factor through one finite representation.

The representation is usable.

It is not sovereign.

### Local Correctness

Omega is the wider stability field.

pi(Omega) is the local test condition.

D is structural validity.

If two systems pass the same local test but fail differently under field expansion, then structural validity does not factor through local correctness.

Correct is not stable.

## Final Form

The strongest OMNIA sentence is:

A projection is valid only for the decisions it preserves.

The strongest operational test is:

D factors through pi or it does not.

If D does not factor through pi, then using pi as the decision object is structurally invalid.

## Final Sentence

OMNIA becomes mathematically operational when the question changes from:

is the answer correct?

to:

does the decision factor through the object being used?\n