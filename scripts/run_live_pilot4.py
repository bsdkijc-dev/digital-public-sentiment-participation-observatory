import csv
import json
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
LIVE_PATH = BASE / "validated-evidence" / "pilot4_live_official_records.csv"


def main():
    with open(LIVE_PATH, encoding="utf-8") as f:
        records = list(csv.DictReader(f))

    summary = {
        "pilot": "PERMA No. 3 Tahun 2017 (Perempuan Berhadapan dengan Hukum)",
        "level_1_2_records_loaded": len(records),
        "evidence_themes": [r["evidence_theme"] for r in records],
        "social_listening_mode": "RESTRICTED_LEVEL_1_2_ONLY_TRAUMA_AND_UU_PDP_SAFEGUARD",
    }
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
