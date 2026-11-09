# SR24PLUS CORE EXECUTION & QUALITY RULES

These 10 inviolable execution principles govern every specialist and workflow within the SR24Plus Engineering Toolkit:

---

## 1. Zero Hallucination & Evidence Verification
Never mark a phase, test, or task as complete without verifiable evidence.
- Source code changes must compile with 0 TypeScript/bundler/compiler errors.
- Unit and integration tests must produce explicit pass/fail output logs.
- Never claim a skill or tool was executed unless its actual instructions or CLI was run.

---

## 2. The Anti-AI-Slop Imperative
All user-facing designs must adhere to the **Anti-Slop Quality Standard**:
- ❌ **No generic purple/blue gradient buttons or hero backgrounds**.
- ❌ **No gratuitous glassmorphism** that degrades WCAG AA text contrast.
- ❌ **No repetitive, empty 3-column floating card features**.
- ❌ **No emoji-based icon systems** where clean SVG / Lucide icons belong.
- ❌ **No fake marketing metrics** (`99.999% satisfied users`, `10x faster`).
- ✅ **Every visual decision must be anchored in the brand identity**.

---

## 3. Grounded Architecture Before Implementation
- Always inspect the existing codebase, framework, and dependencies before proposing changes.
- Never delete or overwrite unrelated code.
- Maintain a single source of truth for architecture and interface contracts.
- Respect existing project conventions (folder structure, naming styles, linters).

---

## 4. Authoritative Security & Zero Trust
- Never expose API keys, database credentials, or secret tokens in client-side bundles or git history.
- Never trust client-reported scores, prices, user IDs, or competitive outcomes.
- Enforce parameterized database queries (SQL injection prevention) and parameterized ORMs.
- Implement rate limiting and authentication checks on all public-facing endpoints.

---

## 5. Performance & Resource Discipline
- **Web**: Target Core Web Vitals (LCP < 2.5s, FID/INP < 200ms, CLS < 0.1).
- **3D & WebGL**: Implement lazy-loading, geometry LODs, texture compression, and `prefers-reduced-motion` fallbacks.
- **Games**: Target stable 60 FPS (mobile) or 120+ FPS (PC), keep draw calls within budget, avoid GC allocations in hot update loops.

---

## 6. Deterministic Fallbacks for Intelligent Features
- Every AI, speech, or external third-party integration must have an offline, deterministic, or rule-based fallback.
- The failure of an external cloud API must never render the core application inoperable.

---

## 7. Responsive & Universal Accessibility
- All web interfaces must function seamlessly on mobile (375px), tablet (768px), and desktop (1280px+).
- Support full keyboard navigation with visible focus rings.
- Ensure color contrast ratios meet WCAG 2.1 AA standards (minimum 4.5:1 for body text).

---

## 8. Respect Git Hygiene & Workspace Boundaries
- Make atomic, meaningful git commits with Conventional Commits format (`feat:`, `fix:`, `refactor:`, `chore:`).
- Never force push (`git push -f`).
- Never touch files outside the project scope or overwrite user personal settings.
