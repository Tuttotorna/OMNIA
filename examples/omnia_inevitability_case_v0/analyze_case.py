"""
Analyze OMNIA inevitability case v0.

Run:
  python examples/omnia_inevitability_case_v0/analyze_case.py
"""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path


BASE_DIR = Path("examples/omnia_inevitability_case_v0")

BASELINE_PATH = BASE_DIR / "baseline_results.jsonl"
SCORES_PATH = BASE_DIR / "omnia_scores.jsonl"
ACTIONS_PATH = BASE_DIR / "gate_actions.jsonl"
FINAL_PATH = BASE_DIR / "final_results.jsonl"


def load_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        raise FileNotFoundError(f"Missing required file: {path}")

    rows = []
    with path.open("r", encoding="utf-8") as f:
        for line_number, line in enumerate(f, start=1):
            stripped = line.strip()
            if not stripped:
                continue
            try:
                row = json.loads(stripped)
            except json.JSONDecodeError as exc:
                raise ValueError(
                    f"{path} line {line_number}: invalid JSON: {exc.msg}"
                ) from exc
            if not isinstance(row, dict):
                raise ValueError(
                    f"{path} line {line_number}: JSON record must be an object"
                )
            rows.append(row)

    return rows


def index_by_case(rows: list[dict]) -> dict[str, dict]:
    indexed: dict[str, dict] = {}
    for row in rows:
        case_id = row.get("case_id")
        if not case_id:
            raise ValueError("Missing case_id in one or more rows")
        if case_id in indexed:
            raise ValueError(f"Duplicate case_id detected: {case_id}")
        indexed[case_id] = row
    return indexed


def main() -> None:
    baseline_rows = load_jsonl(BASELINE_PATH)
    score_rows = load_jsonl(SCORES_PATH)
    action_rows = load_jsonl(ACTIONS_PATH)
    final_rows = load_jsonl(FINAL_PATH)

    baseline = index_by_case(baseline_rows)
    scores = index_by_case(score_rows)
    actions = index_by_case(action_rows)
    final = index_by_case(final_rows)

    baseline_ids = set(baseline)
    score_ids = set(scores)
    action_ids = set(actions)
    final_ids = set(final)

    if not (baseline_ids == score_ids == action_ids == final_ids):
        raise ValueError(
            "Case ID mismatch across inevitability case files"
        )

    total_cases = len(baseline_ids)

    baseline_accept_count = sum(
        1 for row in baseline.values() if row.get("baseline_accept") is True
    )
    baseline_forwarded_count = sum(
        1 for row in final.values() if row.get("baseline_forwarded") is True
    )
    post_gate_forwarded_count = sum(
        1 for row in final.values() if row.get("post_gate_forwarded") is True
    )
    outcome_changed_count = sum(
        1 for row in final.values() if row.get("outcome_changed") is True
    )

    gate_status_counts = Counter(row["gate_status"] for row in scores.values())
    operational_action_counts = Counter(
        row["operational_action"] for row in actions.values()
    )
    final_outcome_counts = Counter(
        row["final_outcome"] for row in final.values()
    )

    print("-" * 56)
    print("OMNIA INEVITABILITY CASE V0")
    print("-" * 56)
    print(f"total_cases: {total_cases}")
    print(f"baseline_accept_count: {baseline_accept_count}")
    print(f"baseline_forwarded_count: {baseline_forwarded_count}")
    print(f"post_gate_forwarded_count: {post_gate_forwarded_count}")
    print(f"outcome_changed_count: {outcome_changed_count}")
    print(
        f"baseline_forwarded_rate: "
        f"{baseline_forwarded_count}/{total_cases}"
    )
    print(
        f"post_gate_forwarded_rate: "
        f"{post_gate_forwarded_count}/{total_cases}"
    )
    print(
        f"delta_forwarded: "
        f"{baseline_forwarded_count - post_gate_forwarded_count}"
    )

    print("\ngate_status_counts:")
    for key, value in gate_status_counts.items():
        print(f"- {key}: {value}")

    print("\noperational_action_counts:")
    for key, value in operational_action_counts.items():
        print(f"- {key}: {value}")

    print("\nfinal_outcome_counts:")
    for key, value in final_outcome_counts.items():
        print(f"- {key}: {value}")

    print("\ncanonical_formula:")
    print("baseline_pass != safe_to_pass_forward")
    print("-" * 56)


if __name__ == "__main__":
    main()