# Decision Object Validator

## Status

This is a prototype operational audit tool.

It does not prove OMNIA.

It does not prove new mathematics.

It does not replace expert analysis.

It checks one narrow failure:

same object value, different required decision.

Formal failure:

pi(omega_1) = pi(omega_2)

D(omega_1) != D(omega_2)

If this occurs, the decision cannot factor through the object used for decision.

## Script

field-tools/TOOLS/decision_object_validator.py

## Minimal use

python field-tools/TOOLS/decision_object_validator.py \
  --input your_data.csv \
  --object-column score \
  --decision-column action \
  --id-column id \
  --hidden-columns segment,exposure \
  --bucket-width 10 \
  --outdir audit_output

## Outputs

The tool writes:

- audit_summary.json
- audit_report.md
- exact_collision_groups.csv
- exact_collision_rows.csv
- bucket_collision_groups.csv
- bucket_collision_rows.csv

## Verdicts

| Verdict | Meaning |
|---|---|
| INSUFFICIENT_EXACT | Same object value leads to different decisions. |
| UNSTABLE_BUCKET | Similar object values lead to different decisions. |
| VALID_ON_OBSERVED_DATA | No contradiction observed in the dataset. Universal validity is not proven. |

## Boundary

This tool does not decide the correct action.

It only tests whether the object used for decision preserves the distinctions required by the observed decision field.
