#!/usr/bin/env python3
"""Generate a project status dashboard from YAML project files.

Usage:
    python scripts/generate_status_dashboard.py

Reads all .yaml/.yml files in projects/ and generates a markdown
status dashboard saved to reports/.
"""

import sys
from datetime import date
from pathlib import Path

try:
    import yaml
except ImportError:
    print("PyYAML required: pip install pyyaml")
    sys.exit(1)


def load_projects(projects_dir: Path) -> list[dict]:
    projects = []
    for f in sorted(projects_dir.glob("*.y*ml")):
        with open(f) as fh:
            data = yaml.safe_load(fh)
            if data:
                data["_file"] = f.name
                projects.append(data)
    return projects


STATUS_ICONS = {
    "on track": "🟢",
    "at risk": "🟡",
    "off track": "🔴",
    "complete": "✅",
    "paused": "⏸️",
}


def get_icon(status: str) -> str:
    return STATUS_ICONS.get(status.lower().strip(), "⚪")


def generate_dashboard(projects: list[dict]) -> str:
    lines = [
        f"# Project Status Dashboard — {date.today().isoformat()}",
        "",
        f"**Projects tracked:** {len(projects)}",
        "",
        "## Active Initiatives",
        "",
        "| Initiative | Owner | Phase | Status | Key Update |",
        "|-----------|-------|-------|--------|-----------|",
    ]

    for p in projects:
        name = p.get("name", p.get("_file", "Unknown"))
        owner = p.get("owner", "TBD")
        phase = p.get("phase", "—")
        status = p.get("status", "unknown")
        update = p.get("key_update", "—")
        icon = get_icon(status)
        lines.append(f"| {name} | {owner} | {phase} | {icon} {status} | {update} |")

    lines.append("")

    blockers = [p for p in projects if p.get("blockers")]
    if blockers:
        lines.extend(["## Blockers", "", "| Initiative | Blocker | Owner |", "|-----------|---------|-------|"])
        for p in blockers:
            name = p.get("name", "Unknown")
            for b in p.get("blockers", []):
                lines.append(f"| {name} | {b.get('description', '—')} | {b.get('owner', 'TBD')} |")
        lines.append("")

    risks = [p for p in projects if p.get("risks")]
    if risks:
        lines.extend(["## Top Risks", "", "| Initiative | Risk | Severity | Mitigation |", "|-----------|------|----------|-----------|"])
        for p in risks:
            name = p.get("name", "Unknown")
            for r in p.get("risks", []):
                lines.append(f"| {name} | {r.get('description', '—')} | {r.get('severity', '—')} | {r.get('mitigation', '—')} |")
        lines.append("")

    return "\n".join(lines)


def main():
    projects_dir = Path("projects")
    if not projects_dir.exists():
        print("No projects/ directory found. Create YAML files there first.")
        sys.exit(1)

    projects = load_projects(projects_dir)
    if not projects:
        print("No .yaml/.yml files found in projects/.")
        print("\nExample project file (projects/website-redesign.yaml):")
        print("---")
        print("name: Website Redesign")
        print("owner: Jennifer")
        print("phase: Development")
        print("status: On Track")
        print("key_update: Frontend build 80% complete")
        print("blockers:")
        print("  - description: Waiting on brand assets")
        print("    owner: Design Team")
        print("risks:")
        print("  - description: CMS migration may take longer")
        print("    severity: Medium")
        print("    mitigation: Parallel workstream started")
        sys.exit(1)

    dashboard = generate_dashboard(projects)
    print(dashboard)

    reports_dir = Path("reports")
    reports_dir.mkdir(exist_ok=True)
    output_file = reports_dir / f"status-dashboard-{date.today().isoformat()}.md"
    output_file.write_text(dashboard)
    print(f"\nSaved to {output_file}")


if __name__ == "__main__":
    main()
