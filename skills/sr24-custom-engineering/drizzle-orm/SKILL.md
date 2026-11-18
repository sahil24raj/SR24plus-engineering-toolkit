---
name: drizzle-orm
description: >-
  Specialist in Drizzle ORM — zero-overhead type-safe SQL queries, schema declaration in TypeScript, migration generation, and Edge/Serverless compatibility.
---

# Drizzle ORM Type-Safe SQL & Serverless Architecture

## 1. When to Activate
Activate this skill whenever a project or prompt requires specialist in drizzle orm — zero-overhead type-safe sql queries, schema declaration in typescript, migration generation, and edge/serverless compatibility.. It is assigned to official engineering phases in the **SR24Plus Engineering Toolkit**.

## 2. When Not to Activate
- Do not activate when the task does not involve drizzle-orm.
- Do not activate as a substitute for simple static mockups where deeper engineering is unnecessary.

## 3. Core Capabilities
- Type-safe relational queries mirroring raw SQL efficiency without code-generation overhead
- Schema definition in pure TypeScript (`pgTable`, `varchar`, `integer`, `timestamp`)
- Automatic type inference (`InferSelectModel`, `InferInsertModel`) for API validation
- Drizzle Kit automated migration generation and interactive Drizzle Studio inspection
- Ultra-low cold-start latency for Cloudflare Workers, Vercel Edge, and AWS Lambda

## 4. Engineering Workflow
1. **Discovery & Architecture**: Inspect technical constraints, performance requirements, and data contracts.
2. **Setup & Configuration**: Install official package dependencies and configure environment variables.
3. **Implementation**: Author production-grade code using clean architecture, strict TypeScript types, and error handling.
4. **Validation & Testing**: Run unit and integration tests confirming zero regressions.
5. **Production Deployment**: Verify build bundle impact, tree-shaking, and observability telemetry.

## 5. Implementation Instructions & Code Patterns

```typescript
import { pgTable, text, integer, timestamp, varchar } from 'drizzle-orm/pg-core';
import { drizzle } from 'drizzle-orm/node-postgres';
import { Pool } from 'pg';

export const users = pgTable('users', {
  id: varchar('id', { length: 36 }).primaryKey(),
  username: varchar('username', { length: 32 }).notNull().unique(),
  coins: integer('coins').default(500).notNull(),
  level: integer('level').default(1).notNull(),
  createdAt: timestamp('created_at').defaultNow().notNull(),
});

export type User = typeof users.$inferSelect;
export type NewUser = typeof users.$inferInsert;

const pool = new Pool({ connectionString: process.env.DATABASE_URL });
export const db = drizzle(pool);
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
- **Repository**: [https://github.com/drizzle-team/drizzle-orm](https://github.com/drizzle-team/drizzle-orm)
- **Category**: SR24-WEB-DEV Canonical Engineering Skill

## 10. License & Attribution
- **License**: Apache-2.0
- **Maintained By**: SR24Plus Autonomous Engineering Architecture
