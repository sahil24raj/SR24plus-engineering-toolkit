# WORKFLOW: /sr24-web-dev — COMPLETE WEBSITE & WEB APPLICATION SQUAD

> **Command**: `/sr24-web-dev [task]`  
> **Natural Language Trigger**: `"Build website"`, `"Develop web application"`, `"Create startup web app"`  
> **Mission**: Coordinate a full 10-phase multidisciplinary engineering squad to build a high-performance, professional, production-ready web application from zero to deployment without generic AI-slop.

---

## SQUAD ROSTER & ARCHITECTURE

```
                      ┌───────────────────────────────────────┐
                      │         PROJECT LEAD / PM             │
                      │       agency-product-manager          │
                      └──────────────────┬────────────────────┘
                                         │
         ┌───────────────────────────────┼───────────────────────────────┐
         ▼                               ▼                               ▼
┌──────────────────┐           ┌──────────────────┐           ┌──────────────────┐
│ BRAND & DESIGN   │           │   FULLSTACK ENG  │           │   SECURITY & QA  │
│ - Brand Guardian │           │ - Frontend Dev   │           │ - AppSec Engineer│
│ - UX Architect   │           │ - Senior Dev     │           │ - Test Automator │
│ - UI Designer    │           │ - Backend Arch   │           │ - Reality Checker│
│ - Anti-Slop Gate │           │ - DB Optimizer   │           │ - SRE / DevOps   │
└──────────────────┘           └──────────────────┘           └──────────────────┘
```

---

## 10-PHASE EXECUTION LIFECYCLE

### PHASE 1 — PRODUCT DISCOVERY & PLANNING
- **Assigned Specialists**:
  - `agency-product-manager` (Lead)
  - `agency-design-ux-researcher`
  - `agency-research-synthesist`
  - `agency-product-sprint-prioritizer`
  - `planning-and-task-breakdown`
- **Execution Checklist**:
  1. Inspect existing project repository, codebase, and dependencies before making assumptions.
  2. Clearly define user problem, target persona, and core value proposition.
  3. Analyze competitor landscape and define market differentiation.
  4. Define MVP scope and strict non-goals (prevent feature creep).
  5. Draft functional specifications and acceptance criteria.
- **Mandatory Deliverables**:
  - `PRD.md` (Product Requirements Document)
  - `MVP_SCOPE.md` with explicit feature cutoff and acceptance criteria.

---

### PHASE 2 — BRAND IDENTITY & POSITIONING
- **Assigned Specialists**:
  - `agency-design-brand-guardian` (Lead)
  - `agency-design-visual-storyteller`
  - `agency-design-image-prompt-engineer`
  - `agency-marketing-content-creator`
- **Execution Checklist**:
  1. Establish product tone of voice, personality, and brand positioning.
  2. Select typography pairings (distinctive display heading + clean functional body font).
  3. Define semantic color tokens (Background, Surface, Accent, Border, Text primary/secondary).
  4. Never generate generic purple gradient SaaS themes or generic placeholder identities.
- **Mandatory Deliverables**:
  - `BRAND_GUIDELINES.md` with color hex tokens, typography scale, and tone definitions.

---

### PHASE 3 — UX ARCHITECTURE
- **Assigned Specialists**:
  - `agency-design-ux-architect` (Lead)
  - `agency-design-ux-researcher`
  - `agency-product-manager`
- **Execution Checklist**:
  1. Map complete user journeys from landing to onboarding to core feature usage.
  2. Define information architecture, sitemap, and hierarchy of navigation.
  3. Plan empty states, loading skeletons, error states, and confirmation dialogs.
  4. Ensure accessible contrast, keyboard navigation, and logical tab order.
- **Mandatory Deliverables**:
  - `SITEMAP.md` and user journey flows.
  - Interaction & state specifications for all primary screens.

---

### PHASE 4 — VISUAL DESIGN & ANTI-AI-SLOP GATE
- **Assigned Specialists**:
  - `agency-design-ui-designer` (Lead)
  - `agency-design-ui-finish-gate-reviewer` (Independent Critic)
  - `ui-ux-pro-max`
  - `impeccable`
  - `antislop` / `antislop-ui`
  - `design-taste-frontend`
- **Anti-Slop Enforcement Rules**:
  - ❌ **No generic AI SaaS templates**: No random 3-column floating card features.
  - ❌ **No unmotivated purple/cyan gradients**.
  - ❌ **No gratuitous glassmorphism** that compromises WCAG text readability.
  - ❌ **No emoji-heavy UI** where clean SVG / Lucide icons belong.
  - ❌ **No fake statistics** or decorative graphics without functional meaning.
  - ✅ **Strong typography**: Clear mathematical hierarchy, proper line heights.
  - ✅ **Intentional spacing**: 4px/8px standard layout grid.
  - ✅ **State completeness**: Default, hover, active, focus, disabled, loading.
- **Mandatory Deliverables**:
  - Design audit critique by `agency-design-ui-finish-gate-reviewer`. All identified slop items must be resolved before Phase 5.

---

### PHASE 5 — FRONTEND ENGINEERING
- **Assigned Specialists**:
  - `agency-engineering-frontend-developer` (Lead)
  - `agency-engineering-senior-developer`
  - `agency-engineering-software-architect`
  - `agency-engineering-minimal-change-engineer`
  - `generative_ui`
- **Execution Checklist**:
  1. Detect existing framework (React, Next.js, Vue, Svelte, Vite). Do not force unnecessary rewrites.
  2. Implement modular, single-responsibility components with strict TypeScript types.
  3. Implement responsive layouts (mobile 375px, tablet 768px, desktop 1280px+).
  4. Integrate accessible form validations, loading states, and error toasts.
  5. If 3D elements or animations are required, use Three.js / React Three Fiber / Motion purposefully with reduced-motion support.
- **Mandatory Deliverables**:
  - Clean, compilable source code with 0 TypeScript/bundler errors.

---

### PHASE 6 — BACKEND & DATABASE ARCHITECTURE
- **Assigned Specialists**:
  - `agency-engineering-backend-architect` (Lead)
  - `agency-engineering-database-optimizer`
  - `agency-engineering-database-reliability-engineer`
  - `agency-engineering-identity-access-engineer`
  - `api-and-interface-design`
  - `agency-engineering-data-engineer`
- **Execution Checklist**:
  1. Design normalized relational schema (PostgreSQL/SQLite) or structured document schema with proper indices.
  2. Implement RESTful / tRPC API endpoints with strict request payload validation (e.g. Zod, Pydantic).
  3. Implement secure authentication, session management, and RBAC authorization.
  4. Enforce rate limiting, atomic transactions, and parameterized queries (SQL injection prevention).
- **Mandatory Deliverables**:
  - `SCHEMA.sql` / ORM models.
  - API endpoint contracts and migration scripts.

---

### PHASE 7 — AI INTEGRATION (WHEN REQUIRED)
- **Assigned Specialists**:
  - `agency-engineering-ai-engineer` (Lead)
  - `agency-engineering-prompt-engineer`
  - `agency-engineering-rag-pipeline-engineer`
  - `agency-engineering-ai-data-remediation-engineer`
- **Execution Checklist**:
  1. Integrate LLM / Speech / Vision APIs securely via server-side endpoints (never expose API keys on client).
  2. Implement structured JSON outputs, prompt evaluations, and schema validations.
  3. Configure local offline fallbacks, retry logic with exponential backoff, and latency budgets.
  4. Implement strict cost and token controls.
- **Mandatory Deliverables**:
  - Server-side AI service wrapper with robust error fallback handling.

---

### PHASE 8 — SECURITY ENGINEERING
- **Assigned Specialists**:
  - `agency-security-appsec-engineer` (Lead)
  - `agency-security-architect`
  - `agency-security-ai-generated-code-auditor`
  - `agency-security-cloud-security-architect`
- **Execution Checklist**:
  1. Audit OWASP Top 10 vulnerabilities (SQLi, XSS, CSRF, SSRF, Broken Auth).
  2. Verify CORS configurations, secure cookie flags (`HttpOnly`, `SameSite`, `Secure`).
  3. Scan codebase for hardcoded secrets, tokens, or environment file leaks.
  4. Audit rate limiting and input sanitization on all public endpoints.
- **Mandatory Deliverables**:
  - Security audit log with zero unaddressed High/Critical findings.

---

### PHASE 9 — TESTING & QUALITY ASSURANCE
- **Assigned Specialists**:
  - `agency-engineering-code-reviewer` (Lead)
  - `agency-testing-test-automation-engineer`
  - `browser-testing-with-devtools`
  - `performance-optimization`
  - `agency-testing-reality-checker`
- **Execution Checklist**:
  1. Execute unit and integration tests (`npm test`, `pytest`, etc.).
  2. Run production build check (`npm run build`). Verify zero compiler or bundle errors.
  3. Conduct Core Web Vitals audit (LCP, FID/INP, CLS).
  4. Verify keyboard accessibility and screen reader friendliness.
- **Mandatory Deliverables**:
  - Test runner output log with 100% passing results and verified build output.

---

### PHASE 10 — DEPLOYMENT & PRODUCTION READINESS
- **Assigned Specialists**:
  - `agency-engineering-devops-automator` (Lead)
  - `agency-engineering-sre`
  - `ci-cd-and-automation`
  - `shipping-and-launch`
  - `agency-engineering-technical-writer`
- **Execution Checklist**:
  1. Prepare production containerization (Dockerfile) or serverless deployment config (`vercel.json`, `netlify.toml`).
  2. Document all required environment variables in `.env.example`.
  3. Create CI/CD automated pipeline for build, test, and lint gates.
  4. Generate production release documentation and healthcheck endpoints.
- **Mandatory Deliverables**:
  - Deployment configuration, `.env.example`, and operational runbook.
