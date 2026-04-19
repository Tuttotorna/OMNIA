from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, Iterable, List


DATASET_PATH = Path("data/support_screening_external_v2.jsonl")
OUTPUT_PATH = Path("examples/support_screening_external_v2_baseline_results.jsonl")


HARD_FAILURE_MARKERS = [
    "the answer seems correct",
    "processed processed processed",
]


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


def is_readable_support_sentence(text: str) -> bool:
    text = text.strip()
    if not text:
        return False
    if len(text) < 12:
        return False
    if " " not in text:
        return False
    alpha_count = sum(ch.isalpha() for ch in text)
    if alpha_count < 8:
        return False
    return True


def has_hard_failure_marker(text: str) -> bool:
    lowered = text.lower()
    return any(marker in lowered for marker in HARD_FAILURE_MARKERS)


def baseline_decision(response: str) -> str:
    response = response.strip()

    if not response:
        return "BLOCK"
    if has_hard_failure_marker(response):
        return "BLOCK"
    if not is_readable_support_sentence(response):
        return "REVIEW"
    return "PASS"


def to_result(item: Dict[str, Any]) -> Dict[str, Any]:
    response = item["response"]
    decision = baseline_decision(response)

    return {
        "case_id": item["case_id"],
        "source": item["source"],
        "prompt": item["prompt"],
        "response": response,
        "label": item["label"],
        "baseline_decision": decision,
    }


def save_jsonl(path: Path, rows: Iterable[Dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")


def summarize(rows: List[Dict[str, Any]]) -> Dict[str, int]:
    summary = {"PASS": 0, "REVIEW": 0, "BLOCK": 0}
    for row in rows:
        summary[row["baseline_decision"]] += 1
    return summary


def main() -> None:
    items = load_jsonl(DATASET_PATH)
    results = [to_result(item) for item in items]
    save_jsonl(OUTPUT_PATH, results)

    summary = summarize(results)

    print(f"Loaded: {len(items)} cases")
    print(f"Wrote: {OUTPUT_PATH}")
    print("Baseline decisions:")
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()