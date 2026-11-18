---
name: gsap-animations
description: >-
  Expert in GSAP (GreenSock Animation Platform) — GSAP 3 core (to, from, fromTo, set), Timelines,
  ScrollTrigger, Flip, Observer, SVG & Canvas animation, React/Next.js (@gsap/react, useGSAP hook),
  staggers, easing, and 60/120fps web performance optimization.
---

# GSAP (GreenSock Animation Platform) Expert Skill

GSAP is the industry-standard JavaScript animation library for high-performance, robust animations across all major browsers, Canvas, WebGL, SVG, and DOM elements.

---

## 1. Core Architecture & Tweens

### Basic Methods (`gsap.to`, `gsap.from`, `gsap.fromTo`, `gsap.set`)
```typescript
import gsap from 'gsap';

// gsap.to (Animate to target state)
gsap.to('.card', {
  x: 100,
  y: 0,
  opacity: 1,
  rotation: 360,
  duration: 1,
  ease: 'power3.out',
  scale: 1.05,
});

// gsap.from (Animate from initial state to current layout)
gsap.from('.hero-title', {
  y: 80,
  opacity: 0,
  duration: 1.2,
  ease: 'expo.out',
});

// gsap.fromTo (Explicit start & end states)
gsap.fromTo('.badge', 
  { scale: 0, opacity: 0 },
  { scale: 1, opacity: 1, duration: 0.6, ease: 'back.out(1.7)' }
);

// gsap.set (Zero-duration instant state update)
gsap.set('.modal', { display: 'block', opacity: 0 });
```

---

## 2. Timelines (Chained & Sequenced Animations)

Timelines orchestrate complex animations with position parameters (`<`, `>`, `+=1`, absolute labels).

```typescript
const tl = gsap.timeline({
  defaults: { duration: 0.8, ease: 'power2.out' },
  onComplete: () => console.log('Timeline finished'),
});

tl.from('.header', { y: -50, opacity: 0 })
  .from('.sidebar', { x: -100, opacity: 0 }, '-=0.4') // Starts 0.4s before header finishes
  .from('.content-card', { 
    y: 40, 
    opacity: 0, 
    stagger: 0.15 // Animates each matching card with 150ms delay
  }, '<0.2') // Starts 0.2s after previous tween begins
  .to('.cta-btn', { scale: 1.1, repeat: 1, yoyo: true }, '+=0.2');
```

---

## 3. React & Next.js Integration (`@gsap/react` / `useGSAP`)

Always use `useGSAP` in React/Next.js to prevent memory leaks, duplicate animations in React 18 Strict Mode, and handle proper cleanup on unmount.

```bash
npm install gsap @gsap/react
```

```tsx
'use client';

import React, { useRef } from 'react';
import gsap from 'gsap';
import { useGSAP } from '@gsap/react';

// Register hook once if needed
gsap.registerPlugin(useGSAP);

export const AnimatedHero: React.FC = () => {
  const containerRef = useRef<HTMLDivElement>(null);

  useGSAP(
    () => {
      // Scoped automatically to containerRef
      gsap.from('.headline', {
        y: 60,
        opacity: 0,
        duration: 1,
        ease: 'power3.out',
      });

      gsap.from('.subhead', {
        y: 30,
        opacity: 0,
        delay: 0.3,
        duration: 0.8,
      });

      gsap.from('.button-group > button', {
        scale: 0.8,
        opacity: 0,
        stagger: 0.1,
        delay: 0.6,
        ease: 'back.out(1.5)',
      });
    },
    { scope: containerRef, dependencies: [] }
  );

  return (
    <div ref={containerRef} className="hero-section">
      <h1 className="headline text-4xl font-bold">Unleash Next-Gen Gaming</h1>
      <p className="subhead text-gray-400 mt-2">Smooth 120fps animations powered by GSAP.</p>
      <div className="button-group mt-6 flex gap-4">
        <button className="px-6 py-2 bg-indigo-600 rounded-lg">Play Now</button>
        <button className="px-6 py-2 bg-gray-700 rounded-lg">Learn More</button>
      </div>
    </div>
  );
};
```

---

## 4. ScrollTrigger Plugin (Scroll-Driven Animations)

```typescript
import { ScrollTrigger } from 'gsap/ScrollTrigger';
gsap.registerPlugin(ScrollTrigger);

// Scrubbed timeline on scroll
const scrollTl = gsap.timeline({
  scrollTrigger: {
    trigger: '.pin-section',
    start: 'top top',       // When top of trigger hits top of viewport
    end: '+=1500',          // Scroll distance of 1500px
    scrub: 1,               // 1 second smooth catch-up
    pin: true,              // Pin the element during scroll
    anticipatePin: 1,
    markers: process.env.NODE_ENV === 'development', // Debug markers
  },
});

scrollTl
  .to('.box-1', { x: 300, rotation: 180 })
  .to('.box-2', { y: -200, scale: 1.5 }, '<')
  .to('.box-3', { opacity: 0 });
```

---

## 5. Flip Plugin (Layout Transitions & FLIP Technique)

First-Last-Invert-Play technique for seamless grid/list reordering and modal expansions.

```typescript
import { Flip } from 'gsap/Flip';
gsap.registerPlugin(Flip);

function switchLayout(container: HTMLElement, newClass: string) {
  // 1. Get initial state
  const state = Flip.getState('.grid-item');

  // 2. Mutate DOM/Class
  container.className = newClass;

  // 3. Animate transition smoothly
  Flip.from(state, {
    duration: 0.7,
    ease: 'power2.inOut',
    stagger: 0.05,
    absolute: true, // Prevents layout snapping during reorder
    onComplete: () => console.log('Flip complete'),
  });
}
```

---

## 6. Staggers & Advanced Easing

### 2D Grid Staggering
```typescript
gsap.to('.grid-cell', {
  scale: 0.1,
  opacity: 0,
  y: 60,
  stagger: {
    grid: [5, 5],       // [rows, columns]
    from: 'center',     // 'start' | 'end' | 'center' | 'edges' | [x, y]
    amount: 0.8,        // Total stagger duration spread across all items
    ease: 'power1.inOut',
  },
});
```

### Custom Easing & Inertia
```typescript
// Easing formats:
// 'power1.out', 'power2.inOut', 'power3.out', 'power4.out',
// 'expo.out', 'circ.out', 'elastic.out(1, 0.3)', 'back.out(1.7)', 'bounce.out'
```

---

## 7. Performance & 60fps Optimization Rules

1. **Animate Composite Properties**: Prioritize `x`, `y`, `scale`, `rotation`, `opacity`, `transform` over layout properties (`width`, `height`, `top`, `left`, `margin`).
2. **`will-change` Management**: Use `force3D: true` (default in GSAP) to promote animated elements to GPU rendering layers.
3. **ScrollTrigger Batching**: For long lists, use `ScrollTrigger.batch()` instead of attaching individual triggers to hundreds of elements.
4. **Kill Inactive Tweens**: Clean up tweens on element destruction using `gsap.killTweensOf(target)` or `ctx.revert()` via `useGSAP`.
