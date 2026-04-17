"""
Analyze OMNIA retrieval-augmented answer mini-result.

Run:
  python examples/analyze_rag_answer_results.py
"""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path


INPUT_PATH = Path("examples/rag_answer_results.jsonl")


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
    surface_ok_true = sum(1 for r in rows if r.get("surface_ok") is True)
    status_counts = Counter(r["gate_status"] for r in rows)

    non_go_cases = [
        r["case_id"]
        for r in rows
        if r.get("surface_ok") is True and r["gate_status"] != "GO"
    ]

    print("-" * 40)
    print("OMNIA ANALYSIS REPORT: RAG ANSWER")
    print("-" * 40)
    print(f"total_cases: {total_cases}")
    print(f"surface_ok_true: {surface_ok_true}")
    print(f"gate_status_counts: {dict(status_counts)}")
    print(f"non_GO_ratio: {len(non_go_cases)}/{total_cases}")

    print("\nnon_GO_surface_ok_cases:")
    for case_id in non_go_cases:
        print(f"- {case_id}")

    print("\ncanonical_formula:")
    print("retrieval-grounded readable output != always structurally admissible")
    print("-" * 40)


if __name__ == "__main__":
    main()