---
name: browser-game-architect
description: Master architect of browser-based HTML5, Canvas, WebGL, Phaser, and PixiJS games — fixed timestep loops, state machines, asset preloading, and 60 FPS mobile-responsive controls.
---

# Browser Game Architecture & Engine Specialist

## Role & Mission
The **Browser Game Architecture Specialist** designs and builds commercial-quality 2D/3D browser games with deterministic fixed-timestep game loops, robust game state machines, instant asset loading, responsive touch/keyboard controls, and consistent 60 FPS rendering on mobile and desktop browsers.

---

## 1. Activation Conditions
Invoke this skill whenever:
- Architecting a new browser game (HTML5 Canvas, PixiJS, Phaser, Three.js).
- Implementing game loop architectures, delta timing, or frame-rate independent physics.
- Designing game state management (Title -> Lobby -> Gameplay -> Game Over).
- Building responsive on-screen touch virtual joysticks or gamepad input abstractions.
- Developing browser gaming platforms (e.g. Vibe Arena, Indian Politics Arena).

---

## 2. Fixed Timestep Game Loop (The Accumulator Pattern)

Never use variable `deltaTime` in physics calculations, as it causes tunneling, erratic physics, and client desynchronization. Use a deterministic fixed timestep:

```typescript
export class GameEngine {
  private readonly fixedDeltaTime = 1 / 60; // 60 ticks per second (16.66ms)
  private accumulator = 0;
  private lastTime = 0;
  private animationFrameId = 0;

  constructor(
    private updatePhysics: (dt: number) => void,
    private render: (interpolation: number) => void
  ) {}

  public start() {
    this.lastTime = performance.now();
    this.animationFrameId = requestAnimationFrame(this.loop);
  }

  public stop() {
    cancelAnimationFrame(this.animationFrameId);
  }

  private loop = (currentTime: number) => {
    let frameTime = (currentTime - this.lastTime) / 1000;
    // Spiral of death prevention: cap maximum frame time to 250ms
    if (frameTime > 0.25) frameTime = 0.25;
    this.lastTime = currentTime;

    this.accumulator += frameTime;

    // Fixed physics updates
    while (this.accumulator >= this.fixedDeltaTime) {
      this.updatePhysics(this.fixedDeltaTime);
      this.accumulator -= this.fixedDeltaTime;
    }

    // Alpha interpolation factor for smooth rendering between physics steps
    const interpolation = this.accumulator / this.fixedDeltaTime;
    this.render(interpolation);

    this.animationFrameId = requestAnimationFrame(this.loop);
  };
}
```

---

## 3. Universal Input Abstraction Layer (Keyboard + Touch + Gamepad)
```typescript
export interface InputState {
  horizontal: number; // -1 (left) to 1 (right)
  vertical: number;   // -1 (up) to 1 (down)
  actionA: boolean;   // Jump / Light Attack
  actionB: boolean;   // Heavy Attack / Special
  pause: boolean;
}

export class UniversalInputManager {
  private state: InputState = { horizontal: 0, vertical: 0, actionA: false, actionB: false, pause: false };
  private keysDown: Set<string> = new Set();

  constructor() {
    window.addEventListener('keydown', (e) => this.keysDown.add(e.code));
    window.addEventListener('keyup', (e) => this.keysDown.delete(e.code));
  }

  public poll(): InputState {
    let h = 0;
    let v = 0;

    if (this.keysDown.has('KeyA') || this.keysDown.has('ArrowLeft')) h -= 1;
    if (this.keysDown.has('KeyD') || this.keysDown.has('ArrowRight')) h += 1;
    if (this.keysDown.has('KeyW') || this.keysDown.has('ArrowUp')) v -= 1;
    if (this.keysDown.has('KeyS') || this.keysDown.has('ArrowDown')) v += 1;

    // Gamepad API integration
    const gamepads = navigator.getGamepads ? navigator.getGamepads() : [];
    const pad = gamepads[0];
    if (pad) {
      const padH = pad.axes[0] || 0;
      const padV = pad.axes[1] || 0;
      if (Math.abs(padH) > 0.15) h = padH;
      if (Math.abs(padV) > 0.15) v = padV;
    }

    this.state.horizontal = Math.max(-1, Math.min(1, h));
    this.state.vertical = Math.max(-1, Math.min(1, v));
    this.state.actionA = this.keysDown.has('Space') || (pad?.buttons[0]?.pressed ?? false);
    this.state.actionB = this.keysDown.has('KeyE') || (pad?.buttons[1]?.pressed ?? false);
    this.state.pause = this.keysDown.has('Escape') || (pad?.buttons[9]?.pressed ?? false);

    return { ...this.state };
  }
}
```

---

## 4. Mobile Screen Adaptability & Viewport Scaling
```typescript
export function setupGameCanvas(canvas: HTMLCanvasElement, targetWidth = 1280, targetHeight = 720) {
  const resize = () => {
    const windowWidth = window.innerWidth;
    const windowHeight = window.innerHeight;

    const scale = Math.min(windowWidth / targetWidth, windowHeight / targetHeight);
    canvas.style.width = `${targetWidth * scale}px`;
    canvas.style.height = `${targetHeight * scale}px`;

    // Maintain crisp pixel ratio
    canvas.width = targetWidth;
    canvas.height = targetHeight;
  };

  window.addEventListener('resize', resize);
  resize();
}
```

---

## 5. Performance & Quality Standards
- [ ] Maintain consistent 60 FPS on both 120Hz displays and mid-tier Android mobile browsers.
- [ ] Zero object instantiation inside the render or physics loop (use Object Pooling for bullets, particles, and damage numbers).
- [ ] Audio playback initiated strictly after first user gesture (satisfying browser autoplay policies).
- [ ] Asset loader provides visual loading percentage bar with pre-compiled WebGL shaders.
