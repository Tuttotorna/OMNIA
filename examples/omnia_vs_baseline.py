import json
import os
from collections import Counter

CASES_PATH = "examples/llm_surface_cases.jsonl"
RESULTS_PATH = "examples/llm_surface_results.jsonl"


def load_jsonl(path):
    rows = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def main():
    if not os.path.exists(CASES_PATH):
        print(f"Missing cases file: {CASES_PATH}")
        return

    if not os.path.exists(RESULTS_PATH):
        print(f"Missing results file: {RESULTS_PATH}")
        return

    cases = load_jsonl(CASES_PATH)
    results = load_jsonl(RESULTS_PATH)

    print("\nOMNIA vs BASELINE — MINI VALIDATION\n")
    print(f"Cases file: {CASES_PATH}")
    print(f"Results file: {RESULTS_PATH}")
    print(f"Cases loaded: {len(cases)}")
    print(f"Results loaded: {len(results)}\n")

    if not results:
        print("No results found")
        return

    keys = Counter()
    gate_status = Counter()
    verdicts = Counter()

    for row in results:
        for k in row.keys():
            keys[k] += 1

        if "gate_status" in row:
            gate_status[str(row["gate_status"])] += 1

        if "verdict" in row:
            verdicts[str(row["verdict"])] += 1

    print("FIELDS FOUND:\n")
    for k, v in keys.most_common():
        print(f"{k}: {v}")

    if gate_status:
        print("\nGATE STATUS COUNTS:\n")
        total = sum(gate_status.values())
        for k, v in gate_status.items():
            print(f"{k}: {v} ({v/total:.3f})")

    if verdicts:
        print("\nVERDICT COUNTS:\n")
        total = sum(verdicts.values())
        for k, v in verdicts.items():
            print(f"{k}: {v} ({v/total:.3f})")

    print("\nSAMPLE ROWS:\n")
    for row in results[:5]:
        print(json.dumps(row, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()