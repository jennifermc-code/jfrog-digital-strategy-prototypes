---
name: strategic-project-management
description: Manage multi-year digital strategy roadmaps, score and prioritize initiatives, track cross-team dependencies, and generate status reports for jfrog.com. Use when building roadmaps, tracking initiatives, managing project portfolios, scoring priorities, creating status dashboards, or planning resource allocation.
---

# Strategic Project Management

## Quick Start

When asked to manage strategic projects:

1. Identify the task (roadmap building, initiative tracking, status reporting, prioritization)
2. Determine the time horizon (quarterly, annual, multi-year)
3. Apply the appropriate framework below
4. Produce structured outputs with clear ownership and timelines

## Multi-Year Roadmap Management

### Roadmap Structure
Organize by time horizon and strategic pillar:

```markdown
# Digital Strategy Roadmap — [Year Range]

## Strategic Pillars
1. [Pillar 1 — e.g., Organic Growth]
2. [Pillar 2 — e.g., Conversion Optimization]
3. [Pillar 3 — e.g., Platform Modernization]
4. [Pillar 4 — e.g., Data & Analytics Maturity]

## Timeline View

### [Current Year] — Foundation
| Q1 | Q2 | Q3 | Q4 |
|----|----|----|-----|
| [Initiative] | [Initiative] | [Initiative] | [Initiative] |

### [Year +1] — Scale
| Q1 | Q2 | Q3 | Q4 |
|----|----|----|-----|

### [Year +2] — Optimize
| Q1 | Q2 | Q3 | Q4 |
|----|----|----|-----|
```

### Roadmap Review Cadence
- **Monthly**: Progress check against milestones
- **Quarterly**: Reprioritization based on results and market changes
- **Annually**: Full roadmap refresh aligned with business planning

## Initiative Scoring

### RICE Scoring (from digital-strategy-analysis)
Use for comparing 5+ initiatives. See the digital-strategy-analysis skill for the full RICE framework.

### Weighted Scoring Model
For more nuanced prioritization, use weighted criteria:

| Criterion | Weight | Score (1-5) | Weighted Score |
|-----------|--------|-------------|----------------|
| Strategic alignment | 25% | | |
| Revenue impact | 20% | | |
| User experience impact | 20% | | |
| Technical feasibility | 15% | | |
| Resource efficiency | 10% | | |
| Time to value | 10% | | |
| **Total** | 100% | | |

## Cross-Team Dependency Tracking

### Dependency Map Format
```markdown
## Initiative: [Name]

### Depends On (Blockers)
| Dependency | Owner Team | Status | Risk if Delayed |
|-----------|-----------|--------|----------------|

### Blocks (Downstream)
| Initiative Blocked | Owner Team | Impact of Our Delay |
|-------------------|-----------|-------------------|

### Shared Resources
| Resource | Shared With | Allocation Split | Conflict Risk |
|----------|-----------|-----------------|--------------|
```

### Dependency Risk Levels
- 🟢 **Low** — Owner confirmed, on track, no concerns
- 🟡 **Medium** — Minor risk of delay, mitigation in place
- 🔴 **High** — Likely to delay, escalation needed

## Status Reporting

### Portfolio Dashboard
```markdown
# Digital Strategy Portfolio — [Date]

## Overall Health: 🟢/🟡/🔴

## Initiative Status
| Initiative | Pillar | Owner | Status | % Complete | On Track | Key Update |
|-----------|--------|-------|--------|-----------|----------|-----------|
| | | | Active/Paused/Complete | | 🟢/🟡/🔴 | |

## Milestones This Quarter
| Milestone | Initiative | Due Date | Status | Notes |
|-----------|-----------|----------|--------|-------|

## Risks & Escalations
| Risk | Initiative | Severity | Mitigation | Escalation Needed |
|------|-----------|----------|-----------|-------------------|

## Resource Utilization
| Team/Role | Allocated | Available | Constraint? |
|-----------|----------|-----------|------------|

## Decisions Needed
1.
```

### Status Update Frequency
| Audience | Frequency | Depth | Format |
|----------|-----------|-------|--------|
| Team | Weekly | Detailed | Standup notes |
| Director/VP | Bi-weekly | Summary + risks | Status dashboard |
| Executive | Monthly/Quarterly | Headlines + asks | Executive summary / QBR |

## Resource Planning

### Capacity Model
```markdown
## Team Capacity — [Quarter]

### Available Capacity
| Role | FTEs | Hours/Quarter | Allocated | Available |
|------|------|--------------|-----------|-----------|

### Allocation by Initiative
| Initiative | Role 1 | Role 2 | Role 3 | Total FTE |
|-----------|--------|--------|--------|-----------|

### Over-allocation Warnings
| Role | Allocated % | Recommended Max | Action Needed |
|------|------------|----------------|--------------|
```

## Annual Planning Framework

When building the annual digital strategy plan:

1. **Review prior year** — What worked, what didn't, key metrics
2. **Assess landscape** — Market changes, competitive moves, tech shifts
3. **Define objectives** — 3-5 strategic goals aligned with business priorities
4. **Generate initiatives** — Brainstorm initiatives per objective
5. **Score and prioritize** — Use weighted scoring model
6. **Map to quarters** — Sequence based on dependencies and capacity
7. **Define success metrics** — OKRs or KPIs for each initiative
8. **Identify risks** — What could derail the plan
9. **Secure resources** — Confirm headcount and budget
10. **Communicate** — Share the plan with stakeholders
