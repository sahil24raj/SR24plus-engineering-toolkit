---
name: gltf-transform-pipeline
description: >-
  Specialist in glTF Transform CLI & SDK — GLB/glTF meshopt compression, Draco geometry encoding, KTX2/Basis Universal texture transcoding, and LOD pruning.
---

# glTF Transform 3D Asset Compression & Optimization Specialist

## 1. When to Activate
Activate this skill whenever a game project or prompt requires specialist in gltf transform cli & sdk — glb/gltf meshopt compression, draco geometry encoding, ktx2/basis universal texture transcoding, and lod pruning.. It is assigned to official engineering phases in the **SR24Plus Engineering Toolkit**.

## 2. When Not to Activate
- Do not activate when the task does not involve gltf-transform-pipeline.
- Do not activate as a substitute for simple static mockups where deeper game systems engineering is unnecessary.

## 3. Core Capabilities
- Shrinking 3D models (GLB) by 70–85% using Meshopt and Draco geometric quantization
- Automated texture transcoding to KTX2 / Basis Universal reducing GPU VRAM consumption by 4x
- Deduplication of accessor buffers and materials eliminating redundant GPU uploads
- Automated level of detail (LOD) generation reducing polygon count for distant assets
- Pruning unused vertex attributes (e.g. vertex colors, second UV channels) to accelerate rendering

## 4. Engineering Workflow
1. **Design & Architecture**: Inspect gameplay loops, frame rate budgets, physics constraints, and network topology.
2. **Setup & Initialization**: Configure libraries, canvas bindings, physics worlds, and input listeners.
3. **Implementation**: Author deterministic game loops, decoupled systems, state machines, and rendering passes.
4. **Optimization**: Audit draw calls, memory allocation, garbage collection, and frame time stability.
5. **Testing & QA**: Execute automated regression, collision checks, network latency tests, and visual snapshot reviews.

## 5. Implementation Instructions & Code Patterns

```typescript
// glTF Transform Node.js Pipeline Script
import { NodeIO } from '@gltf-transform/core';
import { dedup, prune, quantize, reorder } from '@gltf-transform/functions';
import { ALL_EXTENSIONS } from '@gltf-transform/extensions';
import meshopt from 'meshoptimizer';

export async function optimize3DModel(inputPath: string, outputPath: string) {
  const io = new NodeIO().registerExtensions(ALL_EXTENSIONS);
  const document = await io.read(inputPath);

  await document.transform(
    dedup(),
    prune(),
    reorder({ encoder: meshopt }),
    quantize()
  );

  await io.write(outputPath, document);
  console.log(`Optimized 3D asset saved to ${outputPath}`);
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
- **Repository**: [https://github.com/donmccurdy/glTF-Transform](https://github.com/donmccurdy/glTF-Transform)
- **Category**: SR24-GAME-DEV Canonical Engineering Skill

## 10. License & Attribution
- **License**: MIT
- **Maintained By**: SR24Plus Autonomous Engineering Architecture
