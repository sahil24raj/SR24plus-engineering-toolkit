# MASTER PROFILE 2: BROWSER-BASED MULTIPLAYER 3D/2D GAMING PLATFORM
## Dedicated Profile for Real-Time Browser Esports & Canvas Games (Vibe Arena, Multiplayer WebGL)

> **Profile Identity**: Real-Time Browser Multiplayer Gaming Platform  
> **Primary Use Cases**: **Vibe Arena** (Real-Time Arena Brawlers, WebGL 3D Games, Multiplayer HTML5 Canvas Games, 4-Digit Room Codes, Mobile Touch Controls).  
> **Primary Commands**: `/sr24-browser-game [game-concept]` or `/sr24-multiplayer [task]`

---

## 1. Unified Game Architecture & Deterministic Netcode Loop

```
┌────────────────────────────────────────────────────────────────────────┐
│               CLIENT FRONTEND: HTML5 Canvas / Three.js / WebGL         │
│  Fixed 60Hz Timestep Accumulator Loop • Sub-frame State Interpolation   │
│  Universal Input Abstraction: Keyboard, Gamepad, Virtual Touch Sticks  │
│  Client-Side Prediction • Entity Reconciliation • Smooth Dead Reckoning│
│  Memory XOR Obfuscation (Prevents in-browser Cheat Engine tampering)   │
└────────────────────────────────────┬───────────────────────────────────┘
                                     │ WebSocket Binary / JSON Snapshots (20-60Hz)
┌────────────────────────────────────▼───────────────────────────────────┐
│             AUTHORITATIVE GAME SERVER (Node.js / Bun / Go)             │
│  Authoritative 60Hz Physics & Collision Simulation Tick Loop           │
│  Frictionless 4-Character Room Codes (#A9K4) • Instant Matchmaking     │
│  Server-Side Movement Delta Capping (Anti-Speedhack & Teleport Defense)│
│  State Broadcast: Delta-compressed snapshots sent to connected rooms   │
└────────────────────────────────────┬───────────────────────────────────┘
                                     │ Session Storage / Leaderboards
┌────────────────────────────────────▼───────────────────────────────────┐
│              PERSISTENCE & LEADERBOARD DATA LAYER                     │
│  Redis In-Memory Match State • PostgreSQL Player Stats & Elo Ratings   │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Integrated Specialist Squad & Upstream GitHub Sources

| Engineering Phase | Specialist Role | Skill Name | Upstream GitHub Repository | Key Responsibility |
|---|---|---|---|---|
| **Phase 1: Game Loop** | Browser Game Architect | `browser-game-architect` | `SR24Plus Custom Engineering` | Deterministic fixed-timestep loop (`dt = 1/60`), accumulator pattern, zero stutter |
| **Phase 2: Authoritative Netcode** | Multiplayer Engineer | `websocket-multiplayer-engineer` | `SR24Plus Custom Engineering` | Authoritative 60Hz WebSocket server, client prediction, server reconciliation |
| **Phase 3: Anti-Cheat Engine** | Game Security Specialist | `browser-game-anti-cheat-engineer` | `SR24Plus Custom Engineering` | Server-authoritative movement delta distance validation, memory XOR obfuscation for scores |
| **Phase 4: Game Feel & Combat** | Combat Mechanics Lead | `combat-mechanics-engineer` | `SR24Plus Custom Engineering` | Active hitbox/hurtbox frame data, 80ms hitstop impact freezes, dynamic screen shakes |
| **Phase 5: Audio & FX** | Interactive Game Audio Lead | `agency-game-development-game-audio-engineer` | [`msitarzewski/agency-agents`](https://github.com/msitarzewski/agency-agents) | Dynamic Web Audio API sound effects, spatial pan, impact audio triggers |
| **Phase 6: Delight & Polish** | Whimsy & Animation Lead | `agency-design-whimsy-injector` | [`msitarzewski/agency-agents`](https://github.com/msitarzewski/agency-agents) | Visual juicy feedback, particle celebrations, character quips |
| **Phase 7: Lobby & HUD UI** | Game UI Designer | `agency-design-ui-designer` + `ui-ux-pro-max` | [`msitarzewski/agency-agents`](https://github.com/msitarzewski/agency-agents) & [`nextlevelbuilder/ui-ux-pro-max-skill`](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | High-FPS HUD overlay, 4-character room join modal, live leaderboard |
| **Phase 8: Multiplayer QA** | Network Testing Lead | `playwright-automation-engineer` | `SR24Plus Custom Engineering` | Multi-tab headless browser simulation, synthetic 150ms packet latency and jitter testing |

---

## 3. How to Activate This Profile (Prompts & Commands)

### Primary Command:
```text
/sr24-browser-game [game concept]
```
*or for multiplayer netcode:*
```text
/sr24-multiplayer [multiplayer room mechanics]
```

### Copy-Paste Prompt for AI in Chat:
> *"Act as the SR24Plus Principal Game Architect & Realtime Netcode Specialist. I am building [Vibe Arena / Real-Time Browser Multiplayer Game]. Execute the game development pipeline: set up a deterministic 60 FPS fixed-timestep accumulator loop, build an authoritative Node.js WebSocket game server with 4-character room codes, implement client-side prediction and server reconciliation, add server-authoritative anti-cheat (speedhack delta checks & XOR memory masking), design mobile touch controls, and polish with 80ms hitstop impact freezes and Web Audio FX."*

