---
name: web-development
description: Guide web development for jfrog.com including tracking/tagging implementation, performance optimization, component patterns, and translating team analytics requirements into dev specs. Use when working on web development, tracking implementation, tagging, page speed, performance optimization, frontend components, or translating analytics team tag requests into specs.
---

# Web Development

## Quick Start

When asked to work on web development tasks:

1. Identify the task type (tracking/tagging, performance, component, standards)
2. Determine scope (new implementation, optimization, audit, spec creation)
3. Apply the appropriate workflow below
4. Produce implementation-ready specs or code with testing criteria

## Tracking & Tagging Implementation

For the full tagging checklist, see [tagging-checklist.md](tagging-checklist.md).

### Translating Team Tag Requests into Specs

When the analytics team requests tracking or tagging changes:

1. **Parse the request** — Extract: event name, trigger conditions, parameters/dimensions, page scope
2. **Validate completeness** — Check against the tagging checklist for missing fields
3. **Draft the spec** — Produce an implementation-ready document
4. **Identify dependencies** — Data layer changes, GTM updates, consent requirements
5. **Define QA criteria** — How to verify the tag fires correctly

### Tag Implementation Spec Template
```markdown
# Tag Implementation Spec — [Feature/Event Name]

## Overview
[What is being tracked and why]

## Event Details
| Field | Value |
|-------|-------|
| Event Name | |
| Trigger | |
| Page(s) | |
| Data Layer Variable(s) | |

## Parameters
| Parameter | Value/Source | Type | Required |
|-----------|-------------|------|----------|
| | | | |

## Implementation Steps
1. [ ] Data layer update
2. [ ] GTM tag creation
3. [ ] Trigger configuration
4. [ ] Consent integration
5. [ ] QA in staging

## QA Checklist
- [ ] Event fires on correct trigger
- [ ] All parameters populated correctly
- [ ] No duplicate events
- [ ] Works across browsers (Chrome, Firefox, Safari, Edge)
- [ ] Works on mobile and desktop
- [ ] Consent mode respected
- [ ] Data visible in GA4 DebugView
```

## Performance Optimization

### Core Web Vitals Targets
| Metric | Good | Needs Improvement | Poor |
|--------|------|-------------------|------|
| LCP (Largest Contentful Paint) | ≤ 2.5s | ≤ 4.0s | > 4.0s |
| INP (Interaction to Next Paint) | ≤ 200ms | ≤ 500ms | > 500ms |
| CLS (Cumulative Layout Shift) | ≤ 0.1 | ≤ 0.25 | > 0.25 |

### Performance Audit Checklist
- [ ] Images: WebP/AVIF format, responsive sizes, lazy loading below fold
- [ ] JavaScript: Code splitting, defer/async non-critical scripts, tree shaking
- [ ] CSS: Critical CSS inlined, unused CSS removed, no render-blocking stylesheets
- [ ] Fonts: Preloaded, font-display: swap, subset to used characters
- [ ] Caching: Appropriate cache headers, CDN configuration
- [ ] Third-party scripts: Audited for necessity, loaded asynchronously
- [ ] Server: Compression (Brotli/gzip), HTTP/2+, preconnect to origins

### Performance Report Template
```markdown
# Performance Audit — [Page/Section]

## Current Scores
| Metric | Mobile | Desktop | Target |
|--------|--------|---------|--------|
| LCP | | | ≤ 2.5s |
| INP | | | ≤ 200ms |
| CLS | | | ≤ 0.1 |
| Performance Score | | | ≥ 90 |

## Top Issues (by impact)
| Issue | Metric Affected | Est. Improvement | Effort |
|-------|----------------|-----------------|--------|

## Recommendations
1. [Prioritized by impact]
```

## Component Development Standards

When building or reviewing components for jfrog.com:

### Component Checklist
- [ ] Responsive across breakpoints (mobile, tablet, desktop)
- [ ] Accessible (ARIA labels, keyboard nav, screen reader tested)
- [ ] Supports all defined states (default, hover, active, focus, disabled, loading, error, empty)
- [ ] Follows existing design system patterns
- [ ] Performance: no unnecessary re-renders, optimized assets
- [ ] Cross-browser tested (Chrome, Firefox, Safari, Edge)
- [ ] Documented with usage examples

## Code Review Focus Areas

When reviewing web development PRs:

1. **Performance impact** — Will this change affect page load or CWV?
2. **Accessibility** — Does it maintain or improve a11y?
3. **Tracking integrity** — Does it break or modify existing tracking?
4. **SEO impact** — Does it affect crawlability, structured data, or content rendering?
5. **Mobile experience** — Does it work well on mobile?
6. **Security** — No XSS vectors, proper input sanitization
