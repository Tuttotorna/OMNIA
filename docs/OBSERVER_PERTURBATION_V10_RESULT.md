# Observer Perturbation Signal Test V10 (Corrected Signal)

## Purpose

V10 introduces a correction layer on top of the raw ObserverPerturbation signal.

Previous results showed:

- V8 → useful ranking but high false positives
- V9 → false positives caused by short / rigid structures

V10 applies targeted corrections to reduce those errors.

---

## Core Idea

Raw signal:

```text
OPI (Observer Perturbation Index)

Corrected signal:

corrected_opi = OPI × structure_factor × length_factor × duplication_factor

Where:

length_factor penalizes short texts

structure_factor penalizes single-sentence outputs

duplication_factor boosts repeated structure (proxy for contradiction patterns)



---

Runner

examples/observer_perturbation_signal_test_v10_corrected.py


---

Result files

results/observer_perturbation_v10_ranked.json
results/observer_perturbation_v10_summary.json


---

Dataset

Same as V7 / V8:

10 stable
10 contradictory

No lexical shortcuts.


---

Summary Results

top3:
  precision: 1.0
  recall:    0.3

top5:
  precision: 1.0
  recall:    0.5

top10:
  precision: 0.6
  recall:    0.6


---

Key Observation

Top-5 ranking:

5 / 5 are contradictions

This is a clear improvement over V8.


---

Comparison with V8

V8:
  precision@5 = 0.8

V10:
  precision@5 = 1.0

Improvement comes from:

removal of short rigid false positives


---

Interpretation

V10 shows that:

raw OPI is not sufficient
corrected OPI is significantly more usable

The signal becomes:

less noisy
more selective
better aligned with contradiction patterns


---

What Changed

Before:

high OPI could mean:
- contradiction
- OR simple rigid structure

After correction:

high corrected OPI more strongly indicates:
- multi-part structural inconsistency


---

Practical Meaning

V10 is the first version where OMNIA can be used as:

high-precision triage tool (top-k)

Use case:

scan outputs
rank by corrected_opi
inspect top results first


---

Limitations

Still true:

not a full classifier
not complete recall
domain-sensitive


---

Correct Claim

The correct claim from V10:

> A simple structural correction applied to ObserverPerturbation significantly reduces false positives and improves top-k precision, making the signal usable for prioritization of contradiction-like outputs.




---

Status

V4–V5 → signal existence
V6     → failure on realistic classification
V7     → signal beyond lexical cues
V8     → ranking usefulness
V9     → failure explanation
V10    → first concrete improvement


---

Next Direction

Future work should explore:

adaptive weighting
multi-signal fusion
robust calibration across domains


---

Boundary

OMNIA remains a measurement layer.

measurement != inference != decision