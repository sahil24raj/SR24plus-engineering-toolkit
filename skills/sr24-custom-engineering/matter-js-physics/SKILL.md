---
name: matter-js-physics
description: >-
  Expert in Matter.js 2D rigid body physics engine — Engine, World, Composites, Bodies,
  Constraints, MouseConstraint, collision filters/events, Raycasting, custom Canvas/WebGL rendering,
  React/Next.js integration, and performance optimization.
---

# Matter.js 2D Physics Engine Expert Skill

Matter.js is a 2D rigid body JavaScript physics engine for the web. This skill guides the architecture, implementation, advanced collision logic, custom rendering integration, React/Next.js component integration, and performance optimization for interactive web physics simulations and games.

---

## 1. Core Architecture & Modules

Matter.js operates on modular components:

- **`Engine`**: Core simulation controller that handles updates and collision resolution.
- **`World` / `Composite`**: The hierarchical container holding bodies, constraints, and sub-composites.
- **`Render`**: Built-in HTML5 canvas debug renderer (optional, can be replaced by custom Canvas/WebGL renderers).
- **`Runner`**: Coordinates the fixed-timestep or dynamic animation loop using `requestAnimationFrame`.
- **`Bodies` / `Body`**: Factory and manipulation methods for physical objects (rectangles, circles, polygons, custom SVG vertices).
- **`Constraint`**: Distance joints, elastic springs, pins, and hinges.
- **`MouseConstraint`**: Drag-and-drop user interaction via mouse or touch pointers.
- **`Events`**: Lifecycle hooks (`beforeUpdate`, `afterUpdate`, `collisionStart`, `collisionActive`, `collisionEnd`).

---

## 2. Standard Setup with Built-in Renderer

```typescript
import Matter from 'matter-js';

const {
  Engine,
  Render,
  Runner,
  Bodies,
  Composite,
  Constraint,
  Mouse,
  MouseConstraint,
  Events,
} = Matter;

// 1. Create engine and world
const engine = Engine.create({
  gravity: { x: 0, y: 1, scale: 0.001 },
  enableSleeping: true, // Optimizes resting bodies
});
const world = engine.world;

// 2. Create renderer
const render = Render.create({
  element: document.getElementById('physics-container')!,
  engine: engine,
  options: {
    width: 800,
    height: 600,
    wireframes: false,
    background: '#0f172a',
    showVelocity: false,
    showAngleIndicator: false,
  },
});
Render.run(render);

// 3. Create runner (game loop)
const runner = Runner.create();
Runner.run(runner, engine);

// 4. Add Static Boundaries (Walls & Floor)
const ground = Bodies.rectangle(400, 590, 810, 40, {
  isStatic: true,
  render: { fillStyle: '#334155' },
});
const leftWall = Bodies.rectangle(10, 300, 20, 600, { isStatic: true, render: { fillStyle: '#334155' } });
const rightWall = Bodies.rectangle(790, 300, 20, 600, { isStatic: true, render: { fillStyle: '#334155' } });
Composite.add(world, [ground, leftWall, rightWall]);

// 5. Add Dynamic Bodies
const box = Bodies.rectangle(400, 200, 60, 60, {
  restitution: 0.8, // Bounciness (0 = no bounce, 1 = elastic)
  friction: 0.05,   // Surface friction
  frictionAir: 0.01,// Air resistance
  density: 0.002,   // Mass = density * area
  render: { fillStyle: '#38bdf8' },
});
Composite.add(world, box);

// 6. Add Interactive Mouse Control
const mouse = Mouse.create(render.canvas);
const mouseConstraint = MouseConstraint.create(engine, {
  mouse: mouse,
  constraint: {
    stiffness: 0.2,
    render: { visible: true },
  },
});
Composite.add(world, mouseConstraint);
render.mouse = mouse;
```

---

## 3. Advanced Rigid Body Manipulation

### Direct Property Updates
Never set `body.position.x = 100` directly without updating velocity or vertices. Use `Matter.Body` methods:

```typescript
// Position and Rotation
Matter.Body.setPosition(body, { x: 300, y: 150 });
Matter.Body.setAngle(body, Math.PI / 4);

// Linear & Angular Velocity
Matter.Body.setVelocity(body, { x: 10, y: -15 });
Matter.Body.setAngularVelocity(body, 0.1);

// Forces and Impulses (Applied during engine update cycle)
Matter.Body.applyForce(
  body,
  { x: body.position.x, y: body.position.y }, // Point of application
  { x: 0.05, y: -0.08 }                       // Force vector
);

// Scale & Dimensions
Matter.Body.scale(body, 1.5, 1.5);

// Convert to Static / Dynamic
Matter.Body.setStatic(body, true);
```

---

## 4. Collision Categories & Filtering (Bitmasks)

Collision rules are determined by bitwise operations on `category`, `mask`, and `group`.

```typescript
// Define 32-bit Categories
const CAT_DEFAULT    = 0x0001; // 0001
const CAT_PLAYER     = 0x0002; // 0010
const CAT_ENEMY      = 0x0004; // 0100
const CAT_PROJECTILE = 0x0008; // 1000

// Player collides with Default (Walls/Ground) and Enemies, but NOT Player Projectiles
const playerBody = Bodies.circle(200, 200, 30, {
  collisionFilter: {
    category: CAT_PLAYER,
    mask: CAT_DEFAULT | CAT_ENEMY, // Bitwise OR
  },
});

// Friendly Bullet collides only with Enemies and Walls
const bulletBody = Bodies.circle(200, 200, 8, {
  collisionFilter: {
    category: CAT_PROJECTILE,
    mask: CAT_DEFAULT | CAT_ENEMY,
  },
});

// Sensor (Triggers collision events without physical bouncing/pushing)
const triggerZone = Bodies.rectangle(400, 300, 100, 100, {
  isSensor: true,
  isStatic: true,
  render: { fillStyle: 'rgba(234, 179, 8, 0.3)' },
});
```

---

## 5. Collision & Engine Event Handling

```typescript
// Detect Start of Collision
Events.on(engine, 'collisionStart', (event) => {
  const pairs = event.pairs;
  for (let i = 0; i < pairs.length; i++) {
    const { bodyA, bodyB } = pairs[i];

    if (bodyA.label === 'bullet' || bodyB.label === 'bullet') {
      const target = bodyA.label === 'bullet' ? bodyB : bodyA;
      const bullet = bodyA.label === 'bullet' ? bodyA : bodyB;

      if (target.label === 'enemy') {
        // Handle damage & queue body removal after step
        Composite.remove(world, bullet);
      }
    }
  }
});

// Custom Game Logic in Game Loop
Events.on(engine, 'beforeUpdate', (event) => {
  // Apply continuous forces (e.g. wind, magnetic attractors, custom gravity)
});
```

---

## 6. Constraints, Joints, & Soft Bodies

```typescript
// Distance Joint (Rope / Pin / Spring)
const joint = Constraint.create({
  bodyA: boxA,
  pointA: { x: 0, y: 0 },
  bodyB: boxB,
  pointB: { x: 0, y: 0 },
  length: 120,
  stiffness: 0.8, // 1.0 = rigid rod, 0.05 = bouncy spring
  damping: 0.05,
  render: {
    strokeStyle: '#f43f5e',
    lineWidth: 3,
  },
});
Composite.add(world, joint);

// Pin to World Point
const pendulum = Constraint.create({
  pointA: { x: 400, y: 50 }, // Fixed anchor in world
  bodyB: ball,
  length: 200,
  stiffness: 1.0,
});
Composite.add(world, pendulum);
```

---

## 7. Raycasting & Spatial Queries

```typescript
import { Query } from 'matter-js';

// 1. Raycast between two points
const allBodies = Composite.allBodies(world);
const collisions = Query.ray(
  allBodies,
  { x: 100, y: 100 }, // Start point
  { x: 700, y: 500 }, // End point
  10                  // Ray width
);

collisions.forEach((collision) => {
  console.log('Ray hit body:', collision.body.label);
});

// 2. Query point overlap
const clickedBodies = Query.point(allBodies, { x: 400, y: 300 });

// 3. Query region bounds
const bodiesInBox = Query.region(allBodies, {
  min: { x: 100, y: 100 },
  max: { x: 300, y: 300 },
});
```

---

## 8. Decoupling Physics from Custom Rendering (Custom Canvas / Pixi / React)

For production games, avoid `Matter.Render` and drive your own custom Canvas/WebGL rendering loop.

```typescript
// 1. Create Engine without Matter.Render
const engine = Engine.create();
const world = engine.world;

// 2. Custom Render Loop
function gameLoop(timestamp: number) {
  // Fixed step update (16.66ms per step at 60fps)
  Engine.update(engine, 1000 / 60);

  // Clear your Canvas
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  // Render Bodies
  const bodies = Composite.allBodies(world);
  for (const body of bodies) {
    if (!body.render.visible) continue;

    ctx.save();
    ctx.translate(body.position.x, body.position.y);
    ctx.rotate(body.angle);

    // Draw sprite or custom path
    if (body.circleRadius) {
      ctx.beginPath();
      ctx.arc(0, 0, body.circleRadius, 0, Math.PI * 2);
      ctx.fillStyle = '#38bdf8';
      ctx.fill();
    } else {
      // Draw polygon from vertices
      ctx.beginPath();
      const vertices = body.vertices;
      ctx.moveTo(vertices[0].x - body.position.x, vertices[0].y - body.position.y);
      for (let j = 1; j < vertices.length; j++) {
        ctx.lineTo(vertices[j].x - body.position.x, vertices[j].y - body.position.y);
      }
      ctx.closePath();
      ctx.fillStyle = '#ec4899';
      ctx.fill();
    }

    ctx.restore();
  }

  requestAnimationFrame(gameLoop);
}

requestAnimationFrame(gameLoop);
```

---

## 9. React / Next.js Component Integration

```tsx
'use client';

import React, { useEffect, useRef } from 'react';
import Matter from 'matter-js';

export const MatterCanvas: React.FC = () => {
  const sceneRef = useRef<HTMLDivElement>(null);
  const engineRef = useRef<Matter.Engine | null>(null);
  const renderRef = useRef<Matter.Render | null>(null);
  const runnerRef = useRef<Matter.Runner | null>(null);

  useEffect(() => {
    if (!sceneRef.current) return;

    const { Engine, Render, Runner, Bodies, Composite, Mouse, MouseConstraint } = Matter;

    const engine = Engine.create();
    engineRef.current = engine;

    const render = Render.create({
      element: sceneRef.current,
      engine: engine,
      options: {
        width: sceneRef.current.clientWidth || 600,
        height: 400,
        wireframes: false,
        background: 'transparent',
      },
    });
    renderRef.current = render;
    Render.run(render);

    const runner = Runner.create();
    runnerRef.current = runner;
    Runner.run(runner, engine);

    // World bounds
    const ground = Bodies.rectangle(300, 390, 610, 20, { isStatic: true });
    const ball = Bodies.circle(300, 100, 25, { restitution: 0.9 });
    Composite.add(engine.world, [ground, ball]);

    // Mouse control
    const mouse = Mouse.create(render.canvas);
    const mouseConstraint = MouseConstraint.create(engine, {
      mouse,
      constraint: { stiffness: 0.2, render: { visible: false } },
    });
    Composite.add(engine.world, mouseConstraint);
    render.mouse = mouse;

    // Cleanup on unmount
    return () => {
      Render.stop(render);
      Runner.stop(runner);
      Composite.clear(engine.world, false);
      Engine.clear(engine);
      render.canvas.remove();
      render.textures = {};
    };
  }, []);

  return <div ref={sceneRef} className="w-full h-[400px] overflow-hidden rounded-xl bg-slate-900" />;
};
```

---

## 10. Performance, Stability & Gotchas

1. **Tunneling Prevention (Bullet Through Paper)**: Fast-moving or small objects can pass through thin walls in a single step.
   - Fix 1: Make static boundary walls thick (e.g. 50-100px) and position them just outside visible bounds.
   - Fix 2: Substep updates (`for (let i = 0; i < 4; i++) Engine.update(engine, 1000 / 240)`).
2. **Sleeping Bodies**: Enable `engine.enableSleeping = true` when there are large piles or stacks of objects so resting bodies stop consuming collision calculation cycles.
3. **Iterations Tuning**:
   - `engine.positionIterations`: Default 6. Increase to 10-12 to prevent clipping/penetration under heavy stacking.
   - `engine.velocityIterations`: Default 4. Increase to 8 for stiff constraint networks.
4. **Clean Removal**: Never mutate the `world.bodies` array directly. Always use `Composite.remove(engine.world, body)`.
