import json
from pathlib import Path

INPUT = "results/real_validation_v2_results.jsonl"
OUTPUT = "results/real_validation_v2_omnia.jsonl"

def fake_omnia_signal(text):
    # placeholder minimo coerente
    # (finché non colleghi OMNIA reale)

    length = len(text.strip())

    if length == 0:
        return {"Ω": 0.0, "SEI": 1.0, "IRI": 0.0, "gate_status": "NO_GO"}

    if any(x in text for x in ["-","0"]) and len(text) < 3:
        return {"Ω": 0.1, "SEI": 0.9, "IRI": 0.1, "gate_status": "NO_GO"}

    if len(text) > 20:
        return {"Ω": 0.3, "SEI": 0.7, "IRI": 0.5, "gate_status": "UNSTABLE"}

    return {"Ω": 0.6, "SEI": 0.0, "IRI": 1.0, "gate_status": "GO"}


rows = []
counts = {"GO":0,"UNSTABLE":0,"NO_GO":0}

with open(INPUT) as f:
    for line in f:
        row = json.loads(line)
        signal = fake_omnia_signal(row["output"])
        row["omnia_signal"] = signal
        counts[signal["gate_status"]] += 1
        rows.append(row)

with open(OUTPUT, "w") as f:
    for r in rows:
        f.write(json.dumps(r) + "\n")

print("===================================")
print("OMNIA GATE V2")
print("===================================")
print("Counts:", counts)

# evaluation vs ground truth
tp = 0
fn = 0
fp = 0

for r in rows:
    is_error = r["verdict"] == "semantic_error"
    flagged = r["omnia_signal"]["gate_status"] != "GO"

    if is_error and flagged:
        tp += 1
    elif is_error and not flagged:
        fn += 1
    elif not is_error and flagged:
        fp += 1

print("\nDetection:")
print("TP (caught errors):", tp)
print("FN (missed):", fn)
print("FP (false alarm):", fp)