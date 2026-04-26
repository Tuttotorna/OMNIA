import json
import re
import random
import time
from collections import defaultdict

# ==============================
# CONFIG
# ==============================

DATASET_PATH = "examples/gsm_symbolic_v0_questions.jsonl"
OUTPUT_PATH = "results_fragility.jsonl"

MODEL = "gpt-4o-mini"  # oppure cambia con modello open
N_PERTURB = 1

# ==============================
# MODEL CALL (OpenAI)
# ==============================

def call_model(prompt):
    from openai import OpenAI
    client = OpenAI()

    resp = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    return resp.choices[0].message.content.strip()

# ==============================
# EXTRACTION
# ==============================

def extract_final_number(text):
    numbers = re.findall(r"-?\d+\.?\d*", text)
    if not numbers:
        return None
    return numbers[-1]

# ==============================
# PERTURBATION (MINIMA)
# ==============================

def perturb_question(q):
    # semplice: cambia un numero piccolo
    def repl(match):
        val = int(match.group())
        return str(val + 1)

    return re.sub(r"\b\d+\b", repl, q, count=1)

# ==============================
# OMNIA PROXY (placeholder)
# ==============================

def omnia_fragility_score(text):
    # proxy minimale: lunghezza + variazione token
    tokens = text.split()
    if not tokens:
        return 0
    unique_ratio = len(set(tokens)) / len(tokens)
    return 1 - unique_ratio  # più ripetizione = più fragile

# ==============================
# MAIN
# ==============================

def main():
    results = []

    with open(DATASET_PATH) as f:
        data = [json.loads(x) for x in f]

    for i, item in enumerate(data):
        q = item["question"]
        expected = item["expected_answer"]

        # ===== ORIGINAL =====
        raw = call_model(q)
        pred = extract_final_number(raw)
        correct = (pred == expected)

        score = omnia_fragility_score(raw)

        # ===== PERTURB =====
        q_pert = perturb_question(q)
        raw_p = call_model(q_pert)
        pred_p = extract_final_number(raw_p)
        correct_p = (pred_p == expected)

        flipped = (correct and not correct_p)

        results.append({
            "id": i,
            "correct": correct,
            "correct_after_perturb": correct_p,
            "flipped": flipped,
            "fragility_score": score
        })

        print(f"{i}: correct={correct} -> perturbed={correct_p} | flipped={flipped}")

        time.sleep(0.5)

    with open(OUTPUT_PATH, "w") as f:
        for r in results:
            f.write(json.dumps(r) + "\n")

    analyze(results)


# ==============================
# ANALYSIS
# ==============================

def analyze(results):
    high = []
    low = []

    threshold = sorted([r["fragility_score"] for r in results])[len(results)//2]

    for r in results:
        if r["correct"]:
            if r["fragility_score"] >= threshold:
                high.append(r)
            else:
                low.append(r)

    def instability(group):
        if not group:
            return 0
        flips = sum(1 for x in group if x["flipped"])
        return flips / len(group)

    print("\n===== FINAL REPORT =====")
    print(f"HIGH fragility: {len(high)} | instability_rate={instability(high):.3f}")
    print(f"LOW  fragility: {len(low)} | instability_rate={instability(low):.3f}")


if __name__ == "__main__":
    main()