# WORKFLOW: /sr24-game-dev — COMPLETE GAME DEVELOPMENT SQUAD

> **Command**: `/sr24-game-dev [task]`  
> **Natural Language Trigger**: `"Build game"`, `"Develop game"`, `"Create Unity/Unreal/Godot project"`  
> **Mission**: Coordinate a specialized 10-phase game development squad to engineer polished, engaging, optimized, and cross-platform games from concept to release.

---

## SQUAD ROSTER & ARCHITECTURE

```
                      ┌───────────────────────────────────────┐
                      │          GAME DIRECTOR / GDD          │
                      │ agency-game-development-game-designer │
                      └──────────────────┬────────────────────┘
                                         │
         ┌───────────────────────────────┼───────────────────────────────┐
         ▼                               ▼                               ▼
┌──────────────────┐           ┌──────────────────┐           ┌──────────────────┐
│ ART & NARRATIVE  │           │ ENGINE & GAMEPLAY│           │ AUDIO & RELEASE  │
│ - Tech Artist    │           │ - Unity/Godot/UE │           │ - Game Audio Eng │
│ - Narrative Des  │           │ - Gameplay Scrip │           │ - Performance Opt│
│ - Brand Guardian │           │ - Multiplayer Eng│           │ - Game QA Tester │
│ - Game UI/UX     │           │ - Level Designer │           │ - Security Audit │
└──────────────────┘           └──────────────────┘           └──────────────────┘
```

---

## 10-PHASE GAME PRODUCTION LIFECYCLE

### PHASE 1 — GAME DISCOVERY & CONCEPT (GDD)
- **Assigned Specialists**:
  - `agency-game-development-game-designer` (Lead)
  - `agency-game-development-level-designer`
  - `agency-product-manager`
  - `agency-game-development-economy-designer`
- **Execution Checklist**:
  1. Define the unique gameplay hook, target player demographic, and core loop (Action -> Reward -> Progression).
  2. Map out player controls, session length, and difficulty curves.
  3. Design game economy (currencies, sources, sinks, rewards, upgrades).
  4. Author Game Design Document (GDD) with non-goals and MVP scope.
- **Mandatory Deliverables**:
  - `GDD.md` (Game Design Document) with Core Loop and Economy Architecture.

---

### PHASE 2 — BRANDING & CREATIVE ART DIRECTION
- **Assigned Specialists**:
  - `agency-design-brand-guardian` (Lead)
  - `agency-design-visual-storyteller`
  - `agency-game-development-narrative-designer`
  - `agency-design-ui-designer`
- **Execution Checklist**:
  1. Establish art direction (stylized, pixel art, realistic, low-poly, cyberpunk, etc.).
  2. Create character backstories, world lore, and environmental storytelling beats.
  3. Design game typography, color palette, logo concept, and title screen branding.
  4. Ensure visual consistency across 2D/3D assets and UI elements.
- **Mandatory Deliverables**:
  - `ART_STYLE_GUIDE.md` and `NARRATIVE_LORE.md`.

---

### PHASE 3 — ENGINE DETECTION & TECHNICAL ARCHITECTURE
- **Engine Inspection Protocol**:
  Inspect workspace files to identify engine:
  - **Unity Detected** (`Assets/`, `ProjectSettings/`):
    - Load: `agency-game-development-unity-unity-architect`, `agency-game-development-unity-unity-editor-tool-developer`, `agency-game-development-unity-unity-multiplayer-engineer`, `agency-game-development-unity-unity-shader-graph-artist`.
  - **Godot Detected** (`project.godot`):
    - Load: `agency-game-development-godot-godot-gameplay-scripter`, `agency-game-development-godot-godot-multiplayer-engineer`, `agency-game-development-godot-godot-shader-developer`.
  - **Unreal Detected** (`*.uproject`):
    - Load: `agency-game-development-unreal-engine-unreal-systems-engineer`, `agency-game-development-unreal-engine-unreal-technical-artist`, `agency-game-development-unreal-engine-unreal-multiplayer-architect`.
  - **Browser / WebGL Game Detected** (`package.json`, `Three.js`, `Phaser`, `Pixi.js`):
    - Load: `agency-engineering-frontend-developer`, `agency-game-development-game-designer`, `performance-optimization`.
- **Mandatory Deliverables**:
  - `TECHNICAL_ARCHITECTURE.md` establishing single-responsibility systems, ScriptableObjects/nodes, and decoupled game managers.

---

### PHASE 4 — GAMEPLAY ENGINEERING & CORE LOOP
- **Assigned Specialists**:
  - Gameplay Engineer (Engine-specific)
  - `agency-game-development-game-designer`
  - `physics-3d-collision` / `create-2d-physics`
  - Multiplayer Engineer (if networked)
- **Execution Checklist**:
  1. Implement player character controller with tight input handling (keyboard, gamepad, touch).
  2. Build camera controller (cinemachine, smooth follow, screen shake, clipping prevention).
  3. Implement collision detection, triggers, health/damage systems, and state machines.
  4. Build interactive game objects, collectibles, inventory systems, and score managers.
- **Mandatory Deliverables**:
  - Functional, playable core gameplay loop script suite.

---

### PHASE 5 — GAME UI, HUD & USER EXPERIENCE
- **Assigned Specialists**:
  - `agency-design-ui-designer` (Lead)
  - `ui` / `ui-uitk` / `ui-ugui` (for Unity)
  - `agency-design-ui-finish-gate-reviewer`
  - `agency-design-ux-architect`
- **Execution Checklist**:
  1. Build Title Screen, Main Menu, Level Select, and Settings (Audio, Controls, Video).
  2. Implement in-game HUD (Health, Stamina, Score, Ammo, Minimap, Objectives).
  3. Create Pause Screen, Game Over / Victory Screen, and Confirmation Dialogs.
  4. Ensure UI scales across multiple aspect ratios (16:9, 18:9, 21:9, 4:3).
- **Mandatory Deliverables**:
  - Responsive, scalable UI hierarchies matching the game's art direction.

---

### PHASE 6 — AUDIO, VFX & LEVEL DESIGN
- **Assigned Specialists**:
  - `agency-game-development-game-audio-engineer` (Lead)
  - `agency-game-development-level-designer`
  - `agency-game-development-technical-artist`
  - Shader & Particle Specialists
- **Execution Checklist**:
  1. Design interactive sound effects (footsteps, impacts, UI clicks, ambient layers).
  2. Setup audio mixing buses (Master, Music, SFX, Voice) with dynamic ducking.
  3. Author custom shaders, lighting setups, and particle systems (hit sparks, smoke, explosions).
  4. Construct balanced level layouts with proper pacing, cover, flow, and encounter density.
- **Mandatory Deliverables**:
  - Audio mixer routing, particle VFX prefabs, and structured level scenes.

---

### PHASE 7 — PROFILING & PERFORMANCE OPTIMIZATION
- **Assigned Specialists**:
  - `performance-optimization` (Lead)
  - `optimize-audio`
  - `optimize-web` (if WebGL)
  - `manage-sprite-atlas`
  - `validate-urp-render-graph-renderer-feature`
- **Execution Checklist**:
  1. Maintain rock-solid frame rate target (60 FPS on mobile, 120+ FPS on PC/Console).
  2. Reduce draw calls via dynamic batching, GPU instancing, and texture atlases.
  3. Optimize physics tick rate and eliminate garbage collection allocations in hot loops.
  4. Compress audio assets (streaming for music, decompressed on load for short SFX).
- **Mandatory Deliverables**:
  - Performance profiling report with verified draw call and memory budgets.

---

### PHASE 8 — GAME SECURITY & MULTIPLAYER VALIDATION
- **Assigned Specialists**:
  - `agency-security-appsec-engineer` (Lead)
  - `agency-game-development-unity-unity-multiplayer-engineer` / Godot / UE Multiplayer
  - `agency-security-penetration-tester`
- **Execution Checklist**:
  1. Validate all game-critical state server-side (never trust client score or currency packets).
  2. Implement anti-cheat protections (speed hacks, teleportation, wall clipping validation).
  3. Protect save files against local tampering via encryption or cryptographic checksums.
  4. Audit network RPCs, matchmaking lobbies, and player authentication tokens.
- **Mandatory Deliverables**:
  - Multiplayer security audit confirming authoritative server validation.

---

### PHASE 9 — GAMEPLAY QA & POLISH TESTING
- **Assigned Specialists**:
  - `agency-testing-reality-checker` (Lead)
  - `agency-testing-evidence-collector`
  - `test-engineer`
- **Execution Checklist**:
  1. Conduct full playtesting of the primary game loop (Start -> Play -> Win/Lose -> Restart).
  2. Test edge cases: Alt-Tab, window resizing, low battery, audio mute, save/load persistence.
  3. Verify zero unhandled exceptions or memory leaks during prolonged play sessions.
- **Mandatory Deliverables**:
  - QA verification log with confirmed resolution of critical gameplay blockers.

---

### PHASE 10 — RELEASE & DEPLOYMENT READINESS
- **Assigned Specialists**:
  - `shipping-and-launch` (Lead)
  - `agency-marketing-app-store-optimizer`
  - `agency-engineering-technical-writer`
- **Execution Checklist**:
  1. Configure target platform build settings (Windows, macOS, WebGL, Android, iOS).
  2. Generate store assets, release notes, icon sizes, and splash screens.
  3. Verify build checksums, signing certificates, and distribution package integrity.
- **Mandatory Deliverables**:
  - Production build pipeline configuration and launch release checklist.
