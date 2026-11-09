# PROJECT WORKFLOW PROFILE: INDIAN POLITICS ARENA
## Browser-Based Satirical Combat & Fighting Game

> **Project Identity**: INDIAN POLITICS ARENA  
> **Domain**: 2D/3D Browser Fighting Game with Real-Time Multiplayer  
> **Primary Command**: `/sr24-browser-game politics-arena` or `/sr24-multiplayer politics-arena`

---

## 1. Specialist Squad Roster

| Role | Assigned Skill(s) | Primary Mission |
|---|---|---|
| **Browser Game Architect** | `browser-game-architect` | Fixed 60 FPS loop, Canvas/PixiJS rendering, sprite anims |
| **Combat Mechanics Lead** | `combat-mechanics-engineer` | Frame data (startup, active, recovery), hitboxes/hurtboxes, hitstop |
| **Game Feel & VFX** | `game-feel-engineer` + `agency-design-whimsy-injector` | Impact freeze (6-frame hitstop), screen shake, satirical cartoon VFX |
| **Multiplayer Architect** | `websocket-multiplayer-engineer` | Low-latency 1v1 online matches, rollback netcode simulation |
| **Anti-Cheat Specialist** | `browser-game-anti-cheat-engineer` | Server-authoritative health, cooldown verification, anti-speedhack |
| **Game UI Designer** | `agency-design-ui-designer` + `ui-ux-pro-max` | Street fighter style HUD (Health, Super Meter, Dialogue intro) |
| **Audio Engineer** | `agency-game-development-game-audio-engineer` | Satirical voice lines, punch impacts, Indian election crowd ambience |

---

## 2. Combat Mechanics Architecture

- **Frame Rate**: Strictly locked at 60 FPS for deterministic combat timing.
- **Attack Hierarchy**: Light Jab (4F startup), Heavy Punch (9F startup), Political Oratory Special (Super Meter 100%).
- **Hitstop Impact Freeze**: 80ms freeze upon successful hit, creating visceral tactile weight.
- **Input Buffer**: 6-frame lenient combo buffer to allow smooth special move chaining on mobile touchscreens.

---

## 3. Mandatory Quality Gates

1. **Zero Input Delay**: Local character executes instantly via client-side prediction; opponent moves interpolated.
2. **Hitbox Accuracy**: Visual attack sprites match physical bounding boxes within 4-pixel tolerance.
3. **Corner Trap Protection**: Damage scaling reduces consecutive combo hits to prevent infinite wall locks.
4. **Mobile Responsive**: Virtual joystick + 3 action buttons scale dynamically to any mobile aspect ratio.
