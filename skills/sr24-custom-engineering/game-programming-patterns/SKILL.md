---
name: game-programming-patterns
description: >-
  Expert in Bob Nystrom’s Game Programming Patterns — State machines, Command queues, Flyweight, Object Pooling, Game Loop, Spatial Partitioning, and Double Buffering.
---

# Game Programming Patterns Architecture Specialist

## 1. When to Activate
Activate this skill whenever a game project or prompt requires expert in bob nystrom’s game programming patterns — state machines, command queues, flyweight, object pooling, game loop, spatial partitioning, and double buffering.. It is assigned to official engineering phases in the **SR24Plus Engineering Toolkit**.

## 2. When Not to Activate
- Do not activate when the task does not involve game-programming-patterns.
- Do not activate as a substitute for simple static mockups where deeper game systems engineering is unnecessary.

## 3. Core Capabilities
- Hierarchical state machine (FSM/HFSM) design for character states (Idle, Run, Jump, Attack, Stun)
- Command pattern implementation for rebindable inputs, replay systems, and undo/redo buffers
- Zero-garbage object pooling for projectiles, damage numbers, and particle effects
- Spatial partitioning (Grid / Quadtree / BVH) optimizing collision queries from O(N^2) to O(N log N)
- Flyweight pattern minimizing memory footprint for terrain tiles and recurring world instances

## 4. Engineering Workflow
1. **Design & Architecture**: Inspect gameplay loops, frame rate budgets, physics constraints, and network topology.
2. **Setup & Initialization**: Configure libraries, canvas bindings, physics worlds, and input listeners.
3. **Implementation**: Author deterministic game loops, decoupled systems, state machines, and rendering passes.
4. **Optimization**: Audit draw calls, memory allocation, garbage collection, and frame time stability.
5. **Testing & QA**: Execute automated regression, collision checks, network latency tests, and visual snapshot reviews.

## 5. Implementation Instructions & Code Patterns

```typescript
// Object Pool Pattern in TypeScript
export class ObjectPool<T> {
  private available: T[] = [];
  private inUse: Set<T> = new Set();

  constructor(
    private factory: () => T,
    private reset: (item: T) => void,
    initialSize: number = 50
  ) {
    for (let i = 0; i < initialSize; i++) {
      this.available.push(this.factory());
    }
  }

  public acquire(): T {
    const item = this.available.pop() ?? this.factory();
    this.inUse.add(item);
    return item;
  }

  public release(item: T): void {
    if (this.inUse.delete(item)) {
      this.reset(item);
      this.available.push(item);
    }
  }

  public releaseAll(): void {
    for (const item of this.inUse) {
      this.reset(item);
      this.available.push(item);
    }
    this.inUse.clear();
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
- **Repository**: [https://github.com/munificent/game-programming-patterns](https://github.com/munificent/game-programming-patterns)
- **Category**: SR24-GAME-DEV Canonical Engineering Skill

## 10. License & Attribution
- **License**: MIT
- **Maintained By**: SR24Plus Autonomous Engineering Architecture
