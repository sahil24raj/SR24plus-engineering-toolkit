---
name: lost-pixel-visual-regression
description: >-
  Specialist in Lost Pixel visual regression testing — automated screenshot comparison, Storybook snapshotting, pixel diff thresholds, and UI change detection.
---

# Lost Pixel Automated Visual Regression & Pixel Diffing

## 1. When to Activate
Activate this skill whenever a project or prompt requires specialist in lost pixel visual regression testing — automated screenshot comparison, storybook snapshotting, pixel diff thresholds, and ui change detection.. It is assigned to official engineering phases in the **SR24Plus Engineering Toolkit**.

## 2. When Not to Activate
- Do not activate when the task does not involve lost-pixel-visual-regression.
- Do not activate as a substitute for simple static mockups where deeper engineering is unnecessary.

## 3. Core Capabilities
- Automated full-page and component screenshot comparisons across Git branches
- Pixel diffing algorithms highlighting visual shifts, color drift, and typography regressions
- Storybook and Next.js App Router route screenshot automation
- Custom threshold configuration allowing acceptable font anti-aliasing variations
- Visual review workflows preventing unintended CSS regressions from shipping

## 4. Engineering Workflow
1. **Discovery & Architecture**: Inspect technical constraints, performance requirements, and data contracts.
2. **Setup & Configuration**: Install official package dependencies and configure environment variables.
3. **Implementation**: Author production-grade code using clean architecture, strict TypeScript types, and error handling.
4. **Validation & Testing**: Run unit and integration tests confirming zero regressions.
5. **Production Deployment**: Verify build bundle impact, tree-shaking, and observability telemetry.

## 5. Implementation Instructions & Code Patterns

```typescript
// lostpixel.config.ts
import { CustomProjectConfig } from 'lost-pixel';

export const config: CustomProjectConfig = {
  pageShots: {
    pages: [
      { path: '/', name: 'homepage' },
      { path: '/games', name: 'games-catalog' },
      { path: '/game/auto-rush', name: 'auto-rush-lobby' },
    ],
    baseUrl: 'http://127.0.0.1:3000',
  },
  threshold: 0.02, // 2% tolerance for minor anti-aliasing
  generateOnly: true,
  imagePathBaseline: '.lostpixel/baseline',
  imagePathCurrent: '.lostpixel/current',
  imagePathDifference: '.lostpixel/difference',
};
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
- **Repository**: [https://github.com/lost-pixel/lost-pixel](https://github.com/lost-pixel/lost-pixel)
- **Category**: SR24-WEB-DEV Canonical Engineering Skill

## 10. License & Attribution
- **License**: MIT
- **Maintained By**: SR24Plus Autonomous Engineering Architecture
