# PROJECT WORKFLOW PROFILE: INDIAN TRUCK RACING
## Heavy Vehicle 3D Racing Game in Unity

> **Project Identity**: INDIAN TRUCK RACING  
> **Domain**: 3D Vehicle Physics, Indian Highway & Ghat Racing Simulation  
> **Primary Command**: `/sr24-racing-game truck-racing` or `/sr24-unity truck-racing`

---

## 1. Specialist Squad Roster

| Role | Assigned Skill(s) | Primary Mission |
|---|---|---|
| **Unity Lead Architect** | `agency-game-development-unity-unity-architect` | Modular ScriptableObject architecture, decoupled managers |
| **Truck Physics Specialist** | `truck-physics-engineer` | 16-wheeler WheelColliders, high CoM body roll, air brakes |
| **Vehicle Controller** | `realistic-car-controller-engineer` | Ackermann steering geometry, downforce, slip angles |
| **Circuit Design Engineer** | `racing-track-design-engineer` | Spline-based ghat roads, banking hairpins, friction zones |
| **Blender 3D Asset Lead** | `blender-game-asset-engineer` | Tata/Ashok Leyland truck models, custom Indian truck art |
| **Audio Engineer** | `agency-game-development-game-audio-engineer` | Diesel engine RPM pitch curves, pneumatic air brake hiss, multi-tone pressure horns |
| **VFX Technical Artist** | `agency-game-development-unity-unity-shader-graph-artist` | Exhaust black smoke particles, tire skid marks, monsoon rain shaders |
| **Performance Profiler** | `performance-optimization` + `unity-performance-profiler` | 60 FPS mobile target, LOD groups, GPU instancing |
| **Build & Release Engineer** | `unity-build-pipeline-engineer` | Android APK/AAB builds, PC standalone packaging |

---

## 2. Indian Truck Physics Specifications

- **Vehicle Types**: 6-wheeler tippers, 10-wheeler cargo trucks, 16-wheeler heavy freight haulers.
- **Mass Range**: 7,500 kg (Empty) to 24,000 kg (Full Load).
- **Steering**: Dual-front WheelColliders with Ackermann compensation ($32^\circ$ max lock).
- **Drive System**: 6x4 dual rear axle drive with dynamic torque distribution.
- **Environment**: Mumbai-Pune Expressway, Rohtang Pass Ghats, NH44 National Highway.

---

## 3. Mandatory Quality Gates

1. **Anti-Roll Bar Rigidity**: High center-of-mass truck must not flip prematurely during standard highway lane changes.
2. **Terrain Friction Variance**: Track surfaces dynamically alter WheelCollider forward/sideways stiffness:
   - Dry Asphalt: `Stiffness = 1.0`
   - Wet Monsoon Ghats: `Stiffness = 0.65` (Prone to jackknifing on hard braking)
   - Unpaved Mud Detour: `Stiffness = 0.45`
3. **Audio Experience**: Interactive horn system featuring iconic Indian pressure musical horn melodies.
4. **Draw Call Budget**: Maximum 120 draw calls per frame on mobile viewports.

