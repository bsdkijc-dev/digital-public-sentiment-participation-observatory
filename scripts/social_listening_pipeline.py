import argparse
import csv
import json
from pathlib import Path
from pii_scrubber import scrub_pii, contains_pii

BASE = Path(__file__).resolve().parent.parent
TAXONOMY_PATH = BASE / "public-discourse-taxonomy" / "taxonomy.json"

POS_WORDS_ID = {"bagus", "mudah", "cepat", "membantu", "sepakat", "damai", "lancar", "baik", "ramah"}
NEG_WORDS_ID = {"susah", "lama", "lambat", "mahal", "error", "gagal", "rumit", "kecewa", "buruk", "tidak hadir"}
POS_WORDS_EN = {"helpful", "fast", "smooth", "clear", "resolved", "fair", "good"}
NEG_WORDS_EN = {"slow", "expensive", "error", "failed", "confusing", "delay", "absent", "unfair"}


def load_taxonomy() -> dict:
    return json.loads(TAXONOMY_PATH.read_text(encoding="utf-8"))


def classify_topic(text: str, taxonomy: dict) -> str:
    lower = text.lower()
    best_code = "TAX-07"
    best_hits = 0
    for cat in taxonomy["categories"]:
        hits = sum(1 for kw in cat["keywords_id"] + cat["keywords_en"] if kw in lower)
        if hits > best_hits:
            best_hits = hits
            best_code = cat["code"]
    return best_code


def classify_sentiment(text: str) -> str:
    lower = text.lower()
    pos = sum(1 for w in POS_WORDS_ID | POS_WORDS_EN if w in lower)
    neg = sum(1 for w in NEG_WORDS_ID | NEG_WORDS_EN if w in lower)
    if pos > 0 and neg > 0:
        return "MIXED"
    if neg > 0:
        return "NEGATIVE"
    if pos > 0:
        return "POSITIVE"
    if len(lower.split()) < 3:
        return "UNCLEAR"
    return "NEUTRAL"


def process_records(records: list[dict]) -> list[dict]:
    taxonomy = load_taxonomy()
    results = []
    for idx, rec in enumerate(records, start=1):
        clean_text = scrub_pii(rec.get("text", ""))
        assert not contains_pii(clean_text), f"PII leaked in record {idx}"
        topic = classify_topic(clean_text, taxonomy)
        sentiment = classify_sentiment(clean_text)
        results.append({
            "record_id": rec.get("record_id", f"SL-DRY-{idx:03d}"),
            "issue_category": topic,
            "sentiment_label": sentiment,
            "language": rec.get("language", "id"),
            "anonymised_excerpt": clean_text[:200],
        })
    return results


def main():
    parser = argparse.ArgumentParser(description="DSPPO v1.1 Lawful Social Listening Pipeline")
    parser.add_argument("--dry-run", action="store_true", help="Run on built-in synthetic test samples")
    parser.add_argument("--input-csv", type=str, help="Path to anonymised/local input CSV with 'text' column")
    parser.add_argument("--output-csv", type=str, help="Optional output CSV path")
    args = parser.parse_args()

    if args.dry_run or not args.input_csv:
        samples = [
            {"record_id": "DRY-001", "language": "id", "text": "Mediasi di pengadilan sangat membantu dan cepat sepakat, tapi biaya mediator non-hakim perlu dijelaskan di awal."},
            {"record_id": "DRY-002", "language": "id", "text": "Pihak lawan tidak hadir mediasi dan prosesnya lambat. Hubungi saya di user@example.com atau 081234567890."},
            {"record_id": "DRY-003", "language": "id", "text": "Aplikasi e-court sering error saat unggah berkas mediasi elektronik."},
            {"record_id": "DRY-004", "language": "en", "text": "The mediation schedule information on SIPP is clear and helpful."},
        ]
    else:
        with open(args.input_csv, encoding="utf-8") as f:
            samples = list(csv.DictReader(f))

    out = process_records(samples)
    if args.output_csv:
        with open(args.output_csv, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=list(out[0].keys()))
            writer.writeheader()
            writer.writerows(out)
    print(json.dumps(out, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
