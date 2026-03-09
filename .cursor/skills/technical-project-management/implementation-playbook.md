# Technical Implementation Playbook

## Project Types & Approach

### Website Migration
Major platform, CMS, or infrastructure migration.

**Phases:**
1. **Discovery (2-4 weeks)**
   - Audit current site: pages, content, URLs, features, integrations
   - Document current architecture and tech stack
   - Map all redirects needed (URL inventory)
   - Identify SEO-critical pages (top traffic, top ranking, top backlinks)
   - Define success criteria and rollback triggers

2. **Planning (2-3 weeks)**
   - Technical architecture design
   - Content migration plan (manual vs. automated)
   - Redirect mapping (301 redirects for all changed URLs)
   - Tracking/analytics migration plan
   - SEO preservation plan (structured data, canonicals, sitemaps)
   - Testing strategy
   - Cutover plan with specific timing

3. **Development (varies)**
   - Build in phases with regular demos
   - Parallel development: don't take the old site down until new is ready
   - Migration scripts for content
   - Track progress against page/feature inventory

4. **Testing (2-4 weeks)**
   - Functional testing across browsers/devices
   - Content accuracy verification
   - Redirect testing (every single redirect)
   - Performance benchmarking vs. old site
   - Analytics parity verification
   - SEO pre-launch checklist (see below)
   - Accessibility testing
   - Load testing

5. **Cutover (1-2 days)**
   - DNS changes
   - CDN configuration
   - SSL certificate verification
   - Redirect activation
   - Monitoring activation
   - Smoke tests

6. **Post-Migration (2-4 weeks)**
   - Monitor search console for crawl errors
   - Track ranking changes daily
   - Monitor analytics for traffic anomalies
   - Fix broken redirects immediately
   - Validate all tracking is firing
   - Performance monitoring

### SEO Migration Checklist
- [ ] Complete URL redirect map (old → new)
- [ ] No redirect chains (A→B→C)
- [ ] Canonical tags updated
- [ ] XML sitemap updated and submitted
- [ ] Robots.txt updated
- [ ] Structured data migrated and validated
- [ ] Internal links updated (no links to redirected URLs)
- [ ] Hreflang tags updated (if multilingual)
- [ ] Google Search Console property verified for new domain/paths
- [ ] Bing Webmaster Tools updated
- [ ] BrightEdge configuration updated

### Platform Integration
Connecting new tools, APIs, or third-party services.

**Key Steps:**
1. Define integration requirements (data flow, frequency, format)
2. Evaluate API capabilities and limitations
3. Design error handling and failover
4. Build in staging/sandbox first
5. Test with production-like data
6. Monitor after launch

### Tracking Architecture Overhaul
Rebuilding analytics tracking infrastructure.

**Key Steps:**
1. Audit current tracking (what's tracked, what's missing, what's broken)
2. Define ideal measurement framework
3. Design data layer specification
4. Plan GTM container restructuring
5. Implement in phases (don't break existing tracking during transition)
6. QA every event against spec
7. Validate data in GA4 before decommissioning old tracking

## Estimation Guidelines

### Complexity Factors
| Factor | Adds Complexity | Example |
|--------|----------------|---------|
| Multiple teams | High | Frontend + backend + analytics + content |
| External vendors | High | Agency doing development, internal doing QA |
| Data migration | Medium-High | Moving content between CMSes |
| SEO sensitivity | Medium | High-traffic pages that can't lose rankings |
| Integration count | Medium | Each API integration adds risk |
| Regulatory/compliance | Medium | GDPR, accessibility requirements |
| Legacy tech debt | Variable | Unknown unknowns in old systems |

### Buffer Guidelines
- Add 20% buffer for well-understood projects
- Add 30-40% buffer for projects with unknowns
- Add 50%+ buffer for projects with external dependencies you don't control

## Retrospective Template

```markdown
# Retrospective — [Project Name]

## Project Summary
- **Duration:** [Planned] vs [Actual]
- **Scope:** [Delivered vs. planned]
- **Quality:** [Bugs found post-launch, performance, etc.]

## What Went Well
1.

## What Didn't Go Well
1.

## What We Learned
1.

## Action Items for Next Project
| Action | Owner | Due |
|--------|-------|-----|
```
