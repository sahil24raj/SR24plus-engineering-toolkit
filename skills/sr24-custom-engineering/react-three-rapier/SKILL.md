---
name: react-three-rapier
description: >-
  Specialist in @react-three/rapier — declarative 3D physics inside React Three Fiber, Physics provider, RigidBody components, sensors, and collision hooks.
---

# React Three Rapier Declarative Physics Integration

## 1. When to Activate
Activate this skill whenever a game project or prompt requires specialist in @react-three/rapier — declarative 3d physics inside react three fiber, physics provider, rigidbody components, sensors, and collision hooks.. It is assigned to official engineering phases in the **SR24Plus Engineering Toolkit**.

## 2. When Not to Activate
- Do not activate when the task does not involve react-three-rapier.
- Do not activate as a substitute for simple static mockups where deeper game systems engineering is unnecessary.

## 3. Core Capabilities
- Declarative physics provider wrapping R3F scenes with gravity and debug wireframe toggles
- RigidBody component configuration (`type="dynamic"|"fixed"|"kinematicPosition"`), restitution, and friction
- Sensor colliders detecting trigger volume entry and exit without physical momentum transfer
- Collision and intersection callbacks (`onCollisionEnter`, `onIntersectionEnter`) with contact points
- InstancedRigidBodies optimization simulating hundreds of physics objects simultaneously

## 4. Engineering Workflow
1. **Design & Architecture**: Inspect gameplay loops, frame rate budgets, physics constraints, and network topology.
2. **Setup & Initialization**: Configure libraries, canvas bindings, physics worlds, and input listeners.
3. **Implementation**: Author deterministic game loops, decoupled systems, state machines, and rendering passes.
4. **Optimization**: Audit draw calls, memory allocation, garbage collection, and frame time stability.
5. **Testing & QA**: Execute automated regression, collision checks, network latency tests, and visual snapshot reviews.

## 5. Implementation Instructions & Code Patterns

```typescript
import React, { useRef } from 'react';
import { Physics, RigidBody, CuboidCollider, RapierRigidBody } from '@react-three/rapier';

export function PhysicsGameScene() {
  const cubeRef = useRef<RapierRigidBody>(null);

  const jump = () => {
    cubeRef.current?.applyImpulse({ x: 0, y: 15, z: 0 }, true);
  };

  return (
    <Physics gravity={[0, -9.81, 0]}>
      {/* Ground */}
      <RigidBody type="fixed">
        <CuboidCollider args={[20, 0.5, 20]} position={[0, -0.5, 0]} />
      </RigidBody>

      {/* Dynamic Player Cube */}
      <RigidBody ref={cubeRef} position={[0, 5, 0]} colliders="cuboid" onClick={jump}>
        <mesh castShadow>
          <boxGeometry args={[1, 1, 1]} />
          <meshStandardMaterial color="#FF9F1C" />
        </mesh>
      </RigidBody>
    </Physics>
  );
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
- **Repository**: [https://github.com/pmndrs/react-three-rapier](https://github.com/pmndrs/react-three-rapier)
- **Category**: SR24-GAME-DEV Canonical Engineering Skill

## 10. License & Attribution
- **License**: MIT
- **Maintained By**: SR24Plus Autonomous Engineering Architecture
