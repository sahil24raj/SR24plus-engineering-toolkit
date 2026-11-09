# WORKFLOW: /sr24-unity — COMPLETE UNITY 2D/3D ENGINE SQUAD

> **Command**: `/sr24-unity [task]`  
> **Target Projects**: Indian Truck Racing, 2D/3D mobile & PC games  
> **Mission**: Build scalable, high-performance Unity games using ScriptableObjects, decoupled single-responsibility components, URP graphics, and automated build pipelines.

---

## 1. Specialist Squad Roster

- **Unity Architect**: `agency-game-development-unity-unity-architect`
- **Editor Tooling**: `agency-game-development-unity-unity-editor-tool-developer`
- **Shader & VFX Artist**: `agency-game-development-unity-unity-shader-graph-artist`
- **Audio Engineer**: `agency-game-development-game-audio-engineer`
- **Multiplayer Engineer**: `agency-game-development-unity-unity-multiplayer-engineer` (if networked)
- **Profiler & Performance**: `performance-optimization` + `unity-performance-profiler`
- **Build Pipeline**: `unity-build-pipeline-engineer`

---

## 2. 6-Phase Unity Production Lifecycle

1. **Phase 1: Project Architecture & ScriptableObjects**:
   - Decoupled event-driven architecture using ScriptableObject game events.
   - Modular GameManager, AudioManager, and SceneLoader singletons.
2. **Phase 2: Universal Render Pipeline (URP) Setup**:
   - Volume framework configuration (Tonemapping, Color Adjustments, Bloom, Vignette).
   - Render Graph feature validation and GPU instancing enablement.
3. **Phase 3: Gameplay Systems & Input System**:
   - New Unity Input System (`UnityEngine.InputSystem`) actions map for gamepad, keyboard, and touch.
4. **Phase 4: Audio Routing & Mixers**:
   - Master, Music, SFX, and Voice mixer buses with snapshot transitions and ducking.
5. **Phase 5: Performance Profiling & Optimization**:
   - Target 60 FPS mobile; keep draw calls $< 150$ via static/dynamic batching and occlusion culling.
   - Zero GC allocations in `Update()` loops.
6. **Phase 6: Automated Multi-Platform Build**:
   - Automated builds for Android APK/AAB and Windows Standalone via Unity CLI scripts.
