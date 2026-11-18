---
name: rapier-physics
description: >-
  Specialist in Dimforge Rapier — ultra-fast Rust/WebAssembly 2D & 3D physics, rigid bodies, colliders, character controllers, raycasts, and contact events.
---

# Rapier 2D & 3D WebAssembly Physics Engine Specialist

## 1. When to Activate
Activate this skill whenever a game project or prompt requires specialist in dimforge rapier — ultra-fast rust/webassembly 2d & 3d physics, rigid bodies, colliders, character controllers, raycasts, and contact events.. It is assigned to official engineering phases in the **SR24Plus Engineering Toolkit**.

## 2. When Not to Activate
- Do not activate when the task does not involve rapier-physics.
- Do not activate as a substitute for simple static mockups where deeper game systems engineering is unnecessary.

## 3. Core Capabilities
- Wasm-powered 3D rigid body dynamics with deterministic simulation and minimal CPU overhead
- Kinematic character controllers with automatic slope sliding, stepping, and obstacle snapping
- Compound colliders (Trimesh, Convex Hull, Capsule, Box, Ball) with custom collision groups
- High-velocity raycasting and shapecasting for hitscan weapons and ground detection
- Joint simulation (Revolute, Prismatic, Spherical, Fixed) for vehicle suspensions and ragdolls

## 4. Engineering Workflow
1. **Design & Architecture**: Inspect gameplay loops, frame rate budgets, physics constraints, and network topology.
2. **Setup & Initialization**: Configure libraries, canvas bindings, physics worlds, and input listeners.
3. **Implementation**: Author deterministic game loops, decoupled systems, state machines, and rendering passes.
4. **Optimization**: Audit draw calls, memory allocation, garbage collection, and frame time stability.
5. **Testing & QA**: Execute automated regression, collision checks, network latency tests, and visual snapshot reviews.

## 5. Implementation Instructions & Code Patterns

```typescript
import RAPIER from '@dimforge/rapier3d-compat';

export async function initPhysicsWorld() {
  await RAPIER.init();

  const gravity = new RAPIER.Vector3(0.0, -9.81, 0.0);
  const world = new RAPIER.World(gravity);

  // 1. Static Ground Plane
  const groundBodyDesc = RAPIER.RigidBodyDesc.fixed().setTranslation(0, 0, 0);
  const groundBody = world.createRigidBody(groundBodyDesc);
  const groundColliderDesc = RAPIER.ColliderDesc.cuboid(50.0, 0.5, 50.0);
  world.createCollider(groundColliderDesc, groundBody);

  // 2. Dynamic Player Body
  const playerBodyDesc = RAPIER.RigidBodyDesc.dynamic().setTranslation(0, 3, 0);
  const playerBody = world.createRigidBody(playerBodyDesc);
  const playerColliderDesc = RAPIER.ColliderDesc.capsule(0.8, 0.4);
  world.createCollider(playerColliderDesc, playerBody);

  return { world, playerBody };
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
- **Repository**: [https://github.com/dimforge/rapier](https://github.com/dimforge/rapier)
- **Category**: SR24-GAME-DEV Canonical Engineering Skill

## 10. License & Attribution
- **License**: Apache-2.0
- **Maintained By**: SR24Plus Autonomous Engineering Architecture
