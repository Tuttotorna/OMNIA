import json
import re
from pathlib import Path

INPUT_PATH = Path("examples/gsm_symbolic_v1_questions.jsonl")
OUTPUT_PATH = Path("examples/gsm_symbolic_v1_model_outputs.jsonl")


def load_jsonl(path):
    with open(path, "r", encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def save_jsonl(path, data):
    with open(path, "w", encoding="utf-8") as f:
        for row in data:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")


def extract_final_number(text):
    """
    STRICT extraction rule:
    - last numeric token
    - no normalization
    - return as string
    """
    matches = re.findall(r"-?\d+\.?\d*", text)
    if not matches:
        return ""
    return matches[-1]


def mock_model(question):
    """
    Replace this with real model call.

    For now: deterministic naive solver for testing pipeline only.
    This is NOT the real experiment.
    """

    # Very naive pattern-based solver (only for pipeline testing)
    try:
        numbers = list(map(int, re.findall(r"\d+", question)))

        if "boxes" in question and "apples" in question:
            if "buys" in question:
                return str(numbers[0] * numbers[1] + numbers[2])

        if "pages" in question:
            return str(sum(numbers))

        if "pencils" in question:
            return str(numbers[0] - numbers[1] - numbers[2] + numbers[3])

        if "trays" in question:
            return str(numbers[0] * numbers[1] - numbers[2])

        if "euros" in question:
            return str(numbers[0] * numbers[1] - numbers[2])

    except Exception:
        pass

    return "0"


def run():
    data = load_jsonl(INPUT_PATH)
    results = []

    for item in data:
        question = item["question"]
        expected = item["expected_answer"]

        raw_output = mock_model(question)

        extracted = extract_final_number(raw_output)

        is_correct = extracted == expected

        result = {
            "template_id": item["template_id"],
            "variant_id": item["variant_id"],
            "variant_type": item["variant_type"],
            "model_raw_output": raw_output,
            "model_final_extracted_answer": extracted,
            "is_correct": is_correct,
        }

        results.append(result)

    save_jsonl(OUTPUT_PATH, results)

    total = len(results)
    correct = sum(r["is_correct"] for r in results)

    print("===================================")
    print("GSM SYMBOLIC V1 BASELINE RUN")
    print("===================================")
    print(f"Total cases: {total}")
    print(f"Correct: {correct}")
    print(f"Accuracy: {correct/total:.3f}")
    print(f"Output saved to: {OUTPUT_PATH}")
    print("===================================")


if __name__ == "__main__":
    run()