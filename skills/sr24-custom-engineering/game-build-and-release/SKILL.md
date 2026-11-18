---
name: game-build-and-release
description: >-
  Specialist in browser game build pipelines — WebAssembly streaming instantiation, Brotli/Gzip asset compression, Service Worker offline caching, and portal packaging.
---

# Game Build Optimization, Wasm Streaming & Release Specialist

## 1. When to Activate
Activate this skill whenever a game project or prompt requires specialist in browser game build pipelines — webassembly streaming instantiation, brotli/gzip asset compression, service worker offline caching, and portal packaging.. It is assigned to official engineering phases in the **SR24Plus Engineering Toolkit**.

## 2. When Not to Activate
- Do not activate when the task does not involve game-build-and-release.
- Do not activate as a substitute for simple static mockups where deeper game systems engineering is unnecessary.

## 3. Core Capabilities
- Streaming WebAssembly instantiation (`WebAssembly.instantiateStreaming`) for instant startup
- Brotli asset compression configuration for Unity WebGL `.data`, `.wasm`, and `.framework.js` files
- Service Worker progressive web app (PWA) offline game caching
- HTML5 gaming portal compliance packaging (Poki, CrazyGames, itch.io, Y8)
- Automated cache-invalidation headers preventing users loading stale game client scripts

## 4. Engineering Workflow
1. **Design & Architecture**: Inspect gameplay loops, frame rate budgets, physics constraints, and network topology.
2. **Setup & Initialization**: Configure libraries, canvas bindings, physics worlds, and input listeners.
3. **Implementation**: Author deterministic game loops, decoupled systems, state machines, and rendering passes.
4. **Optimization**: Audit draw calls, memory allocation, garbage collection, and frame time stability.
5. **Testing & QA**: Execute automated regression, collision checks, network latency tests, and visual snapshot reviews.

## 5. Implementation Instructions & Code Patterns

```typescript
// Service Worker Game Caching (sw.js)
const CACHE_NAME = 'gullyverse-game-v1';
const ASSETS_TO_CACHE = [
  '/',
  '/brand/gully-environment.jpg',
  '/audio/click.mp3',
  '/models/auto-rickshaw.glb',
];

self.addEventListener('install', (event: any) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => cache.addAll(ASSETS_TO_CACHE))
  );
});

self.addEventListener('fetch', (event: any) => {
  event.respondWith(
    caches.match(event.request).then((cachedResponse) => {
      return cachedResponse || fetch(event.request);
    })
  );
});
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
- **Repository**: [https://github.com/vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills)
- **Category**: SR24-GAME-DEV Canonical Engineering Skill

## 10. License & Attribution
- **License**: MIT
- **Maintained By**: SR24Plus Autonomous Engineering Architecture
