# GSM Symbolic v1 — OMNIA Fragility Validation Protocol

## Status

This is a controlled, bounded, falsifiable validation protocol.

It extends the current OMNIA evidence layer with a new class of test:
**structural fragility under near-equivalent variants**.

---

## Purpose

This protocol tests whether OMNIA can detect structural instability across
near-equivalent problem variants more effectively than surface-level baselines.

It does NOT test general intelligence.  
It does NOT prove reasoning ability.  
It does NOT evaluate semantic correctness beyond final answer matching.

It tests one thing only:

> Whether structurally similar prompts produce outputs that remain stable under controlled transformations.

---

## Core Hypothesis

Given a symbolic template expanded into multiple near-equivalent variants:

- Some outputs will appear valid at surface level
- Some outputs will preserve correctness inconsistently
- Some outputs will exhibit structural instability

OMNIA is expected to detect:

- instability patterns
- fragility under transformation
- regime shifts within variant groups

better than standard baselines.

---

## Dataset Design

Each template is expanded into multiple controlled variants.

### Variant Types

- `base`
- `num_perturbed`
- `clause_augmented`
- `redundant_rephrase`
- `order_shifted`

Each variant preserves the underlying symbolic structure but alters representation.

---

## Record Format

Each record in `gsm_symbolic_v1_questions.jsonl` contains:

- `template_id`
- `variant_id`
- `variant_type`
- `question`
- `expected_answer`

---

## Model Output Fields

Each record in `gsm_symbolic_v1_model_outputs.jsonl` contains:

- `template_id`
- `variant_id`
- `variant_type`
- `model_raw_output`
- `model_final_extracted_answer`
- `is_correct`

### Extraction Rule (STRICT)

- Extract the **last numeric answer** from the output
- Store it as a string
- No units
- No normalization

Examples:
- "10" != "10.0"
- "50%" != "50"

Comparison is exact string match.

---

## Baseline Measurements

The following baselines are computed per template group:

### 1. Final Answer Accuracy
Proportion of correct outputs within the group.

### 2. Answer Consistency
Whether variants that should yield the same answer do so.

### 3. Format Validity
Whether outputs follow expected formatting constraints.

### 4. Surface Similarity
Approximate textual similarity between outputs.

These baselines represent standard surface-level evaluation.

---

## OMNIA Measurement Targets

OMNIA operates as a structural measurement layer.

For each template group, it is expected to estimate:

- structural coherence
- fragility under transformation
- invariance residual
- regime discontinuity

---

## OMNIA Output Schema (Target)

Per template group:

- `coherence_score`
- `fragility_score`
- `regime_shift_flag`
- `group_status`

Where:

- `group_status ∈ {ROBUST, FRAGILE, COLLAPSED}`

---

## Evaluation Criteria

The protocol is considered successful ONLY if:

### Case A
Baseline metrics treat groups as similar, but OMNIA separates them meaningfully.

### Case B
Groups with similar accuracy are distinguished by OMNIA as stable vs unstable.

### Case C
Surface-valid outputs pass baseline checks but are flagged as structurally unstable by OMNIA.

---

## Failure Criteria

The protocol fails if:

- OMNIA does not outperform baseline separation
- OMNIA produces non-informative or uniform scores
- OMNIA cannot identify meaningful instability patterns
- OMNIA signals do not correlate with observed inconsistencies

---

## Scale

Minimum recommended:

- 30 templates
- 5 variants each
- total: 150 cases

This prevents cherry-picking and ensures minimal statistical relevance.

---

## Reproducibility Constraints

- Dataset must be public
- Model outputs must be stored
- No post-hoc modification of rules
- Protocol must remain frozen before execution

---

## Interpretation Boundary

Measurement != inference != decision.

This protocol:

- does NOT prove truth
- does NOT prove intelligence
- does NOT validate reasoning

It tests whether structural instability can be measured
in a controlled and reproducible way.

---

## Expected Outcome

The smallest acceptable positive result is:

> At least one clear case where OMNIA reveals instability
> not captured by baseline evaluation.

Anything beyond that strengthens the claim.

---

## Position in OMNIA Roadmap

This protocol represents:

- the first structured extension beyond "surface-valid failure"
- a bridge toward external validation
- a bounded, inspectable, falsifiable experiment

It does NOT expand architecture.

It validates whether the existing core captures new signal.

---

## Notes

If no meaningful separation emerges, the correct conclusion is:

OMNIA signal is insufficient in this domain.

That outcome is valid and must be reported.

No reinterpretation or adjustment should be made post-hoc.