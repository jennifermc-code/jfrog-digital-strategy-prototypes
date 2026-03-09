---
name: web-design-review
description: Review web designs for quality, accessibility, brand consistency, and responsive behavior for jfrog.com. Use when reviewing designs, conducting accessibility audits, checking WCAG compliance, evaluating brand consistency, reviewing responsive layouts, or critiquing mockups.
---

# Web Design Review

## Quick Start

When asked to review a web design:

1. Identify the review scope (full page, component, redesign, accessibility audit)
2. Determine the format (screenshot, Figma link, live URL, markup)
3. Apply the relevant evaluation criteria below
4. Produce structured, actionable feedback organized by severity

## Design Critique Framework

Evaluate designs across these dimensions:

### 1. Visual Hierarchy
- Is the most important content/CTA immediately visible?
- Does the eye follow a logical path through the page?
- Are headings, subheadings, and body text clearly differentiated?
- Is there appropriate contrast between primary and secondary content?

### 2. Brand Consistency
- Colors align with JFrog brand palette
- Typography matches brand guidelines (families, weights, sizes)
- Iconography style is consistent
- Imagery style/treatment is on-brand
- Tone and voice in UI copy match brand guidelines

### 3. Layout & Spacing
- Consistent grid usage
- Appropriate whitespace (not cramped, not sparse)
- Alignment is precise and intentional
- Content sections have clear boundaries

### 4. Interaction Design
- CTAs are prominent and clearly labeled
- Interactive elements have visible affordances
- Hover/focus/active states are defined
- Form design follows conventions (labels, validation, error states)

### 5. Responsive Design
- Layout adapts appropriately at key breakpoints (mobile, tablet, desktop)
- Touch targets are minimum 44×44px on mobile
- No horizontal scroll on any viewport
- Images and media scale correctly
- Navigation transforms appropriately for mobile

## Accessibility Audit (WCAG 2.1 AA)

### Color & Contrast
- [ ] Text contrast ratio ≥ 4.5:1 (normal text) / ≥ 3:1 (large text)
- [ ] UI component contrast ≥ 3:1 against background
- [ ] Information not conveyed by color alone
- [ ] Links distinguishable from surrounding text without color

### Content Structure
- [ ] Logical heading hierarchy (H1 → H2 → H3, no skips)
- [ ] Meaningful link text (no "click here")
- [ ] All images have descriptive alt text
- [ ] Decorative images use empty alt or CSS background

### Keyboard & Navigation
- [ ] All interactive elements keyboard-accessible
- [ ] Visible focus indicators on all focusable elements
- [ ] Logical tab order
- [ ] Skip navigation link present
- [ ] No keyboard traps

### Forms
- [ ] All inputs have visible labels
- [ ] Required fields clearly indicated
- [ ] Error messages specific and actionable
- [ ] Form validation accessible to screen readers

## Feedback Output Format

```markdown
# Design Review — [Page/Component Name]

## Overall Assessment
[1-2 sentence summary: design quality level, biggest strength, biggest concern]

## Critical Issues (Must Fix)
| Issue | Location | WCAG Criterion | Recommendation |
|-------|----------|---------------|----------------|

## Improvements (Should Fix)
| Issue | Location | Category | Recommendation |
|-------|----------|----------|----------------|

## Enhancements (Nice to Have)
| Suggestion | Location | Expected Benefit |
|-----------|----------|-----------------|

## Strengths
- [What's working well — important for team morale and pattern reinforcement]
```

## Component-Level Review

When reviewing a specific component (nav, hero, card, form, footer):

1. Evaluate against the design system / existing patterns
2. Check consistency with how the component is used elsewhere on jfrog.com
3. Verify all states are defined (default, hover, active, focus, disabled, error, loading, empty)
4. Assess mobile behavior specifically
5. Note any deviations from established patterns and whether they're justified
