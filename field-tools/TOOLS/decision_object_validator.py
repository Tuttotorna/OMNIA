#!/usr/bin/env python3
"""
Decision Object Validator

Minimal operational validator for wrong decision objects.

It checks whether an object used for decision-making
(score, metric, KPI, benchmark, aggregate, representation)
collapses cases that require different decisions.

Core failure:

    pi(omega_1) = pi(omega_2)
    but
    D(omega_1) != D(omega_2)

If this happens, the decision cannot factor through pi.

This script does not prove OMNIA.
This script does not prove new mathematics.
This script does not replace expert analysis.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from datetime import datetime, timezone
from typing import Optional, List

import pandas as pd


def parse_columns(raw: Optional[str]) -> List[str]:
    if not raw:
        return []
    return [x.strip() for x in raw.split(",") if x.strip()]


def safe_string(value) -> str:
    if pd.isna(value):
        return ""
    return str(value)


def require_columns(df: pd.DataFrame, columns: List[str]) -> None:
    missing = [c for c in columns if c not in df.columns]
    if missing:
        raise ValueError("Missing required columns: " + ", ".join(missing))


def markdown_table(df: pd.DataFrame) -> str:
    if df is None or len(df) == 0:
        return "No rows."
    cols = list(df.columns)
    header = "| " + " | ".join(cols) + " |"
    sep = "| " + " | ".join(["---"] * len(cols)) + " |"
    rows = []
    for _, row in df.iterrows():
        values = []
        for c in cols:
            v = row[c]
            if pd.isna(v):
                values.append("")
            else:
                values.append(str(v).replace("\n", " ").replace("|", "/"))
        rows.append("| " + " | ".join(values) + " |")
    return "\n".join([header, sep] + rows)


def build_exact_collision_groups(
    df: pd.DataFrame,
    object_column: str,
    decision_column: str,
    id_column: Optional[str],
    hidden_columns: List[str],
) -> tuple[pd.DataFrame, pd.DataFrame]:
    grouped_rows = []
    collision_indexes = []

    for object_value, group in df.groupby(object_column, dropna=False):
        decisions = sorted(set(safe_string(x) for x in group[decision_column].tolist()))
        distinct_decisions = len(decisions)

        if distinct_decisions > 1:
            collision_indexes.extend(group.index.tolist())

            row = {
                "object_column": object_column,
                "object_value": safe_string(object_value),
                "row_count": int(len(group)),
                "distinct_decision_count": int(distinct_decisions),
                "decisions": " / ".join(decisions),
            }

            if id_column:
                row["example_ids"] = " / ".join(
                    safe_string(x) for x in group[id_column].head(20).tolist()
                )

            for hidden in hidden_columns:
                values = sorted(set(safe_string(x) for x in group[hidden].tolist()))
                row[f"hidden_{hidden}_values"] = " / ".join(values)

            grouped_rows.append(row)

    groups_df = pd.DataFrame(grouped_rows)
    rows_df = df.loc[collision_indexes].copy() if collision_indexes else pd.DataFrame(columns=df.columns)

    return groups_df, rows_df


def build_bucket_collision_groups(
    df: pd.DataFrame,
    object_column: str,
    decision_column: str,
    id_column: Optional[str],
    hidden_columns: List[str],
    bucket_width: float,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    working = df.copy()
    numeric = pd.to_numeric(working[object_column], errors="coerce")
    working["_numeric_object_value"] = numeric

    def bucket_label(value):
        if pd.isna(value):
            return "NaN"
        start = math.floor(float(value) / bucket_width) * bucket_width
        end = start + bucket_width
        return f"[{start:g}, {end:g})"

    working["_object_bucket"] = working["_numeric_object_value"].apply(bucket_label)

    grouped_rows = []
    collision_indexes = []

    for bucket, group in working.groupby("_object_bucket", dropna=False):
        decisions = sorted(set(safe_string(x) for x in group[decision_column].tolist()))
        distinct_decisions = len(decisions)

        if distinct_decisions > 1:
            collision_indexes.extend(group.index.tolist())

            row = {
                "object_column": object_column,
                "bucket_width": bucket_width,
                "bucket": safe_string(bucket),
                "row_count": int(len(group)),
                "distinct_decision_count": int(distinct_decisions),
                "decisions": " / ".join(decisions),
                "min_object_value": float(group["_numeric_object_value"].min()) if group["_numeric_object_value"].notna().any() else None,
                "max_object_value": float(group["_numeric_object_value"].max()) if group["_numeric_object_value"].notna().any() else None,
            }

            if id_column:
                row["example_ids"] = " / ".join(
                    safe_string(x) for x in group[id_column].head(20).tolist()
                )

            for hidden in hidden_columns:
                values = sorted(set(safe_string(x) for x in group[hidden].tolist()))
                row[f"hidden_{hidden}_values"] = " / ".join(values)

            grouped_rows.append(row)

    groups_df = pd.DataFrame(grouped_rows)
    rows_df = (
        working.loc[collision_indexes]
        .drop(columns=["_numeric_object_value", "_object_bucket"], errors="ignore")
        if collision_indexes
        else pd.DataFrame(columns=df.columns)
    )

    return groups_df, rows_df


def determine_verdict(exact_count: int, bucket_count: int, bucket_width: Optional[float]) -> str:
    if exact_count > 0:
        return "INSUFFICIENT_EXACT"
    if bucket_width is not None and bucket_count > 0:
        return "UNSTABLE_BUCKET"
    return "VALID_ON_OBSERVED_DATA"


def write_report(
    outdir: Path,
    input_path: Path,
    object_column: str,
    decision_column: str,
    id_column: Optional[str],
    hidden_columns: List[str],
    bucket_width: Optional[float],
    exact_groups: pd.DataFrame,
    bucket_groups: pd.DataFrame,
    summary: dict,
) -> None:
    lines = []

    lines.append("# Decision Object Validator — Audit Report")
    lines.append("")
    lines.append("## Status")
    lines.append("")
    lines.append("This report is an operational audit.")
    lines.append("")
    lines.append("It does not prove OMNIA.")
    lines.append("")
    lines.append("It does not prove new mathematics.")
    lines.append("")
    lines.append("It does not prove that the corrected decision is automatically right.")
    lines.append("")
    lines.append("## Input")
    lines.append("")
    lines.append(f"- input file: {input_path}")
    lines.append(f"- object column pi: {object_column}")
    lines.append(f"- decision column D: {decision_column}")

    if id_column:
        lines.append(f"- id column: {id_column}")

    if hidden_columns:
        lines.append(f"- hidden/context columns: {', '.join(hidden_columns)}")

    if bucket_width is not None:
        lines.append(f"- bucket width: {bucket_width}")

    lines.append("")
    lines.append("## Core test")
    lines.append("")
    lines.append("The object fails for the decision if:")
    lines.append("")
    lines.append("pi(omega_1) = pi(omega_2)")
    lines.append("")
    lines.append("but:")
    lines.append("")
    lines.append("D(omega_1) != D(omega_2)")
    lines.append("")
    lines.append("Operational meaning: same object value, different required action.")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(f"- verdict: {summary['verdict']}")
    lines.append(f"- rows analyzed: {summary['rows_analyzed']}")
    lines.append(f"- exact collision groups: {summary['exact_collision_group_count']}")
    lines.append(f"- exact collision rows: {summary['exact_collision_row_count']}")
    lines.append(f"- bucket collision groups: {summary['bucket_collision_group_count']}")
    lines.append(f"- bucket collision rows: {summary['bucket_collision_row_count']}")
    lines.append("")
    lines.append("## Interpretation")
    lines.append("")

    if summary["verdict"] == "INSUFFICIENT_EXACT":
        lines.append("Exact collisions were found.")
        lines.append("")
        lines.append("Therefore, the object column alone cannot ground the decision column on the observed data.")
        lines.append("")
        lines.append("Conclusion: D cannot factor through pi.")
    elif summary["verdict"] == "UNSTABLE_BUCKET":
        lines.append("No exact collisions were found, but bucket-level collisions were found.")
        lines.append("")
        lines.append("This suggests local instability: similar object values correspond to different required actions.")
        lines.append("")
        lines.append("Conclusion: the object may be insufficient or unstable for this decision.")
    else:
        lines.append("No contradictory decisions were found for the same object value on the observed data.")
        lines.append("")
        lines.append("This does not prove universal validity.")
        lines.append("")
        lines.append("It only means the failure was not observed in this dataset.")

    lines.append("")
    lines.append("## Exact collision groups")
    lines.append("")
    lines.append(markdown_table(exact_groups))
    lines.append("")
    lines.append("## Bucket collision groups")
    lines.append("")
    if bucket_width is None:
        lines.append("Bucket audit not requested.")
    else:
        lines.append(markdown_table(bucket_groups))
    lines.append("")
    lines.append("## Files generated")
    lines.append("")
    lines.append("- audit_summary.json")
    lines.append("- audit_report.md")
    lines.append("- exact_collision_groups.csv")
    lines.append("- exact_collision_rows.csv")
    lines.append("- bucket_collision_groups.csv")
    lines.append("- bucket_collision_rows.csv")
    lines.append("")
    lines.append("## Boundary")
    lines.append("")
    lines.append("This audit does not decide what the correct decision should be.")
    lines.append("")
    lines.append("It only tests whether the object used for decision preserves the distinctions required by the observed decision field.")
    lines.append("")
    lines.append("Generated at: " + datetime.now(timezone.utc).isoformat())

    (outdir / "audit_report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Detect wrong decision objects: same score/metric/KPI, different decision."
    )

    parser.add_argument("--input", required=True, help="Input CSV file.")
    parser.add_argument("--object-column", required=True, help="Column used as object/proxy pi.")
    parser.add_argument("--decision-column", required=True, help="Column used as decision/action D.")
    parser.add_argument("--outdir", required=True, help="Output directory.")
    parser.add_argument("--id-column", default=None, help="Optional identifier column.")
    parser.add_argument("--hidden-columns", default="", help="Comma-separated context columns to show in collisions.")
    parser.add_argument("--bucket-width", type=float, default=None, help="Optional numeric bucket width for near-collision audit.")

    args = parser.parse_args()

    input_path = Path(args.input)
    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    hidden_columns = parse_columns(args.hidden_columns)
    df = pd.read_csv(input_path)

    required = [args.object_column, args.decision_column]
    if args.id_column:
        required.append(args.id_column)
    required += hidden_columns
    require_columns(df, required)

    exact_groups, exact_rows = build_exact_collision_groups(
        df=df,
        object_column=args.object_column,
        decision_column=args.decision_column,
        id_column=args.id_column,
        hidden_columns=hidden_columns,
    )

    if args.bucket_width is not None:
        bucket_groups, bucket_rows = build_bucket_collision_groups(
            df=df,
            object_column=args.object_column,
            decision_column=args.decision_column,
            id_column=args.id_column,
            hidden_columns=hidden_columns,
            bucket_width=args.bucket_width,
        )
    else:
        bucket_groups = pd.DataFrame()
        bucket_rows = pd.DataFrame(columns=df.columns)

    verdict = determine_verdict(
        exact_count=len(exact_groups),
        bucket_count=len(bucket_groups),
        bucket_width=args.bucket_width,
    )

    summary = {
        "status": "decision object validation audit",
        "verdict": verdict,
        "input": str(input_path),
        "object_column_pi": args.object_column,
        "decision_column_D": args.decision_column,
        "id_column": args.id_column,
        "hidden_columns": hidden_columns,
        "bucket_width": args.bucket_width,
        "rows_analyzed": int(len(df)),
        "exact_collision_group_count": int(len(exact_groups)),
        "exact_collision_row_count": int(len(exact_rows)),
        "bucket_collision_group_count": int(len(bucket_groups)),
        "bucket_collision_row_count": int(len(bucket_rows)),
        "formal_failure": "pi(omega_1)=pi(omega_2) and D(omega_1)!=D(omega_2)",
        "not_claimed": [
            "This does not prove OMNIA.",
            "This does not prove new mathematics.",
            "This does not prove that the corrected decision is automatically right.",
            "This does not replace domain expertise."
        ],
        "generated_at": datetime.now(timezone.utc).isoformat(),
    }

    exact_groups.to_csv(outdir / "exact_collision_groups.csv", index=False)
    exact_rows.to_csv(outdir / "exact_collision_rows.csv", index=False)
    bucket_groups.to_csv(outdir / "bucket_collision_groups.csv", index=False)
    bucket_rows.to_csv(outdir / "bucket_collision_rows.csv", index=False)

    with open(outdir / "audit_summary.json", "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)

    write_report(
        outdir=outdir,
        input_path=input_path,
        object_column=args.object_column,
        decision_column=args.decision_column,
        id_column=args.id_column,
        hidden_columns=hidden_columns,
        bucket_width=args.bucket_width,
        exact_groups=exact_groups,
        bucket_groups=bucket_groups,
        summary=summary,
    )

    print("=" * 100)
    print("DECISION OBJECT VALIDATOR COMPLETE")
    print("=" * 100)
    print("Verdict:", verdict)
    print("Rows analyzed:", len(df))
    print("Exact collision groups:", len(exact_groups))
    print("Exact collision rows:", len(exact_rows))
    print("Bucket collision groups:", len(bucket_groups))
    print("Bucket collision rows:", len(bucket_rows))
    print("Output directory:", outdir)
    print("=" * 100)

    if verdict == "INSUFFICIENT_EXACT":
        print("Conclusion: D cannot factor through pi on the observed data.")
    elif verdict == "UNSTABLE_BUCKET":
        print("Conclusion: no exact failure observed, but bucket instability was detected.")
    else:
        print("Conclusion: no observed failure in this dataset. Universal validity is not proven.")

    print("=" * 100)


if __name__ == "__main__":
    main()
