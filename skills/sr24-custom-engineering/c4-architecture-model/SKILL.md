---
name: c4-architecture-model
description: >-
  Expert in Simon Brown’s C4 architectural modeling (Context, Containers, Components, Code) using PlantUML and Structurizr for rigorous technical specs.
---

# C4 Architecture Modeling & PlantUML Specifications

## 1. When to Activate
Activate this skill whenever a project or prompt requires expert in simon brown’s c4 architectural modeling (context, containers, components, code) using plantuml and structurizr for rigorous technical specs.. It is assigned to official engineering phases in the **SR24Plus Engineering Toolkit**.

## 2. When Not to Activate
- Do not activate when the task does not involve c4-architecture-model.
- Do not activate as a substitute for simple static mockups where deeper engineering is unnecessary.

## 3. Core Capabilities
- System Context Diagrams (Level 1) mapping actors, external APIs, and business systems
- Container Diagrams (Level 2) depicting web apps, APIs, microservices, databases, and message brokers
- Component Diagrams (Level 3) decomposing containers into controllers, services, repositories, and queue consumers
- PlantUML syntax generation with C4-PlantUML standard library styling and icons
- Architecture Decision Record (ADR) synchronization with visual diagrams

## 4. Engineering Workflow
1. **Discovery & Architecture**: Inspect technical constraints, performance requirements, and data contracts.
2. **Setup & Configuration**: Install official package dependencies and configure environment variables.
3. **Implementation**: Author production-grade code using clean architecture, strict TypeScript types, and error handling.
4. **Validation & Testing**: Run unit and integration tests confirming zero regressions.
5. **Production Deployment**: Verify build bundle impact, tree-shaking, and observability telemetry.

## 5. Implementation Instructions & Code Patterns

```typescript
@startuml C4_Elements
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

Person(user, "End User", "Customer using browser or mobile device")
System_Boundary(c1, "SR24Plus SaaS Platform") {
    Container(spa, "Single Page App", "Next.js, React, TypeScript", "Delivers responsive UI, client routing, and state")
    Container(api, "Backend API Gateway", "Node.js, Express/Fastify", "Handles REST endpoints, auth, and business logic")
    ContainerDb(db, "Primary Relational DB", "PostgreSQL", "Stores tenant data, transactions, and users")
    ContainerDb(cache, "Cache & Session Store", "Redis", "Caches hot queries, rate limits, and pub/sub events")
}
System_Ext(payment_gw, "Payment Gateway", "Razorpay / Stripe API")

Rel(user, spa, "Navigates and executes workflows", "HTTPS")
Rel(spa, api, "Invokes GraphQL/REST mutations", "JSON/HTTPS")
Rel(api, db, "Reads and writes transactional data", "TCP/SSL")
Rel(api, cache, "Fetches cached sessions & rate limits", "RESP")
Rel(api, payment_gw, "Creates order sessions & validates webhooks", "HTTPS/HMAC")
@enduml
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
- **Repository**: [https://github.com/plantuml-stdlib/C4-PlantUML](https://github.com/plantuml-stdlib/C4-PlantUML)
- **Category**: SR24-WEB-DEV Canonical Engineering Skill

## 10. License & Attribution
- **License**: MIT
- **Maintained By**: SR24Plus Autonomous Engineering Architecture
