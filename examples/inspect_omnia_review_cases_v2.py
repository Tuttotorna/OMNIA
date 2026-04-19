from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List


DATASET_PATH = Path("data/support_screening_external_v2.jsonl")
BASELINE_RESULTS_PATH = Path("examples/support_screening_external_v2_baseline_results.jsonl")
OMNIA_RESULTS_PATH = Path("examples/support_screening_external_v2_omnia_results.jsonl")


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


def severity(decision: str) -> int:
    mapping = {"PASS": 0, "REVIEW": 1, "BLOCK": 2}
    if decision not in mapping:
        raise ValueError(f"Unknown decision: {decision}")
    return mapping[decision]


def combine_baseline_and_omnia(baseline_decision: str, gate_status: str) -> str:
    omnia_operational = mapped_omnia_gate_to_operational(gate_status)
    return baseline_decision if severity(baseline_decision) >= severity(omnia_operational) else omnia_operational


def main() -> None:
    dataset = index_by_case_id(load_jsonl(DATASET_PATH))
    baseline = index_by_case_id(load_jsonl(BASELINE_RESULTS_PATH))
    omnia = index_by_case_id(load_jsonl(OMNIA_RESULTS_PATH))

    case_ids = sorted(dataset.keys())
    if set(case_ids) != set(baseline.keys()) or set(case_ids) != set(omnia.keys()):
        raise ValueError("Case ID mismatch across dataset, baseline, and OMNIA results")

    improved_cases: List[Dict[str, Any]] = []

    for case_id in case_ids:
        baseline_decision = baseline[case_id]["baseline_decision"]
        gate_status = omnia[case_id]["gate_status"]
        combined_decision = combine_baseline_and_omnia(baseline_decision, gate_status)
        label = dataset[case_id]["label"]

        baseline_pass = baseline_decision == "PASS"
        combined_not_pass = combined_decision in {"REVIEW", "BLOCK"}

        if baseline_pass and combined_not_pass:
            improved_cases.append(
                {
                    "case_id": case_id,
                    "label": label,
                    "prompt": dataset[case_id]["prompt"],
                    "response": dataset[case_id]["response"],
                    "baseline_decision": baseline_decision,
                    "omnia_gate_status": gate_status,
                    "combined_decision": combined_decision,
                    "omega_score": omnia[case_id]["omega_score"],
                    "sei_score": omnia[case_id]["sei_score"],
                    "iri_score": omnia[case_id]["iri_score"],
                    "drift_score": omnia[case_id]["drift_score"],
                    "reason_code": omnia[case_id]["reason_code"],
                }
            )

    print(json.dumps(improved_cases, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()