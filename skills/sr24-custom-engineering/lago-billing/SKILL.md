---
name: lago-billing
description: >-
  Specialist in Lago open-source metering and billing architecture — recurring plans, usage-based fee calculation, invoicing, and payment provider routing.
---

# Lago Usage-Based Metering & Hybrid Subscription Billing

## 1. When to Activate
Activate this skill whenever a project or prompt requires specialist in lago open-source metering and billing architecture — recurring plans, usage-based fee calculation, invoicing, and payment provider routing.. It is assigned to official engineering phases in the **SR24Plus Engineering Toolkit**.

## 2. When Not to Activate
- Do not activate when the task does not involve lago-billing.
- Do not activate as a substitute for simple static mockups where deeper engineering is unnecessary.

## 3. Core Capabilities
- Usage-based event ingestion architecture (`POST /api/v1/events`) with idempotent transaction IDs
- Hybrid subscription models combining base recurring tier fees with pay-per-use meters
- Proration and mid-cycle tier upgrade/downgrade calculation
- Automated PDF invoice generation and payment provider reconciliation (Razorpay, Stripe)
- Prepaid credit wallet architectures for SaaS and API consumption platforms

## 4. Engineering Workflow
1. **Discovery & Architecture**: Inspect technical constraints, performance requirements, and data contracts.
2. **Setup & Configuration**: Install official package dependencies and configure environment variables.
3. **Implementation**: Author production-grade code using clean architecture, strict TypeScript types, and error handling.
4. **Validation & Testing**: Run unit and integration tests confirming zero regressions.
5. **Production Deployment**: Verify build bundle impact, tree-shaking, and observability telemetry.

## 5. Implementation Instructions & Code Patterns

```typescript
import { Client } from 'lago-javascript-client';

const lago = Client(process.env.LAGO_API_KEY || '', {
  baseUrl: process.env.LAGO_API_URL || 'https://api.getlago.com/api/v1',
});

// Record metered usage event (e.g. AI game matches played)
export async function recordGameMatchEvent(customerId: string, matchesCount: number) {
  await lago.events.createEvent({
    event: {
      transaction_id: `tx_${Date.now()}_${customerId}`,
      customer_id: customerId,
      code: 'game_matches_played',
      timestamp: Math.floor(Date.now() / 1000),
      properties: { count: matchesCount },
    },
  });
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
- **Repository**: [https://github.com/getlago/lago](https://github.com/getlago/lago)
- **Category**: SR24-WEB-DEV Canonical Engineering Skill

## 10. License & Attribution
- **License**: AGPL-3.0
- **Maintained By**: SR24Plus Autonomous Engineering Architecture
