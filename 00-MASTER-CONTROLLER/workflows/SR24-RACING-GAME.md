# WORKFLOW: /sr24-racing-game — VEHICLE PHYSICS & RACING GAME SQUAD

> **Command**: `/sr24-racing-game [task]`  
> **Target Projects**: Indian Truck Racing, vehicle simulators, circuit racers  
> **Mission**: Build authentic vehicle handling models, multi-axle heavy truck dynamics, procedural spline tracks, banking curves, and atmospheric racing soundscapes.

---

## 1. Specialist Squad Roster

- **Truck & Heavy Physics**: `truck-physics-engineer`
- **Car Controller Lead**: `realistic-car-controller-engineer`
- **Track & Circuit Designer**: `racing-track-design-engineer`
- **Audio Engineer**: `agency-game-development-game-audio-engineer`
- **3D Assets & Blender**: `blender-game-asset-engineer`
- **Shader & VFX Artist**: `agency-game-development-unity-unity-shader-graph-artist`
- **Performance Profiler**: `performance-optimization`

---

## 2. 6-Phase Racing Game Implementation Pipeline

1. **Phase 1: Rigidbody & Center of Mass Configuration**:
   - Set accurate mass (8,000–16,000 kg for commercial trucks).
   - Configure low center-of-mass helper to balance authentic body roll against rollover stability.
2. **Phase 2: Multi-Axle WheelCollider Setup**:
   - Front steerable axle with Ackermann geometry compensation.
   - Dual-wheel rear drive axles with differential torque split and anti-roll bars.
3. **Phase 3: Track Layout & Camber Curves**:
   - Spline-based road meshes with positive banking ($5^\circ-12^\circ$) on mountain hairpin curves.
   - Surface friction zones (Dry asphalt, wet monsoon asphalt, muddy detours).
4. **Phase 4: Checkpoints & Race Telemetry**:
   - Ordered trigger checkpoints, lap counter, wrong-way detection, and split times.
5. **Phase 5: Audio & Tactile Polish**:
   - RPM-linked diesel audio pitch curves, air brake release hiss, pressure musical horns.
   - Dynamic tire skid marks and tire smoke particle bursts on drift/wheel spin.
6. **Phase 6: 60 FPS Profiling**:
   - LOD groups on truck meshes and roadside vegetation; verify stable 60 FPS on target hardware.

