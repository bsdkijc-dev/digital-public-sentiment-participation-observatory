# Pilot 1 Comprehensive Research Report: PERMA No. 1 Tahun 2016

> **Status:** `PHASE_8_DRAFT` (Synthetic & Official Baseline; not an official Mahkamah Agung RI publication).

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

## 4. Discourse Analysis (Synthetic Baseline)
Using `synthetic-data/sentiment_analysis_results.csv` (`SYNTHETIC_TEST_DATA`, `seed=20261124`), synthetic test distributions model 44.0% `NEGATIVE`, 31.5% `NEUTRAL`, 14.5% `MIXED`, and 10.0% `POSITIVE` mentions. *Real-world empirical counts await `GATE-02` approval for live API ingestion.*

## 5. Stakeholder Perspective Report
Covers three primary groups in `synthetic-data/stakeholder_groups.csv`: Certified Non-Judge Mediators, Legal Aid Organisations (LBH), and Litigant Support Networks.

## 6. Evidence Validation Report
Triangulated against [Laporan Tahunan MA RI 2025](https://kepaniteraan.mahkamahagung.go.id/images/laporan_tahunan/FA_LAPTAH_2025.pdf) and [Bawas IKM Surveys](https://bawas.mahkamahagung.go.id/blog/read/hasil-survei-indeks-kepuasan-masyarakat) per `validated-evidence/evidence-triangulation-protocol.md`.

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
