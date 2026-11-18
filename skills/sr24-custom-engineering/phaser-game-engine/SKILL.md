---
name: phaser-game-engine
description: >-
  Expert in Phaser 3 and HTML5 2D game development — scenes, game loop, physics (Arcade & Matter.js),
  sprites, tweens, animations, audio, input, tilemaps, particle systems, React/Next.js/Vite integration,
  and 2D game optimization.
---

# Phaser 3 Game Engine Expert Skill

Phaser is a fast, fun, and free 2D game framework for HTML5 games in Canvas and WebGL. This skill guides the architecture, implementation, debugging, and framework integration (Next.js / React / TypeScript / Vite) of high-performance 2D web games using Phaser 3.

---

## 1. Core Architecture & Game Configuration

### Basic Setup & Config Structure
```typescript
import Phaser from 'phaser';

const config: Phaser.Types.Core.GameConfig = {
  type: Phaser.AUTO, // Automatically chooses WebGL with Canvas fallback
  parent: 'game-container',
  width: 800,
  height: 600,
  backgroundColor: '#1a1a2e',
  scale: {
    mode: Phaser.Scale.FIT,
    autoCenter: Phaser.Scale.CENTER_BOTH,
  },
  physics: {
    default: 'arcade',
    arcade: {
      gravity: { x: 0, y: 500 },
      debug: process.env.NODE_ENV === 'development',
    },
  },
  scene: [BootScene, PreloadScene, MenuScene, MainGameScene, UIScene],
  pixelArt: false, // Set to true for retro pixel-perfect rendering
  fps: {
    target: 60,
    forceSetTimeOut: false,
  },
};

export const game = new Phaser.Game(config);
```

---

## 2. Scene Lifecycle & Management

Every scene in Phaser inherits from `Phaser.Scene`.

```typescript
export class MainGameScene extends Phaser.Scene {
  private player!: Phaser.Physics.Arcade.Sprite;
  private score: number = 0;

  constructor() {
    super({ key: 'MainGameScene' });
  }

  // 1. Initialize data passed from another scene
  init(data: { startingLevel?: number }) {
    this.score = 0;
    console.log('Starting level:', data.startingLevel ?? 1);
  }

  // 2. Preload assets (Textures, Audio, Tilemaps)
  preload() {
    this.load.image('ground', '/assets/ground.png');
    this.load.spritesheet('player', '/assets/player_sheet.png', {
      frameWidth: 32,
      frameHeight: 48,
    });
    this.load.audio('jump_sfx', '/assets/audio/jump.wav');
  }

  // 3. Create Game Objects, Setup Collisions & Input
  create() {
    this.player = this.physics.add.sprite(100, 450, 'player');
    this.player.setBounce(0.2);
    this.player.setCollideWorldBounds(true);

    // Setup HUD/UI scene in parallel
    this.scene.launch('UIScene', { parentScene: this.scene.key });
  }

  // 4. Per-frame Game Loop (Delta is time in ms since last frame)
  update(time: number, delta: number) {
    // Input and continuous motion logic
  }
}
```

### Scene Operations
- `this.scene.start('NextScene', data)`: Stops current scene and starts target.
- `this.scene.launch('OverlayScene', data)`: Runs target scene concurrently (ideal for HUDs/pause menus).
- `this.scene.pause()` / `this.scene.resume()`: Pauses/resumes update loops.
- `this.scene.sleep()` / `this.scene.wake()`: Pauses rendering & updates while preserving memory state.
- `this.scene.stop()`: Shuts down and cleans up.

---

## 3. Physics Systems

### Arcade Physics (High Performance, AABB & Circle Hitboxes)
Best for platformers, top-down RPGs, arcade shooters, and hyper-casual games.

```typescript
// Static vs Dynamic Bodies
const platforms = this.physics.add.staticGroup();
platforms.create(400, 568, 'ground').setScale(2).refreshBody();

const player = this.physics.add.sprite(100, 450, 'player');

// Collisions & Overlaps
this.physics.add.collider(player, platforms);

const coins = this.physics.add.group({
  key: 'coin',
  repeat: 11,
  setXY: { x: 12, y: 0, stepX: 70 },
});

this.physics.add.overlap(player, coins, (p, coinObj) => {
  const coin = coinObj as Phaser.Physics.Arcade.Sprite;
  coin.disableBody(true, true); // deactivate & hide
  this.events.emit('score-update', 10);
});
```

### Matter.js Physics (Full Rigid Body, Joints, Polygon Collision)
Best for physics puzzles, ragdolls, vehicle mechanics, and complex geometry.

```typescript
const matterSprite = this.matter.add.sprite(400, 100, 'crate', undefined, {
  shape: 'rectangle',
  chamfer: { radius: 10 },
  density: 0.05,
  friction: 0.1,
  restitution: 0.6,
});

// Collision Filtering (Categories & Masks)
const CATEGORY_PLAYER = this.matter.world.nextCategory();
const CATEGORY_ENEMY = this.matter.world.nextCategory();

matterSprite.setCollisionCategory(CATEGORY_PLAYER);
matterSprite.setCollidesWith([CATEGORY_ENEMY]);
```

---

## 4. Input & Controls

### Keyboard Input
```typescript
// Default cursors (Up, Down, Left, Right, Space, Shift)
const cursors = this.input.keyboard!.createCursorKeys();

// Custom Key Mapping
const wasd = this.input.keyboard!.addKeys({
  up: Phaser.Input.Keyboard.KeyCodes.W,
  down: Phaser.Input.Keyboard.KeyCodes.S,
  left: Phaser.Input.Keyboard.KeyCodes.A,
  right: Phaser.Input.Keyboard.KeyCodes.D,
}) as { up: Phaser.Input.Keyboard.Key; down: Phaser.Input.Keyboard.Key; left: Phaser.Input.Keyboard.Key; right: Phaser.Input.Keyboard.Key };

// Inside update()
if (cursors.left.isDown || wasd.left.isDown) {
  player.setVelocityX(-160);
  player.anims.play('left', true);
}
```

### Pointer & Touch Events
```typescript
// Global Pointer
this.input.on('pointerdown', (pointer: Phaser.Input.Pointer) => {
  console.log(`Clicked at: ${pointer.worldX}, ${pointer.worldY}`);
});

// Interactive Game Object
const button = this.add.image(400, 300, 'button').setInteractive({ useHandCursor: true });
button.on('pointerdown', () => this.startGame());
button.on('pointerover', () => button.setTint(0xcccccc));
button.on('pointerout', () => button.clearTint());
```

---

## 5. Animations & Tweens

### Animations (Spritesheets / Texture Atlases)
```typescript
this.anims.create({
  key: 'walk_right',
  frames: this.anims.generateFrameNumbers('player', { start: 5, end: 8 }),
  frameRate: 10,
  repeat: -1, // Infinite loop
});
```

### Tweens (Smooth Property Transitions)
```typescript
this.tweens.add({
  targets: player,
  y: player.y - 50,
  duration: 400,
  ease: 'Power2',
  yoyo: true,
  repeat: 0,
  onComplete: () => {
    // Callback after completion
  },
});
```

---

## 6. Cameras, Viewports & Scaling

```typescript
// Camera Follow with Deadzone & Bounds
this.cameras.main.setBounds(0, 0, 3200, 600);
this.cameras.main.startFollow(this.player, true, 0.08, 0.08);
this.cameras.main.setDeadzone(100, 50);

// Camera FX
this.cameras.main.shake(200, 0.01); // duration, intensity
this.cameras.main.flash(300, 255, 255, 255);
this.cameras.main.fade(500, 0, 0, 0);
```

---

## 7. Audio Management

```typescript
// Background Music
const bgm = this.sound.add('theme_music', {
  loop: true,
  volume: 0.5,
});
bgm.play();

// Sound Effects with pitch modulation
const coinSound = this.sound.add('coin_sfx');
coinSound.play({
  volume: 0.8,
  rate: Phaser.Math.FloatBetween(0.9, 1.1), // Natural sound variation
});
```

---

## 8. React / Next.js Integration Best Practice

When integrating Phaser with React / Next.js:
1. Ensure client-side only initialization (disable SSR).
2. Clean up Phaser instances on component unmount via `game.destroy(true)`.
3. Use a shared Event Bus (`EventEmitter`) to communicate between React UI and Phaser scenes.

### Event Bus Pattern
```typescript
// EventBus.ts
import Phaser from 'phaser';
export const EventBus = new Phaser.Events.EventEmitter();
```

### React Component (`PhaserGame.tsx`)
```tsx
'use client';

import React, { useEffect, useRef } from 'react';
import Phaser from 'phaser';
import { EventBus } from './EventBus';
import { MainGameScene } from './scenes/MainGameScene';

interface PhaserGameProps {
  onScoreUpdate?: (score: number) => void;
}

export const PhaserGame: React.FC<PhaserGameProps> = ({ onScoreUpdate }) => {
  const containerRef = useRef<HTMLDivElement>(null);
  const gameRef = useRef<Phaser.Game | null>(null);

  useEffect(() => {
    if (!containerRef.current || gameRef.current) return;

    const config: Phaser.Types.Core.GameConfig = {
      type: Phaser.AUTO,
      parent: containerRef.current,
      width: 800,
      height: 600,
      physics: {
        default: 'arcade',
        arcade: { gravity: { x: 0, y: 400 }, debug: false },
      },
      scene: [MainGameScene],
    };

    gameRef.current = new Phaser.Game(config);

    const handleScore = (score: number) => {
      onScoreUpdate?.(score);
    };

    EventBus.on('score-change', handleScore);

    return () => {
      EventBus.off('score-change', handleScore);
      if (gameRef.current) {
        gameRef.current.destroy(true);
        gameRef.current = null;
      }
    };
  }, [onScoreUpdate]);

  return <div id="phaser-game-container" ref={containerRef} className="rounded-xl overflow-hidden shadow-2xl" />;
};
```

---

## 9. Performance & Optimization Checklist

1. **Texture Atlases**: Always pack sprites into `.json` texture atlases (e.g. TexturePacker / FreeTexPacker) instead of loading individual images to reduce WebGL draw calls.
2. **Object Pooling**: Avoid instantiating/destroying projectiles and particle emitters on the fly. Use `Phaser.GameObjects.Group` with `get()` and `setActive(false).setVisible(false)`.
3. **Audio Unlock**: Handle browser autoplay restrictions by showing a "Click to Start" overlay so the Web Audio context resumes smoothly.
4. **Memory Leaks**: Clear tweens, timers (`this.time.delayedCall` / `this.time.addEvent`), and event listeners (`this.events.off()`) in `scene.events.on('shutdown')`.
5. **Fixed Timestep vs Delta**: In custom movement calculations, always multiply speeds by `(delta / 1000)` unless using Arcade/Matter physics velocity.
