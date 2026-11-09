# MASTER PROFILE 1: FULL-STACK PRODUCTION SAAS & WEB APPLICATIONS
## Dedicated Profile for High-Impact Web Apps (Dukan Sathi, ExamLoop, B2B SaaS)

> **Profile Identity**: Production SaaS & Full-Stack Web Applications  
> **Primary Use Cases**: **Dukan Sathi** (Offline-First Kirana POS, Voice AI Billing, GST Compliance, Udhaar Ledger), **ExamLoop** (AI Computer Adaptive Testing, IRT Models, KaTeX Engine, Proctoring Telemetry), and Commercial Multi-Tenant B2B SaaS Products.  
> **Primary Commands**: `/sr24-saas [project]` or `/sr24-web-dev [project]` or `/sr24-fullstack [feature]`

---

## 1. Unified Architecture & Tech Stack

```
┌────────────────────────────────────────────────────────────────────────┐
│                   CLIENT / FRONTEND LAYER (Browser/PWA)                 │
│  Next.js 14/15 / React 18/19 • TypeScript • Tailwind CSS • Vite        │
│  Anti-Slop Dark Glassmorphic Design • Three.js Interactive 3D Canvas   │
│  State Management (Zustand) • TanStack Query • Lucide Vector Icons     │
└────────────────────────────────────┬───────────────────────────────────┘
                                     │ JSON / REST / WebSockets / SSE
┌────────────────────────────────────▼───────────────────────────────────┐
│                    API GATEWAY & BACKEND ENGINE                        │
│  FastAPI (Python) / Node.js Express / Next.js Server Actions           │
│  Pydantic & Zod Contract Validation • JWT & Session Auth Middleware    │
│  Indian UPI / Razorpay Orders API • PDF & 80mm/58mm Thermal Printing   │
└────────────────────────────────────┬───────────────────────────────────┘
                                     │ High-Speed Data Layer
┌────────────────────────────────────▼───────────────────────────────────┐
│                 STORAGE & DATABASE RESILIENCE LAYER                    │
│  Client Local: IndexedDB / SQLite WASM (100% Offline-First Store)      │
│  Server Cloud: PostgreSQL / Supabase / SQLite with Composite Indexes   │
│  Background Sync: FIFO Sync Queue with Deterministic Conflict Handler  │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Integrated Specialist Squad & Upstream GitHub Sources

| Engineering Phase | Specialist Role | Skill Name | Upstream GitHub Repository | Key Responsibility |
|---|---|---|---|---|
| **Phase 1: Architecture** | SaaS & System Architect | `agency-engineering-software-architect` + `saas-architect` | [`msitarzewski/agency-agents`](https://github.com/msitarzewski/agency-agents) | Multi-tenant isolation, modular monolith / microservices boundary design |
| **Phase 2: Anti-Slop UI** | UI Critique & Design System | `impeccable` + `antislop-ui` + `ui-ux-pro-max` | [`pbakaus/impeccable`](https://github.com/pbakaus/impeccable) & [`miqdadbadjuber/anti-slop`](https://github.com/miqdadbadjuber/anti-slop) | Strips AI generic templates, enforces 4px/8px rhythm, WCAG AA contrast, and dark glass elegance |
| **Phase 3: Frontend** | Modern Web Engineer | `agency-engineering-frontend-developer` + `agency-engineering-senior-developer` | [`msitarzewski/agency-agents`](https://github.com/msitarzewski/agency-agents) | Component hierarchy, responsive layouts, interactive 3D background integration |
| **Phase 4: Backend API** | High-Throughput API Lead | `agency-engineering-backend-architect` + `api-and-interface-design` | [`msitarzewski/agency-agents`](https://github.com/msitarzewski/agency-agents) & [`addyosmani/agent-skills`](https://github.com/addyosmani/agent-skills) | RESTful / gRPC route design, input validation schemas, rate limiting |
| **Phase 5: Offline Store** | Offline-First POS Lead | `offline-first-kirana-architect` | `SR24Plus Custom Engineering` | IndexedDB / SQLite WASM local storage, background sync, zero internet dropouts |
| **Phase 6: Database** | SQL Query Tuning Lead | `agency-engineering-database-optimizer` | [`msitarzewski/agency-agents`](https://github.com/msitarzewski/agency-agents) | Query indexing, schema normalization, EXPLAIN ANALYZE bottleneck elimination |
| **Phase 7: Fintech & Tax** | UPI & GST Billing Lead | `razorpay-upi-specialist` + `indian-gst-billing-engineer` | `SR24Plus Custom Engineering` | Dynamic UPI QR codes (`upi://pay`), Razorpay HMAC webhooks, CGST/SGST/IGST tax math, thermal slips |
| **Phase 8: Assessment Engine**| Adaptive Testing Lead | `assessment-engine-architect` + `agency-academic-statistician` | `SR24Plus Custom Engineering` & [`msitarzewski/agency-agents`](https://github.com/msitarzewski/agency-agents) | Item Response Theory (1PL Rasch model), Computer Adaptive Testing (CAT), KaTeX equations (used in ExamLoop) |
| **Phase 9: AppSec & Safety**| Security Auditor | `agency-security-appsec-engineer` + `prompt-injection-security-engineer` | [`msitarzewski/agency-agents`](https://github.com/msitarzewski/agency-agents) & `SR24Plus Custom Engineering` | OWASP Top 10 defense, parameterized queries, LLM prompt boundary firewalls |
| **Phase 10: Testing & QA** | E2E Automation Lead | `playwright-automation-engineer` + `test-driven-development` | `SR24Plus Custom Engineering` & [`addyosmani/agent-skills`](https://github.com/addyosmani/agent-skills) | Zero-flake Playwright browser tests, API integration tests, CI test evidence |
| **Phase 11: Deployment** | DevOps & CI/CD Lead | `agency-engineering-devops-automator` + `ci-cd-and-automation` | [`msitarzewski/agency-agents`](https://github.com/msitarzewski/agency-agents) & [`addyosmani/agent-skills`](https://github.com/addyosmani/agent-skills) | Docker multi-stage builds, GitHub Actions pipelines, healthchecks, rollback scripts |
| **Phase 12: Growth & SEO** | Programmatic Growth Lead | `programmatic-seo-engineer` + `product-hunt-launch-specialist` | `SR24Plus Custom Engineering` | Next.js ISR programmatic landing pages, JSON-LD schema markup, Product Hunt launch playbook |

---

## 3. How to Activate This Profile (Prompts & Commands)

### Primary Command:
```text
/sr24-saas [project name or feature specification]
```

### Copy-Paste Prompt for AI in Chat:
> *"Act as the SR24Plus Principal SaaS Architect & Full-Stack Squad. I am building [ExamLoop / Dukan Sathi / B2B SaaS Platform]. Execute the 12-phase production lifecycle: design a modular multi-tenant architecture, enforce the Anti-AI-Slop visual standard with dark glassmorphic styling, set up deterministic offline-first sync (or adaptive testing models), implement secure payment/billing workflows, audit security with OWASP Top 10, and deliver verified Playwright E2E tests with `npm run build` evidence."*
