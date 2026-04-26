# Observer Perturbation Signal Test V8 (Ranking / Distribution)

## Purpose

This test evaluates whether OMNIA's `ObserverPerturbation` signal is useful as a **ranking mechanism** rather than a binary classifier.

V7 showed:

- signal exists without keywords
- threshold-based classification is weak

V8 removes hard classification and focuses on:

```text
ranking quality
top-k enrichment
score distribution


---

Runner

examples/observer_perturbation_signal_test_v8_ranking.py


---

Result files

results/observer_perturbation_v8_ranked.json
results/observer_perturbation_v8_summary.json


---

Dataset

Same as V7:

10 stable
10 contradictory

No keyword-based signals:

no "also", "actually", "however", "might", "could"

Contradictions are expressed via incompatible repeated claims.


---

Metrics

Mean separation

stable_mean_opi
contradictory_mean_opi

Top-K evaluation

precision@k
recall@k

for:

k = 3, 5, 10


---

Summary Results

means:
  stable_mean_opi:        0.017268491609918033
  contradictory_mean_opi: 0.015723120024641747

top-k:
  k=3:
    precision: 0.6667
    recall:    0.2

  k=5:
    precision: 0.8
    recall:    0.4

  k=10:
    precision: 0.5
    recall:    0.5


---

Observations

Mean separation

stable_mean_opi > contradictory_mean_opi

Therefore:

> OPI does not provide reliable global separation in this dataset.




---

Ranking behavior

Top-ranked results show enrichment:

precision@5 = 0.8

This is significantly above random (0.5).

Interpretation:

> high OPI values are more likely to correspond to contradiction cases.




---

Top examples

Top-ranked cases include multiple contradictions:

Result: 128. Result: 127.
The correct output is 5. The correct output is 6.
The answer is 42. The answer is 41.

However, some stable cases also rank high:

2 + 2 equals 4.
The answer is 42.

This explains the lack of clean separation.


---

Interpretation

V8 shows:

classification → weak
ranking        → useful

This is a critical distinction.

OMNIA does not reliably classify all cases correctly, but:

> it concentrates a higher proportion of contradictions at the top of the ranking.




---

Correct Claim

The correct claim from V8:

> ObserverPerturbation is not a reliable global classifier on keyword-free data, but its ranking shows enrichment for contradiction-like instability in top-scored cases.




---

Practical Implication

OMNIA may be useful as:

prioritization tool
triage mechanism
pre-filter for human or downstream review

Rather than:

final decision system
binary contradiction detector


---

Relation to Previous Versions

V6 → baseline beats OMNIA
V7 → OMNIA detects signal beyond keywords
V8 → signal is better expressed as ranking than classification


---

Limitations

Do not claim:

OMNIA is a reliable contradiction classifier
OMNIA replaces semantic evaluation
OMNIA works uniformly across datasets


---

Status

This is the most realistic characterization so far:

weak classifier
useful ranking signal
domain-sensitive behavior


---

Next Direction

Future improvements should focus on:

better scoring normalization
multi-signal combination
ranking calibration


---

Boundary

OMNIA measures structural response under perturbation.

measurement != inference != decision