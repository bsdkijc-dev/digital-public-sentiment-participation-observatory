# Privacy and Research Governance Framework (DSPPO v1.1)

## 1. Legal & Regulatory Basis
DSPPO operates strictly within Indonesian statutory and judicial disclosure frameworks:
- **UU No. 27 Tahun 2022 tentang Pelindungan Data Pribadi (UU PDP)** ([JDIH BPK](https://peraturan.bpk.go.id/Details/229798/uu-no-27-tahun-2022)): Distinguishes *data pribadi bersifat umum* (full name, gender, citizenship, religion, marital status, or combined identifiers) and *data pribadi bersifat spesifik* (health, biometrics, genetics, criminal records, children's data, personal financial data). Enforces lawful basis, purpose limitation, data minimisation, retention limits, and Data Protection Officer/governance accountability.
- **UU No. 14 Tahun 2008 tentang Keterbukaan Informasi Publik (UU KIP)**: Governs public-interest access to public institutional information while protecting exempted personal and judicial deliberation data.
- **SK KMA No. 2-144/KMA/SK/VIII/2022**: Standard for judicial information disclosure and mandatory anonymisation of protected parties (e.g., children, victims of sexual/domestic violence, witnesses).
- **Platform Terms & Technical Controls**: Strict compliance with platform API policies, robots/rate limits, and copyright/database restrictions.

## 2. Core Data Governance Principles
1. **Purpose Limitation**: Data is collected solely for public-interest judicial policy research, regulatory impact assessment, and meaningful participation analysis.
2. **Data Minimisation & Zero-PII**: Never collect, store, or publish names, NIK, phone numbers, email addresses, home addresses, usernames, or case-party identifiers in analytical datasets.
3. **Separation of Raw vs. Analytical Layers**: Raw source references remain strictly separated from anonymised analytical outputs (`discourse_topic_aggregates.csv`, `sentiment_analysis_results.csv`, etc.).
4. **Prohibition on Invasive Collection**:
   - Never scrape private accounts, bypass authentication, or evade WAF/technical access controls (e.g., `putusan3.mahkamahagung.go.id` HTTP 403 WAF remains halted for automated collection).
   - Never conduct individual profiling, political profiling, or automated assessments of judges based on online discourse.
5. **Local-First Processing**: Sensitive or unpublished research data is processed locally on the Dell Precision 7540 workstation (`127.0.0.1` bindings), never sent to commercial third-party APIs.
6. **Zero-Imputation & Auditability**: Missing values remain empty/null with explicit completeness flags; never fabricate or impute missing empirical records.
