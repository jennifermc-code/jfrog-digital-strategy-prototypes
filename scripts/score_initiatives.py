#!/usr/bin/env python3
"""Score and rank initiatives using the RICE framework.

Usage:
    python scripts/score_initiatives.py data/initiatives.csv

Input CSV columns: name, reach, impact, confidence, effort
Output: Ranked table printed to stdout and saved to reports/
"""

import csv
import sys
from datetime import date
from pathlib import Path


def load_initiatives(filepath: str) -> list[dict]:
    with open(filepath, newline="") as f:
        reader = csv.DictReader(f)
        required = {"name", "reach", "impact", "confidence", "effort"}
        if not required.issubset(set(reader.fieldnames or [])):
            missing = required - set(reader.fieldnames or [])
            print(f"Error: Missing columns: {missing}")
            print(f"Required columns: {sorted(required)}")
            sys.exit(1)
        return list(reader)


def calculate_rice(initiative: dict) -> float:
    reach = float(initiative["reach"])
    impact = float(initiative["impact"])
    confidence = float(initiative["confidence"])
    effort = float(initiative["effort"])
    if effort == 0:
        return float("inf")
    return (reach * impact * confidence) / effort


def format_table(initiatives: list[dict]) -> str:
    header = f"{'Rank':<6}{'Initiative':<40}{'Reach':>10}{'Impact':>10}{'Confidence':>12}{'Effort':>10}{'RICE Score':>12}"
    separator = "-" * len(header)
    lines = [header, separator]

    for i, init in enumerate(initiatives, 1):
        score = calculate_rice(init)
        line = (
            f"{i:<6}"
            f"{init['name']:<40}"
            f"{init['reach']:>10}"
            f"{init['impact']:>10}"
            f"{init['confidence']:>12}"
            f"{init['effort']:>10}"
            f"{score:>12.1f}"
        )
        lines.append(line)

    return "\n".join(lines)


def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/score_initiatives.py <initiatives.csv>")
        print("\nExpected CSV columns: name, reach, impact, confidence, effort")
        print("\nExample CSV:")
        print("name,reach,impact,confidence,effort")
        print("Redesign pricing page,5000,2,0.8,3")
        print("New blog content hub,10000,1,0.6,5")
        sys.exit(1)

    filepath = sys.argv[1]
    initiatives = load_initiatives(filepath)
    initiatives.sort(key=calculate_rice, reverse=True)

    table = format_table(initiatives)
    print(table)

    reports_dir = Path("reports")
    reports_dir.mkdir(exist_ok=True)
    output_file = reports_dir / f"initiative-scores-{date.today().isoformat()}.txt"
    output_file.write_text(table)
    print(f"\nSaved to {output_file}")


if __name__ == "__main__":
    main()
