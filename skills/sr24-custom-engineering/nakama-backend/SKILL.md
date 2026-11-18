---
name: nakama-backend
description: >-
  Specialist in Heroic Labs Nakama — real-time multiplayer, global leaderboards, user authentication, social squads, virtual storage, and in-game chat.
---

# Heroic Labs Nakama Open-Source Game Server & Social Backend

## 1. When to Activate
Activate this skill whenever a game project or prompt requires specialist in heroic labs nakama — real-time multiplayer, global leaderboards, user authentication, social squads, virtual storage, and in-game chat.. It is assigned to official engineering phases in the **SR24Plus Engineering Toolkit**.

## 2. When Not to Activate
- Do not activate when the task does not involve nakama-backend.
- Do not activate as a substitute for simple static mockups where deeper game systems engineering is unnecessary.

## 3. Core Capabilities
- Real-time match orchestration supporting turn-based, authoritative, and relayed multiplayer
- Global and territorial leaderboard infrastructure with weekly resets and tier rewards
- Account management supporting device IDs, email, Google, Apple, and Discord authentication
- Virtual currency and inventory storage collections with atomic read-modify-write safety
- TypeScript runtime modules running server-side custom RPCs and anti-cheat validations

## 4. Engineering Workflow
1. **Design & Architecture**: Inspect gameplay loops, frame rate budgets, physics constraints, and network topology.
2. **Setup & Initialization**: Configure libraries, canvas bindings, physics worlds, and input listeners.
3. **Implementation**: Author deterministic game loops, decoupled systems, state machines, and rendering passes.
4. **Optimization**: Audit draw calls, memory allocation, garbage collection, and frame time stability.
5. **Testing & QA**: Execute automated regression, collision checks, network latency tests, and visual snapshot reviews.

## 5. Implementation Instructions & Code Patterns

```typescript
import { Client } from '@heroiclabs/nakama-js';

const client = new Client('defaultkey', '127.0.0.1', '7350', false);

export async function authenticateGamer(deviceId: string) {
  const session = await client.authenticateDevice(deviceId, true);
  const socket = client.createSocket();
  await socket.connect(session, true);

  return { session, socket };
}

export async function submitGamerScore(session: any, leaderboardId: string, score: number) {
  return await client.writeLeaderboardRecord(session, leaderboardId, {
    score,
    subscore: 0,
    metadata: { gameMode: 'ranked' },
  });
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
- **Repository**: [https://github.com/heroiclabs/nakama](https://github.com/heroiclabs/nakama)
- **Category**: SR24-GAME-DEV Canonical Engineering Skill

## 10. License & Attribution
- **License**: Apache-2.0
- **Maintained By**: SR24Plus Autonomous Engineering Architecture
