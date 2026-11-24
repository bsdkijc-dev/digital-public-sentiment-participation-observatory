# Pilot 3 Comprehensive Research Report: PERMA No. 1 Tahun 2019 jo. PERMA No. 7 Tahun 2022

> **Status:** `LIVE_PILOT_3_ACTIVE` (Level 1 Official Baseline Verified; not an official Mahkamah Agung RI publication).

## 1. Research Background
Evaluates public discourse, digital accessibility, and implementation gaps for Indonesia's electronic court administration and e-Litigation framework (`e-Court`).

## 2. Regulatory Profile
- **Base Instrument**: [PERMA No. 1 Tahun 2019](https://peraturan.bpk.go.id/Details/206067/perma-no-1-tahun-2019) (effective 19 August 2019, BN.2019/No.894; revoked PERMA No. 3 Tahun 2018).
- **Amending Instrument**: [PERMA No. 7 Tahun 2022](https://peraturan.bpk.go.id/Details/248072/perma-no-7-tahun-2022) (effective 11 October 2022, BN.2022/No.1039), expanding eligible users, mandating electronic proceedings for electronically filed cases, recognising electronic judgment pronouncement, and adding electronic appeals.

## 3. Public Issue Map
- `TAX-01` (Access & Cost Barriers): *Prodeo* / indigent user onboarding and bank-account/email prerequisites for non-advocate litigants.
- `TAX-02` (Digital & e-Court Usability): File-upload limits, e-Summons delivery reliability, and portal uptime.
- `TAX-04` (Procedural Delay & Transparency): Hybrid evidentiary hearing scheduling and electronic copy access.

## 4. Discourse Analysis (Pipeline Ready)
Uses `public-discourse-taxonomy/taxonomy.json` (`TAX-01`, `TAX-02`, `TAX-04`) and `scripts/run_live_pilot3.py` with `scripts/pii_scrubber.py` for zero-PII local processing.

## 5. Stakeholder Perspective Report
Covers advocates (*pengguna terdaftar*), *pengguna lain* (individuals/prosecutors/incidental representatives), court registrars, and *posbakum* staff.

## 6. Evidence Validation Report (Verified Level 1 Official Milestones)
Per **Ringkasan Eksekutif Laporan Tahunan MA RI 2025** ([FA_EKSUM_2025.pdf](https://kepaniteraan.mahkamahagung.go.id/images/laporan_tahunan/FA_%20EKSUM_%202025.pdf)), logged in `validated-evidence/pilot3_live_official_records.csv`, MA RI expanded electronic justice in 2025 through:
- **SK KMA No. 140/KMA/SK.HK2/VIII/2025** (13 Aug 2025): Electronic *Kasasi* / *Peninjauan Kembali* fee adjustments.
- **SK Panitera MA No. 872/PAN/HK2/SK/SK/VIII/2025** (14 Aug 2025): Electronic *Hak Uji Materiil* (HUM) registration and payment.
- **SK Panitera MA No. 1467A/PAN/HK2.7/SK/XII/2025** (1 Dec 2025): Electronic *PK* for Tax Court decisions via *e-Tax Court*.

## 7. Implementation Gap Analysis
Level 2 research ([Dinasti Review JIHHP](https://dinastirev.org/JIHHP/article/view/2456); [Jurnal UMSB Pagaruyuang](https://jurnal.umsb.ac.id/index.php/pagaruyuang/article/view/6221)) and court guidance ([PA Batang](https://pa-batang.go.id/mengenal-alur-dan-tahapan-e-litigasi-persidangan-elektronik-di-pengadilan-agama-batang-berdasarkan-perma-no-7-tahun-2022/); [PN Baubau](https://www.pn-bau-bau.go.id/page/prosedur-penggunaan-e-court)) highlight digital-divide barriers for *prodeo* and non-advocate users who require email, mobile numbers, and bank accounts to register.

## 8. Ex-Post RIA Report (Dimensions A–J)
Structured for IJRIO & JPAIS interoperability, connecting rapid regulatory expansion (2019–2025) with *prodeo* and rural digital-access safeguards.

## 9. Meaningful Participation Assessment
Evaluated via `MPI-01`–`MPI-08` (`participation-indicators/meaningful-participation-indicators.md`), requiring `GATE-03` approval before external consultation deployment.

## 10. Policy Recommendation Matrix (Draft — `GATE-05` Gated)
- Provide assisted *e-Court* kiosks (*Pojok e-Court* / *Posbakum*) for *prodeo* and non-advocate litigants.
- Publish transparent uptime and e-Summons delivery-failure metrics.

## 11. Research Limitations
See `quality-assurance/research-and-technical-limitations.md`.

## 12. Reproducibility Documentation
All Pilot 3 Level 1 records and validation scripts are version-controlled on `main` (`scripts/run_live_pilot3.py`).
