# Tracking Specification — [Feature/Initiative Name]

## Overview

| Field | Value |
|-------|-------|
| Feature | |
| Requested By | |
| Developer | |
| Status | Draft / Approved / Implemented / Verified |
| Date | |

## Business Context

[Why is this tracking needed? What questions will it answer?]

---

## Events

### Event 1: [event_name]

| Field | Value |
|-------|-------|
| Event Name | |
| Trigger | [User action or page condition] |
| Page(s) | [URL pattern or template] |

**Parameters:**
| Parameter | Value/Source | Type | Required | Example |
|-----------|-------------|------|----------|---------|
| | | string/number/boolean | Yes/No | |

**Data Layer Push:**
```javascript
dataLayer.push({
  event: 'event_name',
  parameter_1: 'value',
  parameter_2: 'value'
});
```

### Event 2: [event_name]

[Repeat structure above]

---

## Data Layer Specification

### New Variables
| Variable Name | Type | Source | Default | Notes |
|--------------|------|--------|---------|-------|

### Modified Variables
| Variable Name | Current Behavior | New Behavior | Breaking Change? |
|--------------|-----------------|-------------|-----------------|

---

## GTM Configuration

### Tags
| Tag Name | Type | Trigger | Variables Used |
|----------|------|---------|---------------|

### Triggers
| Trigger Name | Type | Conditions |
|-------------|------|-----------|

### Variables
| Variable Name | Type | Source |
|--------------|------|--------|

---

## Consent Requirements

| Event/Tag | Consent Category | Behavior Without Consent |
|-----------|-----------------|------------------------|
| | Analytics / Marketing / Functional | Does not fire / Fires anonymously |

---

## QA Plan

### Test Cases
| Scenario | Expected Result | Browser/Device |
|----------|----------------|---------------|
| | | |

### Verification Steps
1. [ ] Enable GTM Preview mode
2. [ ] Trigger each event
3. [ ] Verify in GA4 DebugView
4. [ ] Check all parameters populated
5. [ ] Test consent mode behavior
6. [ ] Cross-browser verification

---

## Sign-Off

| Role | Name | Approved | Date |
|------|------|----------|------|
| Analytics | | ☐ | |
| Development | | ☐ | |
| QA | | ☐ | |
