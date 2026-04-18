"""
Rebuild derived OMNIA inevitability case v0 artifacts.

Run:
    python examples/omnia_inevitability_case_v0/rebuild_case_outputs.py
"""

from __future__ import annotations

import json
from pathlib import Path


BASE_DIR = Path("examples/omnia_inevitability_case_v0")

BASELINE_PATH = BASE_DIR / "baseline_results.jsonl"
SCORES_PATH = BASE_DIR / "omnia_scores.jsonl"
ACTIONS_PATH = BASE_DIR / "gate_actions.jsonl"
FINAL_PATH = BASE_DIR / "final_results.jsonl"


ACTION_MAP = {
    "GO": ("allow", "allow"),
    "RISK": ("flag_for_review", "review_required"),
    "NO_GO": ("block_and_escalate", "escalation_required"),
    "UNSTABLE": ("block_and_escalate", "escalation_required"),
}

ACTION_RATIONALE_MAP = {
    "GO": "structural profile remains admissible for unchanged forwarding",
    "RISK": "surface-acceptable output is structurally fragile and should not pass forward unchanged",
    "NO_GO": "structural profile is not admissible for unchanged forwarding and requires escalation",
    "UNSTABLE": "collapsed structural profile makes the output operationally unreliable",
}


def load_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        raise FileNotFoundError(f"Missing required file: {path}")

    rows: list[dict] = []
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


def write_jsonl(path: Path, rows: list[dict]) -> None:
    with path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=True) + "\n")


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


def build_gate_action(case_id: str, score_row: dict) -> dict:
    gate_status = score_row["gate_status"]
    reason_code = score_row["reason_code"]

    if gate_status not in ACTION_MAP:
        raise ValueError(f"Unsupported gate_status for {case_id}: {gate_status}")

    operational_action, _ = ACTION_MAP[gate_status]
    action_rationale = ACTION_RATIONALE_MAP[gate_status]

    return {
        "case_id": case_id,
        "gate_status": gate_status,
        "reason_code": reason_code,
        "operational_action": operational_action,
        "action_rationale": action_rationale,
    }


def build_final_result(case_id: str, baseline_row: dict, score_row: dict) -> dict:
    gate_status = score_row["gate_status"]

    if gate_status not in ACTION_MAP:
        raise ValueError(f"Unsupported gate_status for {case_id}: {gate_status}")

    operational_action, final_outcome = ACTION_MAP[gate_status]

    # In this bounded v0 case, baseline_accept implies baseline_forwarded.
    baseline_forwarded = baseline_row.get("baseline_accept") is True
    post_gate_forwarded = gate_status == "GO"
    outcome_changed = baseline_forwarded != post_gate_forwarded

    if operational_action == "allow":
        post_gate_status = "allowed"
    elif operational_action == "flag_for_review":
        post_gate_status = "flagged_for_review"
    elif operational_action == "block_and_escalate":
        post_gate_status = "blocked_and_escalated"
    else:
        raise ValueError(
            f"Unsupported operational action for {case_id}: {operational_action}"
        )

    return {
        "case_id": case_id,
        "baseline_forwarded": baseline_forwarded,
        "post_gate_forwarded": post_gate_forwarded,
        "post_gate_status": post_gate_status,
        "outcome_changed": outcome_changed,
        "final_outcome": final_outcome,
    }


def main() -> int:
    baseline_rows = load_jsonl(BASELINE_PATH)
    score_rows = load_jsonl(SCORES_PATH)

    baseline = index_by_case(baseline_rows)
    scores = index_by_case(score_rows)

    if set(baseline) != set(scores):
        raise ValueError(
            "Case ID mismatch between baseline_results.jsonl and omnia_scores.jsonl"
        )

    ordered_case_ids = [row["case_id"] for row in baseline_rows]

    gate_actions = [
        build_gate_action(case_id, scores[case_id])
        for case_id in ordered_case_ids
    ]
    final_results = [
        build_final_result(case_id, baseline[case_id], scores[case_id])
        for case_id in ordered_case_ids
    ]

    write_jsonl(ACTIONS_PATH, gate_actions)
    write_jsonl(FINAL_PATH, final_results)

    print("-" * 56)
    print("OMNIA INEVITABILITY CASE V0 - REBUILD")
    print("-" * 56)
    print(f"baseline input: {BASELINE_PATH}")
    print(f"score input:    {SCORES_PATH}")
    print(f"rebuilt:        {ACTIONS_PATH}")
    print(f"rebuilt:        {FINAL_PATH}")
    print("-" * 56)
    print("done")
    print("-" * 56)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())