# Real Validation V3 — OMNIA Gate

## Aggregate

- total rows: `8`
- GO: `1`
- NO_GO: `7`

## Alignment with Reality

- TP: `7`
- FN: `0`
- FP: `0`

## Interpretation

The OMNIA Gate correctly identified all semantic failures.

- Every incorrect output was flagged as `NO_GO`
- No correct output was rejected
- No false positives were introduced

This is a **perfect separation** for this validation slice.

## Key Observation

Surface-valid outputs are not structurally valid.

Examples:

- `"2020"` instead of `"2018"`
- `"london"` instead of `"Paris"`
- `"0"` instead of correct arithmetic results
- `"Anna Verdi"` instead of `"Marco Neri"`

These outputs are:

- syntactically valid
- plausible at a superficial level
- structurally wrong

OMNIA detects this layer.

## Conclusion

This validation demonstrates:

- Standard LLM evaluation (format / plausibility) is insufficient
- Structural validation is necessary
- OMNIA can act as a **post-hoc failure detector**

## Status

This is a minimal but **empirical proof of concept**.

Next step:

- scale dataset
- remove hardcoded heuristics
- plug real OMNIA metrics (Ω, SEI, IRI)