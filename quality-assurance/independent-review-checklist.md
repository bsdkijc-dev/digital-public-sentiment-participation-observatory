# Independent Quality Assurance & Human Review Checklist (Phase 12)

| Check ID | Dimension | Automated / Human | Status |
| :--- | :--- | :--- | :--- |
| `QA-01` | Duplicate `record_id` check | Automated (`validate_dsppo_datasets.py`) | `PASS` |
| `QA-02` | Valid official source URLs | Automated + Phase 0–2 Verification | `PASS` |
| `QA-03` | Mandatory 14-column metadata completeness | Automated (`validate_dsppo_datasets.py`) | `PASS` |
| `QA-04` | Sampling bias disclosure (non-representative social media) | Human Review | `PASS` |
| `QA-05` | Language classification accuracy (`id` / `en`) | Automated (`test_pipeline.py`) | `PASS` |
| `QA-06` | Sentiment classification guardrails (no false equivalence) | Methodology + `test_pipeline.py` | `PASS` |
| `QA-07` | Unverified allegations isolated from Level 1–2 evidence | Triangulation Protocol | `PASS` |
| `QA-08` | Consistent ISO-8601 dates | Automated Schema Check | `PASS` |
| `QA-09` | Unsupported causal conclusions prohibited | Human Legal Review | `PASS` |
| `QA-10` | Zero-PII & UU PDP 27/2022 compliance | Automated (`pii_scrubber.py` + regex scan) | `PASS` |
| `QA-11` | Legal status verified against JDIH BPK / MA RI | Phase 0–2 Verification | `PASS` |
| `QA-12` | Methodology & reproducibility documentation complete | Repository Audit | `PASS` |
