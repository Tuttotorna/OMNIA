# Decision Object Validator — Audit Report

## Status

This report is an operational audit.

It does not prove OMNIA.

It does not prove new mathematics.

It does not prove that the corrected decision is automatically right.

## Input

- input file: /content/OMNIA-ADD-DECISION-OBJECT-VALIDATOR/field-tools/EXAMPLES/DECISION-OBJECT-VALIDATOR-DEMO/demo_decisions.csv
- object column pi: risk_score
- decision column D: action
- id column: case_id
- hidden/context columns: segment, exposure
- bucket width: 10.0

## Core test

The object fails for the decision if:

pi(omega_1) = pi(omega_2)

but:

D(omega_1) != D(omega_2)

Operational meaning: same object value, different required action.

## Summary

- verdict: INSUFFICIENT_EXACT
- rows analyzed: 8
- exact collision groups: 2
- exact collision rows: 4
- bucket collision groups: 3
- bucket collision rows: 6

## Interpretation

Exact collisions were found.

Therefore, the object column alone cannot ground the decision column on the observed data.

Conclusion: D cannot factor through pi.

## Exact collision groups

| object_column | object_value | row_count | distinct_decision_count | decisions | example_ids | hidden_segment_values | hidden_exposure_values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| risk_score | 72 | 2 | 2 | approve / block | A / B | consumer / enterprise | internal_only / public_api |
| risk_score | 85 | 2 | 2 | defer_patch / urgent_patch | C / D | development / production | isolated_network / public_internet |

## Bucket collision groups

| object_column | bucket_width | bucket | row_count | distinct_decision_count | decisions | min_object_value | max_object_value | example_ids | hidden_segment_values | hidden_exposure_values |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| risk_score | 10.0 | [50, 60) | 2 | 2 | approve / manual_review | 55.0 | 59.0 | G / H | consumer / enterprise | internal_only / partner_access |
| risk_score | 10.0 | [70, 80) | 2 | 2 | approve / block | 72.0 | 72.0 | A / B | consumer / enterprise | internal_only / public_api |
| risk_score | 10.0 | [80, 90) | 2 | 2 | defer_patch / urgent_patch | 85.0 | 85.0 | C / D | development / production | isolated_network / public_internet |

## Files generated

- audit_summary.json
- audit_report.md
- exact_collision_groups.csv
- exact_collision_rows.csv
- bucket_collision_groups.csv
- bucket_collision_rows.csv

## Boundary

This audit does not decide what the correct decision should be.

It only tests whether the object used for decision preserves the distinctions required by the observed decision field.

Generated at: 2026-06-16T09:54:43.913625+00:00
