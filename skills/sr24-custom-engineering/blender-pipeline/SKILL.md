---
name: blender-pipeline
description: >-
  Specialist in Blender headless Python automation — automated mesh decimation, armature/bone hierarchy validation, material baking, and batch GLB export.
---

# Blender Headless Python Automation & Export Pipeline Specialist

## 1. When to Activate
Activate this skill whenever a game project or prompt requires specialist in blender headless python automation — automated mesh decimation, armature/bone hierarchy validation, material baking, and batch glb export.. It is assigned to official engineering phases in the **SR24Plus Engineering Toolkit**.

## 2. When Not to Activate
- Do not activate when the task does not involve blender-pipeline.
- Do not activate as a substitute for simple static mockups where deeper game systems engineering is unnecessary.

## 3. Core Capabilities
- Headless CLI execution (`blender --background --python export_assets.py`) for automated DCC pipelines
- Automated quad decimation reducing high-poly sculpts to game-ready low-poly meshes
- Armature and bone hierarchy validation ensuring compatibility with Three.js and Unity engines
- Material and PBR texture baking (Diffuse, Normal, Roughness, Metalness) into unified UV channels
- Batch conversion of FBX and OBJ assets into optimized GLB files with embedded animations

## 4. Engineering Workflow
1. **Design & Architecture**: Inspect gameplay loops, frame rate budgets, physics constraints, and network topology.
2. **Setup & Initialization**: Configure libraries, canvas bindings, physics worlds, and input listeners.
3. **Implementation**: Author deterministic game loops, decoupled systems, state machines, and rendering passes.
4. **Optimization**: Audit draw calls, memory allocation, garbage collection, and frame time stability.
5. **Testing & QA**: Execute automated regression, collision checks, network latency tests, and visual snapshot reviews.

## 5. Implementation Instructions & Code Patterns

```typescript
# headless_blender_export.py
import bpy
import sys

def optimize_and_export_glb(input_file, output_file, decimate_ratio=0.5):
    # Clear existing scene
    bpy.ops.wm.read_factory_settings(use_empty=True)

    # Import asset
    bpy.ops.import_scene.fbx(filepath=input_file)

    for obj in bpy.context.scene.objects:
        if obj.type == 'MESH':
            # Apply decimate modifier
            mod = obj.modifiers.new(name="Decimate", type='DECIMATE')
            mod.ratio = decimate_ratio
            bpy.context.view_layer.objects.active = obj
            bpy.ops.object.modifier_apply(modifier="Decimate")

    # Export to GLB
    bpy.ops.export_scene.gltf(
        filepath=output_file,
        export_format='GLB',
        export_apply=True,
        export_animations=True
    )
    print(f"Exported clean GLB to {output_file}")

if __name__ == "__main__":
    optimize_and_export_glb(sys.argv[-2], sys.argv[-1])
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
- **Repository**: [https://github.com/blender/blender](https://github.com/blender/blender)
- **Category**: SR24-GAME-DEV Canonical Engineering Skill

## 10. License & Attribution
- **License**: GPL-2.0
- **Maintained By**: SR24Plus Autonomous Engineering Architecture
