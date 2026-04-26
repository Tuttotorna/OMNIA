# Observer Perturbation Signal Test V2

## Purpose

This test evaluates whether OMNIA's `ObserverPerturbation` lens can separate structurally stable outputs from outputs containing ambiguity or contradiction-like instability.

The test is intentionally small, controlled, and reproducible.

---

## Runner

```text
examples/observer_perturbation_signal_test_v2.py


---

Result files

results/observer_perturbation_v2.jsonl
results/observer_perturbation_v2_summary.json


---

Dataset

The test uses 60 synthetic cases:

20 stable
20 ambiguous
20 contradictory

Each case is evaluated under four observer transformations:

identity
add_explanation
optimize_for_clarity
reformat_bullets


---

Metrics

Primary OMNIA metrics:

OPI
ratio

Baseline metrics:

text length
uncertainty keyword count
numeric token count


---

Summary Results

stable:
  avg_opi:          0.001597673728213484
  avg_ratio:        0.08873777690829736
  avg_len:          10.0
  avg_uncertainty:  0.0
  avg_numbers:      1.0

ambiguous:
  avg_opi:          0.0016780700641297278
  avg_ratio:        0.06806952987488671
  avg_len:          15.0
  avg_uncertainty:  3.0
  avg_numbers:      2.0

contradictory:
  avg_opi:          0.005035956103570852
  avg_ratio:        0.12118475817177551
  avg_len:          15.0
  avg_uncertainty:  0.0
  avg_numbers:      2.0


---

Interpretation

The expected full ordering was:

stable < ambiguous < contradictory

That full ordering was not observed.

Observed OPI ordering:

stable ≈ ambiguous < contradictory

Observed ratio ordering:

ambiguous < stable < contradictory

Therefore, V2 does not show that OMNIA cleanly separates all instability types.

It shows something narrower and more useful:

> ObserverPerturbation separates contradiction-like instability more clearly than ambiguity-like uncertainty.




---

Baseline Comparison

The uncertainty baseline strongly separates ambiguous cases:

stable uncertainty:        0.0
ambiguous uncertainty:     3.0
contradictory uncertainty: 0.0

This means ambiguity in this dataset is mostly lexical and is better captured by simple keyword counting.

Contradictory cases are different:

stable uncertainty:        0.0
contradictory uncertainty: 0.0

Yet OMNIA OPI increases:

stable avg_opi:          0.001597673728213484
contradictory avg_opi:   0.005035956103570852

This is the meaningful signal.


---

Correct Claim

The correct claim from V2 is narrow:

> OMNIA's ObserverPerturbation lens detects contradiction-like structural instability more clearly than ambiguity-like lexical uncertainty.



Do not claim:

OMNIA detects all ambiguity.
OMNIA fully separates stable / ambiguous / contradictory.
OMNIA is a semantic contradiction detector.


---

Reproducibility

Run:

python examples/observer_perturbation_signal_test_v2.py

Expected saved outputs:

results/observer_perturbation_v2.jsonl
results/observer_perturbation_v2_summary.json


---

Status

This is a useful positive result, but not a final validation.

It strengthens the previous minimal observer perturbation signal by showing that:

contradictory-like outputs produce higher observer perturbation response than stable outputs

within this controlled dataset.


---

Boundary

This test does not prove semantic truth detection.

It measures structural response under observer transformation.

measurement != inference != decision