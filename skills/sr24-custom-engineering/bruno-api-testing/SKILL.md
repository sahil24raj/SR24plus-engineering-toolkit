---
name: bruno-api-testing
description: >-
  Specialist in Bruno API client — Git-friendly plain-text API collections, automated assertions, environment variable secrets, and CLI test runners.
---

# Bruno Git-Friendly Offline-First API Testing & Automation

## 1. When to Activate
Activate this skill whenever a project or prompt requires specialist in bruno api client — git-friendly plain-text api collections, automated assertions, environment variable secrets, and cli test runners.. It is assigned to official engineering phases in the **SR24Plus Engineering Toolkit**.

## 2. When Not to Activate
- Do not activate when the task does not involve bruno-api-testing.
- Do not activate as a substitute for simple static mockups where deeper engineering is unnecessary.

## 3. Core Capabilities
- Plain-text Bru file format stored directly in repository version control
- Automated pre-request and post-response JavaScript assertion scripting
- Environment variable scoping separating Local, Staging, and Production API secrets
- Bruno CLI (`bru run`) integration for automated API regression testing in CI
- Zero cloud sync requirement guaranteeing API keys never leave local repositories

## 4. Engineering Workflow
1. **Discovery & Architecture**: Inspect technical constraints, performance requirements, and data contracts.
2. **Setup & Configuration**: Install official package dependencies and configure environment variables.
3. **Implementation**: Author production-grade code using clean architecture, strict TypeScript types, and error handling.
4. **Validation & Testing**: Run unit and integration tests confirming zero regressions.
5. **Production Deployment**: Verify build bundle impact, tree-shaking, and observability telemetry.

## 5. Implementation Instructions & Code Patterns

```typescript
// collection/auth/login.bru
meta {
  name: Login User
  type: http
  seq: 1
}

post {
  url: {{baseUrl}}/api/v1/auth/login
  body: json
}

body:json {
  {
    "username": "gamer_champion",
    "password": "{{testUserPassword}}"
  }
}

assert {
  res.status: eq 200
  res.body.success: eq true
  res.body.token: isDefined
}

script:post-response {
  bru.setEnvVar("authToken", res.body.token);
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
- **Repository**: [https://github.com/usebruno/bruno](https://github.com/usebruno/bruno)
- **Category**: SR24-WEB-DEV Canonical Engineering Skill

## 10. License & Attribution
- **License**: MIT
- **Maintained By**: SR24Plus Autonomous Engineering Architecture
