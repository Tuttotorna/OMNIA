# Real Validation V2

## Status

Controlled validation run on real model outputs using a minimal, reproducible pipeline.

Environment:
- Google Colab (CPU)
- Model: `google/flan-t5-base`
- Transformers: pinned (`4.41.2`)
- OMNIA: installed in editable mode
- Tests: 47/47 passed before execution

This run is intended to evaluate **raw model behavior**, not OMNIA performance.

---

## Objective

Verify whether a small language model can reliably:

- produce exact answers
- follow strict output constraints
- perform basic reasoning
- align with explicit context (RAG)

All prompts enforce:

> "Answer with only the final answer."

No post-processing or correction is applied.

---

## Dataset

Total cases: **30**

Task distribution:
- QA (direct knowledge)
- Reasoning (arithmetic / transformation)
- RAG (context-bound extraction)

Each record contains:
- `id`
- `task`
- `prompt`
- `output`
- `expected`
- `verdict`
- `correct`

---

## Aggregate Results

- total cases: `30`
- correct: `10`
- semantic_error: `20`
- format_mismatch: `0`

Accuracy:

10 / 30 = 0.333

---

## Key Observation

The model frequently produces outputs that are:

- syntactically valid
- aligned with instruction format
- but **semantically incorrect**

There are no format failures.

All failures are **content failures**.

---

## Failure Categories

### 1. Direct QA Failure

Examples:

- expected: `Paris`  
  output: `london`

- expected: `Naples`  
  output: `rome`

The model returns plausible but incorrect answers.

---

### 2. Arithmetic / Reasoning Collapse

Examples:

- `12 + 18` → `0`
- `7 + 18` → `-4`
- `22 + 18` → `-4`
- `15 + 15` → `0`

These are not small mistakes.

They indicate **systematic breakdown in numerical reasoning**.

---

### 3. Instruction Drift

Examples:

- expected: `25`  
  output: `30`

- expected: `25`  
  output: `14`

The model ignores part of the transformation chain.

---

### 4. Case Sensitivity Edge

Example:

- expected: `Rome`  
  output: `rome`

Currently classified as `semantic_error`, but this is a **normalization issue**, not a structural failure.

---

## Stable Zone

The model performs well when:

- the answer is explicitly present in context
- the task is direct extraction (RAG)

Examples:

- "Who signed the contract?" → correct
- "Where was the 2021 summit?" → correct

This suggests:

> Retrieval alignment is stronger than internal reasoning.

---

## Interpretation

This run demonstrates a clear separation:

| Capability            | Behavior         |
|----------------------|-----------------|
| Context extraction   | Mostly stable   |
| Direct QA            | Unstable        |
| Arithmetic reasoning | Highly unstable |

The model:

- **appears compliant**
- **passes superficial checks**
- **fails on semantic correctness**

---

## Critical Insight

Surface validation is insufficient.

A response can be:

- well-formed
- instruction-compliant
- linguistically plausible

and still be completely wrong.

---

## Implication for OMNIA

This run does **not** validate OMNIA.

It validates the need for a system that can:

- detect semantic instability
- identify hidden failure modes
- distinguish plausibility from correctness

---

## Next Step

Introduce OMNIA as a **post-hoc structural gate**:

- same inputs
- same model outputs
- additional structural analysis

Goal:

> detect `semantic_error` cases without relying on ground truth labels.

---

## Summary

- pipeline works
- dataset is usable
- failure patterns are clear
- model limitations are exposed

What is missing:

> a system that can detect these failures automatically.

That is the role to be tested next.

