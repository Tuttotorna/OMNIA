# OMNIA — Real Validation V2 Report

## Scope

This report documents a controlled validation run designed to test whether a structural gate (OMNIA-style) can detect semantic failures that pass standard surface-level validation.

The goal is not to prove semantic understanding.

The goal is to verify whether a post-hoc structural layer can identify outputs that are *formally plausible but structurally unreliable*.

---

## Experimental Setup

- Dataset size: 30 cases
- Tasks:
  - QA
  - Reasoning
  - RAG (context-based)

- Model:
  - google/flan-t5-base

- Constraint:
  - "Answer with only the final answer"

- Evaluation criteria:
  - Exact match (ground truth)
  - Structural gate classification

---

## Baseline Results (Model Only)

- Total cases: 30
- Correct: 10
- Semantic errors: 20
- Format mismatch: 0

### Key observation

All outputs are **surface-plausible**.

Many incorrect outputs are:
- syntactically valid
- coherent
- aligned in style with the prompt

Yet semantically wrong.

---

## OMNIA Gate Results

### Aggregate

- GO: 15
- NO_GO: 15
- UNSTABLE: 0

### Alignment with real errors

- True Positives (semantic_error correctly flagged): 15
- False Negatives (missed errors): 5
- False Positives: 0

---

## Metrics

- Precision: 1.00
- Recall: 0.75
- F1 Score: 0.8571

---

## Interpretation

### 1. High precision behavior

The gate does not introduce false alarms in this run.

When the system flags an output as NO_GO, it corresponds to a real semantic failure.

This indicates:

> Structural filtering can be conservative and reliable.

---

### 2. Partial recall

The gate fails to detect 5 out of 20 semantic errors.

This indicates:

> Structural signals are present, but not yet fully captured.

The current implementation is:

- selective
- not exhaustive

---

### 3. Structural vs surface distinction

This experiment reinforces a key principle:

> Surface plausibility != structural validity

Examples observed:

- correct format but wrong answer
- coherent reasoning with incorrect result
- plausible entity substitution
- numerically incorrect but syntactically clean outputs

---

## Nature of Detected Failures

The gate successfully flags cases such as:

- incorrect arithmetic with clean formatting
- wrong entity extraction in RAG
- plausible but incorrect factual answers
- stable-looking outputs with hidden inconsistency

---

## Nature of Missed Failures

The missed cases suggest that:

- some incorrect outputs maintain enough structural coherence
- current heuristics are not sensitive to deeper semantic drift
- the gate lacks certain invariance checks

This is the primary limitation.

---

## Key Result

This is the first measurable signal:

> A post-hoc structural gate can intercept a significant portion of semantic failures without introducing false positives in this controlled setup.

---

## Limitations

- Small dataset (30 cases)
- Synthetic + semi-real prompts
- Simplified structural signal (mock OMNIA layer)
- No transformation-based invariance yet
- No multi-pass perturbation testing

---

## What This Is NOT

- Not a proof of semantic understanding
- Not a replacement for the model
- Not a universal error detector
- Not production-ready

---

## What This IS

- A proof of signal
- A measurable structural effect
- A working prototype of an intervention gate
- A demonstration that:

> external structure-based validation can add value beyond classical checks

---

## Next Steps

1. Analyze False Negatives (5 cases)
2. Introduce transformation-based perturbations
3. Add invariance checks across variations
4. Improve sensitivity without increasing false positives
5. Scale dataset (100+ cases)
6. Compare across multiple models

---

## Core Principle

> Structural admissibility is independent from surface correctness.

---

## Conclusion

OMNIA-style gating shows:

- strong precision
- partial recall
- clear signal

The system is not complete.

But it is already **non-trivial**.

And measurable.

---

## Status

**Phase:** Early empirical validation  
**Confidence:** Medium (signal present, not complete)  
**Action:** Iterate immediately