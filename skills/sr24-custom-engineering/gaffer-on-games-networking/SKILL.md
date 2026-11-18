---
name: gaffer-on-games-networking
description: >-
  Specialist in Glenn Fiedler’s Gaffer on Games networking models — client-side prediction, entity interpolation, snapshot interpolation, and lag compensation.
---

# Gaffer on Games Network Physics & Client Prediction Specialist

## 1. When to Activate
Activate this skill whenever a game project or prompt requires specialist in glenn fiedler’s gaffer on games networking models — client-side prediction, entity interpolation, snapshot interpolation, and lag compensation.. It is assigned to official engineering phases in the **SR24Plus Engineering Toolkit**.

## 2. When Not to Activate
- Do not activate when the task does not involve gaffer-on-games-networking.
- Do not activate as a substitute for simple static mockups where deeper game systems engineering is unnecessary.

## 3. Core Capabilities
- Client-side prediction applying local inputs instantly and buffering unacknowledged ticks
- Server authoritative reconciliation snapping and re-simulating inputs on state divergence
- Snapshot interpolation buffering remote entity states (100ms) with smooth Hermite curves
- Lag compensation rewinding server physics history during weapon hitscan raycasts
- Jitter buffer and packet loss recovery handling unstable mobile cellular connections

## 4. Engineering Workflow
1. **Design & Architecture**: Inspect gameplay loops, frame rate budgets, physics constraints, and network topology.
2. **Setup & Initialization**: Configure libraries, canvas bindings, physics worlds, and input listeners.
3. **Implementation**: Author deterministic game loops, decoupled systems, state machines, and rendering passes.
4. **Optimization**: Audit draw calls, memory allocation, garbage collection, and frame time stability.
5. **Testing & QA**: Execute automated regression, collision checks, network latency tests, and visual snapshot reviews.

## 5. Implementation Instructions & Code Patterns

```typescript
// Snapshot Interpolation Buffer (Hermite / Linear)
export interface EntitySnapshot {
  timestamp: number;
  x: number;
  y: number;
  z: number;
}

export class InterpolationBuffer {
  private snapshots: EntitySnapshot[] = [];

  public push(snapshot: EntitySnapshot) {
    this.snapshots.push(snapshot);
    if (this.snapshots.length > 20) this.snapshots.shift();
  }

  public getInterpolatedPosition(renderTime: number): { x: number; y: number; z: number } {
    if (this.snapshots.length === 0) return { x: 0, y: 0, z: 0 };
    if (this.snapshots.length === 1) return this.snapshots[0];

    // Find two surrounding snapshots
    for (let i = 0; i < this.snapshots.length - 1; i++) {
      const s0 = this.snapshots[i];
      const s1 = this.snapshots[i + 1];
      if (renderTime >= s0.timestamp && renderTime <= s1.timestamp) {
        const factor = (renderTime - s0.timestamp) / (s1.timestamp - s0.timestamp);
        return {
          x: s0.x + (s1.x - s0.x) * factor,
          y: s0.y + (s1.y - s0.y) * factor,
          z: s0.z + (s1.z - s0.z) * factor,
        };
      }
    }
    return this.snapshots[this.snapshots.length - 1];
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
- **Repository**: [https://gafferongames.com/](https://gafferongames.com/)
- **Category**: SR24-GAME-DEV Canonical Engineering Skill

## 10. License & Attribution
- **License**: MIT
- **Maintained By**: SR24Plus Autonomous Engineering Architecture
