# Digital Public Sentiment Engine Specification

## 10 Core Analytical Functions
1. Topic classification (`TAX-01` to `TAX-07`)
2. Issue identification (mapped to PERMA articles)
3. Sentiment classification (`POSITIVE`, `NEGATIVE`, `NEUTRAL`, `MIXED`, `UNCLEAR`)
4. Argument extraction (claim + stated rationale)
5. Recurring complaint identification (clustering across courts/periods)
6. Stakeholder perspective mapping (litigants, mediators, advocates, CSOs, court staff)
7. Policy recommendation extraction
8. Emerging issue detection (quarter-over-quarter spike detection)
9. Temporal trend analysis
10. Evidence triangulation (cross-checking against Level 1–2 sources)

## Methodological Guardrails
- **Bilingual Support**: Indonesian (`id`) and English (`en`) initially; regional languages added only when validated corpora exist.
- **No False Equivalence**: Negative sentiment does not prove institutional failure; positive sentiment does not prove policy success.
- **No Population Extrapolation**: Non-representative social-media samples never represent Indonesia-wide public opinion.
