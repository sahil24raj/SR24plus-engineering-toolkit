---
name: react-testing-library
description: >-
  Specialist in testing-library/react for testing components as real users interact with them — accessible queries, user-event, async element assertions, and mock providers.
---

# React Testing Library Component & Interaction Testing

## 1. When to Activate
Activate this skill whenever a project or prompt requires specialist in testing-library/react for testing components as real users interact with them — accessible queries, user-event, async element assertions, and mock providers.. It is assigned to official engineering phases in the **SR24Plus Engineering Toolkit**.

## 2. When Not to Activate
- Do not activate when the task does not involve react-testing-library.
- Do not activate as a substitute for simple static mockups where deeper engineering is unnecessary.

## 3. Core Capabilities
- Accessible DOM queries prioritizing `getByRole`, `getByLabelText`, and `getByText`
- User-event simulation reproducing actual click, type, blur, and keyboard interactions
- Async assertion handling with `waitFor` and `findByRole` preventing flaky timer tests
- Test wrapper architecture wrapping components with QueryClient, Zustand, and Theme providers
- Coverage analysis measuring branch, function, and line coverage without testing implementation details

## 4. Engineering Workflow
1. **Discovery & Architecture**: Inspect technical constraints, performance requirements, and data contracts.
2. **Setup & Configuration**: Install official package dependencies and configure environment variables.
3. **Implementation**: Author production-grade code using clean architecture, strict TypeScript types, and error handling.
4. **Validation & Testing**: Run unit and integration tests confirming zero regressions.
5. **Production Deployment**: Verify build bundle impact, tree-shaking, and observability telemetry.

## 5. Implementation Instructions & Code Patterns

```typescript
import React from 'react';
import { render, screen, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { QuickMatchButton } from './QuickMatchButton';

describe('QuickMatchButton Component', () => {
  it('triggers matchmaking and enters waiting state on click', async () => {
    const user = userEvent.setup();
    const handleJoin = jest.fn();

    render(<QuickMatchButton onJoin={handleJoin} isSearching={false} />);

    const button = screen.getByRole('button', { name: /quick match/i });
    expect(button).toBeEnabled();

    await user.click(button);
    expect(handleJoin).toHaveBeenCalledTimes(1);
  });

  it('displays searching spinner and disables button when isSearching is true', () => {
    render(<QuickMatchButton onJoin={jest.fn()} isSearching={true} />);

    const button = screen.getByRole('button', { name: /finding opponent/i });
    expect(button).toBeDisabled();
    expect(screen.getByTestId('search-spinner')).toBeInTheDocument();
  });
});
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
- **Repository**: [https://github.com/testing-library/react-testing-library](https://github.com/testing-library/react-testing-library)
- **Category**: SR24-WEB-DEV Canonical Engineering Skill

## 10. License & Attribution
- **License**: MIT
- **Maintained By**: SR24Plus Autonomous Engineering Architecture
