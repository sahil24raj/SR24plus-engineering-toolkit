# WORKFLOW: /sr24-design — DESIGN SYSTEM, VISUAL UI & ANTI-SLOP GATE

> **Command**: `/sr24-design [task]`  
> **Natural Language Trigger**: `"Audit design"`, `"Create design system"`, `"Make UI look professional"`, `"Fix AI slop"`  
> **Mission**: Eliminate generic AI-generated templates and build bespoke, accessible, premium design systems with intentional typography, deliberate color tokens, and polished micro-interactions.

---

## DESIGN SPECIALIST SQUAD

| Role | Skill | Focus |
|---|---|---|
| **Design System Lead** | `ui-ux-pro-max` | Design tokens, component contracts, accessibility guidelines, responsive scales |
| **Visual Designer** | `agency-design-ui-designer` | Custom layout, visual hierarchy, aesthetic balance, micro-copy styling |
| **Anti-Slop Critic** | `antislop` + `antislop-ui` | Enforce zero purple gradients, zero gratuitous glassmorphism, zero floating cards |
| **Finish-Gate Reviewer** | `agency-design-ui-finish-gate-reviewer` | Independent critique grounded in production evidence; hard pass/fail finish gate |
| **Aesthetic Evaluator** | `taste-skill` + `impeccable` | Typography pairing, mathematical spacing, contrast ratios, brand harmony |
| **Creative Animator** | `agency-design-whimsy-injector` | Purposeful micro-interactions, spring physics, meaningful hover/focus feedback |

---

## 5-STEP DESIGN UPGRADE LIFECYCLE

```
[1. Slop Detection & Critique]
              │
              ▼
[2. Design Tokens & Typography Scale]
              │
              ▼
[3. Component Library & Contrast Audit]
              │
              ▼
[4. Micro-Interactions & Motion Budget]
              │
              ▼
[5. Final Finish-Gate Certification]
```

### 1. Slop Detection & Critique
Run independent audit against common AI-generated antipatterns:
- Check for unnecessary purple or neon gradients.
- Check for unreadable low-contrast text on frosted glass.
- Check for repetitive, empty 3-card columns.
- Check for oversized rounded buttons and inconsistent padding.

### 2. Design Tokens & Mathematical Scale
- **Spacing**: Strict 4px/8px scale (`4`, `8`, `12`, `16`, `24`, `32`, `48`, `64`px).
- **Typography Scale**: Major Third (1.25) or Perfect Fourth (1.33) ratio.
- **Color Palette**: Neutral dark slate (`#09090b` / `#18181b`), functional semantic accents (Emerald for success/action, Amber for warning, Rose for critical), zero rainbow clutter.

### 3. Component Architecture
- Build atomic components: Button, Input, Select, Badge, Card, Modal, Dropdown, Table.
- Every interactive element must provide explicit states: `default`, `hover`, `active`, `focus-visible` (with accessible outline), and `disabled`.

### 4. Meaningful Micro-Interactions
- Smooth spring animations for state changes (duration 150ms-250ms).
- Respect `prefers-reduced-motion` media queries on all animations.
- Never add animations that block user productivity.

### 5. Final Finish-Gate Review
- Take visual screenshot or inspect rendered markup.
- `agency-design-ui-finish-gate-reviewer` issues a formal pass/fail report before design is approved for production.
