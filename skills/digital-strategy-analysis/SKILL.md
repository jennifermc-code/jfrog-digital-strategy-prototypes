---
name: digital-strategy-analysis
description: Evaluate digital initiatives, perform competitive analysis, prioritize roadmaps, and synthesize market insights for jfrog.com. Use when analyzing initiatives, scoring priorities, building roadmaps, performing competitive analysis, or working with Profound market data.
---

# Digital Strategy Analysis

## Quick Start

When asked to analyze a digital initiative or strategic question:

1. Clarify the objective (growth, efficiency, brand, retention)
2. Gather available data (market research, analytics, competitive intel)
3. Apply the appropriate framework below
4. Produce a structured recommendation with clear next steps

## Initiative Evaluation — RICE Framework

Score each initiative on four dimensions:

| Dimension | Definition | Scale |
|-----------|-----------|-------|
| **Reach** | How many users/visitors impacted per quarter | Estimated number |
| **Impact** | Effect on the target metric per user | 0.25 (minimal) to 3 (massive) |
| **Confidence** | Certainty in estimates | 100% (high), 80% (medium), 50% (low) |
| **Effort** | Person-months required | Estimated number |

**RICE Score** = (Reach × Impact × Confidence) / Effort

Output as a ranked table with scores and a 1-paragraph recommendation for the top 3.

## Impact/Effort Matrix

When RICE is too heavy, use a 2×2 matrix:

```
         Low Effort    High Effort
High    | Quick Wins  | Major Projects |
Impact  |   DO NOW    |   PLAN NEXT    |
        |-------------|----------------|
Low     | Fill-Ins    | Deprioritize   |
Impact  |   IF TIME   |   AVOID        |
```

Place each initiative in a quadrant with a 1-sentence justification.

## Competitive Analysis

Structure competitive assessments as:

1. **Competitor identification** — Direct (e.g., Sonatype Nexus, GitHub Packages) and adjacent
2. **Feature/capability comparison** — Matrix of capabilities vs. competitors
3. **Digital presence comparison** — Site structure, content depth, SEO visibility, UX quality
4. **Gap analysis** — Where jfrog.com underperforms and opportunities
5. **Recommendations** — Prioritized actions with expected impact

## Market Insights Synthesis (Profound)

When working with Profound research data:

1. Extract key audience segments and their behaviors
2. Identify trends relevant to jfrog.com's target personas (DevOps, platform engineering, security)
3. Map insights to specific website sections or content opportunities
4. Produce a summary table: Insight | Relevance | Recommended Action | Priority

## Roadmap Prioritization

When building or refining a multi-quarter roadmap:

1. List all candidate initiatives
2. Score using RICE or Impact/Effort
3. Identify dependencies between initiatives
4. Map to quarters considering: resource constraints, dependencies, strategic alignment
5. Output a timeline view grouped by quarter with owners and success metrics

## Output Template

```markdown
# [Analysis Title]

## Executive Summary
[2-3 sentences: what was analyzed, key finding, primary recommendation]

## Methodology
[Framework used, data sources, assumptions]

## Findings
[Structured findings — tables, matrices, or ranked lists]

## Recommendations
| Priority | Action | Expected Impact | Effort | Timeline |
|----------|--------|----------------|--------|----------|
| 1        |        |                |        |          |

## Next Steps
- [ ] Action item with owner
```

## Team Input Synthesis

When the team provides strategic input or feedback:

1. Consolidate all inputs into a single view
2. Identify themes and conflicts across team members
3. Flag items that reinforce or contradict current priorities
4. Produce a "Team Alignment Summary" showing consensus vs. debate areas
