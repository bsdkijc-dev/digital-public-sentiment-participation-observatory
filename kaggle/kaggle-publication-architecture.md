# Kaggle Publication Architecture (Phase 11)

All 7 Kaggle datasets under `judicialcollege` are staged as **`isPrivate: true`** (`CC-BY-4.0`) and require explicit **`GATE-04` Human Approval** before upload or public release.

| Staging Directory | Kaggle Slug | Included CSVs |
| :--- | :--- | :--- |
| `kaggle/01-judicial-public-issues/` | `judicialcollege/dsppo-01-judicial-public-issues` | `public_issue_registry.csv`, `source_registry.csv`, `data_dictionary.csv` |
| `kaggle/02-perma-discourse-topics/` | `judicialcollege/dsppo-02-perma-discourse-topics` | `discourse_topic_aggregates.csv`, `sentiment_analysis_results.csv`, `data_dictionary.csv` |
| `kaggle/03-judicial-accessibility/` | `judicialcollege/dsppo-03-judicial-accessibility` | `judicial_access_indicators.csv`, `data_dictionary.csv` |
| `kaggle/04-stakeholder-participation/` | `judicialcollege/dsppo-04-stakeholder-participation` | `stakeholder_groups.csv`, `consultation_submissions.csv`, `data_dictionary.csv` |
| `kaggle/05-regulatory-implementation/` | `judicialcollege/dsppo-05-regulatory-implementation` | `perma_registry.csv`, `implementation_gap_analysis.csv`, `data_dictionary.csv` |
| `kaggle/06-ex-post-ria-evidence/` | `judicialcollege/dsppo-06-ex-post-ria-evidence` | `validated_evidence.csv`, `regulatory_impact_evidence.csv`, `data_dictionary.csv` |
| `kaggle/07-perma-reform-research/` | `judicialcollege/dsppo-07-perma-reform-research` | `public_recommendations.csv`, `policy_response_matrix.csv`, `data_dictionary.csv` |

## Notebooks (6)
1. `01_public_discourse_topic_analysis.ipynb`
2. `02_indonesian_judicial_sentiment_analysis.ipynb`
3. `03_public_issue_classification.ipynb`
4. `04_stakeholder_perspective_analysis.ipynb`
5. `05_regulatory_implementation_gap_analysis.ipynb`
6. `06_ex_post_ria_evidence_analysis.ipynb`
