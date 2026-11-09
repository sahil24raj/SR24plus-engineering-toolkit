---
name: websocket-multiplayer-engineer
description: Architect of real-time multiplayer browser games — authoritative game servers, client prediction, server reconciliation, entity interpolation, room matchmaking, and low-latency WebSockets.
---

# Real-Time WebSocket Multiplayer Architecture Engineer

## Role & Mission
The **Real-Time WebSocket Multiplayer Architecture Engineer** designs, implements, and tunes low-latency, scalable multiplayer networking for browser and mobile games. You build authoritative game servers that eliminate cheating, implement client-side prediction and server reconciliation for zero-perceived-lag input, and manage dynamic room lobbies.

---

## 1. Activation Conditions
Invoke this skill whenever:
- Building real-time multiplayer browser games (fighting games, racing, arena brawlers).
- Implementing authoritative game servers (Node.js, ws, uWebSockets.js).
- Solving lag, jitter, teleportation, or desynchronization across players.
- Implementing matchmaking, private 4-digit room codes, and spectator modes.
- Integrating multiplayer systems in projects like Vibe Arena or Indian Politics Arena.

---

## 2. Core Multiplayer Architecture (Authoritative Server)

```
[Client 1] ─── (Sends Input: { seq: 42, move: RIGHT }) ────► [Authoritative Server]
    │                                                                │
    ▼ (Applies locally immediately: Client Prediction)                ▼ (Runs tick 60Hz)
[Interpolates Other Players] ◄─── (Broadcasts Snapshot @ 20-30Hz) ────┘
```

---

## 3. Implementation: Authoritative Server Loop & Snapshots

### A. Authoritative Server Tick (Node.js / TypeScript)
```typescript
import { WebSocketServer, WebSocket } from 'ws';

interface PlayerState {
  id: string;
  x: number;
  y: number;
  vx: number;
  vy: number;
  hp: number;
  lastProcessedInputSeq: number;
}

export class GameRoom {
  public id: string;
  private players: Map<string, PlayerState> = new Map();
  private sockets: Map<string, WebSocket> = new Map();
  private serverTick = 0;

  constructor(roomId: string) {
    this.id = roomId;
    // 60Hz Server simulation loop
    setInterval(() => this.update(1 / 60), 1000 / 60);
    // 20Hz Network snapshot broadcast loop
    setInterval(() => this.broadcastSnapshot(), 1000 / 20);
  }

  public handlePlayerInput(playerId: string, input: { seq: number; moveX: number; action: boolean }) {
    const player = this.players.get(playerId);
    if (!player) return;

    // Validate inputs against speed caps (anti-cheat)
    const moveX = Math.max(-1, Math.min(1, input.moveX));
    player.vx = moveX * 250; // pixels per sec
    player.lastProcessedInputSeq = input.seq;
  }

  private update(dt: number) {
    this.serverTick++;
    for (const player of this.players.values()) {
      player.x += player.vx * dt;
      player.y += player.vy * dt;
      // World boundary constraints
      player.x = Math.max(0, Math.min(1280, player.x));
    }
  }

  private broadcastSnapshot() {
    const snapshot = {
      tick: this.serverTick,
      timestamp: Date.now(),
      players: Array.from(this.players.values()),
    };
    const message = JSON.stringify({ type: 'SNAPSHOT', data: snapshot });

    for (const ws of this.sockets.values()) {
      if (ws.readyState === WebSocket.OPEN) {
        ws.send(message);
      }
    }
  }
}
```

### B. Client-Side Prediction & Reconciliation
```typescript
export class NetworkedPlayerClient {
  private pendingInputs: Array<{ seq: number; input: any }> = [];
  private currentSeq = 0;
  public localX = 0;

  public sendInput(inputData: any, socket: WebSocket) {
    this.currentSeq++;
    const packet = { seq: this.currentSeq, ...inputData };
    
    // 1. Send packet to server
    socket.send(JSON.stringify({ type: 'INPUT', data: packet }));

    // 2. Client-side prediction: apply input locally immediately
    this.applyLocalInput(packet);

    // 3. Keep in pending queue for server reconciliation
    this.pendingInputs.push({ seq: this.currentSeq, input: packet });
  }

  public onServerSnapshot(serverPlayerState: { lastProcessedInputSeq: number; x: number }) {
    // 1. Authoritative snap to server position
    this.localX = serverPlayerState.x;

    // 2. Remove inputs already acknowledged by server
    this.pendingInputs = this.pendingInputs.filter(
      (item) => item.seq > serverPlayerState.lastProcessedInputSeq
    );

    // 3. Re-simulate all unacknowledged inputs on top of server state
    for (const item of this.pendingInputs) {
      this.applyLocalInput(item.input);
    }
  }

  private applyLocalInput(input: any) {
    this.localX += input.moveX * 250 * (1 / 60);
  }
}
```

---

## 4. Entity Interpolation for Opponents
- Store a 100ms snapshot buffer of opponent states.
- Render opponent position between `Snapshot[t - 100ms]` and `Snapshot[t - 50ms]` via linear interpolation (`lerp`).
- Eliminates stutter and teleports even over fluctuating 150ms 4G connections.

---

## 5. Quality & Stress Testing Checklist
- [ ] Simulate network jitter (100ms latency, 5% packet loss) using Chrome DevTools Network Throttling.
- [ ] Verify zero visual rubberbanding during standard movement.
- [ ] Auto-reconnect with session token restores player to active room within 3 seconds.
- [ ] Room codes use 4-character unambiguous uppercase alphanumeric (e.g. `K9X2`, avoiding `0/O`, `1/I`).
