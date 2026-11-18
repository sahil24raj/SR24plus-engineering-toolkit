---
name: colyseus-multiplayer
description: >-
  Specialist in Colyseus — authoritative multiplayer game servers, room schema state synchronization, matchmaking, client-side prediction, and reconnections.
---

# Colyseus Authoritative Multiplayer Game Server & State Sync

## 1. When to Activate
Activate this skill whenever a game project or prompt requires specialist in colyseus — authoritative multiplayer game servers, room schema state synchronization, matchmaking, client-side prediction, and reconnections.. It is assigned to official engineering phases in the **SR24Plus Engineering Toolkit**.

## 2. When Not to Activate
- Do not activate when the task does not involve colyseus-multiplayer.
- Do not activate as a substitute for simple static mockups where deeper game systems engineering is unnecessary.

## 3. Core Capabilities
- Schema-based binary delta state synchronization minimizing network bandwidth to <5 KB/s
- Authoritative game room lifecycle management (onCreate, onJoin, onLeave, onDispose)
- Built-in matchmaking system (seat reservations, private room codes, ranked lobbies)
- Client reconnection tokens allowing players to resume gameplay after network drops
- Client-side prediction with server state reconciliation eliminating perceived input lag

## 4. Engineering Workflow
1. **Design & Architecture**: Inspect gameplay loops, frame rate budgets, physics constraints, and network topology.
2. **Setup & Initialization**: Configure libraries, canvas bindings, physics worlds, and input listeners.
3. **Implementation**: Author deterministic game loops, decoupled systems, state machines, and rendering passes.
4. **Optimization**: Audit draw calls, memory allocation, garbage collection, and frame time stability.
5. **Testing & QA**: Execute automated regression, collision checks, network latency tests, and visual snapshot reviews.

## 5. Implementation Instructions & Code Patterns

```typescript
// Server Room Definition (room.ts)
import { Room, Client } from 'colyseus';
import { Schema, type, MapSchema } from '@colyseus/schema';

export class PlayerState extends Schema {
  @type('number') x = 0;
  @type('number') y = 0;
  @type('number') score = 0;
}

export class GameState extends Schema {
  @type({ map: PlayerState }) players = new MapSchema<PlayerState>();
}

export class ArenaRoom extends Room<GameState> {
  maxClients = 8;

  onCreate() {
    this.setState(new GameState());

    this.onMessage('move', (client, data) => {
      const player = this.state.players.get(client.sessionId);
      if (player) {
        player.x = data.x;
        player.y = data.y;
      }
    });
  }

  onJoin(client: Client) {
    this.state.players.set(client.sessionId, new PlayerState());
  }

  onLeave(client: Client) {
    this.state.players.delete(client.sessionId);
  }
}
```

## 6. Best Practices
- **Deterministic Loop**: Always use fixed-timestep loops for physics to avoid frame-rate dependency.
- **Zero Allocations in Loop**: Pre-allocate vectors, matrices, and objects; never allocate new objects in `update` or `render`.
- **Responsive Controls**: Support keyboard, gamepad, and virtual touch joysticks with identical input abstractions.
- **Audio Management**: Always unlock audio contexts on first user interaction and manage volumes through bus mixers.

## 7. Common Anti-Patterns to Avoid
- Variable delta-time in physics causing objects to tunnel through geometry at low frame rates.
- Polling in tight loops or allocating garbage that triggers periodic GC stutter.
- Hardcoding screen dimensions instead of responsive canvas auto-scaling.
- Trusting client game state in multiplayer games without server authority.

## 8. Verification & Testing Checklist
- [ ] 60 FPS maintained under maximum entity density.
- [ ] Physics simulation deterministic across varied display refresh rates (60Hz, 120Hz).
- [ ] Zero memory allocations in render loop verified via Chrome DevTools Memory profiler.
- [ ] Responsive controls tested across desktop keyboard and mobile touch viewports.

## 9. Official Source Repository & Upstream Reference
- **Repository**: [https://github.com/colyseus/colyseus](https://github.com/colyseus/colyseus)
- **Category**: SR24-GAME-DEV Canonical Engineering Skill

## 10. License & Attribution
- **License**: MIT
- **Maintained By**: SR24Plus Autonomous Engineering Architecture
