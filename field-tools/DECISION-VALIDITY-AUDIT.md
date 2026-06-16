# Decision-Validity Audit

## One-line claim

A decision cannot be validly founded on an object that does not preserve the distinctions required by that decision.

---

## Core criterion

Let:

`Omega` = accessible field / system / generative structure

`pi: Omega -> P` = projection, metric, benchmark, KPI, score, aggregate, model, representation, classification, or observed output

`D: Omega -> A` = decision, inference, classification, ranking, judgement, or action

The projection `pi` is valid for decision `D` if and only if:

`D = d composed with pi`

for some function:

`d: P -> A`

Equivalently:

`pi(omega1) = pi(omega2) implies D(omega1) = D(omega2)`

---

## Failure condition

The audit fails if there exist two states `omega1` and `omega2` such that:

`pi(omega1) = pi(omega2)`

but:

`D(omega1) != D(omega2)`

In that case, the projection collapses states that the decision must distinguish.

Therefore the decision cannot be founded on that projection.

---

## What this is

This is a decision-validity audit.

It tests whether the object being used to make a decision actually preserves the distinctions the decision requires.

---

## What this is not

This is not proposed as a new factorization theorem.

It is not a theory of everything.

It is not a philosophical claim that "context matters."

It is not a replacement for domain expertise.

It does not recover missing data.

It does not decide the problem automatically.

It only tests whether the decision can be validly made from the object being used.

---

## Audit questions

1. What is the decision `D`?
2. What object `pi` is being used to make it?
3. What field `Omega` is being reduced?
4. Which distinctions must `D` preserve?
5. Does `pi` collapse states that `D` must distinguish?
6. If yes, what richer object is required?
7. What decision changes after correction?

---

## Verdicts

| Verdict | Meaning |
|---|---|
| `VALID_WITHIN_SCOPE` | The projection preserves the decision within the stated scope. |
| `INVALID_OBJECT` | The projection collapses distinctions required by the decision. |
| `INSUFFICIENT_FIELD` | The accessible field is too poor to test validity. |
| `OUT_OF_SCOPE` | The decision is not defined clearly enough to audit. |
| `REQUIRES_REVIEW` | Domain-specific validation is needed. |

---

## Final statement

A projection is valid only for the decisions it preserves.\n