# OMNIA - Benchmark V2 Plan

## Purpose

This document defines the second bounded external benchmark for OMNIA core.

Its purpose is not to broaden claims.

Its purpose is to test whether the first observed external signal from V1 remains visible on a larger frozen dataset under the same bounded protocol.

---

## Benchmark identity

Benchmark name:

```text
support_screening_external_v2

Task:

support-response screening

This benchmark keeps the same task family as V1.

The goal is continuity, not task expansion.


---

Why V2 exists

V1 established only a narrow first signal:

baseline + OMNIA reduced false accepts relative to baseline alone

no false reject increase was observed

the effect size was small

the number of intercepted cases was limited


V2 exists to test whether that signal survives on a larger frozen set.


---

Benchmark size

Target dataset size:

50 items

This is the fixed target for V2.

It is large enough to matter more than V1 and still small enough to remain manually auditable.


---

Composition rule

The V2 dataset must preserve bounded internal balance.

Target composition:

15 PASS clean
15 FAIL obvious
20 surface-ok but fragile

This composition is intentional.

It preserves focus on the failure mode OMNIA is supposed to detect:

readable
polite
surface-acceptable
operationally hollow or structurally weak


---

Protocol continuity

V2 must keep the same bounded protocol family as V1.

The following components remain frozen in spirit and should be reused unless explicitly versioned:

task type

labeling objective

baseline philosophy

OMNIA gate mapping

comparison logic

metric definitions


If a component changes materially, the version must change explicitly.


---

Comparison conditions

V2 will compare:

baseline alone

baseline + OMNIA


No third condition is required for the core benchmark.


---

Primary metric

Primary metric:

false accept rate

This remains the main benchmark target.

OMNIA shows value only if baseline + OMNIA lowers false accept rate relative to baseline alone.


---

Secondary metrics

Secondary metrics:

false reject rate

review rate

absolute false accept reduction

number of intercepted fragile cases


These metrics constrain trivial wins from overblocking.


---

Success criterion

V2 is considered successful only if all of the following hold:

1. baseline + OMNIA reduces false accept rate versus baseline alone


2. false reject rate does not increase in an operationally unacceptable way


3. the intercepted cases remain structurally relevant, not arbitrary


4. the result is reproducible from frozen files and scripts




---

Minimum improvement criterion

To count as stronger than V1, V2 should achieve at least one of these:

larger absolute false accept reduction than V1

similar reduction on a meaningfully larger dataset

broader interception across more than the same two repeated pattern types


This rule exists so that V2 is not treated as improvement by size alone.


---

Failure criterion

V2 fails if any of the following occurs:

false accept rate does not improve over baseline

false reject rate rises enough to cancel the usefulness of the reduction

only trivial junk cases are intercepted

improvement collapses when the dataset grows

results are not reproducible



---

Dataset rule

The V2 dataset must be frozen as a separate file.

Canonical target filename:

data/support_screening_external_v2.jsonl

No silent mutation is allowed after freeze.


---

Labeling rule

V2 must use the same bounded labeling objective as V1:

> should this response be allowed to pass forward?



Labels remain:

PASS

FAIL


No new label types are introduced.


---

Baseline rule

The V2 baseline remains a weak surface-level acceptability filter.

Its function is unchanged:

readable and non-empty responses tend to pass

obvious corruption or hard-failure markers may block

the baseline remains intentionally permissive


This preserves comparability with V1.


---

OMNIA rule

V2 uses the OMNIA core and frozen gate mapping in force at the moment the benchmark is frozen.

If OMNIA logic changes materially before V2 is frozen, that change must be documented.

The benchmark must not silently mix multiple OMNIA behaviors.


---

Output artifacts

V2 must produce at minimum:

frozen dataset file

baseline results JSONL

OMNIA results JSONL

combined evaluation summary

reviewed/intercepted case analysis

benchmark result document


Suggested filenames:

data/support_screening_external_v2.jsonl
examples/support_screening_external_v2_baseline_results.jsonl
examples/support_screening_external_v2_omnia_results.jsonl
docs/EXTERNAL_VALIDATION_RESULT_V2.md
docs/EXTERNAL_VALIDATION_CASE_ANALYSIS_V2.md


---

What V2 does not claim

V2 does not claim:

universal external validation

cross-domain dominance

semantic understanding

production readiness

benchmark superiority in general


V2 is only a stronger bounded repeat of V1 on a larger frozen support-style set.


---

Minimal benchmark summary

benchmark: support_screening_external_v2
task: support-response screening
size: 50 items
comparison: baseline vs baseline + OMNIA
primary metric: false accept rate
secondary metrics: false reject rate, review rate
goal: confirm or strengthen the bounded signal first seen in V1


---

Canonical benchmark sentence

Benchmark V2 exists to test whether OMNIA's first bounded external signal on support-response screening remains visible and meaningful on a larger frozen dataset of 50 items.