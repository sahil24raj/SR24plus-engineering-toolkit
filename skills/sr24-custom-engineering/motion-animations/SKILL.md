---
name: motion-animations
description: >-
  Expert in Motion (formerly Framer Motion) for fluid web micro-interactions, layout animations, exit transitions, gestures, and hardware-accelerated spring physics.
---

# Motion (Framer Motion) Physics & Layout Animations

## 1. When to Activate
Activate this skill whenever a project or prompt requires expert in motion (formerly framer motion) for fluid web micro-interactions, layout animations, exit transitions, gestures, and hardware-accelerated spring physics.. It is assigned to official engineering phases in the **SR24Plus Engineering Toolkit**.

## 2. When Not to Activate
- Do not activate when the task does not involve motion-animations.
- Do not activate as a substitute for simple static mockups where deeper engineering is unnecessary.

## 3. Core Capabilities
- Layout animation transitions (`layout`, `layoutId`) for tabs, accordions, and modal expands
- Spring physics configuration (stiffness, damping, mass) delivering natural physical motion
- AnimatePresence orchestrated enter/exit transitions eliminating unmount pop/flicker
- Drag gestures, virtual joystick gestures, and swipe-to-dismiss mechanics
- Prefers-reduced-motion compliance guaranteeing accessibility for users with vestibular sensitivity

## 4. Engineering Workflow
1. **Discovery & Architecture**: Inspect technical constraints, performance requirements, and data contracts.
2. **Setup & Configuration**: Install official package dependencies and configure environment variables.
3. **Implementation**: Author production-grade code using clean architecture, strict TypeScript types, and error handling.
4. **Validation & Testing**: Run unit and integration tests confirming zero regressions.
5. **Production Deployment**: Verify build bundle impact, tree-shaking, and observability telemetry.

## 5. Implementation Instructions & Code Patterns

```typescript
import React from 'react';
import { motion, AnimatePresence } from 'motion/react';

interface AnimatedModalProps {
  isOpen: boolean;
  onClose: () => void;
  children: React.ReactNode;
}

export const AnimatedModal: React.FC<AnimatedModalProps> = ({ isOpen, onClose, children }) => {
  return (
    <AnimatePresence>
      {isOpen && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4">
          {/* Backdrop with smooth blur */}
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            onClick={onClose}
            className="fixed inset-0 bg-black/75 backdrop-blur-sm"
          />

          {/* Modal Card with spring physics */}
          <motion.div
            initial={{ opacity: 0, scale: 0.92, y: 20 }}
            animate={{ opacity: 1, scale: 1, y: 0 }}
            exit={{ opacity: 0, scale: 0.95, y: 15 }}
            transition={{ type: 'spring', damping: 25, stiffness: 300 }}
            className="relative z-10 w-full max-w-lg rounded-3xl border border-white/15 bg-[#1B1B22] p-6 shadow-2xl"
          >
            {children}
          </motion.div>
        </div>
      )}
    </AnimatePresence>
  );
};
```

## 6. Best Practices
- **Strict Typing**: Never use `any`; use strict interface and generic contracts.
- **Error Boundaries**: Handle all edge cases, offline drops, and network timeouts gracefully.
- **Performance Budget**: Avoid blocking main thread operations; optimize bundle sizes and lazy-load where appropriate.
- **Security**: Never expose private keys, credentials, or sensitive customer data in client-side bundles.

## 7. Common Anti-Patterns to Avoid
- Hardcoding credentials or API endpoints directly into source files.
- Ignoring promise rejections and async exceptions.
- Creating monolithic un-testable files instead of modular single-responsibility units.
- Introducing layout shifts or un-optimized re-renders.

## 8. Verification & Testing Checklist
- [ ] TypeScript compiles cleanly with zero errors (`tsc --noEmit`).
- [ ] Unit tests pass verifying expected behavior and edge cases.
- [ ] Environment variables documented in `.env.example`.
- [ ] Build artifact size verified with tree-shaking confirmed.

## 9. Official Source Repository & Upstream Reference
- **Repository**: [https://github.com/motiondivision/motion](https://github.com/motiondivision/motion)
- **Category**: SR24-WEB-DEV Canonical Engineering Skill

## 10. License & Attribution
- **License**: MIT
- **Maintained By**: SR24Plus Autonomous Engineering Architecture
