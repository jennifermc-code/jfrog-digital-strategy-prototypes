# Report Synthesis Patterns

## Multi-Source Data Reconciliation

When combining data from multiple sources (GA4, BrightEdge, Profound, team reports):

### Common Discrepancies
- **Session counts** — GA4 vs. other tools may differ due to tracking methodology
- **Channel attribution** — Default channel groupings vary across platforms
- **Date ranges** — Ensure all reports cover the same period before comparing

### Reconciliation Steps
1. Align date ranges across all data sources
2. Normalize metrics to common definitions
3. Flag discrepancies > 10% for investigation
4. Use GA4 as the source of truth for traffic/conversion metrics
5. Use BrightEdge as the source of truth for keyword/ranking metrics

## Report Cadence Templates

### Weekly Pulse
- Top-line traffic and conversion numbers
- Notable changes vs. prior week
- Any urgent anomalies
- 3-bullet summary for team standup

### Monthly Deep Dive
- Full channel performance breakdown
- Conversion funnel analysis
- Content performance (top pages, new content performance)
- SEO visibility changes (from BrightEdge)
- Recommendations for next month

### Quarterly Business Review (Analytics Section)
- Quarter-over-quarter and year-over-year trends
- Progress against annual KPI targets
- Channel mix evolution
- Conversion rate trends by segment
- Investment efficiency (if paid data available)
- Strategic recommendations for next quarter

## Visualization Recommendations

When presenting analytics data:

| Data Type | Best Visualization | Notes |
|-----------|-------------------|-------|
| Trends over time | Line chart | Use consistent time intervals |
| Channel comparison | Horizontal bar chart | Sort by value descending |
| Funnel drop-off | Funnel chart or waterfall | Show absolute numbers and percentages |
| Segment comparison | Grouped bar chart | Limit to 4-5 segments |
| KPI vs. target | Bullet chart or gauge | Show target line clearly |
| Distribution | Histogram or box plot | Use for engagement time, page depth |

## Anomaly Investigation Workflow

When a metric shows unexpected movement:

1. **Confirm the data** — Check for tracking issues, tag changes, or filter problems
2. **Isolate the segment** — Which channel, device, geography, or page is affected?
3. **Check the timeline** — When exactly did the change begin?
4. **Correlate with events** — Site changes, campaigns, algorithm updates, competitor actions
5. **Quantify the impact** — What's the estimated effect in sessions, conversions, or revenue?
6. **Recommend response** — Immediate action, monitoring, or no action needed
