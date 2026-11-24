import argparse
import csv
import json
import os
from pathlib import Path
from run_live_pilot1 import fetch_youtube_comments
from social_listening_pipeline import process_records

BASE = Path(__file__).resolve().parent.parent
LIVE_L1_PATH = BASE / "validated-evidence" / "pilot2_live_official_metrics.csv"


def main():
    parser = argparse.ArgumentParser(description="DSPPO Pilot 2 (PERMA 2/2015 jo. 4/2019) Live Runner")
    parser.add_argument("--youtube-video-id", type=str, default="", help="Optional public MA RI YouTube video ID")
    parser.add_argument("--youtube-api-key", type=str, default=os.getenv("YOUTUBE_API_KEY", ""), help="YouTube Data API v3 key")
    args = parser.parse_args()

    with open(LIVE_L1_PATH, encoding="utf-8") as f:
        l1 = list(csv.DictReader(f))

    summary = {
        "pilot": "PERMA No. 2 Tahun 2015 jo. PERMA No. 4 Tahun 2019 (Gugatan Sederhana)",
        "level_1_records_loaded": len(l1),
        "pn_incoming_2025": next(r["metric_value"] for r in l1 if r["record_id"] == "PILOT2-L1-001"),
        "pn_resolved_2025": next(r["metric_value"] for r in l1 if r["record_id"] == "PILOT2-L1-003"),
        "pn_clearance_pct_2025": next(r["metric_value"] for r in l1 if r["record_id"] == "PILOT2-L1-004"),
        "pa_syariah_resolved_2025": next(r["metric_value"] for r in l1 if r["record_id"] == "PILOT2-L1-005"),
    }

    if args.youtube_video_id and args.youtube_api_key:
        raw_comments = fetch_youtube_comments(args.youtube_video_id, args.youtube_api_key)
        processed = process_records(raw_comments)
        out_path = BASE / "validated-evidence" / f"pilot2_yt_{args.youtube_video_id}.csv"
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
