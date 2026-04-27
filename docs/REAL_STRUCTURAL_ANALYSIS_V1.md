# REAL STRUCTURAL ANALYSIS V1

## Purpose

This experiment measures the **structural behavior of real model outputs** using a minimal tri-channel classification:

- atomic
- short
- long

No semantic interpretation is performed.

This is **pure structural measurement**.

---

## Dataset

Source:

data/real_structural_dataset_v1.jsonl

Generated via:

examples/collect_real_outputs_v1.py

- ~60 real model outputs
- mixed prompts (math, factual, open-ended)

---

## Method

Each output is reduced to structural features:

- length (token count)
- digit density
- symbol density
- malformed token count

Classification rule:

length <= 2   → atomic length <= 8   → short else          → long

No thresholds based on meaning.

---

## Results

total: 60

atomic: 9   (15%) short:  9   (15%) long:   42  (70%)

---

## Interpretation

### 1. Dominant regime: LONG (70%)

Most outputs fall into:

> long, unstructured, drift-prone sequences

This matches:

- incoherent continuations
- numeric noise chains
- pseudo-explanations without structure

---

### 2. Atomic collapse exists (15%)

Examples:

- `-30`
- `K`

These represent:

> structural collapse to minimal tokens

---

### 3. Short instability (15%)

Short malformed outputs act as:

> intermediate unstable states

Between:

- atomic collapse
- long incoherence

---

## Structural Insight

Key result:

Real model outputs are not centered around "correctness" They are distributed across structural regimes

Dominant failure mode is:

LONG INCOHERENT DRIFT

Not:

- syntax errors
- empty outputs

---

## OMNIA Relevance

This validates the need for:

- structural measurement (OPI-like signals)
- regime detection (atomic / short / long)
- intervention gates

Because:

surface-valid output != structurally stable output

---

## Next Step

Move from:

rule-based classification

to:

learned structural classifier (tri-channel)

and then:

gate integration (PASS / REVIEW / REJECT)

---

## Status

- Dataset: collected
- Evaluation: complete
- Signal: strong

Next phase:

> structural control layer

