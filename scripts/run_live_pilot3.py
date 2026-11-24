import argparse
import csv
import json
import os
from pathlib import Path
from run_live_pilot1 import fetch_youtube_comments
from social_listening_pipeline import process_records

BASE = Path(__file__).resolve().parent.parent
LIVE_L1_PATH = BASE / "validated-evidence" / "pilot3_live_official_records.csv"


def main():
    parser = argparse.ArgumentParser(description="DSPPO Pilot 3 (PERMA 1/2019 jo. 7/2022) Live Runner")
    parser.add_argument("--youtube-video-id", type=str, default="", help="Optional public MA RI YouTube video ID")
    parser.add_argument("--youtube-api-key", type=str, default=os.getenv("YOUTUBE_API_KEY", ""), help="YouTube Data API v3 key")
    args = parser.parse_args()

    with open(LIVE_L1_PATH, encoding="utf-8") as f:
        l1 = list(csv.DictReader(f))

    summary = {
        "pilot": "PERMA No. 1 Tahun 2019 jo. PERMA No. 7 Tahun 2022 (e-Court & e-Litigation)",
        "level_1_records_loaded": len(l1),
        "instruments": [r["instrument_code"] for r in l1],
    }

    if args.youtube_video_id and args.youtube_api_key:
        raw_comments = fetch_youtube_comments(args.youtube_video_id, args.youtube_api_key)
        processed = process_records(raw_comments)
        out_path = BASE / "validated-evidence" / f"pilot3_yt_{args.youtube_video_id}.csv"
        if processed:
            with open(out_path, "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=list(processed[0].keys()))
                writer.writeheader()
                writer.writerows(processed)
        summary["youtube_comments_processed"] = len(processed)
        summary["youtube_output_csv"] = str(out_path.relative_to(BASE))
    else:
        summary["youtube_live_ingestion"] = "SKIPPED_NO_API_KEY_OR_VIDEO_ID"

    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
