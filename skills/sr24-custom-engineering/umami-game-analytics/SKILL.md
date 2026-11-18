---
name: umami-game-analytics
description: >-
  Specialist in Umami — lightweight, self-hosted, privacy-first game telemetry, event tracking, match completion metrics, and zero-cookie compliance.
---

# Umami Lightweight Privacy-First Game Telemetry Specialist

## 1. When to Activate
Activate this skill whenever a game project or prompt requires specialist in umami — lightweight, self-hosted, privacy-first game telemetry, event tracking, match completion metrics, and zero-cookie compliance.. It is assigned to official engineering phases in the **SR24Plus Engineering Toolkit**.

## 2. When Not to Activate
- Do not activate when the task does not involve umami-game-analytics.
- Do not activate as a substitute for simple static mockups where deeper game systems engineering is unnecessary.

## 3. Core Capabilities
- Ultra-lightweight (<3KB) telemetry tracking script with zero performance impact on game loops
- Custom gaming event tracking (Match Started, Level Cleared, Character Selected, Game Over)
- Zero cookie and zero GDPR consent banner requirement keeping browser game UI uncluttered
- Real-time active concurrent gamer counts and geographic player distribution
- Self-hostable open-source backend on Docker or Vercel with PostgreSQL storage

## 4. Engineering Workflow
1. **Design & Architecture**: Inspect gameplay loops, frame rate budgets, physics constraints, and network topology.
2. **Setup & Initialization**: Configure libraries, canvas bindings, physics worlds, and input listeners.
3. **Implementation**: Author deterministic game loops, decoupled systems, state machines, and rendering passes.
4. **Optimization**: Audit draw calls, memory allocation, garbage collection, and frame time stability.
5. **Testing & QA**: Execute automated regression, collision checks, network latency tests, and visual snapshot reviews.

## 5. Implementation Instructions & Code Patterns

```typescript
export function trackUmamiGameEvent(eventName: string, eventData: Record<string, string | number> = {}) {
  if (typeof window !== 'undefined' && (window as any).umami) {
    (window as any).umami.track(eventName, eventData);
  }
}

// Example: track match completion
export function logMatchResult(gameSlug: string, isVictory: boolean, score: number) {
  trackUmamiGameEvent('match_result', {
    game: gameSlug,
    result: isVictory ? 'victory' : 'defeat',
    final_score: score,
  });
}
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
- **Repository**: [https://github.com/umami-software/umami](https://github.com/umami-software/umami)
- **Category**: SR24-GAME-DEV Canonical Engineering Skill

## 10. License & Attribution
- **License**: MIT
- **Maintained By**: SR24Plus Autonomous Engineering Architecture
