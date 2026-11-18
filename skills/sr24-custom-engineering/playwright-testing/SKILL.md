---
name: playwright-testing
description: >-
  Expert in Microsoft Playwright E2E and component testing — browser automation (Chromium, Firefox, WebKit),
  Locators, auto-waiting, Page Object Model (POM), API testing, visual regression / screenshot comparison,
  network interception, trace viewer, and CI/CD pipelines.
---

# Microsoft Playwright E2E & Automation Expert Skill

Playwright is a framework for Web Testing and Automation. It enables cross-browser, resilient, and fast end-to-end testing across modern web applications.

---

## 1. Core Architecture & Configuration

```typescript
// playwright.config.ts
import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  testDir: './e2e',
  fullyParallel: true,
  forbidOnly: !!process.env.CI,
  retries: process.env.CI ? 2 : 0,
  workers: process.env.CI ? 1 : undefined,
  reporter: [['html', { open: 'never' }], ['list']],
  use: {
    baseURL: process.env.BASE_URL || 'http://localhost:3000',
    trace: 'on-first-retry',
    screenshot: 'only-on-failure',
    video: 'retain-on-failure',
  },
  projects: [
    {
      name: 'chromium',
      use: { ...devices['Desktop Chrome'] },
    },
    {
      name: 'firefox',
      use: { ...devices['Desktop Firefox'] },
    },
    {
      name: 'Mobile Safari',
      use: { ...devices['iPhone 13'] },
    },
  ],
  webServer: {
    command: 'npm run dev',
    url: 'http://localhost:3000',
    reuseExistingServer: !process.env.CI,
    timeout: 120 * 1000,
  },
});
```

---

## 2. Robust Locators & User-Facing Queries

Always prioritize user-facing locators (accessibility roles, text, labels) over fragile CSS/XPath selectors.

```typescript
import { test, expect } from '@playwright/test';

test('Player login and dashboard navigation', async ({ page }) => {
  await page.goto('/');

  // 1. By Role (Recommended: Accessibility tree)
  await page.getByRole('button', { name: /play now/i }).click();

  // 2. By Label (Form fields)
  await page.getByLabel('Player Username').fill('MemeMaster99');

  // 3. By Placeholder
  await page.getByPlaceholder('Enter room code').fill('ROOM-420');

  // 4. By Text
  await expect(page.getByText('Ready to Roll')).toBeVisible();

  // 5. Test ID (Fallback for canvas or non-standard UI elements)
  await page.getByTestId('game-canvas').click({ position: { x: 250, y: 300 } });

  // Auto-waiting Assertions (Retry until condition met or timeout)
  await expect(page.getByRole('heading', { name: 'Scoreboard' })).toBeVisible();
  await expect(page.getByTestId('player-score')).toHaveText('100');
});
```

---

## 3. Page Object Model (POM) Pattern

Encapsulate UI interactions and queries into structured reusable classes.

```typescript
// pages/GamePage.ts
import { Page, Locator, expect } from '@playwright/test';

export class GamePage {
  readonly page: Page;
  readonly canvas: Locator;
  readonly startButton: Locator;
  readonly scoreDisplay: Locator;
  readonly gameOverModal: Locator;

  constructor(page: Page) {
    this.page = page;
    this.canvas = page.locator('#game-canvas');
    this.startButton = page.getByRole('button', { name: 'Start Game' });
    this.scoreDisplay = page.getByTestId('current-score');
    this.gameOverModal = page.getByTestId('game-over-modal');
  }

  async goto() {
    await this.page.goto('/games/spin-cricket');
  }

  async startGame() {
    await this.startButton.click();
    await expect(this.canvas).toBeVisible();
  }

  async clickCanvasAt(x: number, y: number) {
    await this.canvas.click({ position: { x, y } });
  }

  async verifyScore(expectedScore: string) {
    await expect(this.scoreDisplay).toHaveText(expectedScore);
  }
}

// e2e/game.spec.ts
test('Plays spin cricket game round', async ({ page }) => {
  const game = new GamePage(page);
  await game.goto();
  await game.startGame();
  await game.clickCanvasAt(150, 200);
  await game.verifyScore('6 Runs');
});
```

---

## 4. Network Interception & API Mocking

```typescript
test('Mocks high scores API response', async ({ page }) => {
  // Intercept and mock REST API
  await page.route('**/api/leaderboard', async (route) => {
    const json = [
      { rank: 1, username: 'TopG', score: 9999 },
      { rank: 2, username: 'ProGamer', score: 8500 },
    ];
    await route.fulfill({ json, status: 200 });
  });

  await page.goto('/leaderboard');
  await expect(page.getByText('TopG')).toBeVisible();
  await expect(page.getByText('9999')).toBeVisible();
});
```

---

## 5. Visual Regression Testing (Screenshot Diffing)

```typescript
test('Visual snapshot match of shop page', async ({ page }) => {
  await page.goto('/shop');
  // Wait for images and fonts to finish rendering
  await page.waitForLoadState('networkidle');

  // Compare full page screenshot against golden snapshot
  await expect(page).toHaveScreenshot('shop-page.png', {
    maxDiffPixelRatio: 0.05,
    fullPage: true,
  });
});
```

---

## 6. Authentication & Storage State Reuse

Avoid logging in via UI in every single test by saving the session state.

```typescript
// e2e/auth.setup.ts
import { test as setup, expect } from '@playwright/test';

const authFile = 'playwright/.auth/user.json';

setup('authenticate', async ({ page }) => {
  await page.goto('/login');
  await page.getByLabel('Email').fill('testuser@memeverse.com');
  await page.getByLabel('Password').fill('SecurePassword123!');
  await page.getByRole('button', { name: 'Sign In' }).click();

  await page.waitForURL('/dashboard');
  await page.context().storageState({ path: authFile });
});

// playwright.config.ts setup dependency:
// { name: 'setup', testMatch: /.*\.setup\.ts/ },
// { name: 'chromium', use: { storageState: 'playwright/.auth/user.json' }, dependencies: ['setup'] }
```

---

## 7. Best Practices & Debugging

1. **Use Trace Viewer**: When tests fail in CI, run `npx playwright show-trace trace.zip` to inspect DOM snapshots, console logs, and network timeline step-by-step.
2. **Never Use Arbitrary Timeouts (`page.waitForTimeout`)**: Use auto-waiting assertions (`expect(locator).toBeVisible()`) or explicit predicates (`page.waitForResponse()`).
3. **Isolate Test State**: Each test runs in an isolated `BrowserContext` with separate cookies, local storage, and cache.
