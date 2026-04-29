# DOMAIN ADAPTATION RULE

## Scope

This file defines the minimal rule for applying OMNIA to any domain.

OMNIA can be applied only when the following elements can be defined:

1. f(x)
2. d(x, y)
3. T
4. bounded claim

Without these elements, the application is not valid.

---

# 1. Structural Mapping: f(x)

f(x) converts a domain object into a structural representation.

Example:

```text
raw object
->
measurable structure

Examples:

LLM output        -> token / repetition / coherence structure
configuration    -> key-value structural signature
log stream       -> event trajectory
hash output      -> bit vector
database schema  -> field/type/nullability structure
legal clause     -> obligation / condition / exception structure

Requirement:

f(x) must be deterministic enough to reproduce results.


---

2. Distance Function: d(x, y)

d(x, y) measures difference between two structural representations.

Example:

d(f(x), f(y)) -> value in bounded range

Usually:

0 = no structural difference
1 = maximum structural difference

Examples:

bit distance
field mismatch ratio
event-type drift
schema difference
token-pattern divergence
trajectory variance
invariant-set loss

Requirement:

d(x, y) must be explicit.

No hidden interpretation layer.


---

3. Transformation Set: T

T is the set of controlled transformations applied to the input.

Example:

T = {t1, t2, t3, ...}

Examples:

format change
encoding change
field reorder
minor perturbation
clause augmentation
input mutation
configuration change
log trajectory extension
hash input perturbation

Requirement:

T must be controlled.

For semantic domains:

T should preserve intended meaning unless the test explicitly measures semantic drift.


---

4. Bounded Claim

Every OMNIA application must state a bounded claim.

Invalid claim:

OMNIA proves truth.

Valid claim:

Under these transformations, this structural representation shows measurable instability.

Invalid claim:

OMNIA detects all cyber attacks.

Valid claim:

Under this simplified configuration drift test, OMNIA-style structural signals separate surface similarity from security-relevant drift.


---

Minimal Valid Application Template

A valid OMNIA domain application must include:

Domain:
Object x:
Structural mapping f(x):
Distance d(x, y):
Transformations T:
Measured signals:
Bounded claim:
Non-claims:
Reproducibility path:


---

Validity Rule

An OMNIA domain application is valid only if:

f(x) is defined
d(x, y) is defined
T is controlled
claim is bounded
non-claims are explicit

If any element is missing, the application remains conceptual.


---

Domain Examples

AI Output Reliability

f(x): token / structural coherence signature
d(x,y): structural divergence score
T: paraphrase, clause addition, formatting perturbation
claim: correctness may remain stable while structural stability degrades

Cybersecurity

f(x): configuration or log structural signature
d(x,y): field drift / event drift / invariant mismatch
T: controlled configuration or telemetry perturbation
claim: surface operation may persist while security-relevant structure degrades

Cryptography

f(x): bit-vector hash output
d(x,y): normalized bit distance
T: minimal input perturbation
claim: small input changes can produce large output divergence

Data Integrity

f(x): schema / field / type / nullability structure
d(x,y): schema mismatch ratio
T: field deletion, type drift, null insertion, reorder
claim: parseable data may still lose structural integrity

Software Supply Chain

f(x): dependency / file / build artifact structure
d(x,y): dependency drift or artifact difference
T: version change, file mutation, build environment variation
claim: nominally same builds may diverge structurally


---

Architectural Boundary

The OMNIA boundary remains:

measurement != inference != decision

OMNIA measures structure.

Domain interpretation remains external.

Operational decisions remain external.


---

Final Rule

OMNIA can move into a domain only when the domain can be made structurally measurable.

The test is not:

Can we talk about the domain?

The test is:

Can we define f(x), d(x,y), T, and a bounded claim?

