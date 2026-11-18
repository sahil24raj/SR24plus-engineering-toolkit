---
name: axe-core-accessibility
description: >-
  Specialist in Deque Axe-Core automated accessibility auditing, WCAG 2.1 AA/AAA compliance checks, color contrast calculation, and screen reader verification.
---

# Axe-Core Automated Web Accessibility & WCAG 2.1 AA Audit

## 1. When to Activate
Activate this skill whenever a project or prompt requires specialist in deque axe-core automated accessibility auditing, wcag 2.1 aa/aaa compliance checks, color contrast calculation, and screen reader verification.. It is assigned to official engineering phases in the **SR24Plus Engineering Toolkit**.

## 2. When Not to Activate
- Do not activate when the task does not involve axe-core-accessibility.
- Do not activate as a substitute for simple static mockups where deeper engineering is unnecessary.

## 3. Core Capabilities
- Automated accessibility test execution integrated into Playwright and Jest/Vitest test suites
- WCAG 2.1 Level AA violation detection (color contrast, missing form labels, invalid ARIA roles)
- Keyboard navigation focus management and focus-visible indicator verification
- Detailed violation reporting with specific DOM selector, failure summary, and remediation steps
- CI/CD accessibility quality gate preventing PR merge on critical accessibility defects

## 4. Engineering Workflow
1. **Discovery & Architecture**: Inspect technical constraints, performance requirements, and data contracts.
2. **Setup & Configuration**: Install official package dependencies and configure environment variables.
3. **Implementation**: Author production-grade code using clean architecture, strict TypeScript types, and error handling.
4. **Validation & Testing**: Run unit and integration tests confirming zero regressions.
5. **Production Deployment**: Verify build bundle impact, tree-shaking, and observability telemetry.

## 5. Implementation Instructions & Code Patterns

```typescript
import { test, expect } from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';

test.describe('Accessibility Compliance Suite (WCAG 2.1 AA)', () => {
  test('homepage should have zero critical or serious a11y violations', async ({ page }) => {
    await page.goto('/');
    await page.waitForLoadState('networkidle');

    const accessibilityScanResults = await new AxeBuilder({ page })
      .withTags(['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa'])
      .disableRules(['color-contrast']) // Optional: test dark-mode dynamically
      .analyze();

    if (accessibilityScanResults.violations.length > 0) {
      console.error(
        'Accessibility Violations Found:',
        JSON.stringify(accessibilityScanResults.violations, null, 2)
      );
    }

    expect(accessibilityScanResults.violations).toEqual([]);
  });
});
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
- **Repository**: [https://github.com/dequelabs/axe-core](https://github.com/dequelabs/axe-core)
- **Category**: SR24-WEB-DEV Canonical Engineering Skill

## 10. License & Attribution
- **License**: MPL-2.0
- **Maintained By**: SR24Plus Autonomous Engineering Architecture
