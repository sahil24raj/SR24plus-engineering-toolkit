---
name: growthbook-experimentation
description: >-
  Specialist in GrowthBook feature flagging, targeted rollouts, multi-variant A/B experiments, statistical significance calculation, and Bayesian analytics.
---

# GrowthBook Feature Flags & A/B Testing Experimentation

## 1. When to Activate
Activate this skill whenever a project or prompt requires specialist in growthbook feature flagging, targeted rollouts, multi-variant a/b experiments, statistical significance calculation, and bayesian analytics.. It is assigned to official engineering phases in the **SR24Plus Engineering Toolkit**.

## 2. When Not to Activate
- Do not activate when the task does not involve growthbook-experimentation.
- Do not activate as a substitute for simple static mockups where deeper engineering is unnecessary.

## 3. Core Capabilities
- Feature flag management with percentage rollouts, user attribute rules, and kill-switches
- Multi-variant A/B experiment evaluation with zero network roundtrip latency in Next.js
- Tracking experiment exposure events to PostHog, Mixpanel, or custom telemetry endpoints
- Statistical significance analysis (Bayesian / Frequentist) determining winner variants
- Safe continuous deployment rollouts with instant feature rollback upon error spike

## 4. Engineering Workflow
1. **Discovery & Architecture**: Inspect technical constraints, performance requirements, and data contracts.
2. **Setup & Configuration**: Install official package dependencies and configure environment variables.
3. **Implementation**: Author production-grade code using clean architecture, strict TypeScript types, and error handling.
4. **Validation & Testing**: Run unit and integration tests confirming zero regressions.
5. **Production Deployment**: Verify build bundle impact, tree-shaking, and observability telemetry.

## 5. Implementation Instructions & Code Patterns

```typescript
import { GrowthBook } from '@growthbook/growthbook-react';

export const gb = new GrowthBook({
  apiHost: process.env.NEXT_PUBLIC_GROWTHBOOK_API_HOST,
  clientKey: process.env.NEXT_PUBLIC_GROWTHBOOK_CLIENT_KEY,
  enableDevMode: process.env.NODE_ENV !== 'production',
  trackingCallback: (experiment, result) => {
    // Forward exposure to PostHog or custom telemetry
    console.log('[Experiment Viewed]', {
      experimentId: experiment.key,
      variationId: result.variationId,
    });
  },
});

export function getHeroBannerVariant(userId: string) {
  gb.setAttributes({ id: userId });
  return gb.getFeatureValue('hero-banner-layout', 'control');
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
- **Repository**: [https://github.com/growthbook/growthbook](https://github.com/growthbook/growthbook)
- **Category**: SR24-WEB-DEV Canonical Engineering Skill

## 10. License & Attribution
- **License**: MIT
- **Maintained By**: SR24Plus Autonomous Engineering Architecture
