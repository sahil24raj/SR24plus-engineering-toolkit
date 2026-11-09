# WORKFLOW: /sr24-multiplayer — REAL-TIME MULTIPLAYER SQUAD

> **Command**: `/sr24-multiplayer [task]`  
> **Target Projects**: Vibe Arena, Indian Politics Arena, real-time multiplayer applications  
> **Mission**: Build scalable, low-latency, cheat-resistant authoritative multiplayer servers with client-side prediction, server reconciliation, and dynamic room matchmaking.

---

## 1. Specialist Squad Roster

- **Multiplayer Architect**: `websocket-multiplayer-engineer`
- **Anti-Cheat Engineer**: `browser-game-anti-cheat-engineer`
- **Realtime Infrastructure**: `agency-engineering-realtime-collaboration-engineer`
- **Security Auditor**: `agency-security-appsec-engineer`
- **Load Testing Engineer**: `agency-testing-performance-benchmarker`

---

## 2. 5-Stage Multiplayer Deployment Pipeline

1. **Stage 1: Authoritative Game Server Loop**:
   - 60Hz server physics tick; 20Hz snapshot broadcast rate via WebSocket.
   - Server strictly validates inputs (movement speed caps, cooldown checks, boundary clamping).
2. **Stage 2: Client-Side Prediction & Reconciliation**:
   - Clients apply inputs locally immediately with a sequence ID (`seq`).
   - On incoming server snapshot, client snaps to authoritative position and re-applies unacknowledged inputs.
3. **Stage 3: Entity Interpolation for Opponents**:
   - Buffer opponent states over 100ms and smoothly interpolate (`lerp`) to eliminate stutter over 4G networks.
4. **Stage 4: Room Management & Matchmaking**:
   - 4-character room codes (`#A9K4`), private lobbies, spectator slots, and reconnect tokens.
5. **Stage 5: Network Stress Testing**:
   - Simulate 150ms latency and 5% packet loss; verify zero visual desync.

