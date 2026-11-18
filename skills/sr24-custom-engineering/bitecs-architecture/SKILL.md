---
name: bitecs-architecture
description: >-
  Specialist in bitECS — cache-friendly, ultra-fast Entity Component System (ECS) architecture, typed array storage, zero GC allocation, and high-entity simulation.
---

# bitECS High-Performance Data-Oriented Entity Component System

## 1. When to Activate
Activate this skill whenever a game project or prompt requires specialist in bitecs — cache-friendly, ultra-fast entity component system (ecs) architecture, typed array storage, zero gc allocation, and high-entity simulation.. It is assigned to official engineering phases in the **SR24Plus Engineering Toolkit**.

## 2. When Not to Activate
- Do not activate when the task does not involve bitecs-architecture.
- Do not activate as a substitute for simple static mockups where deeper game systems engineering is unnecessary.

## 3. Core Capabilities
- Cache-friendly memory layout using Structure of Arrays (SoA) and raw TypedArrays
- Entity creation, recycling, and bitmask querying with millions of operations per second
- Decoupled system architecture executing deterministic updates on filtered entity queries
- Zero garbage collection allocation in main game loops preventing frame time stutter
- Multi-thread friendly architecture easily serializable across Web Workers

## 4. Engineering Workflow
1. **Design & Architecture**: Inspect gameplay loops, frame rate budgets, physics constraints, and network topology.
2. **Setup & Initialization**: Configure libraries, canvas bindings, physics worlds, and input listeners.
3. **Implementation**: Author deterministic game loops, decoupled systems, state machines, and rendering passes.
4. **Optimization**: Audit draw calls, memory allocation, garbage collection, and frame time stability.
5. **Testing & QA**: Execute automated regression, collision checks, network latency tests, and visual snapshot reviews.

## 5. Implementation Instructions & Code Patterns

```typescript
import { createWorld, addEntity, addComponent, defineComponent, defineQuery, Types } from 'bitecs';

// 1. Component Definitions (Typed Array Storage)
export const Position = defineComponent({ x: Types.f32, y: Types.f32, z: Types.f32 });
export const Velocity = defineComponent({ x: Types.f32, y: Types.f32, z: Types.f32 });

export const world = createWorld();

// 2. Query Definition
export const movementQuery = defineQuery([Position, Velocity]);

// 3. Movement System (Executes in 60Hz Game Loop with ZERO allocations)
export function movementSystem(world: any, dt: number) {
  const entities = movementQuery(world);
  for (let i = 0; i < entities.length; i++) {
    const eid = entities[i];
    Position.x[eid] += Velocity.x[eid] * dt;
    Position.y[eid] += Velocity.y[eid] * dt;
    Position.z[eid] += Velocity.z[eid] * dt;
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
- **Repository**: [https://github.com/NateTheGreatt/bitECS](https://github.com/NateTheGreatt/bitECS)
- **Category**: SR24-GAME-DEV Canonical Engineering Skill

## 10. License & Attribution
- **License**: MIT
- **Maintained By**: SR24Plus Autonomous Engineering Architecture
