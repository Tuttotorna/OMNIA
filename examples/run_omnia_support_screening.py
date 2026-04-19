from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, Iterable, List

from omnia import run_omnia


DATASET_PATH = Path("data/support_screening_external_v1.jsonl")
OUTPUT_PATH = Path("examples/support_screening_external_v1_omnia_results.jsonl")


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


def build_case(item: Dict[str, Any]) -> Dict[str, Any]:
    prompt = item.get("prompt", "")
    response = item.get("response", "")

    if not isinstance(prompt, str):
        raise TypeError(f"case {item.get('case_id', '<unknown>')} has non-string prompt")
    if not isinstance(response, str):
        raise TypeError(f"case {item.get('case_id', '<unknown>')} has non-string response")

    text = response.strip()

    variants = [
        response,
        response.strip(),
        response.rstrip(" .,!?:;"),
        response.lower(),
        f"Answer: {response.strip()}",
        f"Final answer: {response.strip()}",
        f"{prompt.strip()} -> {response.strip()}",
    ]

    return {
        "case_id": item["case_id"],
        "text": text,
        "variants": variants,
    }


def to_result(item: Dict[str, Any]) -> Dict[str, Any]:
    case = build_case(item)
    omnia_result = run_omnia(case)

    return {
        "case_id": item["case_id"],
        "source": item["source"],
        "prompt": item["prompt"],
        "response": item["response"],
        "label": item["label"],
        "omega_score": omnia_result["omega_score"],
        "sei_score": omnia_result["sei_score"],
        "iri_score": omnia_result["iri_score"],
        "drift_score": omnia_result["drift_score"],
        "limit_triggered": omnia_result["limit_triggered"],
        "gate_status": omnia_result["gate_status"],
        "reason_code": omnia_result["reason_code"],
    }


def save_jsonl(path: Path, rows: Iterable[Dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")


def summarize(rows: List[Dict[str, Any]]) -> Dict[str, int]:
    summary: Dict[str, int] = {}
    for row in rows:
        gate = row["gate_status"]
        summary[gate] = summary.get(gate, 0) + 1
    return dict(sorted(summary.items()))


def main() -> None:
    items = load_jsonl(DATASET_PATH)
    results = [to_result(item) for item in items]
    save_jsonl(OUTPUT_PATH, results)

    summary = summarize(results)

    print(f"Loaded: {len(items)} cases")
    print(f"Wrote: {OUTPUT_PATH}")
    print("OMNIA gate distribution:")
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()