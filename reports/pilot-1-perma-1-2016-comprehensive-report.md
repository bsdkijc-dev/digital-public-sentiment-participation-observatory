# Pilot 1 Comprehensive Research Report: PERMA No. 1 Tahun 2016

> **Status:** `LIVE_PILOT_1_ACTIVE` (Level 1 Official Baseline Verified; Level 3 live API ingestion ready on Dell Precision 7540; not an official Mahkamah Agung RI publication).

## 1. Research Background
Evaluates public discourse, service accessibility, and implementation gaps surrounding court-annexed mediation in Indonesia under the DSPPO seven-stage participation model.

## 2. Regulatory Profile
- **Primary Instrument**: [PERMA No. 1 Tahun 2016 tentang Prosedur Mediasi di Pengadilan](https://peraturan.bpk.go.id/Details/209641/perma-no-1-tahun-2016) (effective 4 February 2016, BN.2016/No.175; revoked PERMA No. 01 Tahun 2008).
- **Electronic Complement**: [PERMA No. 3 Tahun 2022 tentang Mediasi di Pengadilan Secara Elektronik](https://peraturan.bpk.go.id/Download/211652/Perma%20Nomor%203%20Tahun%202022.pdf?embed=True) (Pasal 25 preserves PERMA 1/2016).

## 3. Public Issue Map
Mapped to `public-discourse-taxonomy/taxonomy.json`:
- `TAX-01` (Access & Cost Barriers): Non-judge mediator fee clarity and legal aid access.
- `TAX-02` (Digital & e-Court Usability): Bandwidth and document-upload friction in e-mediation.
- `TAX-03` (Mediation & ADR Quality): Good-faith attendance (Pasal 7) and mediator neutrality.

## 4. Discourse Analysis (Baseline & Live Pipeline Ready)
Synthetic baseline (`synthetic-data/sentiment_analysis_results.csv`, `seed=20261124`) models 44.0% `NEGATIVE`, 31.5% `NEUTRAL`, 14.5% `MIXED`, and 10.0% `POSITIVE` mentions. Live public YouTube Data API v3 comment ingestion is ready via `scripts/run_live_pilot1.py`.

## 5. Stakeholder Perspective Report
Covers three primary groups in `synthetic-data/stakeholder_groups.csv`: Certified Non-Judge Mediators, Legal Aid Organisations (LBH), and Litigant Support Networks.

## 6. Evidence Validation Report (Verified Level 1 Official Figures)
Per **Laporan Tahunan Mahkamah Agung RI Tahun 2025** ([PN Tegal / Humas MA RI](https://pn-tegal.go.id/id/mahkamah-agung/sepanjang-tahun-2025-ma-selesaikan-ribuan-perkara-melalui-mediasi-hingga-keadilan-restoratif/)), logged in `validated-evidence/pilot1_live_official_metrics.csv`:
- **2025 Mediation Volume & Resolution**: **39,520** cases successfully resolved via mediation out of **88,365** total mediated cases (**44.72%**).
- **Year-over-Year Trend**: Mediation success rate rose from **28.65%** in 2024 to **44.72%** in 2025 (a **56.11%** relative increase).
- **Triangulation Note**: Despite higher national settlement rates, academic Level 2 studies ([Neliti](https://media.neliti.com/media/publications/209736-analisis-yuridis-terhadap-peraturan-mahk.pdf)) document persistent good-faith (*itikad baik*) attendance friction under Pasal 7.

## 7. Implementation Gap Analysis
Key statutory-to-practice gaps logged in `synthetic-data/implementation_gap_analysis.csv`:
- **Pasal 7 PERMA 1/2016**: Uneven enforcement of good-faith sanctions when principals fail to attend.
- **Pasal 13 PERMA 1/2016**: Geographic shortage of certified non-judge mediators outside major cities.
- **Pasal 4 PERMA 3/2022**: Digital literacy and connectivity barriers in remote jurisdictions.

## 8. Ex-Post RIA Report (Dimensions A–J)
Integrated with IJRIO via `ex-post-ria/ijrio-handoff-package.json` (assessing access-to-justice, institutional efficiency, and pro-forma compliance risks without claiming causal attribution from discourse alone).

## 9. Meaningful Participation Assessment
Evaluated using `MPI-01` to `MPI-08` (`participation-indicators/meaningful-participation-indicators.md`), tracking diversity, accessibility, substantive consideration, and documented rationale rates.

## 10. Policy Recommendation Matrix
Logged in `synthetic-data/policy_response_matrix.csv`:
- `REC-2026-01`: Standardise good-faith assessment checklist (`ACCEPTED_FOR_IJRIO_REVIEW`).
- `REC-2026-02`: Publish anonymised court-level mediation metrics (`PARTIALLY_ACCEPTED` — subject to SK KMA 2-144/2022).
- `REC-2026-03`: Plain-language pre-mediation guides (`ACCEPTED_FOR_PILOT`).

## 11. Research Limitations
See `quality-assurance/research-and-technical-limitations.md` (non-representativeness of social media, `putusan3` HTTP 403 WAF halt, and zero causal attribution).

## 12. Reproducibility Documentation
All schemas, deterministic seeds (`20261124`), PII scrubbing (`scripts/pii_scrubber.py`), and DuckDB builds (`scripts/build_duckdb_warehouse.py`) are version-controlled on `main`.
