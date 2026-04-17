# THRESHOLD_POLICY.md

## Status

This document defines the canonical threshold policy of OMNIA CORE v1.

Its purpose is to specify how canonical structural metrics are converted into:

- `limit_triggered`
- `gate_status`
- `reason_code`

Without this policy, OMNIA CORE v1 remains descriptive but not operational.

This document freezes the bounded decision policy for v1.

---

## 1. Scope

This policy applies only to the canonical metric family:

- `omega_score`
- `sei_score`
- `iri_score`
- `drift_score`

and to the canonical output fields:

- `limit_triggered`
- `gate_status`
- `reason_code`

This is a bounded threshold policy for OMNIA CORE v1.

It is not a universal theory of structural judgment.

---

## 2. Metric orientation

The threshold logic assumes the following directional meaning:

- higher `omega_score` -> better structural persistence
- higher `sei_score` -> more remaining structural extractability
- higher `iri_score` -> worse non-recoverable degradation
- higher `drift_score` -> worse instability / displacement

This directional convention is fixed for v1.

---

## 3. Canonical normalized ranges

All canonical metric values must be normalized to:

```text
[0.0, 1.0]

before threshold evaluation.

Threshold logic is invalid if the emitted values are not normalized.


---

4. Canonical threshold bands

The following threshold bands are canonical for v1.

4.1 omega_score bands

omega_score >= 0.75 -> strong persistence

0.50 <= omega_score < 0.75 -> moderate persistence

0.30 <= omega_score < 0.50 -> weak persistence

omega_score < 0.30 -> collapse-prone persistence



---

4.2 sei_score bands

sei_score >= 0.70 -> strong remaining extractability

0.40 <= sei_score < 0.70 -> reduced but still usable extractability

0.20 <= sei_score < 0.40 -> low extractability

sei_score < 0.20 -> exhaustion boundary zone



---

4.3 iri_score bands

iri_score < 0.25 -> low irreversible loss

0.25 <= iri_score < 0.50 -> moderate irreversible loss

0.50 <= iri_score < 0.75 -> high irreversible loss

iri_score >= 0.75 -> critical irreversible loss



---

4.4 drift_score bands

drift_score < 0.25 -> low drift

0.25 <= drift_score < 0.50 -> moderate drift

0.50 <= drift_score < 0.70 -> high drift

drift_score >= 0.70 -> critical drift



---

5. Canonical limit policy

The field limit_triggered must be set to true when at least one of the following canonical blocking conditions holds:

5.1 Exhaustion boundary

sei_score < 0.20

5.2 Critical irreversible loss

iri_score >= 0.75

5.3 Critical structural collapse tendency

omega_score < 0.30

combined with at least one of:

drift_score >= 0.70

iri_score >= 0.50

sei_score < 0.40


5.4 Explicit collapse profile

A multi-signal collapse pattern is present, such as:

very weak persistence

strong drift

high irreversible loss


in a combined non-admissible state

If none of these conditions holds, then:

limit_triggered = false


---

6. Canonical gate policy

The gate must be computed after threshold evaluation and after limit policy evaluation.


---

6.1 GO policy

Emit:

gate_status = GO
reason_code = stable

only if all of the following hold:

limit_triggered = false

omega_score >= 0.75

sei_score >= 0.70

iri_score < 0.25

drift_score < 0.25


This is the clean admissible profile.


---

6.2 RISK policy

Emit:

gate_status = RISK

when:

limit_triggered = false

the profile is still admissible

but at least one material weakness is present


Canonical RISK conditions include one or more of:

0.50 <= drift_score < 0.70

0.20 <= sei_score < 0.70

0.25 <= iri_score < 0.50

0.30 <= omega_score < 0.75


The primary reason_code must reflect the dominant weakness:

fragile

high_drift

low_extractability


RISK means admissible but non-clean.


---

6.3 NO_GO policy

Emit:

gate_status = NO_GO

when:

structural continuation is no longer admissible

but the profile is not best described as fully collapsed


Canonical NO_GO triggers include:

limit_triggered = true with dominant exhaustion or boundary condition

sei_score < 0.20

drift_score >= 0.70 without full collapse profile

iri_score >= 0.50 with blocking degradation

strong boundary conflict between metrics even without total collapse


Allowed primary reason_code values:

high_drift

low_extractability

irreversible_loss

limit_reached



---

6.4 UNSTABLE policy

Emit:

gate_status = UNSTABLE

when the structural profile is best described as degraded, collapsed, or non-reliable at core level.

Canonical UNSTABLE triggers include one or more of:

omega_score < 0.30

iri_score >= 0.75

drift_score >= 0.70

combined collapse pattern across multiple metrics

limit_triggered = true with profile-level collapse


Allowed primary reason_code values:

irreversible_loss

limit_reached

collapsed_profile


UNSTABLE is stronger than NO_GO.

It is reserved for structurally degraded profiles, not just blocked continuation.


---

7. Canonical reason selection policy

If multiple reasons are active, emit exactly one primary reason_code according to dominant structural severity.

Canonical severity priority:

collapsed_profile
> limit_reached
> irreversible_loss
> high_drift
> low_extractability
> fragile
> stable

This priority is applied only when multiple candidate causes compete.


---

8. Canonical classification summary

GO

Requirements:

strong persistence

strong extractability

low irreversible loss

low drift

no limit trigger


Primary reason:

stable



---

RISK

Requirements:

admissible profile

no limit trigger

at least one material weakness


Primary reason:

fragile

high_drift

low_extractability



---

NO_GO

Requirements:

continuation not admissible

boundary or blocking condition present

profile not necessarily fully collapsed


Primary reason:

high_drift

low_extractability

irreversible_loss

limit_reached



---

UNSTABLE

Requirements:

collapse-prone or collapsed profile

high degradation, high instability, or critical irreversible loss

operational unreliability inside bounded scope


Primary reason:

irreversible_loss

limit_reached

collapsed_profile



---

9. Conflict resolution rule

If threshold conditions overlap, use the strongest valid gate according to the following priority:

UNSTABLE
> NO_GO
> RISK
> GO

This means:

collapse dominates blocking

blocking dominates admissible risk

admissible risk dominates clean admissibility


No weaker gate may be emitted if a stronger gate condition is active.


---

10. Examples

Example A

{
  "omega_score": 0.81,
  "sei_score": 0.76,
  "iri_score": 0.14,
  "drift_score": 0.19,
  "limit_triggered": false,
  "gate_status": "GO",
  "reason_code": "stable"
}

Example B

{
  "omega_score": 0.58,
  "sei_score": 0.55,
  "iri_score": 0.31,
  "drift_score": 0.57,
  "limit_triggered": false,
  "gate_status": "RISK",
  "reason_code": "high_drift"
}

Example C

{
  "omega_score": 0.43,
  "sei_score": 0.16,
  "iri_score": 0.44,
  "drift_score": 0.49,
  "limit_triggered": true,
  "gate_status": "NO_GO",
  "reason_code": "limit_reached"
}

Example D

{
  "omega_score": 0.18,
  "sei_score": 0.09,
  "iri_score": 0.87,
  "drift_score": 0.82,
  "limit_triggered": true,
  "gate_status": "UNSTABLE",
  "reason_code": "collapsed_profile"
}


---

11. Threshold evolution rule

This threshold policy is frozen for OMNIA CORE v1.

A future version may change thresholds only if:

1. the new policy improves bounded benchmarking,


2. the new policy remains readable,


3. the new policy remains reproducible,


4. the new policy preserves the canonical four-way gate logic.



Without all four conditions, the threshold policy must remain unchanged.


---

12. Final policy formula

The shortest correct formula is:

strong residue + strong extractability + low loss + low drift -> GO
admissible but weakened profile -> RISK
blocked continuation -> NO_GO
collapsed or non-reliable profile -> UNSTABLE

This is the canonical threshold policy of OMNIA CORE v1.

