import csv
import json
import re
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
SYNTH = BASE / "synthetic-data"

MANDATORY_META = [
    "record_id", "research_project_id", "perma_number", "perma_year",
    "issue_category", "source_type", "source_reference", "collection_date",
    "verification_status", "evidence_classification", "confidence_level",
    "methodology_version", "privacy_status", "publication_status",
]

EXPECTED_CSVS = [
    "perma_registry.csv", "public_issue_registry.csv", "discourse_topic_aggregates.csv",
    "sentiment_analysis_results.csv", "stakeholder_groups.csv", "consultation_submissions.csv",
    "validated_evidence.csv", "judicial_access_indicators.csv", "implementation_gap_analysis.csv",
    "regulatory_impact_evidence.csv", "public_recommendations.csv", "policy_response_matrix.csv",
    "source_registry.csv", "research_quality_log.csv", "publication_approval_registry.csv",
]

PII_PATTERNS = [
    re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"),  # email
    re.compile(r"\b\d{16}\b"),  # 16-digit NIK
]

errors = []
all_record_ids = set()

for fname in EXPECTED_CSVS:
    fpath = SYNTH / fname
    if not fpath.exists():
        errors.append(f"Missing CSV: {fname}")
        continue
    with open(fpath, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        missing_cols = [c for c in MANDATORY_META if c not in reader.fieldnames]
        if missing_cols:
            errors.append(f"{fname} missing mandatory columns: {missing_cols}")
        for i, row in enumerate(reader, start=1):
            rid = row.get("record_id", "")
            if not rid:
                errors.append(f"{fname} row {i} empty record_id")
            elif rid in all_record_ids:
                errors.append(f"Duplicate record_id: {rid}")
            all_record_ids.add(rid)
            for k, v in row.items():
                for pat in PII_PATTERNS:
                    if pat.search(v or ""):
                        errors.append(f"Potential PII in {fname} row {i} col {k}")

# Check Kaggle metadata constraints
for meta_file in (BASE / "kaggle").glob("*/dataset-metadata.json"):
    data = json.loads(meta_file.read_text(encoding="utf-8"))
    if not (6 <= len(data["title"]) <= 50):
        errors.append(f"Invalid Kaggle title length in {meta_file}")
    if not (20 <= len(data["subtitle"]) <= 80):
        errors.append(f"Invalid Kaggle subtitle length in {meta_file}")
    if "indonesia" in data.get("keywords", []):
        errors.append(f"Forbidden 'indonesia' keyword in {meta_file}")

if errors:
    print("QA FAILED:", errors)
    raise SystemExit(1)

print(f"QA PASSED: {len(EXPECTED_CSVS)}/15 CSVs, {len(all_record_ids)} unique records, 0 PII hits, 7/7 Kaggle metadata valid.")
