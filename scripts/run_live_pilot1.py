import argparse
import csv
import json
import os
import urllib.parse
import urllib.request
from pathlib import Path
from social_listening_pipeline import process_records

BASE = Path(__file__).resolve().parent.parent
LIVE_L1_PATH = BASE / "validated-evidence" / "pilot1_live_official_metrics.csv"


def load_l1_metrics() -> list[dict]:
    with open(LIVE_L1_PATH, encoding="utf-8") as f:
        return list(csv.DictReader(f))


def fetch_youtube_comments(video_id: str, api_key: str, max_results: int = 50) -> list[dict]:
    params = urllib.parse.urlencode({
        "part": "snippet",
        "videoId": video_id,
        "maxResults": max_results,
        "textFormat": "plainText",
        "key": api_key,
    })
    url = f"https://www.googleapis.com/youtube/v3/commentThreads?{params}"
    with urllib.request.urlopen(url, timeout=20) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    records = []
    for i, item in enumerate(data.get("items", []), start=1):
        txt = item["snippet"]["topLevelComment"]["snippet"].get("textDisplay", "")
        records.append({"record_id": f"YT-{video_id}-{i:03d}", "language": "id", "text": txt})
    return records


def main():
    parser = argparse.ArgumentParser(description="DSPPO Pilot 1 (PERMA 1/2016) Live Runner")
    parser.add_argument("--youtube-video-id", type=str, default="", help="Optional public MA RI YouTube video ID")
    parser.add_argument("--youtube-api-key", type=str, default=os.getenv("YOUTUBE_API_KEY", ""), help="YouTube Data API v3 key")
    args = parser.parse_args()

    l1 = load_l1_metrics()
    summary = {
        "pilot": "PERMA No. 1 Tahun 2016 + PERMA No. 3 Tahun 2022",
        "level_1_records_loaded": len(l1),
        "mediation_2024_pct": next(r["metric_value"] for r in l1 if r["record_id"] == "PILOT1-L1-004"),
        "mediation_2025_pct": next(r["metric_value"] for r in l1 if r["record_id"] == "PILOT1-L1-003"),
        "mediation_2025_resolved": next(r["metric_value"] for r in l1 if r["record_id"] == "PILOT1-L1-002"),
        "mediation_2025_total": next(r["metric_value"] for r in l1 if r["record_id"] == "PILOT1-L1-001"),
    }

    if args.youtube_video_id and args.youtube_api_key:
        raw_comments = fetch_youtube_comments(args.youtube_video_id, args.youtube_api_key)
        processed = process_records(raw_comments)
        out_path = BASE / "validated-evidence" / f"pilot1_yt_{args.youtube_video_id}.csv"
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
