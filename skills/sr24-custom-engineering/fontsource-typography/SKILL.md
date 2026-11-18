---
name: fontsource-typography
description: >-
  Expert in Fontsource self-hosted open-source fonts, variable font configuration, font-display optimization, and zero Cumulative Layout Shift (CLS).
---

# Fontsource Self-Hosted Typography & Zero-CLS Systems

## 1. When to Activate
Activate this skill whenever a project or prompt requires expert in fontsource self-hosted open-source fonts, variable font configuration, font-display optimization, and zero cumulative layout shift (cls).. It is assigned to official engineering phases in the **SR24Plus Engineering Toolkit**.

## 2. When Not to Activate
- Do not activate when the task does not involve fontsource-typography.
- Do not activate as a substitute for simple static mockups where deeper engineering is unnecessary.

## 3. Core Capabilities
- Self-hosted font bundles eliminating third-party Google Fonts network requests and GDPR issues
- Variable font weight configuration (100 to 900) reducing HTTP requests to single WOFF2 files
- Tailwind CSS typography integration with strict font-family token definitions
- Font subsetting (Latin, Devanagari, Cyrl) and font-display: swap configuration
- Preloading critical font faces to eliminate Cumulative Layout Shift (CLS) on initial paint

## 4. Engineering Workflow
1. **Discovery & Architecture**: Inspect technical constraints, performance requirements, and data contracts.
2. **Setup & Configuration**: Install official package dependencies and configure environment variables.
3. **Implementation**: Author production-grade code using clean architecture, strict TypeScript types, and error handling.
4. **Validation & Testing**: Run unit and integration tests confirming zero regressions.
5. **Production Deployment**: Verify build bundle impact, tree-shaking, and observability telemetry.

## 5. Implementation Instructions & Code Patterns

```typescript
// 1. Install variable fonts:
// npm install @fontsource-variable/space-grotesk @fontsource-variable/inter

// 2. Import into root layout / entry point:
import '@fontsource-variable/space-grotesk';
import '@fontsource-variable/inter';

// 3. Configure Tailwind typography tokens (tailwind.config.ts):
import type { Config } from 'tailwindcss';

const config: Config = {
  theme: {
    extend: {
      fontFamily: {
        heading: ['"Space Grotesk Variable"', 'sans-serif'],
        body: ['"Inter Variable"', 'sans-serif'],
        mono: ['"JetBrains Mono"', 'monospace'],
      },
      fontSize: {
        'display-2xl': ['4.5rem', { lineHeight: '1.05', letterSpacing: '-0.04em' }],
        'display-xl': ['3.75rem', { lineHeight: '1.1', letterSpacing: '-0.03em' }],
        'heading-lg': ['2.25rem', { lineHeight: '1.2', letterSpacing: '-0.02em' }],
      },
    },
  },
};
export default config;
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
- **Repository**: [https://github.com/fontsource/fontsource](https://github.com/fontsource/fontsource)
- **Category**: SR24-WEB-DEV Canonical Engineering Skill

## 10. License & Attribution
- **License**: MIT
- **Maintained By**: SR24Plus Autonomous Engineering Architecture
