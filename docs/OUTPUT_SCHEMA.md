# OMNIA - Output Schema

## Purpose

This document defines the canonical output contract of OMNIA core.

A valid OMNIA run must produce a bounded machine-readable structural report.

This schema exists to freeze the minimal readable output identity of the system.

---

## Canonical output object

Every valid OMNIA run must return a structured object containing exactly these core fields at minimum:

- `omega_score`
- `sei_score`
- `iri_score`
- `drift_score`
- `limit_triggered`
- `gate_status`
- `reason_code`

Additional fields may exist as optional metadata, but these seven fields define the canonical output surface of OMNIA core.

---

## Required fields

### `omega_score`
**Type:** number  
**Range:** `0.0` to `1.0`

Structural residue or stability under admissible transformations.

Interpretation:
- higher values indicate greater structural stability
- lower values indicate weaker structural persistence across controlled variation

---

### `sei_score`
**Type:** number  
**Range:** `0.0` to `1.0`

Structural Extractability Index.

Measures how much bounded structural extractability remains before the case becomes exhausted.

Interpretation:
- higher values indicate remaining structural headroom
- lower values indicate exhaustion or saturation

---

### `iri_score`
**Type:** number  
**Range:** `0.0` to `1.0`

Irreversibility Index.

Measures the degree of non-recoverable structural degradation.

Interpretation:
- higher values indicate stronger irreversibility
- lower values indicate lower irreversible loss

---

### `drift_score`
**Type:** number  
**Range:** `0.0` to `1.0`

Measures structural displacement, instability, or change across compared states or variants.

Interpretation:
- higher values indicate stronger drift or instability
- lower values indicate lower structural displacement

---

### `limit_triggered`
**Type:** boolean

Indicates whether the structural limit layer has triggered.

Interpretation:
- `true` means further structural continuation inside scope is not justified
- `false` means continuation remains admissible inside tested conditions

A triggered limit is not a proof of truth, not a semantic verdict, and not a universal safety claim.

---

### `gate_status`
**Type:** string  
**Allowed values:**
- `GO`
- `RISK`
- `NO_GO`
- `UNSTABLE`

This is the bounded operational gate output derived from the structural profile.

#### `GO`
Structural behavior remains admissible under tested conditions.

#### `RISK`
The case remains admissible, but fragility or drift is elevated.

#### `NO_GO`
Structural continuation is not admissible under tested conditions.

#### `UNSTABLE`
The structural profile is sufficiently degraded or inconsistent that operational reliability cannot be assumed inside scope.

No other gate values are valid in OMNIA core.

---

### `reason_code`
**Type:** string

A bounded machine-readable reason describing the primary structural condition behind the current gate result.

Examples include:
- `stable_profile`
- `high_drift`
- `low_omega`
- `limit_exhaustion`
- `high_iri`
- `profile_collapse`

Reason codes must remain:
- explicit
- finite
- reproducible
- non-semantic

They must describe structural status, not narrative interpretation.

---

## Canonical example

```json
{
  "omega_score": 0.58,
  "sei_score": 0.55,
  "iri_score": 0.31,
  "drift_score": 0.57,
  "limit_triggered": false,
  "gate_status": "RISK",
  "reason_code": "high_drift"
}

This is a valid canonical OMNIA output.


---

Minimal validity conditions

An OMNIA output is valid only if all the following conditions hold:

1. All seven required fields are present.


2. All numeric fields are finite numbers.


3. All numeric fields are within the closed interval [0.0, 1.0].


4. limit_triggered is boolean.


5. gate_status is one of the four allowed values.


6. reason_code is a non-empty string.


7. The report is serializable to a machine-readable format such as JSON or JSONL.



If one of these conditions fails, the output is not valid OMNIA core output.


---

Optional metadata fields

OMNIA core may include optional metadata fields such as:

case_id

profile_id

input_source

transform_set

threshold_profile

timestamp

schema_version


These fields are optional and do not change the canonical output identity of OMNIA core.


---

Gate interpretation rule

The gate output is a bounded conversion of structural measurement.

It must not be interpreted as:

semantic judgment

truth certification

reasoning score

safety certification in the broad sense

autonomous decision authority


The gate is operationally useful only inside bounded scope.


---

Limit interpretation rule

limit_triggered = true means only:

further structural continuation inside the tested admissible space is not justified


It does not mean:

the answer is false

the answer is true

the model is unsafe in general

the task is solved

the system has understood the problem


The limit layer is structural only.


---

Schema stability rule

The canonical seven-field output contract must remain stable across OMNIA core versions unless a documented versioned schema change is introduced.

This rule exists to preserve:

comparability

reproducibility

benchmark continuity

integration stability


If the output contract changes, the schema version must change explicitly.


---

JSON-style schema summary

{
  "type": "object",
  "required": [
    "omega_score",
    "sei_score",
    "iri_score",
    "drift_score",
    "limit_triggered",
    "gate_status",
    "reason_code"
  ],
  "properties": {
    "omega_score": {
      "type": "number",
      "minimum": 0.0,
      "maximum": 1.0
    },
    "sei_score": {
      "type": "number",
      "minimum": 0.0,
      "maximum": 1.0
    },
    "iri_score": {
      "type": "number",
      "minimum": 0.0,
      "maximum": 1.0
    },
    "drift_score": {
      "type": "number",
      "minimum": 0.0,
      "maximum": 1.0
    },
    "limit_triggered": {
      "type": "boolean"
    },
    "gate_status": {
      "type": "string",
      "enum": ["GO", "RISK", "NO_GO", "UNSTABLE"]
    },
    "reason_code": {
      "type": "string",
      "minLength": 1
    }
  },
  "additionalProperties": true
}

additionalProperties remains allowed because metadata fields are permitted, but the canonical required fields are fixed.


---

Final schema summary

OMNIA core output = bounded structural report

More explicitly:

omega_score
+ sei_score
+ iri_score
+ drift_score
+ limit_triggered
+ gate_status
+ reason_code

Anything less is incomplete. Anything broader must remain optional.

