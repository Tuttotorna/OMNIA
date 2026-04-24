# Real Validation V8 — Structural Gate

## Dataset

- `examples/real_validation_v6_harder.jsonl`

## Model

- `google/flan-t5-base`

## Gate change

V8 moves beyond surface heuristics.

It flags:

- arithmetic incoherence
- wrong prompt-number copying
- entity confusion
- factual/context mismatch

## Results

- GO: `9`
- NO_GO: `11`

## Alignment

- TP: `11`
- FN: `1`
- FP: `0`
- TN: `8`
- Precision: `1.000`
- Recall: `0.917`

## Status

Still minimal.

This is the first step away from shallow output heuristics toward structural mismatch detection.