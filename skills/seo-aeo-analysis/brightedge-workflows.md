# BrightEdge Workflows

## Data Cube Export Analysis

### Parsing Data Cube CSVs

BrightEdge Data Cube exports typically include: keyword, search volume, rank, URL, topic group, page score.

**Workflow:**
1. Load the CSV into a structured format
2. Filter to jfrog.com-owned keywords
3. Segment by:
   - **Striking distance** (rank 4-20, volume > 500) — optimize existing content
   - **Defending** (rank 1-3) — maintain and monitor
   - **Opportunity** (rank 21-50, volume > 1000) — new content or major refresh needed
   - **Not ranking** — competitive gap, assess if topic is relevant
4. Cross-reference with existing content to determine optimize vs. create

### Output Format
```markdown
## Data Cube Analysis — [Date]

### Striking Distance (Quick Wins)
| Keyword | Volume | Current Rank | URL | Recommended Action |
|---------|--------|-------------|-----|-------------------|

### Defending (Monitor)
| Keyword | Volume | Current Rank | URL | Risk Level |
|---------|--------|-------------|-----|------------|

### Opportunity (Content Investment)
| Keyword | Volume | Current Rank | Competitor Ranking | Content Needed |
|---------|--------|-------------|-------------------|----------------|
```

## Share of Voice Reports

### Interpreting SoV Data

BrightEdge Share of Voice measures visibility across keyword groups.

**Key metrics:**
- **Total SoV %** — jfrog.com's visibility vs. total available
- **SoV by topic** — visibility broken down by keyword cluster
- **Competitor SoV** — how competitors compare in same clusters
- **SoV trend** — directional movement (weekly/monthly)

**Analysis workflow:**
1. Identify topic areas where JFrog SoV is declining
2. Cross-reference declining topics with business priority
3. Identify topics where competitors are gaining share
4. Recommend content/technical actions to regain visibility

## Content Recommendations Intake

When BrightEdge surfaces content recommendations:

1. Export the recommendations
2. Match each recommendation to an existing jfrog.com URL (if applicable)
3. Classify as: new page needed, existing page refresh, technical fix, structural change
4. Estimate effort for each action
5. Prioritize by: projected traffic gain × strategic alignment / effort

## Keyword Research Workflow

1. Start with seed topics from product/marketing priorities
2. Pull keyword data from BrightEdge Data Cube
3. Expand with related/long-tail queries
4. Classify by intent: informational, navigational, transactional, commercial investigation
5. Map to funnel stage: awareness, consideration, decision
6. Assign to content type: blog, docs, landing page, product page
