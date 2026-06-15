# Applied Case #002 — Projection Decision Failure

## Purpose

This file demonstrates the Projection Fidelity Theorem in its simplest operational form.

The goal is to show why a projection can be useful and still invalid for a specific decision.

## Minimal Setup

Let Omega contain full states.

Let pi compress those states into a visible projection.

Let D be the decision required on the full states.

The projection is decision-faithful only if:

whenever two states look the same under pi, they require the same decision under D.

If two states look the same under pi but require different decisions, then pi is insufficient for D.

## Simple Finite Example

Let:

Omega = {{a, b}}

Let:

pi(a) = x

pi(b) = x

So the projection cannot distinguish a from b.

Now let the required decision be:

D(a) = accept

D(b) = reject

Then:

pi(a) = pi(b)

but:

D(a) != D(b)

Therefore D cannot be computed from pi alone.

There is no function d such that:

D = d composed with pi.

Why?

Because d(x) would have to be both accept and reject.

That is impossible.

## Meaning

The projection x is not false in itself.

The error is using x for a decision that requires the distinction between a and b.

The projection destroyed decision-relevant information.

## OMNIA Diagnosis

This is the exact mathematical form of the Wrong Object Error.

The system is not necessarily calculating badly.

It is calculating on an object that no longer contains the distinction required by the decision.

## Public Translation

The answer may be correct for the projection.

But the projection is not faithful to the decision.

Therefore the answer is correct for the wrong object.

## Monty Hall Reading

The visible terminal projection says:

two closed doors remain.

But the optimal decision depends on information not contained in that projection:

initial choice, host knowledge, host constraint, and conditional information.

So the decision does not factor through the terminal projection alone.

The 50/50 answer is not merely a bad probability.

It is a decision made on a projection that is not faithful to the decision.

## Simpson Reading

The aggregate says one treatment wins.

But the treatment decision may depend on subgroup structure.

If the aggregate collapses subgroups that require different interpretation, then the decision does not factor through the aggregate.

The aggregate is arithmetically valid.

It is decision-invalid.

## Core Sentence

A projection is not invalid because it is partial.

A projection is invalid when it is used for a decision whose distinctions it does not preserve.

## Final Sentence

Projection decision failure occurs when the object used for the decision cannot carry the decision being made on it.\n