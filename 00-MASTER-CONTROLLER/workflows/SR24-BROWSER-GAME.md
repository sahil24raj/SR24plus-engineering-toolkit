# WORKFLOW: /sr24-browser-game — BROWSER GAME DEVELOPMENT SQUAD

> **Command**: `/sr24-browser-game [task]`  
> **Target Projects**: Vibe Arena, Indian Politics Arena, HTML5/Canvas/WebGL games  
> **Mission**: Build high-performance, responsive 60 FPS browser-based games with deterministic loops, visceral game feel, touch virtual controls, and instant web loading.

---

## 1. Specialist Squad Roster

- **Lead Architect**: `browser-game-architect`
- **Combat & Mechanics**: `combat-mechanics-engineer` (if combat/fighting)
- **Game Feel & VFX**: `game-feel-engineer` + `agency-design-whimsy-injector`
- **Asset Pipeline**: `game-asset-optimization-engineer` + `manage-sprite-atlas`
- **Audio Specialist**: `agency-game-development-game-audio-engineer`
- **Anti-Cheat Lead**: `browser-game-anti-cheat-engineer`
- **QA Automation**: `playwright-automation-engineer`

---

## 2. 6-Phase Browser Game Production Pipeline

1. **Phase 1: Deterministic Game Loop**:
   - Establish fixed timestep accumulator loop ($60\text{Hz}$) with interpolation for rendering.
   - Configure Canvas viewport auto-scaling for mobile and desktop screens.
2. **Phase 2: Universal Input Abstraction**:
   - Implement unified input listener handling WASD, Arrow keys, Gamepad API, and on-screen touch virtual joysticks.
3. **Phase 3: Core Mechanics & Feel**:
   - Implement movement, jumping, combat hitboxes/hurtboxes.
   - Add hitstop impact freezes (60–120ms), screen shake, and hit spark particle bursts.
4. **Phase 4: Asset & Memory Discipline**:
   - Use object pooling for bullets, particles, and damage floaters (zero allocations in update loop).
   - Bundle sprites into compressed texture atlases with WebP fallbacks.
5. **Phase 5: Audio & Autoplay Compliance**:
   - Defer Web Audio context initialization until first user tap or click.
   - Mix background music, ambient loops, and punchy impact SFX buses.
6. **Phase 6: Performance & Browser QA**:
   - Audit 60 FPS performance on 4x CPU throttling in Chrome DevTools.
   - Verify zero memory growth over 10 minutes of active gameplay.

