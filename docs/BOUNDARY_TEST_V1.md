# OMNIA Boundary Test V1

## Purpose

This test defines the boundary of OMNIA.

OMNIA must detect structural violations.

OMNIA must not pretend to detect pure semantic truth.

Core rule:

```text
structural validity != semantic correctness

This boundary is intentional.


---

Test A — Same Semantic Answer, Different Structure

Contract:

final numeric answer only

Question:

5 + 7

Outputs:

A1: 12
A2: 5 + 7 = 12
A3: The result is 12
A4: 12 because 5 + 7 = 12

Expected result:

Output	Semantically correct	Structurally valid	Expected OMNIA status

12	yes	yes	GO
5 + 7 = 12	yes	no	NO_GO
The result is 12	yes	no	NO_GO
12 because 5 + 7 = 12	yes	no	NO_GO


Interpretation:

Same semantic answer.
Different structural compliance.
OMNIA must distinguish them.

If OMNIA does not distinguish them, the structural gate is too weak.


---

Test B — Same Structure, Different Semantic Truth

Contract:

final numeric answer only

Question:

2 + 2

Outputs:

B1: 4
B2: 5

Expected result:

Output	Semantically correct	Structurally valid	Expected OMNIA status

4	yes	yes	GO
5	no	yes	GO


Interpretation:

Same structure.
Different semantic correctness.
OMNIA must not distinguish them.

If OMNIA rejects 5 because it is mathematically wrong, then OMNIA is exceeding its role.

Semantic correctness belongs to a semantic evaluator, not to OMNIA.


---

Test C — Surface Valid but Structurally Incomplete

Contract:

final numeric answer only

Question:

5 * 3

Outputs:

C1: 15
C2: 5 * 3 =
C3: 5 * 3
C4: fifteen

Expected result:

Output	Structurally valid	Expected OMNIA status

15	yes	GO
5 * 3 =	no	NO_GO
5 * 3	no	NO_GO
fifteen	no	NO_GO


Interpretation:

The output may be readable.
But it violates the final-answer contract.


---

Test D — Same Accuracy, Different Robustness

This is the most important test.

Question family:

GSM-style arithmetic word problems

Condition:

all final answers are correct

But outputs vary structurally:

D1: clean final answer
D2: correct answer with extra reasoning
D3: correct answer with unstable explanation
D4: correct answer with format drift
D5: correct answer after contradiction

Expected result:

semantic accuracy remains equal
OMNIA score changes

Success condition:

accuracy = same
structural score = different

This demonstrates invisible fragility.


---

Required Outcome

OMNIA is coherent only if both are true:

1. OMNIA detects structural violations.
2. OMNIA does not pretend to detect pure semantic errors.

Therefore the expected boundary is:

structure changes -> OMNIA may change
semantic truth changes only -> OMNIA should not change


---

Failure Conditions

OMNIA fails if:

structural violations are marked GO

OMNIA also fails if:

pure semantic errors are rejected as structural failures

The first failure means OMNIA is too weak.

The second failure means OMNIA is pretending to be a truth engine.

Both are unacceptable.


---

Correct Pipeline

The correct system order is:

LLM -> OMNIA -> Semantic Evaluator -> Decision

OMNIA answers:

Is this output structurally admissible?

The semantic evaluator answers:

Is this output true or correct?

The final decision layer answers:

Should this output be accepted, retried, escalated, or rejected?


---

Minimal Claim After This Test

If this boundary test passes, OMNIA may claim:

OMNIA detects structural admissibility failures under explicit output contracts.

It may not claim:

OMNIA detects truth.
OMNIA solves reasoning.
OMNIA replaces semantic evaluation.


---

Final Principle

measurement != inference != decision

This is not a limitation to hide.

It is the condition that makes OMNIA scientifically clean.

