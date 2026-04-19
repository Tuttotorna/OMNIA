from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List


DATASET_PATH = Path("data/account_access_hollow_responses_v1.jsonl")
BASELINE_RESULTS_PATH = Path("examples/account_access_hollow_v1_baseline_results.jsonl")
OMNIA_RESULTS_PATH = Path("examples/account_access_hollow_v1_omnia_results.jsonl")


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


def severity_of_operational_decision(decision: str) -> int:
    mapping = {
        "PASS": 0,
        "REVIEW": 1,
        "BLOCK": 2,
    }
    if decision not in mapping:
        raise ValueError(f"Unknown operational decision: {decision}")
    return mapping[decision]


def mapped_omnia_gate_to_operational(gate_status: str) -> str:
    mapping = {
        "GO": "PASS",
        "RISK": "REVIEW",
        "NO_GO": "BLOCK",
        "UNSTABLE": "BLOCK",
    }
    if gate_status not in mapping:
        raise ValueError(f"Unknown OMNIA gate_status: {gate_status}")
    return mapping[gate_status]


def combine_baseline_and_omnia(baseline_decision: str, gate_status: str) -> str:
    omnia_operational = mapped_omnia_gate_to_operational(gate_status)

    baseline_severity = severity_of_operational_decision(baseline_decision)
    omnia_severity = severity_of_operational_decision(omnia_operational)

    return baseline_decision if baseline_severity >= omnia_severity else omnia_operational


def allows_pass_forward(operational_decision: str) -> bool:
    if operational_decision == "PASS":
        return True
    if operational_decision in {"REVIEW", "BLOCK"}:
        return False
    raise ValueError(f"Unknown operational decision: {operational_decision}")


def evaluate_system(
    dataset: Dict[str, Dict[str, Any]],
    decisions: Dict[str, str],
) -> Dict[str, Any]:
    total_cases = len(dataset)
    total_pass_labels = 0
    total_fail_labels = 0

    true_accepts = 0
    true_rejects = 0
    false_accepts = 0
    false_rejects = 0
    review_count = 0

    per_case: List[Dict[str, Any]] = []

    for case_id in sorted(dataset.keys()):
        label = dataset[case_id]["label"]
        decision = decisions[case_id]

        if label not in {"PASS", "FAIL"}:
            raise ValueError(f"Invalid label for {case_id}: {label}")

        if decision == "REVIEW":
            review_count += 1

        pass_forward = allows_pass_forward(decision)

        if label == "PASS":
            total_pass_labels += 1
            if pass_forward:
                true_accepts += 1
                outcome = "true_accept"
            else:
                false_rejects += 1
                outcome = "false_reject"
        else:
            total_fail_labels += 1
            if pass_forward:
                false_accepts += 1
                outcome = "false_accept"
            else:
                true_rejects += 1
                outcome = "true_reject"

        per_case.append(
            {
                "case_id": case_id,
                "label": label,
                "decision": decision,
                "outcome": outcome,
            }
        )

    far = false_accepts / total_fail_labels if total_fail_labels else 0.0
    frr = false_rejects / total_pass_labels if total_pass_labels else 0.0
    review_rate = review_count / total_cases if total_cases else 0.0

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
        "review_count": review_count,
        "review_rate": round(review_rate, 6),
        "per_case": per_case,
    }


def main() -> None:
    dataset_rows = load_jsonl(DATASET_PATH)
    baseline_rows = load_jsonl(BASELINE_RESULTS_PATH)
    omnia_rows = load_jsonl(OMNIA_RESULTS_PATH)

    dataset = index_by_case_id(dataset_rows)
    baseline = index_by_case_id(baseline_rows)
    omnia = index_by_case_id(omnia_rows)

    if set(dataset.keys()) != set(baseline.keys()) or set(dataset.keys()) != set(omnia.keys()):
        raise ValueError("Case ID mismatch across dataset, baseline, and OMNIA results")

    baseline_decisions: Dict[str, str] = {}
    combined_decisions: Dict[str, str] = {}

    for case_id in sorted(dataset.keys()):
        baseline_decision = baseline[case_id]["baseline_decision"]
        gate_status = omnia[case_id]["gate_status"]

        baseline_decisions[case_id] = baseline_decision
        combined_decisions[case_id] = combine_baseline_and_omnia(
            baseline_decision=baseline_decision,
            gate_status=gate_status,
        )

    baseline_report = evaluate_system(dataset, baseline_decisions)
    combined_report = evaluate_system(dataset, combined_decisions)

    summary = {
        "baseline": {k: v for k, v in baseline_report.items() if k != "per_case"},
        "baseline_plus_omnia": {k: v for k, v in combined_report.items() if k != "per_case"},
    }

    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()