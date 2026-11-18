---
name: react-three-fiber
description: >-
  Specialist in React Three Fiber (R3F) and @react-three/drei — declarative 3D component trees, useFrame game loop hooks, Drei helpers, and postprocessing.
---

# React Three Fiber (R3F) Declarative 3D Game Scene Architecture

## 1. When to Activate
Activate this skill whenever a game project or prompt requires specialist in react three fiber (r3f) and @react-three/drei — declarative 3d component trees, useframe game loop hooks, drei helpers, and postprocessing.. It is assigned to official engineering phases in the **SR24Plus Engineering Toolkit**.

## 2. When Not to Activate
- Do not activate when the task does not involve react-three-fiber.
- Do not activate as a substitute for simple static mockups where deeper game systems engineering is unnecessary.

## 3. Core Capabilities
- Declarative React scene composition decoupling camera, lighting, environment, and actor meshes
- Zero-garbage-collection `useFrame` game loop orchestration mutating references directly
- Drei ecosystem integration (useGLTF, OrbitControls, Sky, Environment, Html, Float)
- Postprocessing pipeline integration (Bloom, Vignette, Depth of Field, Tone Mapping)
- Suspense-based 3D asset preloading with smooth fallback progress bars

## 4. Engineering Workflow
1. **Design & Architecture**: Inspect gameplay loops, frame rate budgets, physics constraints, and network topology.
2. **Setup & Initialization**: Configure libraries, canvas bindings, physics worlds, and input listeners.
3. **Implementation**: Author deterministic game loops, decoupled systems, state machines, and rendering passes.
4. **Optimization**: Audit draw calls, memory allocation, garbage collection, and frame time stability.
5. **Testing & QA**: Execute automated regression, collision checks, network latency tests, and visual snapshot reviews.

## 5. Implementation Instructions & Code Patterns

```typescript
import React, { useRef } from 'react';
import { Canvas, useFrame } from '@react-three/fiber';
import { useGLTF, Environment } from '@react-three/drei';
import * as THREE from 'three';

function PlayerVehicle({ position }: { position: [number, number, number] }) {
  const vehicleRef = useRef<THREE.Group>(null);
  const { scene } = useGLTF('/models/auto-rickshaw.glb');

  useFrame((state, delta) => {
    if (vehicleRef.current) {
      // Direct ref mutation avoiding React re-renders
      vehicleRef.current.position.z += 12 * delta;
    }
  });

  return <primitive ref={vehicleRef} object={scene} position={position} castShadow />;
}

export function Game3DCanvas() {
  return (
    <Canvas shadows camera={{ position: [0, 5, -10], fov: 60 }}>
      <ambientLight intensity={0.5} />
      <directionalLight position={[10, 20, 15]} intensity={1.5} castShadow />
      <PlayerVehicle position={[0, 0, 0]} />
      <Environment preset="city" />
    </Canvas>
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
- **Repository**: [https://github.com/pmndrs/react-three-fiber](https://github.com/pmndrs/react-three-fiber)
- **Category**: SR24-GAME-DEV Canonical Engineering Skill

## 10. License & Attribution
- **License**: MIT
- **Maintained By**: SR24Plus Autonomous Engineering Architecture
