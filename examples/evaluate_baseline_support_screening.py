from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List


DATASET_PATH = Path("data/support_screening_external_v1.jsonl")
BASELINE_RESULTS_PATH = Path("examples/support_screening_external_v1_baseline_results.jsonl")


def load_jsonl(path: Path) -> List[Dict[str, Any]]:
    items: List[Dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as f:
        for line_no, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                items.append(json.loads(line))
            except json.JSONDecodeError as exc:
                raise ValueError(f"Invalid JSON on line {line_no} of {path}: {exc}") from exc
    return items


def index_by_case_id(items: List[Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:
    out: Dict[str, Dict[str, Any]] = {}
    for item in items:
        case_id = item.get("case_id")
        if not isinstance(case_id, str) or not case_id.strip():
            raise ValueError("Each item must contain a non-empty string case_id")
        if case_id in out:
            raise ValueError(f"Duplicate case_id found: {case_id}")
        out[case_id] = item
    return out


def decision_allows_pass_forward(decision: str) -> bool:
    if decision == "PASS":
        return True
    if decision in {"REVIEW", "BLOCK"}:
        return False
    raise ValueError(f"Unknown baseline_decision: {decision}")


def evaluate(dataset_rows: List[Dict[str, Any]], baseline_rows: List[Dict[str, Any]]) -> Dict[str, Any]:
    dataset = index_by_case_id(dataset_rows)
    baseline = index_by_case_id(baseline_rows)

    if set(dataset.keys()) != set(baseline.keys()):
        missing_in_baseline = sorted(set(dataset.keys()) - set(baseline.keys()))
        missing_in_dataset = sorted(set(baseline.keys()) - set(dataset.keys()))
        raise ValueError(
            f"Case ID mismatch. Missing in baseline: {missing_in_baseline}. "
            f"Missing in dataset: {missing_in_dataset}."
        )

    total_cases = len(dataset)
    total_pass_labels = 0
    total_fail_labels = 0

    false_accepts = 0
    false_rejects = 0
    true_accepts = 0
    true_rejects = 0

    per_case: List[Dict[str, Any]] = []

    for case_id in sorted(dataset.keys()):
        label = dataset[case_id].get("label")
        decision = baseline[case_id].get("baseline_decision")

        if label not in {"PASS", "FAIL"}:
            raise ValueError(f"Invalid label for {case_id}: {label}")
        if decision not in {"PASS", "REVIEW", "BLOCK"}:
            raise ValueError(f"Invalid baseline_decision for {case_id}: {decision}")

        allows_pass = decision_allows_pass_forward(decision)

        if label == "PASS":
            total_pass_labels += 1
            if allows_pass:
                true_accepts += 1
                outcome = "true_accept"
            else:
                false_rejects += 1
                outcome = "false_reject"
        else:
            total_fail_labels += 1
            if allows_pass:
                false_accepts += 1
                outcome = "false_accept"
            else:
                true_rejects += 1
                outcome = "true_reject"

        per_case.append(
            {
                "case_id": case_id,
                "label": label,
                "baseline_decision": decision,
                "allows_pass_forward": allows_pass,
                "outcome": outcome,
            }
        )

    far = false_accepts / total_fail_labels if total_fail_labels else 0.0
    frr = false_rejects / total_pass_labels if total_pass_labels else 0.0

    return {
        "total_cases": total_cases,
        "total_pass_labels": total_pass_labels,
        "total_fail_labels": total_fail_labels,
        "true_accepts": true_accepts,
        "true_rejects": true_rejects,
        "false_accepts": false_accepts,
        "false_rejects": false_rejects,
        "false_accept_rate": round(far, 6),
        "false_reject_rate": round(frr, 6),
        "per_case": per_case,
    }


def main() -> None:
    dataset_rows = load_jsonl(DATASET_PATH)
    baseline_rows = load_jsonl(BASELINE_RESULTS_PATH)

    report = evaluate(dataset_rows, baseline_rows)

    print(json.dumps(
        {k: v for k, v in report.items() if k != "per_case"},
        indent=2,
        sort_keys=True,
    ))


if __name__ == "__main__":
    main()