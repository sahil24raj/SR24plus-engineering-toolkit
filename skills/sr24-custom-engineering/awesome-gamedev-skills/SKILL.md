---
name: awesome-gamedev-skills
description: >-
  Specialist in formal Game Design Document (GDD) authoring, mathematical mechanics balancing, economy modeling, progression curves, and retention loops.
---

# Game Design Document (GDD) & Mechanics Balancing Specialist

## 1. When to Activate
Activate this skill whenever a game project or prompt requires specialist in formal game design document (gdd) authoring, mathematical mechanics balancing, economy modeling, progression curves, and retention loops.. It is assigned to official engineering phases in the **SR24Plus Engineering Toolkit**.

## 2. When Not to Activate
- Do not activate when the task does not involve awesome-gamedev-skills.
- Do not activate as a substitute for simple static mockups where deeper game systems engineering is unnecessary.

## 3. Core Capabilities
- Comprehensive GDD authoring (Core Loop, Meta Loop, Economy Sinks & Sources, Control Scheme)
- Mathematical weapon, vehicle, and character attribute balancing curves
- Player retention pacing (D1, D7, D30 retention loops, daily streaks, reward chests)
- Level pacing curves balancing tension, release, encounter density, and checkpoint frequency
- Monetization system design maintaining competitive integrity (battle passes, cosmetics, zero pay-to-win)

## 4. Engineering Workflow
1. **Design & Architecture**: Inspect gameplay loops, frame rate budgets, physics constraints, and network topology.
2. **Setup & Initialization**: Configure libraries, canvas bindings, physics worlds, and input listeners.
3. **Implementation**: Author deterministic game loops, decoupled systems, state machines, and rendering passes.
4. **Optimization**: Audit draw calls, memory allocation, garbage collection, and frame time stability.
5. **Testing & QA**: Execute automated regression, collision checks, network latency tests, and visual snapshot reviews.

## 5. Implementation Instructions & Code Patterns

```typescript
// Progression Curve Mathematical Model
export class ProgressionCurve {
  // Experience required for level L: XP = Base * (L ^ Exponent)
  public static calculateXPForLevel(level: number, baseXP = 100, exponent = 1.5): number {
    if (level <= 1) return 0;
    return Math.floor(baseXP * Math.pow(level - 1, exponent));
  }

  // Soft currency reward balancing with diminishing returns
  public static calculateMatchReward(score: number, isWin: boolean, multiplier = 1.0): number {
    const baseReward = isWin ? 250 : 100;
    const scoreBonus = Math.min(500, Math.floor(score * 0.1));
    return Math.floor((baseReward + scoreBonus) * multiplier);
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
- **Repository**: [https://github.com/gamedev-skills/awesome-gamedev-agent-skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills)
- **Category**: SR24-GAME-DEV Canonical Engineering Skill

## 10. License & Attribution
- **License**: MIT
- **Maintained By**: SR24Plus Autonomous Engineering Architecture
