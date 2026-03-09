---
name: web-analytics-analysis
description: Analyze GA4 web analytics data, synthesize team analytics reports, interpret Profound research insights, evaluate conversion funnels, and build KPI dashboards for jfrog.com. Use when working with analytics, GA4, conversions, traffic, A/B tests, Profound data, or synthesizing team analytics reports.
---

# Web Analytics Analysis

## Quick Start

When asked to work with analytics data:

1. Identify the analysis type (traffic, conversion, A/B test, team report synthesis, KPI dashboard)
2. Determine data sources (GA4 export, Profound, team reports)
3. Apply the appropriate workflow below
4. Produce insight-driven recommendations, not just data summaries

## GA4 Analysis Workflows

### Traffic Analysis
When reviewing traffic data:

1. **Segment by channel** — Organic, paid, direct, referral, social, email
2. **Period comparison** — Compare to prior period and same period last year
3. **Identify anomalies** — Spikes/drops and correlate with known events (launches, campaigns, algorithm updates)
4. **Engagement quality** — Engagement rate, pages/session, average engagement time per channel

Output format:
```markdown
## Traffic Summary — [Period]

### Channel Performance
| Channel | Sessions | Δ vs Prior | Δ vs YoY | Engagement Rate | Avg Engagement Time |
|---------|----------|-----------|----------|----------------|-------------------|

### Key Observations
1. [Observation with supporting data]

### Anomalies
| Date Range | Metric Affected | Δ Change | Likely Cause |
|-----------|----------------|----------|-------------|
```

### Conversion Funnel Analysis
1. Define the funnel stages (e.g., landing → product page → pricing → trial signup → activation)
2. Calculate drop-off rates between each stage
3. Segment by: device, channel, geography, new vs. returning
4. Identify the highest-leverage drop-off point
5. Recommend interventions with expected lift estimates

### A/B Test Evaluation
When reviewing test results:

1. **Statistical validity** — Sample size, confidence level, test duration
2. **Primary metric** — Did the variant beat control at ≥95% confidence?
3. **Secondary metrics** — Any negative downstream effects?
4. **Segmented analysis** — Does the variant win uniformly or only for certain segments?
5. **Recommendation** — Ship, iterate, or kill with reasoning

## Profound Insights Integration

When working with Profound research data:

1. Extract audience behavioral insights relevant to jfrog.com
2. Map insights to website sections and user journeys
3. Identify content or experience gaps based on audience needs
4. Cross-reference with GA4 behavioral data for validation
5. Produce actionable recommendations tied to specific pages/flows

## Synthesize Team Analytics Reports

When the team provides analytics reports or findings:

1. **Consolidate** — Gather all reports into a unified view
2. **Extract key metrics** — Pull out the headline numbers from each report
3. **Cross-reference** — Identify where reports reinforce or contradict each other
4. **Trend identification** — Surface patterns that span multiple reports
5. **Executive narrative** — Distill into a story with clear "so what" for leadership

### Team Report Synthesis Output
```markdown
# Analytics Synthesis — [Period]

## Key Metrics at a Glance
| Metric | Current | vs Prior Period | vs Target | Status |
|--------|---------|----------------|-----------|--------|

## Themes Across Reports
1. [Theme with supporting data from multiple reports]

## Conflicting Signals
| Signal A | Signal B | Resolution / Investigation Needed |
|----------|----------|----------------------------------|

## Recommended Actions
| Action | Supporting Data | Expected Impact | Owner |
|--------|----------------|-----------------|-------|

## Questions for Leadership
1.
```

## KPI Dashboard Framework

Standard KPIs for jfrog.com reporting:

### Acquisition
- Sessions (total, by channel)
- New users
- Organic search visibility (via BrightEdge SoV)

### Engagement
- Engagement rate
- Pages per session
- Average engagement time
- Scroll depth on key pages

### Conversion
- Trial signups
- Demo requests
- Content downloads (gated assets)
- Pricing page visits → trial conversion rate

### Retention
- Return visitor rate
- Feature page revisits

For additional report synthesis patterns, see [report-synthesis.md](report-synthesis.md).
