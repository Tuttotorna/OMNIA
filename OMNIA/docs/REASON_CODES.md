# OMNIA CORE v1 — Reason Codes

## Status

This document defines the canonical `reason_code` vocabulary for OMNIA CORE v1.

Its purpose is to make gate outputs explicit, bounded, machine-readable, and traceable to structural conditions.

A gate status without a reason code is incomplete.

This document freezes the allowed categories for v1.

---

## 1. Function of reason codes

A `reason_code` explains, in compact categorical form, why a bounded gate output was emitted.

It does not explain meaning.
It does not provide narrative interpretation.
It does not justify a philosophical conclusion.

It only identifies the dominant structural cause associated with the emitted gate result.

---

## 2. Canonical rule

Every valid OMNIA CORE v1 output must contain exactly one primary `reason_code`.

Optional secondary metadata may exist, but the canonical output must always expose one explicit primary reason code.

---

## 3. Allowed canonical reason codes

OMNIA CORE v1 allows only the following primary `reason_code` values:

- `stable`
- `fragile`
- `high_drift`
- `low_extractability`
- `irreversible_loss`
- `limit_reached`
- `collapsed_profile`

No other primary reason code is canonical in v1.

---

## 4. Meaning of each reason code

### 4.1 stable

Meaning:

The structural profile remains admissible under the tested conditions, with no dominant instability, exhaustion boundary, or irrecoverable degradation signal.

Typical associated gate:

- `GO`

This is the cleanest admissible state inside bounded scope.

---

### 4.2 fragile

Meaning:

The case remains admissible, but its structural profile is weakened.

Typical signals may include:

- weakened residue persistence
- borderline instability
- partial degradation
- reduced robustness under controlled variation

Typical associated gate:

- `RISK`

`fragile` does not mean collapsed.
It means structurally non-clean.

---

### 4.3 high_drift

Meaning:

The dominant structural issue is instability, displacement, or divergence across variants, adjacent states, or bounded comparisons.

Typical signals may include:

- elevated `drift_score`
- unstable behavior under admissible transformations
- non-trivial displacement between comparable structural states

Typical associated gate:

- `RISK`
- sometimes `NO_GO` if drift crosses blocking conditions

`high_drift` is specifically about instability dominance.

---

### 4.4 low_extractability

Meaning:

The dominant structural issue is exhaustion of remaining usable signal.

Typical signals may include:

- low `sei_score`
- diminishing residual structural extractability
- continuation approaching structural futility

Typical associated gate:

- `RISK`
- `NO_GO` if continuation is no longer justified

This code is about exhaustion, not collapse.

---

### 4.5 irreversible_loss

Meaning:

The dominant structural issue is non-recoverable degradation.

Typical signals may include:

- elevated `iri_score`
- loss patterns that cannot be structurally recovered inside bounded continuation
- degradation that has crossed recoverability tolerance

Typical associated gate:

- `NO_GO`
- sometimes `UNSTABLE` in more severe cases

This code is about structural loss that is not meaningfully reversible inside scope.

---

### 4.6 limit_reached

Meaning:

The formal structural stopping boundary has been reached.

Typical signals may include:

- `limit_triggered = true`
- exhaustion, collapse, or non-admissibility at boundary level
- continuation no longer justified inside the admissible transformation space

Typical associated gate:

- `NO_GO`
- sometimes `UNSTABLE`

This is the cleanest explicit boundary code.

---

### 4.7 collapsed_profile

Meaning:

The structural profile is sufficiently degraded, inconsistent, or non-reliable that it cannot be treated as operationally stable inside bounded scope.

Typical signals may include:

- very weak residue
- strong instability
- severe irrecoverable degradation
- profile-level collapse across multiple metric dimensions

Typical associated gate:

- `UNSTABLE`

This is the strongest structural failure code in v1.

---

## 5. Canonical mapping between gate_status and reason_code

The mapping is constrained, but not one-to-one.

### 5.1 GO

Allowed primary reason codes:

- `stable`

No other primary reason code should map to `GO` in v1.

---

### 5.2 RISK

Allowed primary reason codes:

- `fragile`
- `high_drift`
- `low_extractability`

`RISK` means the case remains admissible, but a material structural weakness is present.

---

### 5.3 NO_GO

Allowed primary reason codes:

- `high_drift`
- `low_extractability`
- `irreversible_loss`
- `limit_reached`

`NO_GO` means structural continuation is no longer admissible for the bounded use case.

---

### 5.4 UNSTABLE

Allowed primary reason codes:

- `irreversible_loss`
- `limit_reached`
- `collapsed_profile`

`UNSTABLE` is reserved for degraded, collapsed, or non-reliable structural states.

---

## 6. Primary code selection rule

If multiple structural problems are present, OMNIA CORE v1 must emit the single reason code corresponding to the dominant blocking or dominant diagnostic cause.

Priority should follow structural severity, not cosmetic ordering.

Canonical severity ordering:

```text
collapsed_profile
> limit_reached
> irreversible_loss
> high_drift
> low_extractability
> fragile
> stable

This ordering is used only when multiple competing reason conditions are simultaneously active.


---

7. Selection logic guidance

The primary reason code should be selected according to this logic:

Case A — clean admissible profile

If the profile is admissible and no material weakness dominates:

emit stable


Case B — admissible but weakened profile

If the profile is still admissible, but weakness is present without blocking continuation:

emit fragile

or high_drift

or low_extractability


depending on dominant cause

Case C — blocked continuation

If the profile is not admissible for bounded continuation:

emit high_drift

or low_extractability

or irreversible_loss

or limit_reached


depending on dominant blocking cause

Case D — structural collapse

If the profile is degraded to the point of operational unreliability:

emit collapsed_profile

or irreversible_loss

or limit_reached


depending on dominant collapse cause


---

8. Why the vocabulary is intentionally small

The vocabulary is intentionally minimal.

Reasons:

easier to trace

easier to serialize

easier to benchmark

easier to keep stable

harder to inflate semantically


A larger vocabulary would increase ambiguity without improving the core.


---

9. Forbidden reason code behavior

The following are forbidden in OMNIA CORE v1 reason codes:

narrative sentences

semantic interpretations

philosophical labels

emotional wording

domain-specific judgments

open-ended prose explanations

unbounded code creation at runtime


Reason codes must remain categorical and bounded.


---

10. Machine-readability rule

A valid reason_code must be:

lowercase

snake_case

deterministic

from the canonical vocabulary only


This guarantees stable parsing and stable evaluation.


---

11. Minimal examples

Example 1

{
  "omega_score": 0.82,
  "sei_score": 0.74,
  "iri_score": 0.11,
  "drift_score": 0.18,
  "limit_triggered": false,
  "gate_status": "GO",
  "reason_code": "stable"
}

Example 2

{
  "omega_score": 0.59,
  "sei_score": 0.52,
  "iri_score": 0.21,
  "drift_score": 0.63,
  "limit_triggered": false,
  "gate_status": "RISK",
  "reason_code": "high_drift"
}

Example 3

{
  "omega_score": 0.41,
  "sei_score": 0.18,
  "iri_score": 0.38,
  "drift_score": 0.47,
  "limit_triggered": true,
  "gate_status": "NO_GO",
  "reason_code": "limit_reached"
}

Example 4

{
  "omega_score": 0.12,
  "sei_score": 0.09,
  "iri_score": 0.88,
  "drift_score": 0.84,
  "limit_triggered": true,
  "gate_status": "UNSTABLE",
  "reason_code": "collapsed_profile"
}


---

12. Versioning rule

This reason code vocabulary is frozen for OMNIA CORE v1.

A future version may extend it only if all of the following are true:

1. the new code adds structural clarity,


2. the new code remains non-semantic,


3. the new code does not overlap ambiguously with an existing code,


4. the new code improves benchmarking or operational traceability.



Without all four conditions, the vocabulary must remain unchanged.


---

13. Final rule

A gate output without a bounded primary reason_code is not a complete OMNIA CORE v1 result.

The gate says what happened.

The reason_code says why, in the smallest structural form allowed by the core.

