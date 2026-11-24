import shutil
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
SYNTH = BASE / "synthetic-data"
DD = BASE / "data-dictionaries" / "data_dictionary.csv"

MAPPING = {
    "01-judicial-public-issues": ["public_issue_registry.csv", "source_registry.csv"],
    "02-perma-discourse-topics": ["discourse_topic_aggregates.csv", "sentiment_analysis_results.csv"],
    "03-judicial-accessibility": ["judicial_access_indicators.csv"],
    "04-stakeholder-participation": ["stakeholder_groups.csv", "consultation_submissions.csv"],
    "05-regulatory-implementation": ["perma_registry.csv", "implementation_gap_analysis.csv"],
    "06-ex-post-ria-evidence": ["validated_evidence.csv", "regulatory_impact_evidence.csv"],
    "07-perma-reform-research": ["public_recommendations.csv", "policy_response_matrix.csv"],
}

for slug, csvs in MAPPING.items():
    dest = BASE / "kaggle" / slug
    dest.mkdir(parents=True, exist_ok=True)
    for c in csvs:
        shutil.copy2(SYNTH / c, dest / c)
    shutil.copy2(DD, dest / "data_dictionary.csv")

print(f"Staged CSVs and data_dictionary.csv into {len(MAPPING)}/7 Kaggle dataset folders.")
