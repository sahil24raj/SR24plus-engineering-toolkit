# PROJECT WORKFLOW PROFILE: VIBE ARENA
## High-Performance Browser Gaming Platform

> **Project Identity**: VIBE ARENA  
> **Domain**: Real-Time Browser Gaming & Esports Platform  
> **Primary Command**: `/sr24-browser-game vibe-arena` or `/sr24-multiplayer vibe-arena`

---

## 1. Specialist Squad Roster

| Role | Assigned Skill(s) | Primary Mission |
|---|---|---|
| **Lead Game Architect** | `browser-game-architect` | Fixed timestep loop, canvas/WebGL scaling, state machine |
| **Multiplayer Architect** | `websocket-multiplayer-engineer` | Authoritative server, snapshot interpolation, room codes |
| **Anti-Cheat Engineer** | `browser-game-anti-cheat-engineer` | Delta distance checks, memory XOR obfuscation, bot detection |
| **Game UI/UX Designer** | `agency-design-ui-designer` + `ui-ux-pro-max` | High-FPS game HUD, matchmaking lobby, leaderboard |
| **Realtime Systems** | `agency-engineering-realtime-collaboration-engineer` | Low-latency WebSocket connections, heartbeat keep-alive |
| **Performance Engineer**| `webgl-game-performance-engineer` + `performance-optimization` | 60 FPS mobile WebGL budget, asset sprite atlasing |
| **Analytics Specialist** | `agency-support-analytics-reporter` | Retention analytics, session length, player churn metrics |
| **QA Automation** | `playwright-automation-engineer` | E2E matchmaking tests, simulated packet drop tests |
| **DevOps & Cloud** | `agency-engineering-devops-automator` + `agency-engineering-sre` | WebSocket cluster scaling, Redis pub/sub room routing |

---

## 2. Technical Architecture & Network Topology

```
[Browser Client (WebGL / PixiJS)]
      │
      ▼ (WSS: WebSocket Secure)
[Edge Reverse Proxy (Cloudflare / NGINX)]
      │
      ▼
[Authoritative Game Server (Node.js 60Hz Tick)]
      ├── In-Memory Game State
      ├── Anti-Cheat Verification Matrix
      └── Redis Pub/Sub (Cross-Room Matchmaking)
```

---

## 3. Mandatory Execution Phases

1. **Lobby & Matchmaking**: 4-digit room codes (`#K9X2`), quick match queues, private friend challenges.
2. **Authoritative Simulation**: Player position and hit detection calculated on server; clients run client-prediction with 100ms interpolation buffer.
3. **Anti-Cheat Defense**: Server rejects any movement exceeding speed caps; high scores require signed HMAC tokens.
4. **Mobile Optimization**: Responsive touch virtual joystick with haptic feedback, 60 FPS on iOS Safari & Chrome Mobile.
5. **QA & Stress Gate**: Verified under simulated 150ms 4G network jitter and 5% packet loss with zero rubberbanding.
