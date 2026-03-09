# JFrog Digital Strategy Toolkit

This repo contains specialized skills, templates, and scripts for jfrog.com digital strategy work.

## Skills

Before starting any task, check the `skills/` directory at the repo root for a relevant skill. Each skill has a `SKILL.md` with step-by-step instructions, frameworks, and output templates. Read the matching `SKILL.md` before beginning work.

| Skill directory | When to use |
|----------------|------------|
| `skills/digital-strategy-analysis/` | Initiative evaluation, RICE scoring, competitive analysis, roadmap prioritization |
| `skills/seo-aeo-analysis/` | SEO audits, BrightEdge data, keyword gaps, AEO evaluation, team SEO recommendations |
| `skills/web-analytics-analysis/` | GA4 analysis, Profound data, conversion funnels, A/B tests, team report synthesis |
| `skills/web-design-review/` | Design critique, accessibility/WCAG audits, brand consistency, responsive review |
| `skills/ui-ux-research/` | Heuristic evaluation, user journeys, usability findings, persona alignment |
| `skills/web-development/` | Tracking/tagging implementation specs, performance/CWV optimization, component standards |
| `skills/executive-communication/` | QBRs, executive summaries, stakeholder presentations, data storytelling |
| `skills/strategic-project-management/` | Multi-year roadmaps, initiative scoring, dependency tracking, status dashboards |
| `skills/technical-project-management/` | Technical implementation plans, migrations, go-live checklists, risk registers, vendor coordination |

Some skills include supporting reference files (e.g., `brightedge-workflows.md`, `tagging-checklist.md`, `qbr-template.md`). These are linked from the SKILL.md — read them when the task requires that level of detail.

## Templates

Reusable deliverable templates are in `templates/`. Copy and fill them in for standardized outputs.

## Scripts

Python utility scripts in `scripts/`:
- `score_initiatives.py` — RICE-score a CSV of initiatives
- `summarize_ga4_export.py` — Summarize a GA4 CSV export
- `generate_status_dashboard.py` — Build a status dashboard from YAML project files in `projects/`

## Data & Reports

- Drop analytics exports and data files into `data/`
- Generated reports go to `reports/`
- Track active initiatives as YAML files in `projects/`
