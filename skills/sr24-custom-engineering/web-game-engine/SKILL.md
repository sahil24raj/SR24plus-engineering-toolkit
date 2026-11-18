---
name: web-game-engine
description: >-
  Specialist in HTML5 Canvas 2D/WebGL game engine architecture — deterministic fixed-timestep accumulator loops, sub-frame interpolation, virtual touch controls, and audio sync.
---

# HTML5 Canvas 60 FPS Deterministic Game Loop Engine

## 1. When to Activate
Activate this skill whenever a game project or prompt requires specialist in html5 canvas 2d/webgl game engine architecture — deterministic fixed-timestep accumulator loops, sub-frame interpolation, virtual touch controls, and audio sync.. It is assigned to official engineering phases in the **SR24Plus Engineering Toolkit**.

## 2. When Not to Activate
- Do not activate when the task does not involve web-game-engine.
- Do not activate as a substitute for simple static mockups where deeper game systems engineering is unnecessary.

## 3. Core Capabilities
- Fixed-timestep accumulator loop (`dt = 1/60s`) guaranteeing identical physics across 60Hz, 120Hz, and 144Hz displays
- Sub-frame alpha interpolation rendering smooth visuals without physics jitter
- Responsive high-DPI canvas scaling with devicePixelRatio crisp text and sharp lines
- Multi-touch virtual joysticks and arcade buttons with responsive touch hit testing
- Automatic pause on window blur and tab visibility change preventing physics explosions

## 4. Engineering Workflow
1. **Design & Architecture**: Inspect gameplay loops, frame rate budgets, physics constraints, and network topology.
2. **Setup & Initialization**: Configure libraries, canvas bindings, physics worlds, and input listeners.
3. **Implementation**: Author deterministic game loops, decoupled systems, state machines, and rendering passes.
4. **Optimization**: Audit draw calls, memory allocation, garbage collection, and frame time stability.
5. **Testing & QA**: Execute automated regression, collision checks, network latency tests, and visual snapshot reviews.

## 5. Implementation Instructions & Code Patterns

```typescript
export class DeterministicGameLoop {
  private lastTime = 0;
  private accumulator = 0;
  private readonly fixedStep = 1 / 60; // 60Hz physics
  private isRunning = false;
  private animFrameId = 0;

  constructor(
    private updatePhysics: (dt: number) => void,
    private renderScene: (alpha: number) => void
  ) {}

  public start(): void {
    if (this.isRunning) return;
    this.isRunning = true;
    this.lastTime = performance.now();
    this.accumulator = 0;
    this.animFrameId = requestAnimationFrame(this.tick);
  }

  public stop(): void {
    this.isRunning = false;
    cancelAnimationFrame(this.animFrameId);
  }

  private tick = (currentTime: number): void => {
    if (!this.isRunning) return;

    let frameTime = (currentTime - this.lastTime) / 1000;
    if (frameTime > 0.25) frameTime = 0.25; // Spiral of death clamp
    this.lastTime = currentTime;

    this.accumulator += frameTime;

    while (this.accumulator >= this.fixedStep) {
      this.updatePhysics(this.fixedStep);
      this.accumulator -= this.fixedStep;
    }

    const alpha = this.accumulator / this.fixedStep;
    this.renderScene(alpha);

    this.animFrameId = requestAnimationFrame(this.tick);
  };
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
- **Repository**: [https://github.com/agioracle/web-game-development-skills](https://github.com/agioracle/web-game-development-skills)
- **Category**: SR24-GAME-DEV Canonical Engineering Skill

## 10. License & Attribution
- **License**: MIT
- **Maintained By**: SR24Plus Autonomous Engineering Architecture
