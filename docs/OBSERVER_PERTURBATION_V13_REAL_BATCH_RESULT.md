# Observer Perturbation V13 — Real Batch Evaluation

## Purpose

V13 evaluates OMNIA on a larger, more realistic batch of outputs.

The goal is to test whether the corrected structural signal:

- scales beyond small controlled sets
- remains useful in triage conditions
- still improves prioritization over raw OPI

---

## Setup

Dataset:

```text
100 outputs total
70 stable
30 problematic (contradictions / inconsistencies)

Source:

data/v13_real_batch.jsonl

Runner:

examples/observer_perturbation_real_batch_v13.py

Results:

results/observer_perturbation_v13_summary.json
results/observer_perturbation_v13_raw_ranked.json
results/observer_perturbation_v13_corrected_ranked.json


---

Results

Raw OPI

top5:
  precision: 0.0
  recall:    0.0

top10:
  precision: 0.3
  recall:    0.1

top20:
  precision: 0.2
  recall:    0.133


---

Corrected OPI

top5:
  precision: 1.0
  recall:    0.167

top10:
  precision: 0.5
  recall:    0.167

top20:
  precision: 0.45
  recall:    0.3


---

Key Observation

raw OPI fails completely at top5
corrected OPI isolates only problematic outputs at top5

Comparison:

top5 precision:
  raw       = 0.0
  corrected = 1.0


---

Interpretation

Using corrected_opi:

review top 5 outputs
→ find 5 problematic cases out of 5

This is maximum precision at minimal review cost.


---

Failure Mode

A new limitation appears:

short stable outputs (e.g. "2 + 2 equals 4.")
can still appear in top-k due to duplication

Observed behavior:

repeated short sentences inflate ranking positions

not semantic errors

structural bias of the signal



---

Meaning

V13 confirms two things simultaneously:

Strength

corrected_opi scales and maintains high top-k precision

Weakness

duplicate short stable outputs remain a failure mode


---

Practical Use

Recommended workflow:

LLM outputs
→ rank by corrected_opi
→ review top 5–10
→ escalate or verify

This reduces review effort significantly.


---

What This Proves

V13 is the first larger-batch confirmation that:

OMNIA can reduce human attention cost at scale


---

Limitations

Still true:

not a full detector
not complete recall
not semantic understanding


---

Correct Claim

> corrected_opi scales to larger batches and significantly improves top-k prioritization, but duplicate short outputs remain a structural bias.




---

Position in Validation Path

V6  → failure (classification)
V8  → ranking signal
V9  → failure explained
V10 → correction
V11 → realistic small-scale validation
V12 → triage use-case
V13 → larger batch validation + new failure mode


---

Final Boundary

measurement != inference != decision

OMNIA remains a structural measurement layer.

---

