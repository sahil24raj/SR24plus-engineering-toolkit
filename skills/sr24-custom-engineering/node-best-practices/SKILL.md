---
name: node-best-practices
description: >-
  Specialist in Goldberger’s Node.js best practices — robust error handling, unhandled rejection capture, async process termination, security headers, and clean layering.
---

# Node.js Production Architecture & Security Practices

## 1. When to Activate
Activate this skill whenever a project or prompt requires specialist in goldberger’s node.js best practices — robust error handling, unhandled rejection capture, async process termination, security headers, and clean layering.. It is assigned to official engineering phases in the **SR24Plus Engineering Toolkit**.

## 2. When Not to Activate
- Do not activate when the task does not involve node-best-practices.
- Do not activate as a substitute for simple static mockups where deeper engineering is unnecessary.

## 3. Core Capabilities
- Centralized error handling architecture distinguishing operational errors from programming bugs
- Graceful process shutdown on SIGINT/SIGTERM closing open DB pools and active HTTP connections
- Security hardening (Helmet, CORS whitelist, rate limiting, parameter pollution protection)
- Layered architecture separating Controllers, Domain Services, Data Access Objects (DAO), and DTOs
- Production logging with structured JSON output (Pino/Winston) and correlation request IDs

## 4. Engineering Workflow
1. **Discovery & Architecture**: Inspect technical constraints, performance requirements, and data contracts.
2. **Setup & Configuration**: Install official package dependencies and configure environment variables.
3. **Implementation**: Author production-grade code using clean architecture, strict TypeScript types, and error handling.
4. **Validation & Testing**: Run unit and integration tests confirming zero regressions.
5. **Production Deployment**: Verify build bundle impact, tree-shaking, and observability telemetry.

## 5. Implementation Instructions & Code Patterns

```typescript
import express, { Request, Response, NextFunction } from 'express';
import helmet from 'helmet';
import cors from 'cors';

export class AppError extends Error {
  constructor(
    public override message: string,
    public statusCode: number = 500,
    public isOperational: boolean = true
  ) {
    super(message);
    Error.captureStackTrace(this, this.constructor);
  }
}

export const app = express();
app.use(helmet());
app.use(cors({ origin: process.env.ALLOWED_ORIGINS?.split(',') || false }));
app.use(express.json({ limit: '1mb' }));

// Global Error Handling Middleware
app.use((err: Error, req: Request, res: Response, _next: NextFunction) => {
  const isAppError = err instanceof AppError;
  const status = isAppError ? err.statusCode : 500;
  const message = isAppError && err.isOperational ? err.message : 'Internal Server Error';

  console.error('[Error Occurred]', {
    message: err.message,
    stack: err.stack,
    path: req.path,
    method: req.method,
  });

  res.status(status).json({ success: false, error: message });
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
- **Repository**: [https://github.com/goldbergyoni/nodebestpractices](https://github.com/goldbergyoni/nodebestpractices)
- **Category**: SR24-WEB-DEV Canonical Engineering Skill

## 10. License & Attribution
- **License**: MIT
- **Maintained By**: SR24Plus Autonomous Engineering Architecture
