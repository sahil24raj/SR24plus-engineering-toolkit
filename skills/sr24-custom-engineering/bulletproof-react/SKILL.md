---
name: bulletproof-react
description: >-
  Expert in Alan Buscaglia’s Bulletproof React architecture — feature-based folder organization, isolated API slices, custom hooks, and scalable state boundaries.
---

# Bulletproof React Production Architecture & Modularity

## 1. When to Activate
Activate this skill whenever a project or prompt requires expert in alan buscaglia’s bulletproof react architecture — feature-based folder organization, isolated api slices, custom hooks, and scalable state boundaries.. It is assigned to official engineering phases in the **SR24Plus Engineering Toolkit**.

## 2. When Not to Activate
- Do not activate when the task does not involve bulletproof-react.
- Do not activate as a substitute for simple static mockups where deeper engineering is unnecessary.

## 3. Core Capabilities
- Feature-based project structure (`src/features/<feature-name>/{api,components,hooks,types}`)
- Strict boundary isolation preventing cross-feature spaghetti imports
- Centralized shared primitives in `src/components/ui/` with typed props contracts
- TanStack Query (React Query) query factory and mutation management
- Global Error Boundary hierarchies with fallback UI and error tracking integration

## 4. Engineering Workflow
1. **Discovery & Architecture**: Inspect technical constraints, performance requirements, and data contracts.
2. **Setup & Configuration**: Install official package dependencies and configure environment variables.
3. **Implementation**: Author production-grade code using clean architecture, strict TypeScript types, and error handling.
4. **Validation & Testing**: Run unit and integration tests confirming zero regressions.
5. **Production Deployment**: Verify build bundle impact, tree-shaking, and observability telemetry.

## 5. Implementation Instructions & Code Patterns

```typescript
/*
Recommended Feature Structure:
src/
  features/
    tournaments/
      api/
        getTournaments.ts
        joinTournament.ts
      components/
        TournamentCard.tsx
        TournamentList.tsx
      hooks/
        useTournamentTimer.ts
      types/
        index.ts
      index.ts  // Explicit public API barrel export
*/

import { useQuery } from '@tanstack/react-query';
import { Tournament } from '../types';

async function fetchActiveTournaments(): Promise<Tournament[]> {
  const res = await fetch('/api/tournaments?status=active');
  if (!res.ok) throw new Error('Failed to fetch tournaments');
  return res.json();
}

export function useActiveTournaments() {
  return useQuery({
    queryKey: ['tournaments', 'active'],
    queryFn: fetchActiveTournaments,
    staleTime: 1000 * 60 * 2, // 2 minutes
    refetchInterval: 1000 * 30, // 30 seconds polling
  });
}
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
- **Repository**: [https://github.com/alan2207/bulletproof-react](https://github.com/alan2207/bulletproof-react)
- **Category**: SR24-WEB-DEV Canonical Engineering Skill

## 10. License & Attribution
- **License**: MIT
- **Maintained By**: SR24Plus Autonomous Engineering Architecture
