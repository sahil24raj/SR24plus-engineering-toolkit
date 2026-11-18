---
name: github-actions-ci
description: >-
  Specialist in GitHub Actions — automated test pipelines, dependency caching, matrix builds, release automation, and branch protection checks.
---

# GitHub Actions CI/CD Pipelines & Automated Release Gates

## 1. When to Activate
Activate this skill whenever a project or prompt requires specialist in github actions — automated test pipelines, dependency caching, matrix builds, release automation, and branch protection checks.. It is assigned to official engineering phases in the **SR24Plus Engineering Toolkit**.

## 2. When Not to Activate
- Do not activate when the task does not involve github-actions-ci.
- Do not activate as a substitute for simple static mockups where deeper engineering is unnecessary.

## 3. Core Capabilities
- High-speed CI workflows utilizing pnpm/npm caching to achieve sub-2 minute runs
- Matrix testing across Node versions (18, 20, 22) and operating systems
- Automated pull-request verification (lint, typecheck, unit tests, Playwright E2E)
- Automated semantic versioning and release changelog generation on main branch merge
- Deployment dispatch triggering production deployments on Vercel, Docker, or Kubernetes

## 4. Engineering Workflow
1. **Discovery & Architecture**: Inspect technical constraints, performance requirements, and data contracts.
2. **Setup & Configuration**: Install official package dependencies and configure environment variables.
3. **Implementation**: Author production-grade code using clean architecture, strict TypeScript types, and error handling.
4. **Validation & Testing**: Run unit and integration tests confirming zero regressions.
5. **Production Deployment**: Verify build bundle impact, tree-shaking, and observability telemetry.

## 5. Implementation Instructions & Code Patterns

```typescript
name: Production CI Pipeline
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: 'npm'

      - name: Install Dependencies
        run: npm ci

      - name: Typecheck
        run: npx tsc --noEmit

      - name: Lint
        run: npm run lint

      - name: Run Unit Tests
        run: npm run test -- --ci --maxWorkers=2

      - name: Install Playwright Browsers
        run: npx playwright install --with-deps chromium

      - name: Run E2E Tests
        run: npx playwright test
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
- **Repository**: [https://github.com/actions/runner](https://github.com/actions/runner)
- **Category**: SR24-WEB-DEV Canonical Engineering Skill

## 10. License & Attribution
- **License**: MIT
- **Maintained By**: SR24Plus Autonomous Engineering Architecture
