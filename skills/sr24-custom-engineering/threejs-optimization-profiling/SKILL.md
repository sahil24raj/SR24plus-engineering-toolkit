---
name: threejs-optimization-profiling
description: >-
  Specialist in WebGL performance profiling — Spector.js draw-call auditing, Stats.js frame monitoring, texture memory budgeting, and GPU bottleneck remediation.
---

# Three.js WebGL Performance Profiling & Optimization Specialist

## 1. When to Activate
Activate this skill whenever a game project or prompt requires specialist in webgl performance profiling — spector.js draw-call auditing, stats.js frame monitoring, texture memory budgeting, and gpu bottleneck remediation.. It is assigned to official engineering phases in the **SR24Plus Engineering Toolkit**.

## 2. When Not to Activate
- Do not activate when the task does not involve threejs-optimization-profiling.
- Do not activate as a substitute for simple static mockups where deeper game systems engineering is unnecessary.

## 3. Core Capabilities
- Draw-call auditing identifying redundant state changes, unmerged geometries, and texture thrashing
- Real-time FPS, frame time (MS), and memory (MB) monitoring overlays via Stats.js
- Frustum culling and occlusion culling verification ensuring off-screen actors are never rendered
- Texture memory budgeting ensuring total WebGL VRAM consumption stays below 200MB on mobile
- Shader compilation pre-warming (`renderer.compile(scene, camera)`) eliminating in-game hitching

## 4. Engineering Workflow
1. **Design & Architecture**: Inspect gameplay loops, frame rate budgets, physics constraints, and network topology.
2. **Setup & Initialization**: Configure libraries, canvas bindings, physics worlds, and input listeners.
3. **Implementation**: Author deterministic game loops, decoupled systems, state machines, and rendering passes.
4. **Optimization**: Audit draw calls, memory allocation, garbage collection, and frame time stability.
5. **Testing & QA**: Execute automated regression, collision checks, network latency tests, and visual snapshot reviews.

## 5. Implementation Instructions & Code Patterns

```typescript
import Stats from 'stats.js';
import * as THREE from 'three';

export class WebGLPerformanceProfiler {
  private stats = new Stats();

  constructor(private renderer: THREE.WebGLRenderer) {
    this.stats.showPanel(0); // 0: fps, 1: ms, 2: mb
    document.body.appendChild(this.stats.dom);
  }

  public beginFrame(): void {
    this.stats.begin();
  }

  public endFrame(): void {
    this.stats.end();
  }

  public logRenderMetrics(): void {
    const info = this.renderer.info;
    console.log('[WebGL Render Info]', {
      drawCalls: info.render.calls,
      triangles: info.render.triangles,
      geometries: info.memory.geometries,
      textures: info.memory.textures,
    });
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
- **Repository**: [https://github.com/mrdoob/stats.js](https://github.com/mrdoob/stats.js)
- **Category**: SR24-GAME-DEV Canonical Engineering Skill

## 10. License & Attribution
- **License**: MIT
- **Maintained By**: SR24Plus Autonomous Engineering Architecture
