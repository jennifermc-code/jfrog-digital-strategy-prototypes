---
name: seo-aeo-analysis
description: Perform SEO audits, keyword gap analysis, AEO evaluation, and synthesize team SEO/AEO recommendations for jfrog.com. Uses BrightEdge data. Use when working with SEO, AEO, keywords, search performance, rankings, BrightEdge, content optimization, or synthesizing team SEO recommendations.
---

# SEO/AEO Analysis

## Quick Start

When asked to work with SEO or AEO data:

1. Identify the analysis type (audit, keyword gap, content optimization, AEO, team rec synthesis)
2. Determine data sources available (BrightEdge export, GSC data, manual audit)
3. Apply the appropriate workflow below
4. Produce actionable recommendations ranked by impact

## BrightEdge Workflows

For detailed BrightEdge-specific workflows, see [brightedge-workflows.md](brightedge-workflows.md).

### Data Cube Analysis
- Import BrightEdge Data Cube exports
- Identify keyword clusters by topic/intent
- Flag ranking opportunities (positions 4-20 with high volume)
- Produce a prioritized keyword action table

### Share of Voice Tracking
- Parse Share of Voice reports
- Compare jfrog.com vs. competitors across key topic areas
- Trend SoV over time to show momentum or decline
- Recommend content investments to gain share

### Content Recommendations
- Intake BrightEdge content recommendations
- Cross-reference with existing jfrog.com content inventory
- Identify net-new content needs vs. optimization of existing pages
- Score by estimated traffic opportunity

## Technical SEO Audit

Evaluate against this checklist:

### Crawlability & Indexing
- [ ] Robots.txt configuration
- [ ] XML sitemap completeness and freshness
- [ ] Canonical tag implementation
- [ ] Hreflang tags (if multilingual)
- [ ] Index bloat / thin content pages

### On-Page
- [ ] Title tag optimization (unique, keyword-targeted, <60 chars)
- [ ] Meta descriptions (unique, compelling, <160 chars)
- [ ] H1 structure (single, descriptive)
- [ ] Header hierarchy (H2-H4 logical nesting)
- [ ] Internal linking structure and anchor text
- [ ] Image alt text coverage

### Performance
- [ ] Core Web Vitals (LCP, INP, CLS)
- [ ] Page load time
- [ ] Render-blocking resources
- [ ] Image optimization

### Structured Data
- [ ] Schema markup implementation
- [ ] FAQ schema where applicable
- [ ] Product/Software schema
- [ ] Organization schema

## AEO (AI Engine Optimization)

Evaluate how well jfrog.com content performs for AI-generated answers:

### Assessment Criteria
1. **Answer-readiness** — Does the content directly answer common questions in the first 2-3 sentences?
2. **Structured data** — Is content marked up for easy extraction?
3. **Authority signals** — Expert authorship, citations, data backing
4. **Topical coverage** — Does the content comprehensively cover the topic?
5. **Conversational alignment** — Does the content match how people ask questions to AI?

### AEO Audit Output
| Page/URL | Target Query | Answer-Readiness Score (1-5) | Missing Elements | Recommended Changes |
|----------|-------------|------------------------------|------------------|-------------------|

## Keyword Gap Analysis

1. Compare jfrog.com keyword portfolio vs. top 3 competitors
2. Identify keywords where competitors rank but JFrog doesn't
3. Classify gaps by: intent (informational, navigational, transactional), volume, difficulty
4. Prioritize by opportunity: high volume + low difficulty + high business relevance

Output as a table sorted by opportunity score.

## Synthesize Team SEO/AEO Recommendations

When the team provides SEO or AEO feedback/recommendations:

1. **Consolidate** — Gather all team inputs into a single list
2. **Deduplicate** — Merge overlapping recommendations
3. **Categorize** — Group by type (technical, content, on-page, AEO, link building)
4. **Prioritize** — Score each by: estimated traffic impact, effort to implement, strategic alignment
5. **Map to owners** — Identify who needs to act (content, dev, design)

### Team Rec Synthesis Output
```markdown
# SEO/AEO Team Recommendations — [Date]

## Summary
[X] total recommendations consolidated from team input

## By Category

### Technical SEO
| Rec | Impact (H/M/L) | Effort (H/M/L) | Owner | Status |
|-----|----------------|-----------------|-------|--------|

### Content Optimization
| Rec | Impact (H/M/L) | Effort (H/M/L) | Owner | Status |
|-----|----------------|-----------------|-------|--------|

### AEO Improvements
| Rec | Impact (H/M/L) | Effort (H/M/L) | Owner | Status |
|-----|----------------|-----------------|-------|--------|

## Top 5 Quick Wins
1.
2.
3.
4.
5.

## Next Steps
- [ ] Action with owner and deadline
```
