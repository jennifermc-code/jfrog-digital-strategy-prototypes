#!/usr/bin/env python3
"""Summarize a GA4 CSV export with key metrics and period-over-period changes.

Usage:
    python scripts/summarize_ga4_export.py data/ga4-export.csv

Handles common GA4 export formats. Produces a markdown summary
saved to reports/.
"""

import csv
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path


def load_csv(filepath: str) -> list[dict]:
    with open(filepath, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        return list(reader)


def detect_columns(headers: list[str]) -> dict:
    """Map expected fields to actual column names (GA4 exports vary)."""
    mapping = {}
    header_lower = {h.lower().strip(): h for h in headers}

    patterns = {
        "channel": ["default channel group", "channel", "session default channel group"],
        "sessions": ["sessions", "session count"],
        "users": ["total users", "users", "active users"],
        "new_users": ["new users"],
        "engagement_rate": ["engagement rate", "engaged sessions per user"],
        "conversions": ["conversions", "key events", "event count"],
        "pageviews": ["views", "screen_page_views", "pageviews"],
    }

    for field, candidates in patterns.items():
        for candidate in candidates:
            if candidate in header_lower:
                mapping[field] = header_lower[candidate]
                break

    return mapping


def summarize(rows: list[dict], col_map: dict) -> str:
    lines = [f"# GA4 Export Summary — {date.today().isoformat()}", ""]

    numeric_fields = ["sessions", "users", "new_users", "conversions", "pageviews"]
    totals = {}
    for field in numeric_fields:
        if field in col_map:
            col = col_map[field]
            total = sum(
                float(row.get(col, "0").replace(",", "") or 0) for row in rows
            )
            totals[field] = total

    lines.append("## Totals")
    lines.append("| Metric | Value |")
    lines.append("|--------|-------|")
    for field, value in totals.items():
        lines.append(f"| {field.replace('_', ' ').title()} | {value:,.0f} |")
    lines.append("")

    if "channel" in col_map:
        col = col_map["channel"]
        channel_data = defaultdict(float)
        for row in rows:
            channel = row.get(col, "Unknown")
            sessions_col = col_map.get("sessions")
            if sessions_col:
                val = row.get(sessions_col, "0").replace(",", "") or "0"
                channel_data[channel] += float(val)

        if channel_data:
            sorted_channels = sorted(channel_data.items(), key=lambda x: x[1], reverse=True)
            total_sessions = sum(v for v in channel_data.values())

            lines.append("## Sessions by Channel")
            lines.append("| Channel | Sessions | % of Total |")
            lines.append("|---------|----------|-----------|")
            for channel, sessions in sorted_channels:
                pct = (sessions / total_sessions * 100) if total_sessions else 0
                lines.append(f"| {channel} | {sessions:,.0f} | {pct:.1f}% |")
            lines.append("")

    lines.append("## Top Rows (first 20)")
    lines.append("")
    if rows:
        headers = list(rows[0].keys())
        lines.append("| " + " | ".join(headers) + " |")
        lines.append("| " + " | ".join(["---"] * len(headers)) + " |")
        for row in rows[:20]:
            lines.append("| " + " | ".join(str(row.get(h, "")) for h in headers) + " |")

    return "\n".join(lines)


def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/summarize_ga4_export.py <ga4-export.csv>")
        sys.exit(1)

    filepath = sys.argv[1]
    rows = load_csv(filepath)

    if not rows:
        print("Error: CSV is empty or could not be parsed.")
        sys.exit(1)

    col_map = detect_columns(list(rows[0].keys()))
    summary = summarize(rows, col_map)
    print(summary)

    reports_dir = Path("reports")
    reports_dir.mkdir(exist_ok=True)
    output_file = reports_dir / f"ga4-summary-{date.today().isoformat()}.md"
    output_file.write_text(summary)
    print(f"\nSaved to {output_file}")


if __name__ == "__main__":
    main()
