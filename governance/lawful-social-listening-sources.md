# Lawful and Technically Permissible Social-Listening Sources

Public availability on the internet does **not** automatically establish unrestricted permission to collect, process, or republish personal data under UU No. 27 Tahun 2022 (UU PDP). DSPPO restricts social listening to lawful, non-invasive, and technically permissible channels:

| Source Category | Specific Channel / Mechanism | Lawful & Technical Basis | Restrictions & Safeguards |
| :--- | :--- | :--- | :--- |
| **Official Complaint & Feedback Portals** | **SP4N-LAPOR!** ([lapor.go.id](https://www.lapor.go.id/instansi/mahkamah-agung-134750)), **SIWAS MA RI** ([siwas.mahkamahagung.go.id](https://siwas.mahkamahagung.go.id/)), **IKM Surveys** ([bawas.mahkamahagung.go.id](https://bawas.mahkamahagung.go.id/blog/read/hasil-survei-indeks-kepuasan-masyarakat)) | Publicly published aggregate statistics & official institutional portals | Use only published aggregate statistics or formally requested public datasets; never scrape individual complaint tickets |
| **App Store Public Reviews** | Google Play Store / Apple App Store public reviews for official judicial apps (e.g., e-Court, SIWAS APK) | Publicly posted service-quality feedback | Strip reviewer display names/profile IDs; aggregate to topic & sentiment level; respect rate limits |
| **Official YouTube Channels** | YouTube Data API v3 (free quota) on official MA RI / Ditjen Badilum / Badilag / BSDK public broadcasts | Official API within free-tier quota (`Rp0`) | Hash or drop author channel IDs; store only anonymised comment text/topic & timestamp |
| **Public News & Legal Forums** | Publicly accessible online news articles & institutional announcements (e.g., [Dandapala](https://dandapala.com/), Hukumonline public articles, university/LBH publications) | Publicly accessible editorial & academic discourse | Record URL, publication date, retrieval date; paraphrase rather than republish full copyrighted text |
| **Direct Stakeholder Consultations** | Structured opt-in consultation forms (Stage 4 — INVITE) | Explicit informed consent under UU PDP | Requires **Human Approval Gate** before launch; store consent metadata |

## Prohibited Sources & Practices
- **Bypassing `putusan3.mahkamahagung.go.id` WAF (HTTP 403)**: Automated scraping remains strictly halted.
- **Private Groups / Closed Messaging**: WhatsApp groups, private Telegram channels, locked X/Instagram/Facebook accounts.
- **Unauthorised Bulk Scraping**: Any platform scraping that violates Terms of Service or circumvents authentication/CAPTCHAs.
- **Judge Profiling**: Automated scoring, ranking, or sentiment profiling of individual judges or court staff.
