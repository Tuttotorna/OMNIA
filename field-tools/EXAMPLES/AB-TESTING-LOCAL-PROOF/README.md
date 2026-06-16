# A/B Testing Local Proof

## Status

This is a local counterexample only.

It does not prove OMNIA.

It does not prove a new mathematical theory.

It does not prove empirical value in real deployments.

It proves one specific point:

**Aggregate conversion rate cannot ground segment-preserving rollout decisions in general.**

---

## Definitions

`Omega` = segmented A/B-test field

`pi` = aggregate conversion rates by variant

`D` = segment-preserving rollout decision

The decision `D` chooses the best variant separately for each segment.

---

## Formal structure

The constructed fields satisfy:

`pi(omega_1) = pi(omega_2)`

but:

`D(omega_1) != D(omega_2)`

Therefore:

`D` cannot factor through `pi`.

So the aggregate projection cannot ground the segment-preserving rollout decision.

---

## Full segmented fields

| world   | segment   | variant   |   trials |   conversions |   rate |
|:--------|:----------|:----------|---------:|--------------:|-------:|
| omega_1 | S1        | A         |      100 |            90 |    0.9 |
| omega_1 | S1        | B         |      100 |            10 |    0.1 |
| omega_1 | S2        | A         |      100 |            10 |    0.1 |
| omega_1 | S2        | B         |      100 |            90 |    0.9 |
| omega_2 | S1        | A         |      100 |            10 |    0.1 |
| omega_2 | S1        | B         |      100 |            90 |    0.9 |
| omega_2 | S2        | A         |      100 |            90 |    0.9 |
| omega_2 | S2        | B         |      100 |            10 |    0.1 |

---

## Aggregate projection pi

| world   | variant   |   trials |   conversions |   aggregate_rate |
|:--------|:----------|---------:|--------------:|-----------------:|
| omega_1 | A         |      200 |           100 |              0.5 |
| omega_1 | B         |      200 |           100 |              0.5 |
| omega_2 | A         |      200 |           100 |              0.5 |
| omega_2 | B         |      200 |           100 |              0.5 |

Result:

`pi(omega_1) = pi(omega_2)` is `True`.

---

## Segment-preserving decision D

| world   | segment   | chosen_variant   |   chosen_rate |
|:--------|:----------|:-----------------|--------------:|
| omega_1 | S1        | A                |           0.9 |
| omega_1 | S2        | B                |           0.9 |
| omega_2 | S1        | B                |           0.9 |
| omega_2 | S2        | A                |           0.9 |

Result:

`D(omega_1) = D(omega_2)` is `False`.

---

## Failure condition

The failure condition is:

`pi(omega_1) = pi(omega_2)`

and:

`D(omega_1) != D(omega_2)`

In this construction:

`pi(omega_1) = pi(omega_2)` is `True`.

`D(omega_1) != D(omega_2)` is `True`.

Therefore:

`factorization_failure = True`.

---

## Conclusion

Because the same aggregate projection corresponds to two different segment-preserving decisions, the decision cannot factor through the aggregate projection.

So:

`D != d composed with pi`

for any function `d` from aggregate conversion rates to segment-preserving rollout decisions.

Therefore:

**aggregate conversion rate cannot ground segment-preserving rollout decisions in general.**

---

## Public sentence

Correct answers to the wrong object are not solutions.

---

## Files

- `full_segmented_fields.csv`
- `aggregate_projection_pi.csv`
- `segment_preserving_decision_D.csv`
- `verdict.json`
- `reproduce.py`
