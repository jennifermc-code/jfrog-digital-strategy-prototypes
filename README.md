# JFrog Digital Strategy Toolkit

A centralized workspace for digital strategy analysis, SEO/AEO optimization, web analytics, design review, UX research, web development, executive communication, and project management for jfrog.com.

## Quick Start

Open this repo in Cursor to automatically activate all 9 skills. They'll appear in the agent's available skills and trigger contextually based on your requests.

## Skills

| Skill | What It Does |
|-------|-------------|
| **digital-strategy-analysis** | Initiative evaluation, competitive analysis, roadmap prioritization, market insights |
| **seo-aeo-analysis** | BrightEdge data analysis, keyword/content gaps, AEO evaluation, team SEO rec synthesis |
| **web-analytics-analysis** | GA4/Profound interpretation, team report synthesis, conversion analysis, KPI dashboards |
| **web-design-review** | Design critique, accessibility/WCAG audits, brand consistency, responsive evaluation |
| **ui-ux-research** | Heuristic evaluation, user journey mapping, usability findings, persona alignment |
| **web-development** | JFrog web standards, tracking/tagging implementation specs, performance optimization |
| **executive-communication** | QBRs, executive summaries, stakeholder presentations, data storytelling |
| **strategic-project-management** | Multi-year roadmaps, initiative scoring, cross-team dependencies, status reporting |
| **technical-project-management** | Implementation plans, migration playbooks, sprint tracking, risk registers, go-live checklists |

## Directory Structure

```
├── .cursor/skills/       # Cursor agent skills (auto-discovered)
├── templates/            # Reusable deliverable templates
│   ├── qbr/              # Quarterly business review
│   ├── initiative-brief/ # Initiative one-pagers
│   ├── seo-audit/        # SEO audit reports
│   ├── analytics-report/ # Analytics summaries
│   ├── tracking-spec/    # Tagging/tracking specifications
│   ├── technical-implementation-plan/
│   └── project-status/   # Status dashboards
├── data/                 # Analytics exports, CSVs, crawl data
├── reports/              # Generated analyses and reports
├── projects/             # Active initiative tracking
└── scripts/              # Python utilities for analysis
```

## Tools & Platforms

- **BrightEdge** — SEO platform (rank tracking, Data Cube, Share of Voice, content recommendations)
- **Profound** — Research and audience intelligence
- **GA4** — Web analytics
- **Google Search Console** — Search performance and indexing

## Usage

Drop data exports into `data/`, ask Cursor to analyze them, and the relevant skill will activate. Generated reports land in `reports/`. Track active initiatives in `projects/`.

### Example Prompts

- *"Synthesize the team's SEO recommendations from this BrightEdge export"*
- *"Build a QBR deck summarizing Q1 web performance"*
- *"Create a technical implementation plan for the new tracking architecture"*
- *"Score these 5 initiatives using RICE and recommend prioritization"*
- *"Analyze this GA4 export and identify conversion drop-off points"*
