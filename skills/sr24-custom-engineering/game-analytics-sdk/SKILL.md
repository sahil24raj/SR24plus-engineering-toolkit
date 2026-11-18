---
name: game-analytics-sdk
description: >-
  Specialist in GameAnalytics SDK integration — progression tracking (Start/Complete/Fail), economy resource sinks & sources, error logging, and cohort analysis.
---

# GameAnalytics SDK Core Loop Telemetry & Retention Specialist

## 1. When to Activate
Activate this skill whenever a game project or prompt requires specialist in gameanalytics sdk integration — progression tracking (start/complete/fail), economy resource sinks & sources, error logging, and cohort analysis.. It is assigned to official engineering phases in the **SR24Plus Engineering Toolkit**.

## 2. When Not to Activate
- Do not activate when the task does not involve game-analytics-sdk.
- Do not activate as a substitute for simple static mockups where deeper game systems engineering is unnecessary.

## 3. Core Capabilities
- Progression event tracking (`addProgressionEvent(ProgressionStatus, world, level, phase)`)
- Resource sink and source tracking (currencies spent, earned, and soft balances)
- Design telemetry tracking (weapon selections, control preferences, death coordinates)
- In-game error and FPS drop automated telemetry reporting
- Player cohort retention analysis calculating average session time and match completion rates

## 4. Engineering Workflow
1. **Design & Architecture**: Inspect gameplay loops, frame rate budgets, physics constraints, and network topology.
2. **Setup & Initialization**: Configure libraries, canvas bindings, physics worlds, and input listeners.
3. **Implementation**: Author deterministic game loops, decoupled systems, state machines, and rendering passes.
4. **Optimization**: Audit draw calls, memory allocation, garbage collection, and frame time stability.
5. **Testing & QA**: Execute automated regression, collision checks, network latency tests, and visual snapshot reviews.

## 5. Implementation Instructions & Code Patterns

```typescript
// GameAnalytics TypeScript Wrapper
export enum ProgressionStatus {
  Start = 1,
  Complete = 2,
  Fail = 3,
}

export class GameTelemetry {
  public static trackLevelStart(level: number, gameName: string): void {
    console.log(`[Telemetry] Level Start: ${gameName} Level ${level}`);
    if (typeof window !== 'undefined' && (window as any).GameAnalytics) {
      (window as any).GameAnalytics.addProgressionEvent(
        ProgressionStatus.Start,
        gameName,
        `Level_${level}`
      );
    }
  }

  public static trackLevelComplete(level: number, gameName: string, score: number): void {
    console.log(`[Telemetry] Level Complete: ${gameName} Level ${level} Score ${score}`);
    if (typeof window !== 'undefined' && (window as any).GameAnalytics) {
      (window as any).GameAnalytics.addProgressionEvent(
        ProgressionStatus.Complete,
        gameName,
        `Level_${level}`,
        undefined,
        score
      );
    }
  }
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
- **Repository**: [https://github.com/GameAnalytics/GA-SDK](https://github.com/GameAnalytics/GA-SDK)
- **Category**: SR24-GAME-DEV Canonical Engineering Skill

## 10. License & Attribution
- **License**: MIT
- **Maintained By**: SR24Plus Autonomous Engineering Architecture
