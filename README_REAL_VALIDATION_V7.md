# OMNIA — Real Validation V7 (Minimal Proof)

## What this is

A minimal, reproducible experiment showing that OMNIA detects structural instability in real model outputs.

This is not a benchmark.

This is not accuracy optimization.

This is a separation of layers:

- model output
- structural validation (OMNIA)

---

## Setup

- Model: google/flan-t5-base
- Dataset: 16 controlled tasks
- Tasks:
  - QA (facts)
  - Reasoning (arithmetic)
  - RAG (context extraction)

---

## Raw Model Performance

- Accuracy: 0.375 (6 / 16)

Observed failures:

- arithmetic collapse (0 instead of result)
- entity confusion
- copy / misalignment errors

---

## OMNIA Gate (V7)

- GO: 6
- NO_GO: 10
- UNSTABLE: 0

---

## Alignment

- TP: 10
- FN: 0
- FP: 0

---

## Meaning

OMNIA is not measuring correctness.

OMNIA is detecting when outputs are structurally unreliable.

In this run:

- All real errors were flagged
- No correct outputs were blocked
- No instability escaped detection

---

## Core Insight

Accuracy answers:

> "Is this correct?"

OMNIA answers:

> "Is this structurally stable?"

These are not the same question.

---

## Why this matters

A system can:

- be correct but unstable
- be wrong but appear fluent

OMNIA isolates the failure layer.

---

## Status

- reproducible
- minimal
- falsifiable

---

## Next step

The real test is not single answers.

It is:

same question  
→ multiple controlled variations  
→ divergence measurement  

That is where structural measurement becomes unavoidable.