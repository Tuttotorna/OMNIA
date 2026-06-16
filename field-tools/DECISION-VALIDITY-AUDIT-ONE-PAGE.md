# Decision-Validity Audit

## A one-page operational criterion for detecting wrong decision objects

### Problem

A score, metric, benchmark, KPI, aggregate, or representation can be correct and still be the wrong object for a decision.

The failure appears when the same object value hides states that require different actions.

Minimal form:

`same score, different required action`

---

### Criterion

Let:

`Omega` = the richer decision-relevant field.

`pi: Omega -> P` = the object used for decision: score, metric, benchmark, aggregate, KPI, projection, representation.

`D: Omega -> A` = the decision, action, classification, prioritization, or inference.

The decision is valid through `pi` only if there exists:

`d: P -> A`

such that:

`D = d composed with pi`

Meaning:

`D(omega)` can be recovered from `pi(omega)` alone.

---

### Failure test

The object `pi` fails for decision `D` if:

`pi(omega_1) = pi(omega_2)`

but:

`D(omega_1) != D(omega_2)`

Then no decision function from `pi` alone can produce the required decision.

Therefore:

`D cannot factor through pi`

Operational conclusion:

**the object used for decision is insufficient for that decision.**

---

### Plain sentence

**Correct answers to the wrong object are not solutions.**

More operationally:

**Before trusting a score, prove that the decision can factor through it.**

---

### Three demonstrated cases

| Case | Object used | Hidden field | Result |
|---|---|---|---|
| A/B testing | aggregate conversion rate | segmented user field | same aggregate, different segment-preserving rollout |
| Kidney stones | aggregate treatment success rate | stone-size-conditioned field | aggregate recommends one treatment, conditioned field another |
| Cyber risk CVSS | CVSS base score | exploitation / threat context | same CVSS 9.8, different patch-priority decision |

Paths:

- `field-tools/EXAMPLES/AB-TESTING-LOCAL-PROOF/`
- `field-tools/EXAMPLES/KIDNEY-STONES-REAL-PUBLIC-CASE/`
- `field-tools/EXAMPLES/CYBER-RISK-CVSS-DECISION-VALIDITY-CASE/`

---

### What this proves

It can prove a local insufficiency claim:

- this metric cannot ground this decision;
- this benchmark cannot ground this deployment choice;
- this aggregate cannot ground this conditioned decision;
- this score cannot ground this prioritization;
- this representation does not preserve the distinctions required by the action.

---

### What this does not prove

It does not prove:

- OMNIA as a total theory;
- new mathematics;
- novelty over sufficiency, invariance, quotient maps, measurement validity, causal abstraction, Simpson's paradox, Goodhart's law, or proxy failure;
- practical superiority over expert analysis;
- automatic correction of the decision.

---

### Current allowed claim

**Decision-Validity Audit is a minimal operational method for detecting when a decision cannot be grounded in the object used to make it.**

---

### Reviewer question

For any proposed decision, ask:

**Can two states have the same object value but require different actions?**

If yes, the object is not a valid decision object for that decision.

Generated at: 2026-06-16T09:13:54.112802+00:00
