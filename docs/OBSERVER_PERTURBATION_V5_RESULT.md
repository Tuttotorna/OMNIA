# Observer Perturbation Signal Test V5 (Multi-Domain)

## Purpose

This test evaluates whether OMNIA's `ObserverPerturbation` lens produces a consistent signal of contradiction-like structural instability across multiple domains.

V4 demonstrated that the signal exists under controlled structure.

V5 tests whether that signal persists across different types of reasoning contexts.

---

## Runner

```text
examples/observer_perturbation_signal_test_v5_multidomain.py


---

Result files

results/observer_perturbation_v5.jsonl
results/observer_perturbation_v5_summary.json


---

Dataset

The test uses 80 controlled cases across 4 domains:

math
qa
reasoning
instruction

Each domain includes:

10 stable
10 contradictory

All cases share a controlled template per domain.

The only intended structural difference is the presence of a contradictory final-answer clause.


---

Observers

Each case is evaluated under four observer transformations:

identity
add_explanation
optimize_for_clarity
reformat_bullets


---

Metrics

Primary metrics:

OPI   (Observer Perturbation Index)
ratio


---

Summary Results

math:
  stable_avg_opi:         0.0004782036842693609
  contradictory_avg_opi:  0.0006260490735551477
  opi_gap:                0.00014784538928578678

  stable_avg_ratio:         0.052171275878429416
  contradictory_avg_ratio:  0.047975391306639345
  ratio_gap:               -0.004195884571790071


qa:
  stable_avg_opi:         0.0004785128583145601
  contradictory_avg_opi:  0.0007246873129750802
  opi_gap:                0.0002461744546605201

  stable_avg_ratio:         0.05316204607799337
  contradictory_avg_ratio:  0.06188283796914303
  ratio_gap:                0.00872079189114966


reasoning:
  stable_avg_opi:         0.00026185460035219017
  contradictory_avg_opi:  0.002431523772603225
  opi_gap:                0.002169669172251035

  stable_avg_ratio:         0.029877219335170117
  contradictory_avg_ratio:  0.16072195770739545
  ratio_gap:                0.13084473837222532


instruction:
  stable_avg_opi:         0.0004625165028639724
  contradictory_avg_opi:  0.002180725601501719
  opi_gap:                0.001718209098637747

  stable_avg_ratio:         0.05416001133277744
  contradictory_avg_ratio:  0.1532145624338579
  ratio_gap:                0.09905455110108045


---

Observed Pattern

Across all domains:

contradictory_avg_opi > stable_avg_opi

This ordering holds consistently.

However, the magnitude of the gap varies significantly by domain.


---

Domain Sensitivity

Signal strength varies:

math        → weak separation
qa          → moderate separation
reasoning   → strong separation
instruction → strong separation

This indicates that the observer perturbation signal is domain-dependent.


---

Ratio Behavior

The ratio metric is not consistent:

negative or near-zero in math

weak in QA

strong in reasoning and instruction


Conclusion:

> ratio is not a stable primary signal across domains.




---

Interpretation

V5 shows that:

> OMNIA's ObserverPerturbation produces a consistent but domain-dependent signal for contradiction-like structural instability.



The signal is strongest when:

structure involves reasoning chains or instruction-following

The signal is weakest when:

structure is shallow or primarily numeric


---

Relation to Previous Versions

V1 → minimal signal
V2 → partial separation
V3 → failure due to surface-form bias
V4 → signal recovered under controlled structure
V5 → signal persists across domains, but not uniformly


---

Correct Claim

The correct claim from V5 is:

> ObserverPerturbation produces a consistent but domain-dependent signal for contradiction-like structural instability, with stronger separation in reasoning and instruction-like contexts than in simple numeric contexts.




---

What This Does NOT Show

Do not claim:

OMNIA detects all contradictions
OMNIA detects semantic truth
OMNIA works uniformly across all domains
OMNIA is robust on unconstrained LLM outputs


---

Reproducibility

Run:

python examples/observer_perturbation_signal_test_v5_multidomain.py

Expected outputs:

results/observer_perturbation_v5.jsonl
results/observer_perturbation_v5_summary.json


---

Status

This is the strongest result in the observer perturbation line so far.

It demonstrates:

existence of signal

reproducibility

domain sensitivity

identifiable limits


It does not demonstrate full generalization.


---

Boundary

This test measures structural response under observer perturbation.

It does not measure semantic truth.

measurement != inference != decision