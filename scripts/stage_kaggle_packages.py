import json
import shutil
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
SYNTH = BASE / "synthetic-data"
VAL = BASE / "validated-evidence"
DD = BASE / "data-dictionaries" / "data_dictionary.csv"

MAPPING = {
    "01-judicial-public-issues": [SYNTH / "public_issue_registry.csv", SYNTH / "source_registry.csv"],
    "02-perma-discourse-topics": [SYNTH / "discourse_topic_aggregates.csv", SYNTH / "sentiment_analysis_results.csv"],
    "03-judicial-accessibility": [SYNTH / "judicial_access_indicators.csv"],
    "04-stakeholder-participation": [SYNTH / "stakeholder_groups.csv", SYNTH / "consultation_submissions.csv"],
    "05-regulatory-implementation": [
        SYNTH / "perma_registry.csv",
        SYNTH / "implementation_gap_analysis.csv",
        VAL / "pilot1_live_official_metrics.csv",
        VAL / "pilot2_live_official_metrics.csv",
        VAL / "pilot3_live_official_records.csv",
    ],
    "06-ex-post-ria-evidence": [
        SYNTH / "validated_evidence.csv",
        SYNTH / "regulatory_impact_evidence.csv",
        VAL / "pilot4_live_official_records.csv",
        VAL / "pilot5_live_official_records.csv",
    ],
    "07-perma-reform-research": [SYNTH / "public_recommendations.csv", SYNTH / "policy_response_matrix.csv"],
}

for slug, csvs in MAPPING.items():
    dest = BASE / "kaggle" / slug
    dest.mkdir(parents=True, exist_ok=True)
    for src in csvs:
        if src.exists():
            shutil.copy2(src, dest / src.name)
    shutil.copy2(DD, dest / "data_dictionary.csv")
    meta_path = dest / "dataset-metadata.json"
    if meta_path.exists():
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
        meta["keywords"] = [k for k in meta.get("keywords", []) if k not in ("public-policy", "indonesia")]
        meta_path.write_text(json.dumps(meta, indent=2), encoding="utf-8")

print(f"Staged updated CSVs and cleaned Kaggle tags across {len(MAPPING)}/7 Kaggle dataset folders.")
