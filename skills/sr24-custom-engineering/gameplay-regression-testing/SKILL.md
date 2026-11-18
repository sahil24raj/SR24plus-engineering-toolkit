---
name: gameplay-regression-testing
description: >-
  Specialist in automated gameplay regression testing with Playwright — keyboard input simulation, collision trigger verification, state machine checks, and game stability.
---

# Automated Gameplay Regression Testing & Collision QA Specialist

## 1. When to Activate
Activate this skill whenever a game project or prompt requires specialist in automated gameplay regression testing with playwright — keyboard input simulation, collision trigger verification, state machine checks, and game stability.. It is assigned to official engineering phases in the **SR24Plus Engineering Toolkit**.

## 2. When Not to Activate
- Do not activate when the task does not involve gameplay-regression-testing.
- Do not activate as a substitute for simple static mockups where deeper game systems engineering is unnecessary.

## 3. Core Capabilities
- Automated input sequence replay validating movement, steering, acceleration, and jumping
- In-game state verification via window debug bridges (`window.__GAME_STATE__`)
- Collision boundary testing ensuring vehicles and runners never fall off track corridors
- Boss battle and QTE sequence progression testing ensuring zero softlocks or frozen timers
- Visual screenshot regression testing catching broken textures, inverted controls, or UI clipping

## 4. Engineering Workflow
1. **Design & Architecture**: Inspect gameplay loops, frame rate budgets, physics constraints, and network topology.
2. **Setup & Initialization**: Configure libraries, canvas bindings, physics worlds, and input listeners.
3. **Implementation**: Author deterministic game loops, decoupled systems, state machines, and rendering passes.
4. **Optimization**: Audit draw calls, memory allocation, garbage collection, and frame time stability.
5. **Testing & QA**: Execute automated regression, collision checks, network latency tests, and visual snapshot reviews.

## 5. Implementation Instructions & Code Patterns

```typescript
import { test, expect } from '@playwright/test';

test.describe('Giant Rush 3D Gameplay Regression', () => {
  test('player navigates track, collects color runners, and initiates boss QTE', async ({ page }) => {
    await page.goto('/game/giant-rush');
    await page.waitForSelector('canvas');

    // Wait for gameplay start
    await page.waitForFunction(() => (window as any).__GIANT_RUSH_PHASE__ === 'RUNNING', { timeout: 10000 });

    // Test steering controls (A/D)
    await page.keyboard.down('KeyA');
    await page.waitForTimeout(500);
    await page.keyboard.up('KeyA');

    const stateAfterLeft = await page.evaluate(() => (window as any).__GIANT_RUSH_PLAYER_POS__);
    expect(stateAfterLeft.x).toBeLessThan(0); // Successfully steered left

    // Wait for finish line approach and verify QTE transition
    await page.waitForFunction(() => (window as any).__GIANT_RUSH_PHASE__ === 'BOSS_QTE', { timeout: 35000 });
    const qteState = await page.evaluate(() => (window as any).__GIANT_RUSH_PHASE__);
    expect(qteState).toBe('BOSS_QTE');
  });
});
```

## 6. Best Practices
- **Deterministic Loop**: Always use fixed-timestep loops for physics to avoid frame-rate dependency.
- **Zero Allocations in Loop**: Pre-allocate vectors, matrices, and objects; never allocate new objects in `update` or `render`.
- **Responsive Controls**: Support keyboard, gamepad, and virtual touch joysticks with identical input abstractions.
- **Audio Management**: Always unlock audio contexts on first user interaction and manage volumes through bus mixers.

## 7. Common Anti-Patterns to Avoid
- Variable delta-time in physics causing objects to tunnel through geometry at low frame rates.
- Polling in tight loops or allocating garbage that triggers periodic GC stutter.
- Hardcoding screen dimensions instead of responsive canvas auto-scaling.
- Trusting client game state in multiplayer games without server authority.

## 8. Verification & Testing Checklist
- [ ] 60 FPS maintained under maximum entity density.
- [ ] Physics simulation deterministic across varied display refresh rates (60Hz, 120Hz).
- [ ] Zero memory allocations in render loop verified via Chrome DevTools Memory profiler.
- [ ] Responsive controls tested across desktop keyboard and mobile touch viewports.

## 9. Official Source Repository & Upstream Reference
- **Repository**: [https://github.com/microsoft/playwright](https://github.com/microsoft/playwright)
- **Category**: SR24-GAME-DEV Canonical Engineering Skill

## 10. License & Attribution
- **License**: Apache-2.0
- **Maintained By**: SR24Plus Autonomous Engineering Architecture
