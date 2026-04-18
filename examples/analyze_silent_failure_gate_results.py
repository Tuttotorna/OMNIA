"""
Analyze OMNIA Silent Failure Gate first case.

Run:
  python examples/analyze_silent_failure_gate_results.py
"""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path


INPUT_PATH = Path("examples/silent_failure_gate_results.jsonl")


def main() -> None:
    if not INPUT_PATH.exists():
        raise FileNotFoundError(
            f"Missing input file: {INPUT_PATH}. "
            "Run the JSONL pipeline first."
        )

    rows = []
    with INPUT_PATH.open("r", encoding="utf-8") as f:
        for line in f:
            stripped = line.strip()
            if not stripped:
                continue
            rows.append(json.loads(stripped))

    total_cases = len(rows)
    baseline_pass_true = sum(1 for r in rows if r.get("baseline_pass") is True)
    surface_ok_true = sum(1 for r in rows if r.get("surface_ok") is True)
    status_counts = Counter(r["gate_status"] for r in rows)

    non_go_cases = [
        r["case_id"]
        for r in rows
        if r.get("gate_status") != "GO"
    ]

    action_map = {
        "GO": "allow",
        "RISK": "flag_for_review",
        "NO_GO": "block_and_escalate",
        "UNSTABLE": "block_and_escalate",
    }

    action_counts = Counter(action_map[r["gate_status"]] for r in rows)

    print("-" * 48)
    print("OMNIA ANALYSIS REPORT: SILENT FAILURE GATE")
    print("-" * 48)
    print(f"total_cases: {total_cases}")
    print(f"baseline_pass_true: {baseline_pass_true}")
    print(f"surface_ok_true: {surface_ok_true}")
    print(f"gate_status_counts: {dict(status_counts)}")
    print(f"non_GO_ratio: {len(non_go_cases)}/{total_cases}")
    print(f"derived_action_counts: {dict(action_counts)}")

    print("\nnon_GO_cases:")
    for case_id in non_go_cases:
        print(f"- {case_id}")

    print("\ncanonical_formula:")
    print("baseline_pass != safe_to_pass_forward")
    print("-" * 48)


if __name__ == "__main__":
    main()