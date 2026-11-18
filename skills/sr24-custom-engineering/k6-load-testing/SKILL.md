---
name: k6-load-testing
description: >-
  Specialist in Grafana k6 — developer-centric load testing, performance benchmarking, stress testing, virtual user concurrency, and threshold assertion.
---

# Grafana k6 API Load Testing & Performance Benchmarking

## 1. When to Activate
Activate this skill whenever a project or prompt requires specialist in grafana k6 — developer-centric load testing, performance benchmarking, stress testing, virtual user concurrency, and threshold assertion.. It is assigned to official engineering phases in the **SR24Plus Engineering Toolkit**.

## 2. When Not to Activate
- Do not activate when the task does not involve k6-load-testing.
- Do not activate as a substitute for simple static mockups where deeper engineering is unnecessary.

## 3. Core Capabilities
- JavaScript-authored load test scripts with realistic user ramp-up and cool-down stages
- Quantitative SLA threshold enforcement (e.g. `http_req_duration: ["p(95)<300"]`)
- WebSocket load testing simulating concurrent multiplayer game room traffic
- Spike and stress testing determining maximum backend request breaking points
- Real-time metric telemetry export to Grafana, Datadog, or terminal summaries

## 4. Engineering Workflow
1. **Discovery & Architecture**: Inspect technical constraints, performance requirements, and data contracts.
2. **Setup & Configuration**: Install official package dependencies and configure environment variables.
3. **Implementation**: Author production-grade code using clean architecture, strict TypeScript types, and error handling.
4. **Validation & Testing**: Run unit and integration tests confirming zero regressions.
5. **Production Deployment**: Verify build bundle impact, tree-shaking, and observability telemetry.

## 5. Implementation Instructions & Code Patterns

```typescript
import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  stages: [
    { duration: '30s', target: 50 },  // Ramp-up to 50 concurrent users
    { duration: '1m', target: 50 },   // Sustained load
    { duration: '20s', target: 0 },   // Ramp-down
  ],
  thresholds: {
    http_req_duration: ['p(95)<250'], // 95% of requests must complete under 250ms
    http_req_failed: ['rate<0.01'],    // Error rate must be under 1%
  },
};

export default function () {
  const res = http.get('https://staging.gullyverse.com/api/v1/games/catalog');
  check(res, {
    'status is 200': (r) => r.status === 200,
    'body has games': (r) => r.body.includes('auto-rush'),
  });
  sleep(1);
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
- **Repository**: [https://github.com/grafana/k6](https://github.com/grafana/k6)
- **Category**: SR24-WEB-DEV Canonical Engineering Skill

## 10. License & Attribution
- **License**: AGPL-3.0
- **Maintained By**: SR24Plus Autonomous Engineering Architecture
