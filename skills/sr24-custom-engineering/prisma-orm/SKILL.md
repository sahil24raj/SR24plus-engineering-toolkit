---
name: prisma-orm
description: >-
  Specialist in Prisma ORM schema authoring, migration pipelines, relational query optimization, client extensions, connection pooling, and multi-tenant scoping.
---

# Prisma ORM Modeling, Migrations & Query Optimization

## 1. When to Activate
Activate this skill whenever a project or prompt requires specialist in prisma orm schema authoring, migration pipelines, relational query optimization, client extensions, connection pooling, and multi-tenant scoping.. It is assigned to official engineering phases in the **SR24Plus Engineering Toolkit**.

## 2. When Not to Activate
- Do not activate when the task does not involve prisma-orm.
- Do not activate as a substitute for simple static mockups where deeper engineering is unnecessary.

## 3. Core Capabilities
- Declarative `schema.prisma` modeling with relations, enums, indexes, and unique constraints
- Migration management (`prisma migrate dev/deploy`) ensuring zero data loss across deployments
- N+1 query elimination using explicit `include` and `select` query projection
- Prisma Client extensions ($extends) for soft-deletes, multi-tenant row filtering, and audit logging
- Connection pool tuning for serverless functions (Prisma Accelerate / pgBouncer)

## 4. Engineering Workflow
1. **Discovery & Architecture**: Inspect technical constraints, performance requirements, and data contracts.
2. **Setup & Configuration**: Install official package dependencies and configure environment variables.
3. **Implementation**: Author production-grade code using clean architecture, strict TypeScript types, and error handling.
4. **Validation & Testing**: Run unit and integration tests confirming zero regressions.
5. **Production Deployment**: Verify build bundle impact, tree-shaking, and observability telemetry.

## 5. Implementation Instructions & Code Patterns

```typescript
// schema.prisma
datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}

generator client {
  provider = "prisma-client-js"
}

model GameRoom {
  id          String       @id @default(uuid())
  code        String       @unique @db.VarChar(6)
  gameSlug    String
  status      RoomStatus   @default(WAITING)
  maxPlayers  Int          @default(4)
  createdAt   DateTime     @default(now())
  updatedAt   DateTime     @updatedAt
  players     RoomPlayer[]

  @@index([status, gameSlug])
}

enum RoomStatus {
  WAITING
  IN_PROGRESS
  FINISHED
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
- **Repository**: [https://github.com/prisma/prisma](https://github.com/prisma/prisma)
- **Category**: SR24-WEB-DEV Canonical Engineering Skill

## 10. License & Attribution
- **License**: Apache-2.0
- **Maintained By**: SR24Plus Autonomous Engineering Architecture
