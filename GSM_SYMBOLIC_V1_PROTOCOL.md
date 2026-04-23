# GSM Symbolic v1 - OMNIA Fragility Validation Protocol

## Purpose

This protocol tests whether OMNIA can detect structural fragility across near-equivalent problem variants better than standard surface-level checks.

It does not test semantic intelligence in general.
It does not claim proof of reasoning.
It tests structural stability under controlled perturbation.

## Core hypothesis

Near-equivalent prompts derived from the same symbolic template may generate outputs that appear superficially valid while being structurally unstable.

OMNIA should detect this instability more clearly than standard baselines.

## Dataset structure

Each template is expanded into multiple controlled variants:

- base
- num_perturbed
- clause_augmented
- redundant_rephrase
- order_shifted

Each record contains:

- template_id
- variant_id
- variant_type
- question
- expected_answer

## Model output fields

- model_raw_output
- model_final_extracted_answer
- is_correct

## Baselines

The following non-OMNIA baselines are computed:

- final answer correctness
- answer consistency across variants
- output format validity
- surface similarity

## OMNIA target

OMNIA is expected to measure:

- structural coherence
- fragility under transformation
- regime instability
- invariance residual

## Evaluation criterion

OMNIA is considered useful only if it separates robust vs fragile groups better than surface-level baselines, or reveals instability that baseline checks fail to expose.

## Failure criterion

The protocol fails if OMNIA does not improve discrimination, produces non-informative scores, or cannot identify meaningful instability patterns.

## Interpretation boundary

Measurement != inference != decision.

This protocol does not claim that OMNIA proves truth, intelligence, or semantic understanding.
It tests whether OMNIA captures structural instability in model behavior.