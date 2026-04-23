import json
import os
from collections import defaultdict, Counter

# =========================
# CONFIG
# =========================

QUESTIONS_PATH = "examples/gsm_symbolic_v0_questions.jsonl"
MODEL_OUTPUTS_PATH = "examples/gsm_symbolic_v0_model_outputs.jsonl"
OMNIA_SCORES_PATH = "examples/gsm_symbolic_v0_omnia_scores.jsonl"

# soglie (tuning semplice)
FRAGILITY_THRESHOLD = None  # se None → usa ranking relativo
CONSISTENCY_RUNS = 1        # se hai multi-run, aumenta


# =========================
# UTILS
# =========================

def load_jsonl(path):
    data = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            data.append(json.loads(line))
    return data


def group_by_template(records):
    grouped = defaultdict(list)
    for r in records:
        grouped[r["template_id"]].append(r)
    return grouped


def find_base_variant(variants):
    for v in variants:
        if v["variant_type"] == "base":
            return v
    return None


def is_high_fragility(base_variant, variants):
    # Caso 1: uso diretto fragility_rank
    if "fragility_rank" in base_variant:
        # rank più alto = più fragile (assunzione coerente col tuo schema)
        ranks = [v.get("fragility_rank") for v in variants if "fragility_rank" in v]
        if not ranks:
            return False
        max_rank = max(ranks)
        return base_variant["fragility_rank"] == max_rank

    # Caso 2: fallback su omnia_score
    if "omnia_score" in base_variant:
        scores = [v.get("omnia_score") for v in variants if "omnia_score" in v]
        if not scores:
            return False

        # più basso = più fragile (assunzione tipica)
        min_score = min(scores)
        return base_variant["omnia_score"] == min_score

    return False


def baseline_consistency(variants):
    """
    Versione minimale:
    misura quanto le risposte sono coerenti tra varianti.
    """
    answers = [v.get("model_final_extracted_answer") for v in variants]
    answers = [a for a in answers if a is not None]

    if not answers:
        return 0.0

    count = Counter(answers)
    most_common = count.most_common(1)[0][1]

    return most_common / len(answers)


def baseline_flag_low_consistency(variants, threshold=0.6):
    return baseline_consistency(variants) < threshold


# =========================
# MAIN
# =========================

def main():

    if not os.path.exists(MODEL_OUTPUTS_PATH):
        print("Missing model outputs file")
        return

    if not os.path.exists(OMNIA_SCORES_PATH):
        print("Missing OMNIA scores file")
        return

    outputs = load_jsonl(MODEL_OUTPUTS_PATH)
    omnia = load_jsonl(OMNIA_SCORES_PATH)

    # merge per template_id + variant_type
    merged = []
    for o, om in zip(outputs, omnia):
        m = {}
        m.update(o)
        m.update(om)
        merged.append(m)

    grouped = group_by_template(merged)

    total_templates = len(grouped)

    surface_correct = 0
    collapsing = 0

    omnia_hits = 0
    baseline_hits = 0

    analyzed = []

    for template_id, variants in grouped.items():

        base = find_base_variant(variants)
        if not base:
            continue

        if not base.get("is_correct"):
            continue

        surface_correct += 1

        # verifica collasso
        collapse = any(not v.get("is_correct", False) for v in variants)

        if not collapse:
            continue

        collapsing += 1

        omnia_flag = is_high_fragility(base, variants)
        baseline_flag = baseline_flag_low_consistency(variants)

        if omnia_flag:
            omnia_hits += 1

        if baseline_flag:
            baseline_hits += 1

        analyzed.append({
            "template_id": template_id,
            "collapse": True,
            "omnia_flag": omnia_flag,
            "baseline_flag": baseline_flag
        })

    # =========================
    # REPORT
    # =========================

    print("\nOMNIA vs BASELINE — MINI VALIDATION\n")

    print(f"Templates analyzed: {total_templates}")
    print(f"Surface-correct: {surface_correct}")
    print(f"Collapsing under perturbation: {collapsing}\n")

    if collapsing > 0:
        print(f"OMNIA detection rate: {omnia_hits / collapsing:.3f}")
        print(f"Baseline detection rate: {baseline_hits / collapsing:.3f}")
    else:
        print("No collapsing cases detected")

    print("\nSample cases:\n")

    for r in analyzed[:10]:
        print(r)


if __name__ == "__main__":
    main()