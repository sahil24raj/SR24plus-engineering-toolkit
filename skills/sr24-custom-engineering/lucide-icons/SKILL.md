---
name: lucide-icons
description: >-
  Specialist in Lucide icon systems for modern web interfaces — tree-shaking, SVG accessibility, dynamic sizing, animation wrappers, and visual consistency.
---

# Lucide Icon System Architecture & Design Tokens

## 1. When to Activate
Activate this skill whenever a project or prompt requires specialist in lucide icon systems for modern web interfaces — tree-shaking, svg accessibility, dynamic sizing, animation wrappers, and visual consistency.. It is assigned to official engineering phases in the **SR24Plus Engineering Toolkit**.

## 2. When Not to Activate
- Do not activate when the task does not involve lucide-icons.
- Do not activate as a substitute for simple static mockups where deeper engineering is unnecessary.

## 3. Core Capabilities
- Tree-shaken icon imports eliminating bundle bloat in React/Next.js and Vue applications
- Strict SVG accessibility (aria-hidden for decorative icons, aria-label/title for interactive controls)
- Consistent stroke-width tokens (1.5px, 2px), bounding box alignment (24px grid), and color cascading
- Animated icon wrappers using Motion / Framer Motion for micro-interactions
- Dynamic icon registry resolver with type-safe lookup by icon name string

## 4. Engineering Workflow
1. **Discovery & Architecture**: Inspect technical constraints, performance requirements, and data contracts.
2. **Setup & Configuration**: Install official package dependencies and configure environment variables.
3. **Implementation**: Author production-grade code using clean architecture, strict TypeScript types, and error handling.
4. **Validation & Testing**: Run unit and integration tests confirming zero regressions.
5. **Production Deployment**: Verify build bundle impact, tree-shaking, and observability telemetry.

## 5. Implementation Instructions & Code Patterns

```typescript
import React from 'react';
import * as LucideIcons from 'lucide-react';

interface DynamicIconProps {
  name: keyof typeof LucideIcons;
  size?: number;
  className?: string;
  strokeWidth?: number;
  'aria-label'?: string;
}

export const DynamicIcon: React.FC<DynamicIconProps> = ({
  name,
  size = 20,
  className = '',
  strokeWidth = 2,
  'aria-label': ariaLabel,
}) => {
  const IconComponent = LucideIcons[name] as React.ElementType;

  if (!IconComponent) {
    return <LucideIcons.HelpCircle size={size} className={className} />;
  }

  const isInteractive = Boolean(ariaLabel);

  return (
    <IconComponent
      size={size}
      strokeWidth={strokeWidth}
      className={`shrink-0 ${className}`}
      aria-hidden={!isInteractive}
      aria-label={ariaLabel}
      role={isInteractive ? 'img' : undefined}
    />
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
- **Repository**: [https://github.com/lucide-icons/lucide](https://github.com/lucide-icons/lucide)
- **Category**: SR24-WEB-DEV Canonical Engineering Skill

## 10. License & Attribution
- **License**: ISC
- **Maintained By**: SR24Plus Autonomous Engineering Architecture
