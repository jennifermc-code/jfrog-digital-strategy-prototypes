---
name: ui-ux-research
description: Conduct heuristic evaluations, user journey mapping, usability analysis, and persona alignment assessments for jfrog.com. Use when performing UX research, usability analysis, heuristic evaluation, user journey mapping, task flow analysis, or persona alignment review.
---

# UI/UX Research & Analysis

## Quick Start

When asked to perform UX analysis:

1. Identify the research method needed (heuristic evaluation, journey mapping, usability review, persona analysis)
2. Define scope (full site, specific flow, single page)
3. Apply the appropriate framework below
4. Produce findings with severity ratings and actionable recommendations

## Heuristic Evaluation (Nielsen's 10)

Evaluate against each heuristic — score 0 (no issues) to 4 (usability catastrophe):

| # | Heuristic | What to Evaluate |
|---|-----------|-----------------|
| 1 | **Visibility of system status** | Loading indicators, progress bars, confirmation messages, active states |
| 2 | **Match between system and real world** | Terminology familiar to DevOps/developer audience, logical ordering |
| 3 | **User control and freedom** | Undo, back, cancel, escape routes from flows |
| 4 | **Consistency and standards** | Same action = same result across site, follows web conventions |
| 5 | **Error prevention** | Form validation, confirmation dialogs, smart defaults |
| 6 | **Recognition over recall** | Visible options, contextual help, breadcrumbs |
| 7 | **Flexibility and efficiency** | Shortcuts for power users, customization, search |
| 8 | **Aesthetic and minimalist design** | No irrelevant information competing for attention |
| 9 | **Help users recognize and recover from errors** | Clear error messages, suggested fixes |
| 10 | **Help and documentation** | Accessible help, searchable docs, contextual tooltips |

### Heuristic Evaluation Output
```markdown
# Heuristic Evaluation — [Page/Flow]

## Summary
[Overall usability score, top 3 concerns]

## Findings by Heuristic
### H1: Visibility of System Status
- **Severity:** [0-4]
- **Findings:** [Specific observations]
- **Recommendation:** [Actionable fix]

[Repeat for each heuristic with findings]

## Priority Matrix
| Finding | Severity (0-4) | Frequency | Recommended Fix | Effort |
|---------|----------------|-----------|----------------|--------|
```

## User Journey Mapping

Map end-to-end experiences for key jfrog.com journeys:

### Key Journeys to Evaluate
1. **Awareness → Trial** — First visit through trial signup
2. **Evaluation → Purchase** — Pricing research through purchase decision
3. **Problem → Solution** — Search for a problem through finding JFrog's solution
4. **Docs → Success** — Finding documentation through completing a task

### Journey Map Structure
For each stage of the journey, capture:

| Stage | User Goal | Touchpoints | Actions | Thoughts | Emotions | Pain Points | Opportunities |
|-------|-----------|-------------|---------|----------|----------|-------------|---------------|

### Identifying Friction Points
- Where do users have to make unnecessary decisions?
- Where is information missing or hard to find?
- Where does the experience break across device types?
- Where does navigation fail to match user mental models?

## Task Flow Analysis

When evaluating a specific task (e.g., "sign up for a free trial"):

1. **Define the task** — Clear start and end states
2. **Map the ideal flow** — Minimum steps to completion
3. **Map the actual flow** — Steps users actually take (from analytics or observation)
4. **Identify deviations** — Where does actual diverge from ideal?
5. **Count steps and decisions** — Fewer = better
6. **Recommend simplifications** — Remove steps, reduce decisions, improve defaults

## Persona Alignment

JFrog's primary web personas (adapt as needed):

| Persona | Role | Goals on jfrog.com | Key Content Needs |
|---------|------|-------------------|------------------|
| **DevOps Engineer** | Hands-on practitioner | Evaluate tools, find docs, solve problems | Tutorials, docs, integration guides |
| **Platform Engineer** | Infrastructure/tooling | Assess platform capabilities, compare | Architecture docs, case studies |
| **Security Lead** | AppSec/DevSecSec | Evaluate security features, compliance | Security docs, compliance info |
| **Engineering Manager** | Team lead | Understand ROI, team productivity gains | Case studies, ROI calculators |
| **IT Decision Maker** | VP/Director | Business case, pricing, vendor comparison | Pricing, enterprise features, ROI |

When reviewing content or UX, assess:
1. Which persona(s) does this serve?
2. Does the content/UX match their technical depth?
3. Does the CTA align with their decision stage?
4. Are there persona gaps — key audiences with unmet needs?

## Usability Findings Synthesis

When compiling findings from any UX research:

```markdown
# UX Research Findings — [Scope]

## Methodology
[What was evaluated and how]

## Key Findings (Ranked by Impact)
| # | Finding | Severity | Affected Personas | Evidence | Recommendation |
|---|---------|----------|------------------|----------|----------------|

## Themes
1. [Cross-cutting theme with supporting findings]

## Quick Wins (High impact, low effort)
1.

## Strategic Recommendations (Require investment)
1.
```
