"""
Generic OMNIA result analyzer.

Run:
  python examples/analyze_results.py --input examples/llm_surface_results.jsonl
  python examples/analyze_results.py --input examples/surface_ok_results.jsonl
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any


def load_rows(input_path: Path) -> list[dict[str, Any]]:
    if not input_path.exists():
        raise FileNotFoundError(f"Missing input file: {input_path}")

    rows: list[dict[str, Any]] = []
    with input_path.open("r", encoding="utf-8") as f:
        for line_number, line in enumerate(f, start=1):
            stripped = line.strip()
            if not stripped:
                continue

            try:
                row = json.loads(stripped)
            except json.JSONDecodeError as exc:
                raise ValueError(
                    f"Line {line_number}: invalid JSON: {exc.msg}"
                ) from exc

            if not isinstance(row, dict):
                raise ValueError(
                    f"Line {line_number}: JSON record must be an object"
                )

            rows.append(row)

    return rows


def analyze_rows(rows: list[dict[str, Any]]) -> dict[str, Any]:
    total_cases = len(rows)
    surface_ok_true = sum(1 for r in rows if r.get("surface_ok") is True)
    gate_status_counts = dict(Counter(r["gate_status"] for r in rows if "gate_status" in r))

    non_go_cases = [
        r["case_id"]
        for r in rows
        if r.get("surface_ok") is True
        and r.get("gate_status") != "GO"
        and "case_id" in r
    ]

    result: dict[str, Any] = {
        "total_cases": total_cases,
        "surface_ok_true": surface_ok_true,
        "gate_status_counts": gate_status_counts,
        "non_GO_ratio": f"{len(non_go_cases)}/{total_cases}" if total_cases else "0/0",
        "non_GO_surface_ok_cases": non_go_cases,
    }

    return result


def print_report(input_path: Path, analysis: dict[str, Any]) -> None:
    print("-" * 40)
    print("OMNIA ANALYSIS REPORT")
    print("-" * 40)
    print(f"input_file: {input_path}")
    print(f"total_cases: {analysis['total_cases']}")
    print(f"surface_ok_true: {analysis['surface_ok_true']}")
    print(f"gate_status_counts: {analysis['gate_status_counts']}")
    print(f"non_GO_ratio: {analysis['non_GO_ratio']}")

    print("\nnon_GO_surface_ok_cases:")
    non_go_cases = analysis["non_GO_surface_ok_cases"]
    if non_go_cases:
        for case_id in non_go_cases:
            print(f"- {case_id}")
    else:
        print("- none")

    print("\ncanonical_formula:")
    print("surface-readable output != always structurally admissible")
    print("-" * 40)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Analyze OMNIA JSONL result files."
    )
    parser.add_argument(
        "--input",
        required=True,
        type=Path,
        help="Path to a JSONL results file produced by OMNIA.",
    )
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    rows = load_rows(args.input)
    analysis = analyze_rows(rows)
    print_report(args.input, analysis)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())