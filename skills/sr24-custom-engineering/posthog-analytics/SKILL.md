---
name: posthog-analytics
description: >-
  Specialist in PostHog product telemetry — custom event instrumentation, funnel conversion analysis, session replays, feature flags, and retention cohort tracking.
---

# PostHog Product Analytics, Session Replay & Telemetry

## 1. When to Activate
Activate this skill whenever a project or prompt requires specialist in posthog product telemetry — custom event instrumentation, funnel conversion analysis, session replays, feature flags, and retention cohort tracking.. It is assigned to official engineering phases in the **SR24Plus Engineering Toolkit**.

## 2. When Not to Activate
- Do not activate when the task does not involve posthog-analytics.
- Do not activate as a substitute for simple static mockups where deeper engineering is unnecessary.

## 3. Core Capabilities
- Client and server-side custom event tracking with rich JSON properties
- Session replay recording user journeys, drop-offs, and UI rage-clicks
- Funnel analysis tracking step-by-step conversion from landing to match play
- Cohort segmentation and retention curves calculating Day 1, Day 7, Day 30 retention
- Privacy-compliant IP masking and GDPR cookie-less telemetry modes

## 4. Engineering Workflow
1. **Discovery & Architecture**: Inspect technical constraints, performance requirements, and data contracts.
2. **Setup & Configuration**: Install official package dependencies and configure environment variables.
3. **Implementation**: Author production-grade code using clean architecture, strict TypeScript types, and error handling.
4. **Validation & Testing**: Run unit and integration tests confirming zero regressions.
5. **Production Deployment**: Verify build bundle impact, tree-shaking, and observability telemetry.

## 5. Implementation Instructions & Code Patterns

```typescript
import posthog from 'posthog-js';

export function initAnalytics() {
  if (typeof window !== 'undefined' && process.env.NEXT_PUBLIC_POSTHOG_KEY) {
    posthog.init(process.env.NEXT_PUBLIC_POSTHOG_KEY, {
      api_host: process.env.NEXT_PUBLIC_POSTHOG_HOST || 'https://app.posthog.com',
      capture_pageview: true,
      session_recording: {
        maskAllInputs: true,
      },
    });
  }
}

export function trackGameEvent(eventName: string, properties: Record<string, unknown> = {}) {
  if (typeof window !== 'undefined') {
    posthog.capture(eventName, {
      timestamp: new Date().toISOString(),
      ...properties,
    });
  }
}
```

## 6. Best Practices
- **Strict Typing**: Never use `any`; use strict interface and generic contracts.
- **Error Boundaries**: Handle all edge cases, offline drops, and network timeouts gracefully.
- **Performance Budget**: Avoid blocking main thread operations; optimize bundle sizes and lazy-load where appropriate.
- **Security**: Never expose private keys, credentials, or sensitive customer data in client-side bundles.

## 7. Common Anti-Patterns to Avoid
- Hardcoding credentials or API endpoints directly into source files.
- Ignoring promise rejections and async exceptions.
- Creating monolithic un-testable files instead of modular single-responsibility units.
- Introducing layout shifts or un-optimized re-renders.

## 8. Verification & Testing Checklist
- [ ] TypeScript compiles cleanly with zero errors (`tsc --noEmit`).
- [ ] Unit tests pass verifying expected behavior and edge cases.
- [ ] Environment variables documented in `.env.example`.
- [ ] Build artifact size verified with tree-shaking confirmed.

## 9. Official Source Repository & Upstream Reference
- **Repository**: [https://github.com/PostHog/posthog](https://github.com/PostHog/posthog)
- **Category**: SR24-WEB-DEV Canonical Engineering Skill

## 10. License & Attribution
- **License**: MIT
- **Maintained By**: SR24Plus Autonomous Engineering Architecture
