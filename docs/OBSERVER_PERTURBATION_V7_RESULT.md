# Observer Perturbation Signal Test V7 (Keyword-Free)

## Purpose

This test evaluates whether OMNIA's `ObserverPerturbation` lens can detect contradiction-like structural instability in cases where simple lexical cues are removed.

V6 showed that simple baselines outperform OMNIA when obvious keywords or numeric conflicts are present.

V7 removes those signals to test whether OMNIA detects deeper structural inconsistency.

---

## Runner

```text
examples/observer_perturbation_signal_test_v7_keyword_free.py


---

Result files

results/observer_perturbation_v7.jsonl
results/observer_perturbation_v7_summary.json


---

Dataset

The test uses 20 cases:

10 stable
10 contradictory

Constraints:

No keywords such as:

also, actually, however, might, could

Contradictions are expressed by duplicated incompatible claims.

Structure is simple and controlled.



---

Observers

Each case is evaluated under:

identity
add_explanation
optimize_for_clarity
reformat_bullets


---

Metrics

Primary:

avg_opi
avg_ratio

Classification:

Threshold = mean(avg_opi)



---

Summary Results

threshold: 0.016495805817279892

OMNIA:
  TP: 5
  FP: 5
  TN: 5
  FN: 5

BASELINE:
  TP: 0
  FP: 0
  TN: 10
  FN: 10


---

Derived Metrics

OMNIA:
  recall:    0.50
  precision: 0.50

BASELINE:
  recall:    0.00


---

Interpretation

The baseline fails completely in keyword-free conditions:

no keywords → no detection

OMNIA still produces a signal:

detects 50% of contradiction cases

However:

false positives are high

This shows:

> ObserverPerturbation captures a structural signal not reducible to simple lexical heuristics.



But also:

> current thresholding is too crude for reliable classification.




---

Relation to Previous Versions

V6:
  baseline > OMNIA

V7:
  baseline collapses
  OMNIA retains partial signal

This isolates the unique contribution of OMNIA.


---

Correct Claim

The correct claim from V7:

> In keyword-free contradiction scenarios, ObserverPerturbation detects structural instability signals where simple baselines detect none, but current classification performance is limited by thresholding and noise.




---

What This Does NOT Show

Do not claim:

OMNIA reliably detects contradictions
OMNIA outperforms all baselines
OMNIA is production-ready


---

Status

V7 is the first scenario where OMNIA demonstrates a unique capability:

detection beyond lexical cues

However:

signal quality is not yet sufficient for deployment


---

Next Direction

Improvement must focus on:

threshold calibration
distribution analysis
combining OPI with additional signals


---

Boundary

OMNIA measures structural response under observer perturbation.

measurement != inference != decision