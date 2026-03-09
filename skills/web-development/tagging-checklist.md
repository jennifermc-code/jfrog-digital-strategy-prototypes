# Tracking & Tagging Checklist

## Pre-Implementation Checklist

Before implementing any new tracking:

### Requirements Gathering
- [ ] Event name defined (follows naming convention)
- [ ] Business question this tracking answers is documented
- [ ] Trigger condition clearly specified
- [ ] All required parameters/dimensions listed
- [ ] Page scope defined (all pages, specific templates, specific URLs)
- [ ] User segment targeting (all users, logged in, specific cohorts)

### Naming Convention
Events should follow: `category_action_label`
- **category**: page area or feature (e.g., `nav`, `hero`, `pricing`, `form`)
- **action**: what happened (e.g., `click`, `view`, `submit`, `scroll`)
- **label**: specific element (e.g., `cta_primary`, `tab_features`, `field_email`)

Example: `pricing_click_plan_enterprise`

### Data Layer Requirements
- [ ] Required data layer variables documented
- [ ] Variable naming follows convention
- [ ] Variable types specified (string, number, boolean, array)
- [ ] Default/fallback values defined
- [ ] Data layer push timing documented (on load, on interaction, on state change)

## Implementation Checklist

### Google Tag Manager
- [ ] Tag created with correct event name
- [ ] Trigger configured with correct conditions
- [ ] Variables mapped to data layer
- [ ] Tag sequencing set if dependencies exist
- [ ] Consent mode integration configured
- [ ] Tag priority set appropriately

### Data Layer Code
- [ ] `dataLayer.push()` calls added at correct points
- [ ] Event object structure matches spec
- [ ] No PII (personally identifiable information) in data layer
- [ ] Error handling for missing data
- [ ] Works with single-page app navigation (if applicable)

## QA Checklist

### Functional Testing
- [ ] Event fires on correct trigger (and only on that trigger)
- [ ] All parameters populated with correct values
- [ ] No duplicate event fires
- [ ] Event fires on first interaction and subsequent interactions
- [ ] Works after page navigation (SPA)

### Cross-Environment
- [ ] Verified in GTM Preview mode
- [ ] Verified in GA4 DebugView
- [ ] Tested on Chrome, Firefox, Safari, Edge
- [ ] Tested on mobile (iOS Safari, Android Chrome)
- [ ] Tested with ad blocker enabled (graceful degradation)

### Data Validation
- [ ] Event appears in GA4 Realtime report
- [ ] Parameters visible in GA4 event detail
- [ ] No unexpected null/undefined values
- [ ] Data types are correct in GA4

### Consent & Privacy
- [ ] Tag respects consent mode settings
- [ ] No tracking fires before consent is granted (where required)
- [ ] Tag is categorized correctly (analytics, marketing, functional)
- [ ] Privacy policy updated if new data collection

## Post-Launch Verification

- [ ] Monitor for 48-72 hours after launch
- [ ] Compare event volume to expected baseline
- [ ] Verify no impact on page performance
- [ ] Confirm data flows to any downstream dashboards/reports
- [ ] Document in tracking inventory spreadsheet
