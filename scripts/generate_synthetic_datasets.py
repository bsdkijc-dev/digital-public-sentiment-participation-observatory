import csv
import json
import os
import random
from pathlib import Path

SEED = 20261124
random.seed(SEED)

BASE = Path("artifacts/file_generation/ttl=63d/intermediate/digital-public-sentiment-participation-observatory")

MANDATORY_META = [
    "record_id",
    "research_project_id",
    "perma_number",
    "perma_year",
    "issue_category",
    "source_type",
    "source_reference",
    "collection_date",
    "verification_status",
    "evidence_classification",
    "confidence_level",
    "methodology_version",
    "privacy_status",
    "publication_status",
]

# 1. Verified PERMA Registry (real official metadata)
PERMA_RECORDS = [
    ("PERMA-2015-02", "2", "2015", "TAX-04", "OFFICIAL_JDIH", "https://peraturan.bpk.go.id/Details/209475/perma-no-2-tahun-2015", "2026-11-24", "VERIFIED", "LEVEL_1_OFFICIAL", "HIGH", "v1.1", "PUBLIC_OFFICIAL", "APPROVED_PUBLIC_METADATA", "Tata Cara Penyelesaian Gugatan Sederhana", "AMENDED_BY_PERMA_4_2019", "2015-08-07"),
    ("PERMA-2019-04", "4", "2019", "TAX-04", "OFFICIAL_JDIH", "https://peraturan.bpk.go.id/Details/206070/perma-no-4-tahun-2019", "2026-11-24", "VERIFIED", "LEVEL_1_OFFICIAL", "HIGH", "v1.1", "PUBLIC_OFFICIAL", "APPROVED_PUBLIC_METADATA", "Perubahan atas PERMA Nomor 2 Tahun 2015 tentang Tata Cara Penyelesaian Gugatan Sederhana", "IN_FORCE", "2019-08-20"),
    ("PERMA-2016-01", "1", "2016", "TAX-03", "OFFICIAL_JDIH", "https://peraturan.bpk.go.id/Details/209641/perma-no-1-tahun-2016", "2026-11-24", "VERIFIED", "LEVEL_1_OFFICIAL", "HIGH", "v1.1", "PUBLIC_OFFICIAL", "APPROVED_PUBLIC_METADATA", "Prosedur Mediasi di Pengadilan", "IN_FORCE_PILOT_1", "2016-02-04"),
    ("PERMA-2022-03", "3", "2022", "TAX-02", "OFFICIAL_JDIH", "https://peraturan.bpk.go.id/Download/211652/Perma%20Nomor%203%20Tahun%202022.pdf?embed=True", "2026-11-24", "VERIFIED", "LEVEL_1_OFFICIAL", "HIGH", "v1.1", "PUBLIC_OFFICIAL", "APPROVED_PUBLIC_METADATA", "Mediasi di Pengadilan Secara Elektronik", "IN_FORCE_COMPLEMENTS_1_2016", "2022-06-01"),
    ("PERMA-2017-03", "3", "2017", "TAX-05", "OFFICIAL_JDIH", "https://peraturan.bpk.go.id/Details/209695/perma-no-3-tahun-2017", "2026-11-24", "VERIFIED", "LEVEL_1_OFFICIAL", "HIGH", "v1.1", "PUBLIC_OFFICIAL", "APPROVED_PUBLIC_METADATA", "Pedoman Mengadili Perkara Perempuan Berhadapan dengan Hukum", "IN_FORCE", "2017-08-04"),
    ("PERMA-2019-01", "1", "2019", "TAX-02", "OFFICIAL_JDIH", "https://peraturan.bpk.go.id/Details/206067/perma-no-1-tahun-2019", "2026-11-24", "VERIFIED", "LEVEL_1_OFFICIAL", "HIGH", "v1.1", "PUBLIC_OFFICIAL", "APPROVED_PUBLIC_METADATA", "Administrasi Perkara dan Persidangan di Pengadilan Secara Elektronik", "AMENDED_BY_PERMA_7_2022", "2019-08-19"),
    ("PERMA-2022-07", "7", "2022", "TAX-02", "OFFICIAL_JDIH", "https://peraturan.bpk.go.id/Details/248072/perma-no-7-tahun-2022", "2026-11-24", "VERIFIED", "LEVEL_1_OFFICIAL", "HIGH", "v1.1", "PUBLIC_OFFICIAL", "APPROVED_PUBLIC_METADATA", "Perubahan atas PERMA Nomor 1 Tahun 2019 tentang Administrasi Perkara dan Persidangan di Pengadilan Secara Elektronik", "IN_FORCE", "2022-10-11"),
    ("PERMA-2022-01", "1", "2022", "TAX-06", "OFFICIAL_JDIH", "https://peraturan.bpk.go.id/Details/209702/perma-no-1-tahun-2022", "2026-11-24", "VERIFIED", "LEVEL_1_OFFICIAL", "HIGH", "v1.1", "PUBLIC_OFFICIAL", "APPROVED_PUBLIC_METADATA", "Tata Cara Penyelesaian Permohonan dan Pemberian Restitusi dan Kompensasi kepada Korban Tindak Pidana", "IN_FORCE", "2022-03-01"),
]

def write_csv(path: Path, fieldnames: list[str], rows: list[dict]):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

def base_meta(rec_id, perma_num="1", perma_yr="2016", cat="TAX-03", src_type="SYNTHETIC_PILOT", src_ref="SYNTHETIC_SEED_20261124", ver="UNVERIFIED_SYNTHETIC", ev="SYNTHETIC_TEST_DATA", conf="MEDIUM", priv="ANONYMISED_ZERO_PII", pub="INTERNAL_STAGING"):
    return {
        "record_id": rec_id,
        "research_project_id": "DSPPO-PILOT-2026-01",
        "perma_number": perma_num,
        "perma_year": perma_yr,
        "issue_category": cat,
        "source_type": src_type,
        "source_reference": src_ref,
        "collection_date": "2026-11-24",
        "verification_status": ver,
        "evidence_classification": ev,
        "confidence_level": conf,
        "methodology_version": "v1.1",
        "privacy_status": priv,
        "publication_status": pub,
    }

# 1. perma_registry.csv
perma_fields = MANDATORY_META + ["official_title", "legal_status", "effective_date"]
perma_rows = []
for r in PERMA_RECORDS:
    perma_rows.append({
        "record_id": r[0], "research_project_id": "DSPPO-PILOT-2026-01",
        "perma_number": r[1], "perma_year": r[2], "issue_category": r[3],
        "source_type": r[4], "source_reference": r[5], "collection_date": r[6],
        "verification_status": r[7], "evidence_classification": r[8],
        "confidence_level": r[9], "methodology_version": r[10],
        "privacy_status": r[11], "publication_status": r[12],
        "official_title": r[13], "legal_status": r[14], "effective_date": r[15]
    })
write_csv(BASE / "perma-registry/perma_registry.csv", perma_fields, perma_rows)
write_csv(BASE / "synthetic-data/perma_registry.csv", perma_fields, perma_rows)

# Remaining 14 synthetic datasets
DATASETS_SPEC = {
    "public_issue_registry.csv": (["issue_title", "language", "severity_score"], [
        ("Biaya mediator non-hakim dan pemahaman para pihak", "id", "3.8"),
        ("Kepatuhan itikad baik dalam mediasi 30 hari", "id", "4.2"),
        ("Aksesibilitas mediasi elektronik bagi pihak di daerah", "id", "3.5"),
    ]),
    "discourse_topic_aggregates.csv": (["topic_label", "mention_count", "period_quarter"], [
        ("Mediator_Neutrality_and_Training", "42", "2026-Q3"),
        ("Good_Faith_Sanctions_Art_22", "31", "2026-Q3"),
        ("Electronic_Mediation_Connectivity", "27", "2026-Q3"),
    ]),
    "sentiment_analysis_results.csv": (["sentiment_label", "language", "model_name", "share_pct"], [
        ("NEGATIVE", "id", "indobenchmark-synthetic-eval", "44.0"),
        ("NEUTRAL", "id", "indobenchmark-synthetic-eval", "31.5"),
        ("MIXED", "id", "indobenchmark-synthetic-eval", "14.5"),
        ("POSITIVE", "id", "indobenchmark-synthetic-eval", "10.0"),
    ]),
    "stakeholder_groups.csv": (["stakeholder_group", "jurisdiction_scope", "engagement_channel"], [
        ("Certified_Non_Judge_Mediators", "National", "Opt_In_Consultation"),
        ("Legal_Aid_Organizations_LBH", "Provincial", "Opt_In_Consultation"),
        ("Litigant_Support_Networks", "District", "Accessible_Survey"),
    ]),
    "consultation_submissions.csv": (["stakeholder_group", "submission_channel", "language", "consent_recorded"], [
        ("Certified_Non_Judge_Mediators", "Web_Form_Anonymised", "id", "YES"),
        ("Legal_Aid_Organizations_LBH", "Written_Brief_Anonymised", "id", "YES"),
        ("Litigant_Support_Networks", "Accessible_Audio_Transcript", "id", "YES"),
    ]),
    "validated_evidence.csv": (["triangulation_source", "finding_summary", "alignment_status"], [
        ("Laptah_MA_RI_2025", "Mediation settlement rate varies by court class", "CORROBORATED"),
        ("Bawas_IKM_Survey", "Service clarity scores higher than timeline satisfaction", "PARTIAL_MATCH"),
        ("Academic_ADR_Review", "Good-faith sanction enforcement remains uneven", "CORROBORATED"),
    ]),
    "judicial_access_indicators.csv": (["indicator_code", "indicator_name", "baseline_value", "unit"], [
        ("JAI-01", "Mediation_Room_Accessibility_Rate", "78.5", "percent"),
        ("JAI-02", "Certified_Mediator_Availability", "64.0", "percent"),
        ("JAI-03", "E_Mediation_Readiness_Index", "61.2", "score_100"),
    ]),
    "implementation_gap_analysis.csv": (["perma_article", "intended_outcome", "observed_gap", "gap_severity"], [
        ("Pasal_7_PERMA_1_2016", "Good-faith attendance by all parties", "Frequent absence of principals without sanction", "HIGH"),
        ("Pasal_13_PERMA_1_2016", "Certified mediator availability", "Shortage of certified non-judge mediators in rural PN", "MEDIUM"),
        ("Pasal_4_PERMA_3_2022", "Accessible e-mediation option", "Bandwidth and digital literacy barriers", "MEDIUM"),
    ]),
    "regulatory_impact_evidence.csv": (["ria_dimension", "traceability_link", "impact_direction"], [
        ("Access_to_Justice", "PUBLIC_CONCERN->GAP->RIA_01", "MIXED_POSITIVE"),
        ("Institutional_Efficiency", "PUBLIC_CONCERN->GAP->RIA_02", "MODERATE_IMPROVEMENT"),
        ("Unintended_Consequences", "PUBLIC_CONCERN->GAP->RIA_03", "PRO_FORMA_COMPLIANCE_RISK"),
    ]),
    "public_recommendations.csv": (["recommendation_summary", "target_article", "proposed_by_group"], [
        ("Standardise good-faith assessment checklist for mediators", "Pasal_7", "Certified_Non_Judge_Mediators"),
        ("Publish anonymised court-level mediation success metrics", "Pasal_34", "Legal_Aid_Organizations_LBH"),
        ("Provide plain-language pre-mediation video guides", "Pasal_17", "Litigant_Support_Networks"),
    ]),
    "policy_response_matrix.csv": (["recommendation_id", "response_status", "reasoned_explanation"], [
        ("REC-2026-01", "ACCEPTED_FOR_IJRIO_REVIEW", "Directly addresses documented pro-forma mediation risk"),
        ("REC-2026-02", "PARTIALLY_ACCEPTED", "Subject to SK KMA 2-144/2022 privacy aggregation"),
        ("REC-2026-03", "ACCEPTED_FOR_PILOT", "Low-cost educational intervention aligned with Badilum PTSP"),
    ]),
    "source_registry.csv": (["source_name", "source_level", "retrieval_date", "limitations"], [
        ("JDIH_BPK_PERMA_1_2016", "LEVEL_1", "2026-11-24", "Official statutory text only"),
        ("Kepaniteraan_MA_Laptah_2025", "LEVEL_1", "2026-11-24", "National aggregate figures"),
        ("SP4N_LAPOR_MA_RI", "LEVEL_3", "2026-11-24", "Self-selected complainant sample"),
    ]),
    "research_quality_log.csv": (["check_name", "check_result", "reviewer_role"], [
        ("Zero_PII_Regex_Scan", "PASS", "Automated_QA_Script"),
        ("Mandatory_14_Column_Schema", "PASS", "Automated_QA_Script"),
        ("Legal_Status_Verification", "PASS", "Phase_0_Audit"),
    ]),
    "publication_approval_registry.csv": (["dataset_name", "target_platform", "approval_status", "approver"], [
        ("dsppo-public-issues-pilot", "Kaggle_Private_Staging", "REQUIRES_HUMAN_APPROVAL", "PENDING_HUMAN_GATE"),
        ("dsppo-sentiment-eval-pilot", "Kaggle_Private_Staging", "REQUIRES_HUMAN_APPROVAL", "PENDING_HUMAN_GATE"),
        ("digital-public-sentiment-participation-observatory", "GitHub_Public_Candidate", "REQUIRES_HUMAN_APPROVAL", "PENDING_HUMAN_GATE"),
    ]),
}

for fname, (extra_cols, sample_rows) in DATASETS_SPEC.items():
    rows = []
    for idx, vals in enumerate(sample_rows, start=1):
        rec_id = f"{fname.replace('.csv','').upper()}-{idx:03d}"
        if fname == "source_registry.csv" and idx <= 2:
            urls = [
                "https://peraturan.bpk.go.id/Details/209641/perma-no-1-tahun-2016",
                "https://kepaniteraan.mahkamahagung.go.id/images/laporan_tahunan/FA_LAPTAH_2025.pdf",
            ]
            row = base_meta(rec_id, src_type="OFFICIAL_PORTAL", src_ref=urls[idx-1], ver="VERIFIED", ev="LEVEL_1_OFFICIAL", conf="HIGH", priv="PUBLIC_OFFICIAL", pub="APPROVED_PUBLIC_METADATA")
        elif fname == "source_registry.csv" and idx == 3:
            row = base_meta(rec_id, src_type="PUBLIC_PORTAL", src_ref="https://www.lapor.go.id/instansi/mahkamah-agung-134750", ver="VERIFIED", ev="LEVEL_3_PUBLIC_DISCOURSE", conf="MEDIUM", priv="PUBLIC_OFFICIAL", pub="APPROVED_PUBLIC_METADATA")
        else:
            row = base_meta(rec_id)
        for col, val in zip(extra_cols, vals):
            row[col] = val
        rows.append(row)
    write_csv(BASE / "synthetic-data" / fname, MANDATORY_META + extra_cols, rows)

# Data Dictionary & Master Schema
dd_rows = []
for col in MANDATORY_META:
    dd_rows.append({"dataset": "ALL_15_DATASETS", "column_name": col, "required": "YES", "pii_allowed": "NO", "description": f"Mandatory DSPPO v1.1 metadata field: {col}"})
write_csv(BASE / "data-dictionaries/data_dictionary.csv", ["dataset", "column_name", "required", "pii_allowed", "description"], dd_rows)

with open(BASE / "data-dictionaries/master-schema-v1.json", "w", encoding="utf-8") as f:
    json.dump({"version": "1.1", "mandatory_metadata_columns": MANDATORY_META, "datasets": ["perma_registry.csv"] + list(DATASETS_SPEC.keys())}, f, indent=2)

# 6 Starter Notebooks
NOTEBOOKS = [
    ("01_public_discourse_topic_analysis.ipynb", "DSPPO Notebook 01: Public Discourse Topic Analysis"),
    ("02_indonesian_judicial_sentiment_analysis.ipynb", "DSPPO Notebook 02: Indonesian Judicial Sentiment Analysis"),
    ("03_public_issue_classification.ipynb", "DSPPO Notebook 03: Public Issue Classification"),
    ("04_stakeholder_perspective_analysis.ipynb", "DSPPO Notebook 04: Stakeholder Perspective Analysis"),
    ("05_regulatory_implementation_gap_analysis.ipynb", "DSPPO Notebook 05: Regulatory Implementation Gap Analysis"),
    ("06_ex_post_ria_evidence_analysis.ipynb", "DSPPO Notebook 06: Ex-Post RIA Evidence Analysis"),
]
for nb_file, title in NOTEBOOKS:
    nb_json = {
        "cells": [
            {"cell_type": "markdown", "metadata": {}, "source": [f"# {title}\n\nDSPPO v1.1 — Synthetic & Approved Aggregate Pipeline (Zero-PII)"]},
            {"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": ["import pandas as pd\nprint('DSPPO v1.1 notebook ready for local Dell Precision 7540 execution')"]},
        ],
        "metadata": {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"}},
        "nbformat": 4,
        "nbformat_minor": 5,
    }
    with open(BASE / "notebooks" / nb_file, "w", encoding="utf-8") as f:
        json.dump(nb_json, f, indent=2)

# 7 Kaggle Dataset Metadata Packages (Title 6-50 chars, Subtitle 20-80 chars, NO 'indonesia' tag!)
KAGGLE_DATASETS = [
    ("01-judicial-public-issues", "Judicial Public Issues Registry", "Structured judicial service public issues dataset for PERMA research", ["law", "government", "nlp", "public-policy"]),
    ("02-perma-discourse-topics", "PERMA Discourse Topic Aggregates", "Anonymised topic aggregates on Indonesian Supreme Court regulations", ["law", "nlp", "text-mining", "government"]),
    ("03-judicial-accessibility", "Judicial Service Accessibility Data", "Indicators of court service accessibility and digital readiness", ["government", "law", "tabular", "public-policy"]),
    ("04-stakeholder-participation", "Judicial Stakeholder Participation", "Meaningful public participation metrics and consultation records", ["government", "law", "public-policy"]),
    ("05-regulatory-implementation", "Judicial Regulatory Implementation", "Implementation gap analysis across Supreme Court PERMA pilots", ["law", "government", "public-policy"]),
    ("06-ex-post-ria-evidence", "Ex-Post Judicial RIA Evidence", "Triangulated regulatory impact assessment evidence for PERMA", ["law", "government", "tabular"]),
    ("07-perma-reform-research", "PERMA Regulatory Reform Dataset", "Policy recommendations and reasoned response matrices for reform", ["law", "government", "public-policy"]),
]
for slug, title, subtitle, keywords in KAGGLE_DATASETS:
    assert 6 <= len(title) <= 50, f"Title length out of bounds: {title}"
    assert 20 <= len(subtitle) <= 80, f"Subtitle length out of bounds: {subtitle}"
    assert "indonesia" not in keywords, "Kaggle rejects 'indonesia' tag"
    ds_dir = BASE / "kaggle" / slug
    ds_dir.mkdir(parents=True, exist_ok=True)
    meta = {
        "title": title,
        "id": f"judicialcollege/dsppo-{slug}",
        "subtitle": subtitle,
        "licenses": [{"name": "CC-BY-4.0"}],
        "keywords": keywords,
        "isPrivate": True,
    }
    with open(ds_dir / "dataset-metadata.json", "w", encoding="utf-8") as f:
        json.dump(meta, f, indent=2)

print("Generated 15 CSVs, data dictionary, 6 notebooks, and 7 Kaggle metadata packages.")
