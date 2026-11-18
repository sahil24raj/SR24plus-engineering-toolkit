---
name: sentry-monitoring
description: >-
  Specialist in Sentry application performance monitoring (APM) — exception tracking, source map uploads, distributed tracing, and user crash diagnostics.
---

# Sentry Real-Time Error Tracking & Release Performance Health

## 1. When to Activate
Activate this skill whenever a project or prompt requires specialist in sentry application performance monitoring (apm) — exception tracking, source map uploads, distributed tracing, and user crash diagnostics.. It is assigned to official engineering phases in the **SR24Plus Engineering Toolkit**.

## 2. When Not to Activate
- Do not activate when the task does not involve sentry-monitoring.
- Do not activate as a substitute for simple static mockups where deeper engineering is unnecessary.

## 3. Core Capabilities
- Client and server error tracking capturing unhandled exceptions with full stack traces
- Source-map generation and automated release artifact upload for de-minified traces
- Performance transaction tracing monitoring Core Web Vitals (LCP, FID, CLS, TTFB)
- Session replay recording DOM interactions leading up to customer-facing exceptions
- Alert rule configuration alerting engineering on error spikes in Discord / Slack

## 4. Engineering Workflow
1. **Discovery & Architecture**: Inspect technical constraints, performance requirements, and data contracts.
2. **Setup & Configuration**: Install official package dependencies and configure environment variables.
3. **Implementation**: Author production-grade code using clean architecture, strict TypeScript types, and error handling.
4. **Validation & Testing**: Run unit and integration tests confirming zero regressions.
5. **Production Deployment**: Verify build bundle impact, tree-shaking, and observability telemetry.

## 5. Implementation Instructions & Code Patterns

```typescript
import * as Sentry from '@sentry/nextjs';

Sentry.init({
  dsn: process.env.NEXT_PUBLIC_SENTRY_DSN,
  environment: process.env.NODE_ENV,
  tracesSampleRate: process.env.NODE_ENV === 'production' ? 0.2 : 1.0,
  replaysSessionSampleRate: 0.1,
  replaysOnErrorSampleRate: 1.0,
  integrations: [
    Sentry.replayIntegration({
      maskAllText: true,
      blockAllMedia: true,
    }),
  ],
});

export function logHandledError(error: unknown, context?: Record<string, unknown>) {
  console.error('[Logged Error]', error);
  Sentry.captureException(error, { extra: context });
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
- **Repository**: [https://github.com/getsentry/sentry](https://github.com/getsentry/sentry)
- **Category**: SR24-WEB-DEV Canonical Engineering Skill

## 10. License & Attribution
- **License**: FSL-1.1-Apache-2.0
- **Maintained By**: SR24Plus Autonomous Engineering Architecture
