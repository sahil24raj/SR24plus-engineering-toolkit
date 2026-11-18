---
name: dbml-schema-design
description: >-
  Specialist in Database Markup Language (DBML) for readable database design, entity relationship visualization, automated SQL DDL export, and team documentation.
---

# DBML Visual Database Modeling & Documentation

## 1. When to Activate
Activate this skill whenever a project or prompt requires specialist in database markup language (dbml) for readable database design, entity relationship visualization, automated sql ddl export, and team documentation.. It is assigned to official engineering phases in the **SR24Plus Engineering Toolkit**.

## 2. When Not to Activate
- Do not activate when the task does not involve dbml-schema-design.
- Do not activate as a substitute for simple static mockups where deeper engineering is unnecessary.

## 3. Core Capabilities
- Clean DBML schema syntax defining tables, columns, constraints, and relational cardinality
- Bi-directional conversion between DBML, PostgreSQL DDL, MySQL, and Prisma schemas
- Visual Entity-Relationship Diagram (ERD) generation for architecture specifications
- Table indexing and composite key documentation with explicit business rationale
- Schema changelog tracking for team reviews before executing migration scripts

## 4. Engineering Workflow
1. **Discovery & Architecture**: Inspect technical constraints, performance requirements, and data contracts.
2. **Setup & Configuration**: Install official package dependencies and configure environment variables.
3. **Implementation**: Author production-grade code using clean architecture, strict TypeScript types, and error handling.
4. **Validation & Testing**: Run unit and integration tests confirming zero regressions.
5. **Production Deployment**: Verify build bundle impact, tree-shaking, and observability telemetry.

## 5. Implementation Instructions & Code Patterns

```typescript
// schema.dbml
Project gullyverse_gaming_platform {
  database_type: 'PostgreSQL'
  Note: 'Desi Browser Gaming Universe Database Schema'
}

Table users {
  id varchar(36) [pk]
  username varchar(32) [unique, not null]
  coins integer [default: 500]
  xp integer [default: 0]
  level integer [default: 1]
  created_at timestamp [default: `now()`]
}

Table game_matches {
  id varchar(36) [pk]
  game_slug varchar(64) [not null]
  winner_id varchar(36) [ref: > users.id]
  score integer [not null]
  duration_seconds integer
  created_at timestamp [default: `now()`]
}

Table match_participants {
  id varchar(36) [pk]
  match_id varchar(36) [ref: > game_matches.id]
  user_id varchar(36) [ref: > users.id]
  final_rank integer
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
- **Repository**: [https://github.com/holistics/dbml](https://github.com/holistics/dbml)
- **Category**: SR24-WEB-DEV Canonical Engineering Skill

## 10. License & Attribution
- **License**: Apache-2.0
- **Maintained By**: SR24Plus Autonomous Engineering Architecture
