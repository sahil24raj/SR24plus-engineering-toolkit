---
name: typescript-eslint
description: >-
  Specialist in typescript-eslint configuration, strict type checking, no-explicit-any enforcement, type-aware lint rules, and modern code quality standards.
---

# TypeScript ESLint Strict Type-Safety & Code Hygiene

## 1. When to Activate
Activate this skill whenever a project or prompt requires specialist in typescript-eslint configuration, strict type checking, no-explicit-any enforcement, type-aware lint rules, and modern code quality standards.. It is assigned to official engineering phases in the **SR24Plus Engineering Toolkit**.

## 2. When Not to Activate
- Do not activate when the task does not involve typescript-eslint.
- Do not activate as a substitute for simple static mockups where deeper engineering is unnecessary.

## 3. Core Capabilities
- Strict type-checked linting configuration (`@typescript-eslint/recommended-type-checked`)
- Prohibition of `any` types with type assertion guardrails (`@typescript-eslint/no-explicit-any`)
- Floating promise detection guaranteeing proper async/await error catching
- Consistent type import enforcement (`import type { ... } from "..."`) for clean tree-shaking
- Exhaustive switch/union handling preventing unhandled enum/type cases

## 4. Engineering Workflow
1. **Discovery & Architecture**: Inspect technical constraints, performance requirements, and data contracts.
2. **Setup & Configuration**: Install official package dependencies and configure environment variables.
3. **Implementation**: Author production-grade code using clean architecture, strict TypeScript types, and error handling.
4. **Validation & Testing**: Run unit and integration tests confirming zero regressions.
5. **Production Deployment**: Verify build bundle impact, tree-shaking, and observability telemetry.

## 5. Implementation Instructions & Code Patterns

```typescript
// eslint.config.mjs
import tsEslint from 'typescript-eslint';

export default tsEslint.config(
  ...tsEslint.configs.recommendedTypeChecked,
  {
    languageOptions: {
      parserOptions: {
        project: true,
        tsconfigRootDir: import.meta.dirname,
      },
    },
    rules: {
      '@typescript-eslint/no-explicit-any': 'error',
      '@typescript-eslint/no-floating-promises': 'error',
      '@typescript-eslint/await-thenable': 'error',
      '@typescript-eslint/consistent-type-imports': [
        'error',
        { prefer: 'type-imports', fixStyle: 'inline-type-imports' },
      ],
      '@typescript-eslint/no-unused-vars': [
        'warn',
        { argsIgnorePattern: '^_', varsIgnorePattern: '^_' },
      ],
    },
  }
);
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
- **Repository**: [https://github.com/typescript-eslint/typescript-eslint](https://github.com/typescript-eslint/typescript-eslint)
- **Category**: SR24-WEB-DEV Canonical Engineering Skill

## 10. License & Attribution
- **License**: BSD-2-Clause
- **Maintained By**: SR24Plus Autonomous Engineering Architecture
