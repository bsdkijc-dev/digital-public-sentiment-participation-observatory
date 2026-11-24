# Record of Data Processing Activities (UU No. 27 Tahun 2022)

**Controller:** DSPPO Independent Research Initiative (Cecep Mustafa)  
**Legal Basis:** Public-interest research & open-government transparency ([UU No. 27 Tahun 2022](https://peraturan.bpk.go.id/Details/229798/uu-no-27-tahun-2022); UU No. 14 Tahun 2008).

| Processing Activity | Data Category | PII Present | Retention & Storage | Safeguard |
| :--- | :--- | :--- | :--- | :--- |
| Official PERMA & Laptah Ingestion | Level 1 public statutory & aggregate court data | No | Permanent version-controlled local storage | Official URL provenance |
| Synthetic Pilot Modeling | Deterministic synthetic records (`seed=20261124`) | No | Git-tracked `synthetic-data/` | Automated zero-PII regex QA |
| Social Listening (Phase 5+) | Public YouTube/Play Store/LAPOR! aggregates | Stripped | Raw text local-only (`127.0.0.1`); 12-month raw TTL | Immediate author/handle stripping |
| Stakeholder Consultation (Phase 7+) | Opt-in anonymised submissions | Consent-gated | Encrypted local volume; never published raw | Explicit `GATE-03` approval |
