---
name: threejs-ui-hud
description: >-
  Specialist in Three.js in-game HUDs — world-space health bars, floating damage numbers, 3D compass markers, billboard sprites, and screen-space coordinate projection.
---

# Three.js 3D In-Game HUD & Screen Projection Specialist

## 1. When to Activate
Activate this skill whenever a game project or prompt requires specialist in three.js in-game huds — world-space health bars, floating damage numbers, 3d compass markers, billboard sprites, and screen-space coordinate projection.. It is assigned to official engineering phases in the **SR24Plus Engineering Toolkit**.

## 2. When Not to Activate
- Do not activate when the task does not involve threejs-ui-hud.
- Do not activate as a substitute for simple static mockups where deeper game systems engineering is unnecessary.

## 3. Core Capabilities
- World-to-screen coordinate projection (`vector.project(camera)`) for crisp HTML/SVG HUD overlays
- Billboard text and health meters always facing active camera with zero gimbal lock
- Floating combat text with parabolic pop-up physics and alpha fade-out
- Mini-map radar projection calculating top-down relative vehicle / player bearings
- Optimized sprite rendering combining instanced UI matrices with single-draw-call batches

## 4. Engineering Workflow
1. **Design & Architecture**: Inspect gameplay loops, frame rate budgets, physics constraints, and network topology.
2. **Setup & Initialization**: Configure libraries, canvas bindings, physics worlds, and input listeners.
3. **Implementation**: Author deterministic game loops, decoupled systems, state machines, and rendering passes.
4. **Optimization**: Audit draw calls, memory allocation, garbage collection, and frame time stability.
5. **Testing & QA**: Execute automated regression, collision checks, network latency tests, and visual snapshot reviews.

## 5. Implementation Instructions & Code Patterns

```typescript
import * as THREE from 'three';

export class WorldSpaceHUD {
  private tempVec = new THREE.Vector3();

  constructor(private camera: THREE.Camera, private containerWidth: number, private containerHeight: number) {}

  public projectToScreen(worldPos: THREE.Vector3): { x: number; y: number; visible: boolean } {
    this.tempVec.copy(worldPos);
    this.tempVec.project(this.camera);

    // Behind camera check
    const isVisible = this.tempVec.z < 1.0;

    const x = (this.tempVec.x * 0.5 + 0.5) * this.containerWidth;
    const y = (-(this.tempVec.y * 0.5) + 0.5) * this.containerHeight;

    return { x, y, visible: isVisible };
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
- **Repository**: [https://github.com/emiliodominguez/threejs-skills](https://github.com/emiliodominguez/threejs-skills)
- **Category**: SR24-GAME-DEV Canonical Engineering Skill

## 10. License & Attribution
- **License**: MIT
- **Maintained By**: SR24Plus Autonomous Engineering Architecture
