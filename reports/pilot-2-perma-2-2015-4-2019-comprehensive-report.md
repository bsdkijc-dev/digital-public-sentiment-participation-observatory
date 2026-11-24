# Pilot 2 Comprehensive Research Report: PERMA No. 2 Tahun 2015 jo. PERMA No. 4 Tahun 2019

> **Status:** `LIVE_PILOT_2_ACTIVE` (Level 1 Official Baseline Verified; not an official Mahkamah Agung RI publication).

## 1. Research Background
Evaluates public discourse, access-to-justice outcomes, and post-judgment enforcement gaps for Indonesia's Small Claim Court (*Gugatan Sederhana*) mechanism.

## 2. Regulatory Profile
- **Base Instrument**: [PERMA No. 2 Tahun 2015](https://peraturan.bpk.go.id/Details/209475/perma-no-2-tahun-2015) (effective 7 August 2015, BN.2015/No.1172).
- **Amending Instrument**: [PERMA No. 4 Tahun 2019](https://peraturan.bpk.go.id/Details/206070/perma-no-4-tahun-2019) (effective 20 August 2019, BN.2019/No.942), raising the claim ceiling to **Rp500,000,000**, adding electronic administration, *verzet*, and *sita jaminan*, with a 25-working-day adjudication limit and final 7-day *keberatan*.

## 3. Public Issue Map
- `TAX-01` (Access & Cost Barriers): Upfront court fee (*panjar*) vs. small-claim recovery value, especially for UMKM litigants.
- `TAX-04` (Procedural Delay & Transparency): 25-day adjudication speed vs. same-jurisdiction domicile constraint.
- `TAX-06` (Victim Restitution & Enforcement): Post-judgment execution (*eksekusi putusan*) friction.

## 4. Discourse Analysis (Pipeline Ready)
Uses `public-discourse-taxonomy/taxonomy.json` (`TAX-01`, `TAX-04`, `TAX-06`) and `scripts/run_live_pilot2.py` with `scripts/pii_scrubber.py` for zero-PII local processing.

## 5. Stakeholder Perspective Report
Focuses on UMKM plaintiffs, individual debtors/defendants, district court registrars (*kepaniteraan*), and legal aid clinics (*posbakum*).

## 6. Evidence Validation Report (Verified Level 1 Official Figures)
Per **Laporan Tahunan Mahkamah Agung RI Tahun 2025** ([FA_LAPTAH_2025.pdf](https://kepaniteraan.mahkamahagung.go.id/images/laporan_tahunan/FA_LAPTAH_2025.pdf) & [PN Tegal / Humas MA RI](https://pn-tegal.go.id/id/mahkamah-agung/sepanjang-tahun-2025-ma-selesaikan-ribuan-perkara-melalui-mediasi-hingga-keadilan-restoratif/)), logged in `validated-evidence/pilot2_live_official_metrics.csv`:
- **Pengadilan Negeri (2025)**: `7,597` incoming cases (`8,288` total workload with `691` carry-over), **`7,065`** resolved (**`92.63%`** resolution ratio).
- **Pengadilan Agama (2025)**: **`348`** *gugatan sederhana ekonomi syariah* cases resolved.

## 7. Implementation Gap Analysis
While first-instance adjudication achieves a **92.63%** resolution ratio, court commentary ([PN Wamena](https://pn-wamena.go.id/new/content/artikel/202512310318102086136512695495f2cd1d6.html)) and academic studies ([UNSRAT Lex Administratum](https://ejournal.unsrat.ac.id/v3/index.php/administratum/article/download/63398/50145/159986); [UIN Jakarta Salam](https://journal.uinjkt.ac.id/index.php/salam/article/view/27073)) highlight that **post-judgment execution** still relies on conventional civil execution procedures, creating disproportionate cost and delay for small-claim winners.

## 8. Ex-Post RIA Report (Dimensions A–J)
Structured for IJRIO interoperability: high first-instance efficiency (`92.63%` clearance) paired with a documented post-judgment enforcement bottleneck.

## 9. Meaningful Participation Assessment
Evaluated via `MPI-01`–`MPI-08` (`participation-indicators/meaningful-participation-indicators.md`), requiring `GATE-03` approval before launching UMKM/litigant consultations.

## 10. Policy Recommendation Matrix (Draft — `GATE-05` Gated)
- Streamline simplified execution (*eksekusi sederhana*) or voluntary compliance incentives for *gugatan sederhana* judgments.
- Clarify electronic *aanmaning* workflows under PERMA 4/2019 + PERMA 7/2022.

## 11. Research Limitations
See `quality-assurance/research-and-technical-limitations.md` (`putusan3` HTTP 403 WAF halt prevents automated case-level judgment scraping).

## 12. Reproducibility Documentation
All Pilot 2 Level 1 records and validation scripts are version-controlled on `main` (`scripts/run_live_pilot2.py`).
