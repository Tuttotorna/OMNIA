# Observer Perturbation Signal Test V4

## Purpose

This test evaluates whether OMNIA's `ObserverPerturbation` lens detects contradiction-like structural instability when length and structure are controlled.

V3 showed that observer perturbation metrics can be dominated by surface form and text length.

V4 controls the template structure to test whether the signal remains when stable and contradictory cases share the same base form.

---

## Runner

```text
examples/observer_perturbation_signal_test_v4_length_controlled.py


---

Result files

results/observer_perturbation_v4.jsonl
results/observer_perturbation_v4_summary.json


---

Dataset

The test uses 40 controlled cases:

20 stable
20 contradictory

Both classes share the same base structure.

The only intended difference is the presence or absence of a contradictory final-answer clause.


---

Observers

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

OPI means Observer Perturbation Index.


---

Summary Results

stable:
  avg_opi:    0.00048281315005679155
  avg_ratio:  0.05433859326905387

contradictory:
  avg_opi:    0.0015163308513652446
  avg_ratio:  0.10449869748697187


---

Observed Ordering

contradictory > stable

for both:

avg_opi
avg_ratio


---

Interpretation

V4 shows that, under controlled length and structure conditions, contradictory cases produce a higher observer perturbation response than stable cases.

This supports the narrow claim that OMNIA's ObserverPerturbation lens can detect contradiction-like structural instability when surface-form confounds are controlled.


---

Relation to V3

V3 produced an inverted result:

stable OPI > contradictory OPI

This showed that the metric can be affected by text length and surface form.

V4 corrects that confound by using controlled templates.

Therefore:

V3 exposed a surface-form bias.
V4 shows the signal can reappear when structure is controlled.


---

Correct Claim

The correct claim from V4 is narrow:

> OMNIA's ObserverPerturbation lens detects contradiction-like structural instability under controlled length/structure conditions.



Do not claim:

OMNIA detects all contradictions.
OMNIA detects semantic truth.
OMNIA is a contradiction oracle.
OMNIA works on all natural LLM outputs without controls.


---

Reproducibility

Run:

python examples/observer_perturbation_signal_test_v4_length_controlled.py

Expected saved outputs:

results/observer_perturbation_v4.jsonl
results/observer_perturbation_v4_summary.json


---

Status

This is a controlled positive result.

It strengthens the observer perturbation line by showing that the contradiction signal survives when length and structure are controlled.

It does not yet prove generalization to unconstrained real-world model outputs.


---

Boundary

This test does not prove semantic truth detection.

It measures structural response under observer transformation.

measurement != inference != decision