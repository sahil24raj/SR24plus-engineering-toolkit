# WORKFLOW: /sr24-saas — COMPLETE SAAS PRODUCT & PLATFORM SQUAD

> **Command**: `/sr24-saas [task]`  
> **Natural Language Trigger**: `"Build SaaS"`, `"Create SaaS MVP"`, `"Launch software subscription product"`  
> **Mission**: Orchestrate a multi-disciplinary startup squad to build, harden, and launch a commercial SaaS application with multi-tenancy, billing, authentication, and enterprise-grade reliability.

---

## SAAS SPECIALIST SQUAD

| Role | Primary Skill Assigned | Responsibilities |
|---|---|---|
| **Product & Monetization** | `agency-product-manager` + `agency-product-sprint-prioritizer` | PRD, tier pricing model, churn reduction, feature roadmaps |
| **Brand & Positioning** | `agency-design-brand-guardian` | High-trust enterprise identity, typography, professional design language |
| **UX & App Flow** | `agency-design-ux-architect` | Multi-tenant dashboards, customer onboarding, self-serve settings |
| **UI & Anti-Slop Gate** | `agency-design-ui-designer` + `ui-ux-pro-max` + `antislop-ui` | High-density data tables, filters, charts, zero generic AI slop |
| **Frontend Architecture** | `agency-engineering-frontend-developer` + `agency-engineering-senior-developer` | React/Next.js/Vue, SSR/SSG, optimistic UI, caching, responsive HUD |
| **Backend & Multi-Tenancy** | `agency-engineering-backend-architect` + `agency-engineering-database-optimizer` | Tenant isolation, PostgreSQL RLS, scalable APIs, background jobs |
| **Auth & Billing** | `agency-engineering-identity-access-engineer` + `agency-engineering-payments-billing-engineer` | OAuth2/OIDC, Stripe/Razorpay webhooks, subscription lifecycle, RBAC |
| **Security & Compliance** | `agency-security-appsec-engineer` + `agency-support-legal-compliance-checker` | SOC 2 / GDPR readiness, API rate limiting, audit logging |
| **QA & Reliability** | `agency-engineering-code-reviewer` + `agency-testing-test-automation-engineer` | Integration tests, billing test clocks, regression coverage |
| **SRE & Production Cloud** | `agency-engineering-devops-automator` + `agency-engineering-sre` | Multi-region deployment, zero-downtime migrations, APM monitoring |

---

## 8-STAGE SAAS EXECUTION PIPELINE

1. **Stage 1: SaaS Strategy & Pricing Model**:
   - Define subscription tiers (Free, Pro, Enterprise), seat-based or usage-based quotas.
   - Establish strict MVP scope and onboarding activation metrics.
2. **Stage 2: Enterprise Identity & Brand System**:
   - Establish trust-inducing visual aesthetics: neutral slates, precise borders, deliberate accents.
   - Avoid generic brightly colored cartoon templates; focus on operational clarity.
3. **Stage 3: Information Architecture & Dashboard UX**:
   - Design tenant workspace navigation, team settings, user invitations, and billing portals.
   - Implement empty states with actionable "First Success" onboarding cards.
4. **Stage 4: Multi-Tenant Database & API Design**:
   - Implement database schema with strict `tenant_id` foreign keys and Row Level Security (RLS).
   - Design idempotency keys for billing and critical mutation endpoints.
5. **Stage 5: High-Density UI & Frontend Engineering**:
   - Build virtualized data tables, faceted filters, real-time status indicators, and keyboard shortcuts.
   - Run Anti-Slop visual gate to ensure zero generic styling.
6. **Stage 6: Payments & Subscription Lifecycle**:
   - Implement webhook listener with signature verification for `invoice.paid`, `customer.subscription.deleted`.
   - Build graceful downgrade and grace-period warning flows.
7. **Stage 7: Security & Multi-Tenant Audit**:
   - Test tenant data isolation: verify Tenant A cannot query Tenant B's data under any parameter tampering.
   - Audit rate limits on authentication, password resets, and high-frequency webhook endpoints.
8. **Stage 8: CI/CD & Production Launch**:
   - Automate database migrations in pre-deploy hooks.
   - Setup health checks, error tracking (Sentry), and uptime alerting.
