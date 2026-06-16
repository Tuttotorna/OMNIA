# Decision-Validity Audit — Minimal Operational Criterion

## Status

This document is a minimal operational front door.

It does not claim that OMNIA is proven.

It does not claim new mathematics.

It does not claim novelty over statistics, decision theory, causal inference, cybersecurity, or measurement theory.

It states one limited criterion:

**a decision cannot be validly founded on an object that does not preserve the distinctions required by that decision.**

---

## Core objects

Let:

`Omega` = the richer field, system, state space, or decision-relevant structure.

`pi: Omega -> P` = the projection, metric, score, benchmark, KPI, aggregate, representation, or reduced object used for decision.

`D: Omega -> A` = the decision, action, classification, prioritization, or inference that must be made.

The projection `pi` is valid for the decision `D` only if there exists a function:

`d: P -> A`

such that:

`D = d composed with pi`

Operationally:

`D(omega) = d(pi(omega))`

This means the decision can be made from the projected object without needing information removed by the projection.

---

## Equivalent failure test

A projection fails for a decision if there exist two states:

`omega_1, omega_2 in Omega`

such that:

`pi(omega_1) = pi(omega_2)`

but:

`D(omega_1) != D(omega_2)`

If this happens, then no function from `pi` alone can produce the required decision.

So the object used for decision is insufficient.

---

## Minimal sentence

**Correct answers to the wrong object are not solutions.**

More formally:

**If the object used for a decision collapses distinctions required by that decision, the decision cannot validly factor through that object.**

---

## What this proves

This proves only a local insufficiency claim.

It can prove that:

- a metric is insufficient for a specific decision;
- a benchmark score is insufficient for a specific deployment choice;
- an aggregate is insufficient for a conditioned decision;
- a risk score is insufficient for a priority decision;
- a KPI is insufficient for a management action.

It does not prove that the richer framework is complete.

It does not prove that the whole theory is new.

It does not prove that the decision is correct after replacing the object.

It proves only that the original object cannot ground the decision as stated.

---

## What this does not prove

This does not prove:

- OMNIA as a total theory;
- a new mathematical theorem;
- a new law of science;
- novelty over quotient maps, sufficiency, invariance, measurement validity, causal abstraction, Simpson's paradox, Goodhart's law, or proxy failure;
- practical superiority over expert analysis;
- automatic correction of the decision.

The criterion is valid only when the objects are explicitly defined.

---

## Demonstrated artifacts

### 1. Constructed A/B testing proof

Path:

`field-tools/EXAMPLES/AB-TESTING-LOCAL-PROOF/`

Result:

Two segmented worlds have the same aggregate conversion projection but require different segment-preserving rollout decisions.

Therefore:

`aggregate conversion rate alone cannot ground the segment-preserving rollout decision.`

Status:

Constructed counterexample.

Not new mathematics.

Useful as a reproducible proof artifact.

---

### 2. Kidney stone public case

Path:

`field-tools/EXAMPLES/KIDNEY-STONES-REAL-PUBLIC-CASE/`

Result:

Aggregate treatment success rate recommends one treatment, while stone-size-conditioned success rates recommend another.

Therefore:

`aggregate treatment success rate is the wrong object for a stone-size-conditioned treatment decision.`

Status:

Real public historical case.

Known Simpson's paradox case.

Not original as statistics.

Useful as a decision-object reframing.

---

### 3. Cyber risk CVSS case

Path:

`field-tools/EXAMPLES/CYBER-RISK-CVSS-DECISION-VALIDITY-CASE/`

Result:

Two CVEs have the same CVSS base score, but different exploitation / threat context leads to different patch-priority decisions under an explicit policy.

Therefore:

`CVSS base score alone is the wrong object for that patch-priority decision.`

Status:

Real public operational case.

Not novel in cybersecurity.

Useful as a same-score / different-action audit artifact.

---

## Operational audit checklist

For any proposed decision, ask:

1. What is the decision `D`?
2. What object `pi` is being used to make it?
3. What richer field `Omega` is being reduced?
4. Which distinctions does `D` require?
5. Does `pi` preserve those distinctions?
6. Can two states have the same `pi` but require different `D`?
7. If yes, the decision cannot factor through `pi`.
8. The object is then invalid or insufficient for that decision.

---

## Claim allowed today

The only defensible claim today is:

**Decision-Validity Audit is a minimal operational method for detecting when a decision cannot be grounded in the object used to make it.**

---

## Claim not allowed today

The following claim is not justified:

**OMNIA is a new foundational theory.**

The demonstrated evidence does not support that claim.

---

## Current objective verdict

The formal core is likely already known.

The residual value, if any, is operational:

**making wrong decision-object failures explicit, reproducible, and transferable across domains.**

Generated at: 2026-06-16T08:28:08.235580+00:00
