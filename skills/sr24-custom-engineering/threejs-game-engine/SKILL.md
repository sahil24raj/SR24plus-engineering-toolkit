---
name: threejs-game-engine
description: >-
  Expert in Three.js WebGL 3D game engines — instanced mesh pipelines, custom shader materials, cascading shadow maps, skyboxes, and asset cache management.
---

# Three.js 3D WebGL Browser Game Architecture

## 1. When to Activate
Activate this skill whenever a game project or prompt requires expert in three.js webgl 3d game engines — instanced mesh pipelines, custom shader materials, cascading shadow maps, skyboxes, and asset cache management.. It is assigned to official engineering phases in the **SR24Plus Engineering Toolkit**.

## 2. When Not to Activate
- Do not activate when the task does not involve threejs-game-engine.
- Do not activate as a substitute for simple static mockups where deeper game systems engineering is unnecessary.

## 3. Core Capabilities
- InstancedMesh rendering drawing thousands of buildings, trees, and coins in single draw calls
- Cascading shadow maps and directional sunlight tuned for 60 FPS mobile browser execution
- GLTF / GLB model loading with Draco mesh decompression and KTX2 compressed textures
- Smooth third-person chase camera controllers with collision avoidance and dampening
- Particle emitter systems with custom vertex shader GPU updates for fire, smoke, and sparks

## 4. Engineering Workflow
1. **Design & Architecture**: Inspect gameplay loops, frame rate budgets, physics constraints, and network topology.
2. **Setup & Initialization**: Configure libraries, canvas bindings, physics worlds, and input listeners.
3. **Implementation**: Author deterministic game loops, decoupled systems, state machines, and rendering passes.
4. **Optimization**: Audit draw calls, memory allocation, garbage collection, and frame time stability.
5. **Testing & QA**: Execute automated regression, collision checks, network latency tests, and visual snapshot reviews.

## 5. Implementation Instructions & Code Patterns

```typescript
import * as THREE from 'three';
import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader.js';
import { DRACOLoader } from 'three/examples/jsm/loaders/DRACOLoader.js';

export class ThreeGameEngine {
  public scene = new THREE.Scene();
  public camera: THREE.PerspectiveCamera;
  public renderer: THREE.WebGLRenderer;
  private gltfLoader = new GLTFLoader();

  constructor(canvas: HTMLCanvasElement) {
    this.camera = new THREE.PerspectiveCamera(60, canvas.clientWidth / canvas.clientHeight, 0.1, 1000);
    this.renderer = new THREE.WebGLRenderer({ canvas, antialias: true, powerPreference: 'high-performance' });
    this.renderer.setSize(canvas.clientWidth, canvas.clientHeight, false);
    this.renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    this.renderer.shadowMap.enabled = true;
    this.renderer.shadowMap.type = THREE.PCFSoftShadowMap;

    const dracoLoader = new DRACOLoader();
    dracoLoader.setDecoderPath('/draco/');
    this.gltfLoader.setDRACOLoader(dracoLoader);
  }

  public loadModel(url: string): Promise<THREE.Group> {
    return new Promise((resolve, reject) => {
      this.gltfLoader.load(url, (gltf) => resolve(gltf.scene), undefined, reject);
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
- **Repository**: [https://github.com/majidmanzarpour/threejs-game-skills](https://github.com/majidmanzarpour/threejs-game-skills)
- **Category**: SR24-GAME-DEV Canonical Engineering Skill

## 10. License & Attribution
- **License**: MIT
- **Maintained By**: SR24Plus Autonomous Engineering Architecture
