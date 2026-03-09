---
name: technical-project-management
description: Manage large technical implementation projects including migrations, platform integrations, tracking architectures, and complex web development initiatives for jfrog.com. Use when creating technical implementation plans, managing migrations, building go-live checklists, tracking sprints/phases, managing technical risk registers, or coordinating with vendors on technical projects.
---

# Technical Project Management

## Quick Start

When asked to manage a technical implementation project:

1. Identify the project type (migration, integration, new build, infrastructure, tracking architecture)
2. Determine the phase (planning, active development, testing, go-live, post-launch)
3. Apply the appropriate framework below
4. Produce implementation-ready plans with clear phases, owners, and acceptance criteria

## Technical Implementation Plan

For the full playbook template, see [implementation-playbook.md](implementation-playbook.md).

### Plan Structure
```markdown
# Technical Implementation Plan — [Project Name]

## Overview
| Field | Value |
|-------|-------|
| Project | |
| Owner | |
| Tech Lead | |
| Start Date | |
| Target Go-Live | |
| Status | Planning / In Progress / Testing / Complete |

## Objective
[What this project achieves — 2-3 sentences]

## Scope
### In Scope
- [Deliverable 1]

### Out of Scope
- [Explicitly excluded item]

## Architecture / Technical Approach
[High-level technical design — diagrams if helpful]

## Phases
| Phase | Duration | Key Deliverables | Exit Criteria |
|-------|----------|-----------------|---------------|
| 1. Discovery & Design | | | |
| 2. Development | | | |
| 3. Testing & QA | | | |
| 4. Staging & UAT | | | |
| 5. Go-Live | | | |
| 6. Post-Launch | | | |

## Dependencies
| Dependency | Owner | Status | Impact if Delayed |
|-----------|-------|--------|-------------------|

## Risks
| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|-----------|
```

## Phase-Based Tracking

### Sprint/Phase Status Template
```markdown
## Phase [X]: [Name] — Status: 🟢/🟡/🔴

### Dates: [Start] — [End]

### Deliverables
| Deliverable | Owner | Status | Blockers | Notes |
|------------|-------|--------|----------|-------|

### Completed This Sprint
- [Item with link to PR/doc]

### Carry-Over to Next Sprint
- [Item with reason for delay]

### Blockers
| Blocker | Owner | Resolution Path | ETA |
|---------|-------|----------------|-----|
```

## Risk Register

### Risk Assessment Matrix
```
              Low Impact    High Impact
High       |  Monitor    |  Mitigate    |
Likelihood |             |  Immediately |
           |-------------|--------------|
Low        |  Accept     |  Contingency |
Likelihood |             |  Plan Ready  |
```

### Risk Register Template
| ID | Risk | Category | Likelihood (1-5) | Impact (1-5) | Score | Mitigation Plan | Owner | Status |
|----|------|----------|------------------|--------------|-------|----------------|-------|--------|
| R1 | | Technical/Resource/Timeline/External | | | | | | Open/Mitigated/Closed |

### Risk Categories
- **Technical** — Technology won't work as expected, integration failures, data issues
- **Resource** — Key person unavailable, skill gaps, competing priorities
- **Timeline** — Dependencies delayed, scope creep, underestimated complexity
- **External** — Vendor delays, API changes, third-party outages

## Go-Live Checklist

### Pre-Launch (T-2 weeks)
- [ ] All acceptance criteria met for in-scope deliverables
- [ ] Performance testing completed — meets CWV targets
- [ ] Security review completed
- [ ] Accessibility testing passed (WCAG 2.1 AA)
- [ ] Cross-browser testing completed
- [ ] Mobile testing completed
- [ ] Analytics/tracking verified in staging
- [ ] SEO impact assessed (redirects, canonical tags, structured data)
- [ ] Content reviewed and approved
- [ ] Stakeholder demo/sign-off obtained

### Launch Day (T-0)
- [ ] Deployment plan documented and reviewed
- [ ] Rollback plan documented and tested
- [ ] Monitoring dashboards configured
- [ ] On-call team identified
- [ ] Communication sent to stakeholders
- [ ] Deployment executed
- [ ] Smoke tests passed in production
- [ ] Analytics data flowing correctly
- [ ] No console errors or broken functionality

### Post-Launch (T+1 to T+14)
- [ ] Monitor error rates for 48 hours
- [ ] Verify analytics data accuracy after 24 hours
- [ ] Check Core Web Vitals in production (CrUX data at T+28 days)
- [ ] Collect user/team feedback
- [ ] Address P1 bugs within 24 hours
- [ ] Retrospective scheduled and conducted
- [ ] Documentation updated
- [ ] Knowledge transfer to support/maintenance team

## Vendor Coordination

When working with external vendors or agencies:

### Vendor Management Checklist
- [ ] SOW/contract reviewed and signed
- [ ] Technical requirements document shared
- [ ] Access provisioned (staging environments, repos, tools)
- [ ] Communication cadence established (standups, weeklies)
- [ ] Escalation path defined
- [ ] Acceptance criteria agreed upon
- [ ] Delivery milestones with payment gates
- [ ] IP and data ownership clarified
- [ ] Exit/transition plan outlined

### Vendor Status Tracking
| Vendor | Project | Status | Next Milestone | Risk | Notes |
|--------|---------|--------|---------------|------|-------|

## Meeting Cadence for Large Projects

| Meeting | Frequency | Attendees | Purpose |
|---------|-----------|-----------|---------|
| Daily standup | Daily | Core team | Blockers, progress, plan for today |
| Tech sync | 2x/week | Tech leads | Architecture decisions, technical blockers |
| Stakeholder update | Weekly | PM, stakeholders | Status, risks, decisions needed |
| Sprint review | Bi-weekly | Full team + stakeholders | Demo deliverables, gather feedback |
| Retrospective | End of phase | Core team | Process improvements |
