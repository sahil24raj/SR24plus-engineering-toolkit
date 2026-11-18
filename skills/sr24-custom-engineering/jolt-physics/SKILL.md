---
name: jolt-physics
description: >-
  Specialist in Jolt Physics — multi-core 3D physics, raycast vehicle controllers, tire friction, suspension damping, ragdolls, and large-world collision systems.
---

# Jolt Physics Multi-Threaded 3D Rigid Body & Vehicle Dynamics

## 1. When to Activate
Activate this skill whenever a game project or prompt requires specialist in jolt physics — multi-core 3d physics, raycast vehicle controllers, tire friction, suspension damping, ragdolls, and large-world collision systems.. It is assigned to official engineering phases in the **SR24Plus Engineering Toolkit**.

## 2. When Not to Activate
- Do not activate when the task does not involve jolt-physics.
- Do not activate as a substitute for simple static mockups where deeper game systems engineering is unnecessary.

## 3. Core Capabilities
- Multi-threaded rigid body physics simulation scaling across all CPU hardware cores
- Raycast vehicle suspension calculation with Ackermann steering and spring-damper dynamics
- Pacejka tire friction formulation calculating longitudinal slip and lateral drift forces
- Continuous Collision Detection (CCD) preventing high-speed vehicles tunneling through walls
- Ragdoll physics with angular joint constraints and dynamic skeleton blending

## 4. Engineering Workflow
1. **Design & Architecture**: Inspect gameplay loops, frame rate budgets, physics constraints, and network topology.
2. **Setup & Initialization**: Configure libraries, canvas bindings, physics worlds, and input listeners.
3. **Implementation**: Author deterministic game loops, decoupled systems, state machines, and rendering passes.
4. **Optimization**: Audit draw calls, memory allocation, garbage collection, and frame time stability.
5. **Testing & QA**: Execute automated regression, collision checks, network latency tests, and visual snapshot reviews.

## 5. Implementation Instructions & Code Patterns

```typescript
// Conceptual Jolt Raycast Vehicle Suspension Equations
export class VehicleSuspension {
  public static calculateSuspensionForce(
    compressionLength: number,
    velocityAlongNormal: number,
    springK = 35000, // Spring stiffness (N/m)
    dampingC = 4500  // Damper coefficient (N*s/m)
  ): number {
    const springForce = springK * compressionLength;
    const damperForce = dampingC * velocityAlongNormal;
    return Math.max(0, springForce + damperForce);
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
- **Repository**: [https://github.com/jrouwe/JoltPhysics](https://github.com/jrouwe/JoltPhysics)
- **Category**: SR24-GAME-DEV Canonical Engineering Skill

## 10. License & Attribution
- **License**: MIT
- **Maintained By**: SR24Plus Autonomous Engineering Architecture
