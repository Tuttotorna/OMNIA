# OMNIA — V18 Final Position

## 1. Claim

OMNIA can decompose structural failure into distinct regimes.

These regimes are not reducible to a single scalar score.

The minimal decomposition observed is:

```text
1. atomic malformed
2. short malformed
3. long incoherent

This is the core result.


---

2. Evidence (V18)

V18 introduced a tri-channel structural diagnostic model.

Each channel captures a different failure mode:

Atomic malformed

empty or near-empty outputs

single-token degeneration

non-recoverable structure


Short malformed

short outputs (2–8 tokens)

local corruption

partial structure breakdown


Long incoherent

longer outputs

multi-sentence instability

global inconsistency


Key observation:

different failure modes occupy different regions
and cannot be reliably captured by a single score


---

3. Negative Results (V19–V21)

Attempts were made to convert the tri-channel diagnostic into a decision gate using manual threshold calibration.

Results:

V19 → partial improvement
V20 → better local fit
V21 → degradation

Observed behavior:

thresholds overfit small datasets

improvements do not generalize

small rule changes produce instability

classification becomes inconsistent


Conclusion:

manual gating based on small datasets is unstable


---

4. Boundary

OMNIA does NOT currently provide:

a stable decision gate

a universal classifier of output quality

semantic correctness evaluation

final decision capability


OMNIA remains:

a structural measurement and diagnostic system


---

5. Correct Interpretation

The correct role of OMNIA at this stage is:

diagnostic layer, not decision layer

It reveals structure.

It does not decide.


---

6. Value

Despite the failed gating attempts, the value is clear:

interpretable decomposition of failure

separation of structural regimes

diagnostic clarity

reproducible measurement behavior



---

7. Next Direction

The correct next step is not further manual tuning.

Required:

1. larger dataset
2. automatic calibration
3. statistical validation
4. possible learning-based mapping from channels → decisions


---

8. Final Statement

OMNIA successfully identifies that structural failure is multi-regime.
However, mapping these regimes into a robust decision system requires
scale, data, and calibration beyond manual threshold design.


---

9. Status

V18 → valid structural discovery
V19–V21 → negative calibration results (useful)

This is the current stable position.