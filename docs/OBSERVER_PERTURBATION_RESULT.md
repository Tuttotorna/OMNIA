# Observer Perturbation — Minimal Result

## Setup

- 20 cases
  - 10 stable
  - 10 unstable (internally contradictory)

- 4 observers:
  - identity
  - add_explanation
  - optimize_for_clarity
  - reformat_bullets

- Metric:
  - OPI (Observer Perturbation Index)
  - ratio

---

## Result

Stable:
avg OPI   ≈ 0.0016
avg ratio ≈ 0.089

Unstable:
avg OPI   ≈ 0.0062
avg ratio ≈ 0.284

Gap:
OPI   ≈ +0.0046
ratio ≈ +0.195

---

## Interpretation

Unstable outputs change significantly more under observer perturbation.

OMNIA detects this difference without using correctness labels.

---

## Reproducibility

Run:

python examples/observer_perturbation_signal_test.py



> “OMNIA detects instability under observer perturbation, measurable via OPI.”



