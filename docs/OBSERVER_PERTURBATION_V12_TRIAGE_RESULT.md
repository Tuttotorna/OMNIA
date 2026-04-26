# Observer Perturbation V12 — Triage Use Case

## Purpose

V12 evaluates OMNIA in a practical scenario:

> prioritizing which LLM outputs to review first.

OMNIA does not attempt to classify all errors.

Instead, it ranks outputs so that reviewing top-k finds more issues with less effort.

---

## Setup

Dataset:

```text
30 outputs total
15 stable
15 problematic (contradiction / inconsistency)

Runner:

examples/observer_perturbation_triage_demo_v12.py

Results:

results/observer_perturbation_v12_summary.json
results/observer_perturbation_v12_raw_ranked.json
results/observer_perturbation_v12_corrected_ranked.json


---

Results

Raw OPI

top5:
  precision: 0.4
  recall:    0.133

top10:
  precision: 0.5
  recall:    0.333


---

Corrected OPI

top5:
  precision: 1.0
  recall:    0.333

top10:
  precision: 0.9
  recall:    0.6


---

Key Observation

corrected_opi drastically improves prioritization

Comparison:

top5 precision:
  raw       = 0.4
  corrected = 1.0

top10 precision:
  raw       = 0.5
  corrected = 0.9


---

Interpretation

Instead of reviewing all outputs:

review top 10 corrected-ranked outputs
→ find 9 issues out of 10 reviewed

This represents a significant reduction in review cost.


---

Practical Meaning

OMNIA can be used as a triage layer:

LLM outputs
→ rank by corrected_opi
→ review top-k
→ escalate if needed

OMNIA does not decide correctness.

OMNIA prioritizes attention.


---

What This Proves

V12 is the first test showing real operational value:

less work → more issues found

This is a measurable improvement over raw OPI.


---

Limitations

Still true:

not a full detector
not complete recall
not a semantic verifier

OMNIA alone cannot guarantee correctness.


---

Correct Claim

The correct claim from V12:

> corrected_opi significantly improves triage efficiency by concentrating structurally inconsistent outputs in the top-ranked subset.




---

Position in Validation Path

V6  → failure (classification)
V8  → ranking signal emerges
V9  → failure explained
V10 → correction introduced
V11 → correction generalizes
V12 → real use-case validated


---

Final Boundary

measurement != inference != decision

OMNIA remains a structural measurement layer.

---

