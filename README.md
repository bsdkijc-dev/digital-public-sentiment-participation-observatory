<div align="center">

<img src="assets/logo.svg" alt="Digital Public Sentiment and Participation Observatory (DSPPO) Logo" width="140">

# Digital Public Sentiment and Participation Observatory (DSPPO)

### Independent public-interest research infrastructure connecting public discourse and ex-post judicial regulatory impact.

[![License](https://img.shields.io/badge/License-MIT_/_CC_BY_4.0-blue?style=flat)](LICENSE) ![Stack](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat&logo=python&logoColor=white) [![CI](https://github.com/bsdkijc-dev/digital-public-sentiment-participation-observatory/actions/workflows/ci_qa.yml/badge.svg)](https://github.com/bsdkijc-dev/digital-public-sentiment-participation-observatory/actions/workflows/ci_qa.yml)

[Documentation](methodology/) · [Repository](https://github.com/bsdkijc-dev/digital-public-sentiment-participation-observatory)

</div>

---

**Independent Public-Interest Research Infrastructure for Indonesian Judicial Policy**

> *LISTEN → ANALYSE → VALIDATE → PARTICIPATE → EVALUATE → RESPOND → IMPROVE*

DSPPO is an independent, zero-cost (`Rp0` additional infrastructure expenditure) research and technology initiative within the proposed **Indonesia Open Judicial Policy Ecosystem**. It connects public discourse, digital public sentiment, citizen experiences, stakeholder participation, judicial service performance, and ex-post Regulatory Impact Assessment (RIA) to inform future Peraturan Mahkamah Agung (PERMA) reform.

> **Disclaimer:** DSPPO operates as an independent research and technology initiative. It is **not** an official representative of Mahkamah Agung RI and never claims institutional endorsement without explicit authorisation.

---

## Ecosystem Architecture

| Initiative | Role | Primary Repository |
| :--- | :--- | :--- |
| **IJRIO** | Indonesia Judicial Regulatory Impact Observatory — systematic PERMA evaluation & ex-post RIA | `bsdkijc-dev/indonesia-judicial-regulatory-impact-observatory` |
| **DSPPO** | Digital Public Sentiment and Participation Observatory — public discourse, stakeholder evidence & participation | `bsdkijc-dev/digital-public-sentiment-participation-observatory` |
| **JPAIS** | Judicial Policy Analyst AI Suite — sovereign legal AI & judicial knowledge infrastructure | `bsdkijc-dev/JPAIS` |
| **JDCL** | Justice Delivery Competition Lab — open-source collaboration & public-interest challenges | `bsdkijc-dev/jdcl` |

---

## Seven-Stage Participation Model

1. **LISTEN** — Identify public concerns through lawful, proportionate social listening.
2. **IDENTIFY** — Translate recurring concerns into clearly defined policy problems.
3. **VALIDATE** — Triangulate findings with administrative data, official statistics, and direct stakeholder evidence.
4. **INVITE** — Provide accessible opportunities for affected communities to participate.
5. **CONSIDER** — Document how policymakers or researchers assess substantive contributions.
6. **RESPOND** — Prepare a response matrix identifying accepted, partially accepted, and rejected recommendations with reasons.
7. **EVALUATE** — Determine whether contributions influenced policy design or implementation.

---

## Data Architecture (15 Core Datasets)

All datasets enforce a strict **14-column mandatory metadata standard**, zero-imputation rules, separation of raw source records from anonymised analytical outputs, and compliance with **UU No. 27 Tahun 2022 (UU PDP)** and **UU No. 14 Tahun 2008 (UU KIP)**.

1. `perma_registry.csv`
2. `public_issue_registry.csv`
3. `discourse_topic_aggregates.csv`
4. `sentiment_analysis_results.csv`
5. `stakeholder_groups.csv`
6. `consultation_submissions.csv`
7. `validated_evidence.csv`
8. `judicial_access_indicators.csv`
9. `implementation_gap_analysis.csv`
10. `regulatory_impact_evidence.csv`
11. `public_recommendations.csv`
12. `policy_response_matrix.csv`
13. `source_registry.csv`
14. `research_quality_log.csv`
15. `publication_approval_registry.csv`

---

## Technical Stack (Local Workstation)

- **Workstation**: Dell Precision 7540 (Ubuntu Linux) — zero additional hardware (`Rp0` model)
- **Data & Analytics**: Python 3.11+, Pandas, DuckDB, PostgreSQL (where justified), Scikit-learn, spaCy, Hugging Face open-source models
- **Visualisation & Notebooks**: JupyterLab, Matplotlib, Plotly, Streamlit (if needed)
- **Publication**: GitHub Free (`bsdkijc-dev`), Kaggle Community (`judicialcollege`)

---

## Human Approval Gate

No personal data beyond approved parameters, stakeholder engagement on behalf of an institution, external dataset publication, or institutional policy recommendation may be published without **explicit human approval**.

---

<div align="center">

**Digital Public Sentiment and Participation Observatory (DSPPO)**

[github.com/bsdkijc-dev/digital-public-sentiment-participation-observatory](https://github.com/bsdkijc-dev/digital-public-sentiment-participation-observatory)

</div>
