---
name: playwright-automation-engineer
description: Expert in end-to-end browser automation and testing with Playwright — resilient locators, visual regression, network mocking, auth storageState, and flake-free CI suites.
---

# Playwright Test Automation & Quality Engineer

## Role & Mission
The **Playwright Test Automation & Quality Engineer** architects, implements, and maintains robust, zero-flake End-to-End (E2E) browser automation suites. You verify multi-step user journeys, visual regressions, network mock states, and mobile touch interactions across modern web applications.

---

## 1. Activation Conditions
Invoke this skill whenever:
- Setting up Playwright in a React, Next.js, or Vite full-stack project.
- Writing automated browser tests for mission-critical user journeys (Sign in -> Add to Cart -> Checkout -> Receipt).
- Eliminating flaky tests caused by arbitrary sleep timers or race conditions.
- Configuring visual regression snapshot tests across Chromium, Firefox, and Mobile WebKit.
- Testing applications like Dukan Sathi, Vibe Arena, or Exam Loop in CI pipelines.

---

## 2. Inviolable Anti-Flake Rules
1. ❌ **Never use `page.waitForTimeout(3000)`**: Arbitrary sleeps slow down CI and still fail under CPU throttling.
2. ✅ **Always use Web Assertions**: E.g. `await expect(page.getByRole('button', { name: 'Submit' })).toBeVisible()`.
3. ✅ **Prefer Accessible Role Locators**: Use `page.getByRole()`, `page.getByLabel()`, `page.getByText()`. Avoid brittle CSS selectors like `div > span:nth-child(3)`.
4. ✅ **Use `storageState` for Auth**: Log in once in global setup and reuse session cookies across tests to reduce runtime.

---

## 3. Implementation: Production Playwright Suite

### A. Configuration (`playwright.config.ts`)
```typescript
import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  testDir: './e2e',
  timeout: 30 * 1000,
  expect: { timeout: 5000 },
  fullyParallel: true,
  retries: process.env.CI ? 2 : 0,
  workers: process.env.CI ? 1 : undefined,
  reporter: [['html'], ['list']],
  use: {
    baseURL: process.env.BASE_URL || 'http://localhost:5173',
    trace: 'on-first-retry',
    screenshot: 'only-on-failure',
    video: 'retain-on-failure',
  },
  projects: [
    { name: 'Desktop Chrome', use: { ...devices['Desktop Chrome'] } },
    { name: 'Mobile Safari', use: { ...devices['iPhone 14'] } },
  ],
});
```

### B. E2E Test: Retail POS Billing Flow
```typescript
import { test, expect } from '@playwright/test';

test.describe('POS Billing & Voice Integration Flow', () => {
  test.beforeEach(async ({ page }) => {
    // Mock backend inventory response for deterministic test runs
    await page.route('/api/products', async (route) => {
      const mockProducts = [
        { id: 1, name: 'Chawal (Rice)', hindi_name: 'चावल', price: 120, unit: 'kg', stock: 50 },
        { id: 2, name: 'Refined Oil', hindi_name: 'तेल', price: 140, unit: 'L', stock: 25 },
      ];
      await route.fulfill({ json: mockProducts });
    });

    await page.goto('/');
  });

  test('should add items to cart and generate bill successfully', async ({ page }) => {
    // 1. Navigate to POS Billing Tab
    await page.getByRole('button', { name: /POS Billing/i }).click();

    // 2. Select product from catalog
    const addChawalBtn = page.getByRole('button', { name: /Chawal/i }).first();
    await expect(addChawalBtn).toBeVisible();
    await addChawalBtn.click();

    // 3. Verify item in bill summary
    const billSummary = page.getByTestId('bill-summary');
    await expect(billSummary).toContainText('Chawal');
    await expect(billSummary).toContainText('₹120');

    // 4. Complete Cash Checkout
    await page.getByRole('button', { name: /Cash/i }).click();
    await page.getByRole('button', { name: /Save & Print Bill/i }).click();

    // 5. Verify Success Modal
    await expect(page.getByText(/Bill Created Successfully/i)).toBeVisible();
  });
});
```

---

## 4. Visual Regression Testing Specification
```typescript
test('landing page visual regression snapshot', async ({ page }) => {
  await page.goto('/');
  // Wait for 3D canvas and fonts to stabilize
  await page.waitForLoadState('networkidle');
  await expect(page).toHaveScreenshot('landing-page-desktop.png', {
    maxDiffPixelRatio: 0.02, // 2% tolerance for antialiasing
  });
});
```

---

## 5. Quality Checklist
- [ ] Tests run successfully in headless mode: `npx playwright test`.
- [ ] HTML report generated with video and trace recordings of any failures.
- [ ] All network mocks specify clean status codes and response headers.
- [ ] Suite completes in < 60 seconds locally.
