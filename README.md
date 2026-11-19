<p align="center">
  <img src="./assets/sr24plus-banner.jpg" alt="SR24Plus Engineering Toolkit Banner" width="100%" />
</p>

# SR24Plus Engineering Toolkit
### Build Smarter. Engineer Better. Ship Production-Ready.

[![Canonical Skills](https://img.shields.io/badge/Canonical%20Skills-479%20In--Repo-0f172a.svg?style=for-the-badge&logo=codeforces&logoColor=38bdf8)](./SKILL-REGISTRY.md)
[![Master Commands](https://img.shields.io/badge/Master%20Commands-14%20Workflows-0f172a.svg?style=for-the-badge&logo=powershell&logoColor=f59e0b)](./docs/SR24PLUS-MASTER-COMMANDS.md)
[![Core Intelligence](https://img.shields.io/badge/Core%20Intelligence-Autonomous%20Loop-0f172a.svg?style=for-the-badge&logo=probot&logoColor=10b981)](./docs/SR24PLUS-CORE-INTELLIGENCE.md)
[![Upstream Sources](https://img.shields.io/badge/Upstream%20Sources-66%20Verified%20Repos-0f172a.svg?style=for-the-badge&logo=github&logoColor=white)](./registry/SR24PLUS-UPSTREAM-SOURCES.md)
[![Verified Coverage](https://img.shields.io/badge/Lifecycle%20Coverage-10.0%20%2F%2010-0f172a.svg?style=for-the-badge&logo=checkmarx&logoColor=fbbf24)](#4-flagship-engineering-packs)
[![License](https://img.shields.io/badge/License-MIT%20%7C%20Apache--2.0-0f172a.svg?style=for-the-badge&logo=opensourceinitiative&logoColor=cbd5e1)](#12-license--legal-attribution)

---

## Executive Overview

The **SR24Plus Engineering Toolkit** is a modular, AI-assisted software engineering ecosystem designed to streamline full-stack web development, game development, quality engineering, production auditing, and autonomous debugging through specialized skills and intelligent multi-agent orchestration.

Traditional AI coding assistants often produce generic templates ("AI slop")—unmotivated purple gradients, brittle copy-pasted UI, missing database indexes, unhardened endpoints, and jittery browser game loops. SR24Plus eliminates these defects by deploying **479 canonical production skills** across a disciplined multi-agent squad structure governed by strict engineering contracts, upstream open-source methodologies, and automated quality gates.

```
                                 USER TASK OR GOAL
                                         │
                                         ▼
                            SR24 INTELLIGENCE ENGINE
               (Static Codebase Scan • Stack Detection • 12 Archetypes)
                                         │
                                         ▼
                            MULTI-AGENT ORCHESTRATION
                         ┌───────────────┴───────────────┐
                         ▼                               ▼
                 SR24-WEB-DEV                     SR24-GAME-DEV
              (12-Phase SaaS Squad)            (12-Phase Game Squad)
                         │                               │
                         └───────────────┬───────────────┘
                                         │
                                         ▼
                             SR24 PRODUCTION AUDITOR
                   (8-Dimension Forensic Readiness Inspection)
                                         │
                                         ▼
                           SR24 SELF-HEALING ENGINEER
                 (Detect ➔ Diagnose ➔ Plan ➔ Repair ➔ Test ➔ Verify)
                                         │
                                         ▼
                                PRODUCTION RELEASE
                 (Multi-Stage Docker • CI/CD • Verified Delivery)
```

---

## Master Documentation Portal

| Manual / Specification | Operational Focus & Highlights |
|---|---|
| [**`docs/SR24PLUS-MASTER-COMMANDS.md`**](./docs/SR24PLUS-MASTER-COMMANDS.md) | **14 Master Workflow Commands** — Comprehensive CLI syntax, options, mobilized skills, and upstream repositories. |
| [**`docs/SR24PLUS-CORE-INTELLIGENCE.md`**](./docs/SR24PLUS-CORE-INTELLIGENCE.md) | **Core Intelligence Layer Manual** — Intelligence Engine, 8-dimension Auditor, and 6-step Self-Healing loop. |
| [**`docs/README-SR24-WEB-DEV.md`**](./docs/README-SR24-WEB-DEV.md) | **Web & SaaS Pack (58 Skills)** — 12-phase lifecycle, PRD specs, Anti-Slop UI, React 18/Next.js, Drizzle, Lago. |
| [**`docs/README-SR24-GAME-DEV.md`**](./docs/README-SR24-GAME-DEV.md) | **Game Dev Pack (52 Skills)** — 12-phase lifecycle, Rapier physics, Three.js/R3F, Colyseus 60Hz, truck physics. |
| [**`registry/SR24PLUS-UPSTREAM-SOURCES.md`**](./registry/SR24PLUS-UPSTREAM-SOURCES.md) | **Central Upstream Source Registry** — 66+ verified open-source repositories, canonical authors, and licenses. |
| [**`docs/SR24PLUS-SOURCE-ATTRIBUTION.md`**](./docs/SR24PLUS-SOURCE-ATTRIBUTION.md) | **Upstream Attribution Directory** — Comprehensive attribution matrix across Categories A–J with verified links. |
| [**`docs/SR24PLUS-SKILL-PROVENANCE.md`**](./docs/SR24PLUS-SKILL-PROVENANCE.md) | **Unified Skill Provenance Matrix** — Complete lineage, upstream origins, and integration status for all 479 skills. |
| [**`docs/SR24PLUS-GITHUB-LINK-VALIDATION.md`**](./docs/SR24PLUS-GITHUB-LINK-VALIDATION.md) | **Global Hyperlink Validation Report** — Automated link integrity verification across 650+ active repository links. |
| [**`docs/SR24PLUS-ROOT-README-LINK-AUDIT.md`**](./docs/SR24PLUS-ROOT-README-LINK-AUDIT.md) | **Root README Link Audit** — Forensic audit confirming 100% clickable upstream repository and skill links. |
| [**`docs/SR24PLUS-TECH-STACK.md`**](./docs/SR24PLUS-TECH-STACK.md) | **Technology Ecosystem** — Detailed tiers of supported web, game, AI, database, and DevOps technologies. |
| [**`docs/SR24PLUS-README-AUDIT.md`**](./docs/SR24PLUS-README-AUDIT.md) | **Forensic Repository Audit** — Complete audit of existing commands, packs, phases, and baseline architecture. |
| [**`SKILL-REGISTRY.md`**](./SKILL-REGISTRY.md) | **Master Skill Registry** — Exhaustive manifest of 479 production skills with directory paths and licenses. |
| [**`SKILL-INDEX.md`**](./SKILL-INDEX.md) | **Alphabetical Jump Index** — Fast alphabetical index of all 479 canonical skills. |

---

## 1. Master Command Center

The toolkit provides **14 Primary Workflow Commands**, each backed by an executable runbook in `00-MASTER-CONTROLLER/workflows/`:

| No. | Master Command | Category | What It Does | Skills / Upstream Repositories | Target Runbook |
|:---:|---|---|---|---|:---:|
| **01** | `/sr24-auto [task]` | Orchestration | Automatically scans workspace, detects tech stack, and selects the matching squad. | `sr24-intelligence-engine`, `sr24-production-auditor` ([agency-agents](https://github.com/msitarzewski/agency-agents), [agent-skills](https://github.com/addyosmani/agent-skills), [SR24plus-engineering-toolkit](https://github.com/sahil24raj/SR24plus-engineering-toolkit/tree/main/skills/sr24-custom-engineering)) | [`SR24-AUTO.md`](./00-MASTER-CONTROLLER/workflows/SR24-AUTO.md) |
| **02** | `/sr24-web-dev [task]` | Web Development | Executes the complete 12-phase web application lifecycle from PRD to production deploy. | `bulletproof-react`, `drizzle-orm`, `supabase-engineering` ([bulletproof-react](https://github.com/alan2207/bulletproof-react), [agent-skills](https://github.com/vercel-labs/agent-skills), [drizzle-orm](https://github.com/drizzle-team/drizzle-orm), [agent-skills](https://github.com/addyosmani/agent-skills)) | [`README-SR24-WEB-DEV.md`](./docs/README-SR24-WEB-DEV.md) |
| **03** | `/sr24-game-dev [task]` | Game Development | End-to-end 12-phase game development across WebGL 2D/3D, Rapier physics, and Unity 3D. | `rapier-physics`, `colyseus-multiplayer`, `threejs-game-engine` ([three.js](https://github.com/mrdoob/three.js), [rapier](https://github.com/dimforge/rapier), [colyseus](https://github.com/colyseus/colyseus)) | [`README-SR24-GAME-DEV.md`](./docs/README-SR24-GAME-DEV.md) |
| **04** | `/sr24-saas [task]` | SaaS Engineering | Multi-tenant SaaS platform, subscription billing, multi-tier auth, dashboard HUD, SRE. | `razorpay-upi-specialist`, `indian-gst-billing-engineer`, `lago-billing` ([lago](https://github.com/getlago/lago), [prisma](https://github.com/prisma/prisma), [SR24plus-engineering-toolkit](https://github.com/sahil24raj/SR24plus-engineering-toolkit/tree/main/skills/sr24-custom-engineering)) | [`SR24-SAAS.md`](./00-MASTER-CONTROLLER/workflows/SR24-SAAS.md) |
| **05** | `/sr24-fullstack [task]` | Fullstack Engineering | TypeScript contracts, database migrations, REST/tRPC API endpoints, responsive UI. | `zod-schema-validation`, `drizzle-orm`, `node-best-practices` ([zod](https://github.com/colinhacks/zod), [drizzle-orm](https://github.com/drizzle-team/drizzle-orm), [nodebestpractices](https://github.com/goldbergyoni/nodebestpractices)) | [`SR24-FULLSTACK.md`](./00-MASTER-CONTROLLER/workflows/SR24-FULLSTACK.md) |
| **06** | `/sr24-browser-game [task]` | Browser Gaming | 60 FPS HTML5/WebGL browser games, fixed-timestep loop, mobile virtual joypads, game feel. | `browser-game-architect`, `threejs-game-engine`, `matter-js-physics` ([three.js](https://github.com/mrdoob/three.js), [matter-js](https://github.com/liabru/matter-js), [howler.js](https://github.com/goldfire/howler.js)) | [`SR24-BROWSER-GAME.md`](./00-MASTER-CONTROLLER/workflows/SR24-BROWSER-GAME.md) |
| **07** | `/sr24-multiplayer [task]` | Multiplayer Systems | Low-latency authoritative game servers, client prediction, reconciliation, room codes. | `colyseus-multiplayer`, `socketio-realtime`, `redis-in-memory-datastore` ([colyseus](https://github.com/colyseus/colyseus), [socket.io](https://github.com/socketio/socket.io), [redis](https://github.com/redis/redis)) | [`SR24-MULTIPLAYER.md`](./00-MASTER-CONTROLLER/workflows/SR24-MULTIPLAYER.md) |
| **08** | `/sr24-unity [task]` | Native 3D Engine | Unity 2D/3D development, ScriptableObjects, URP shaders, audio mixers, headless builds. | `unity-cli`, `urp-postprocessing`, `initialize-ai-navigation` ([com.unity.entities](https://github.com/Unity-Technologies/com.unity.entities), [agency-agents](https://github.com/msitarzewski/agency-agents)) | [`SR24-UNITY.md`](./00-MASTER-CONTROLLER/workflows/SR24-UNITY.md) |
| **09** | `/sr24-racing-game [task]` | Vehicle Simulation | Heavy truck & vehicle physics, WheelColliders, Ackermann steering, banked hairpin circuits. | `truck-physics-engineer`, `realistic-car-controller-engineer` ([SR24plus-engineering-toolkit](https://github.com/sahil24raj/SR24plus-engineering-toolkit/tree/main/skills/sr24-custom-engineering), [com.unity.entities](https://github.com/Unity-Technologies/com.unity.entities)) | [`SR24-RACING-GAME.md`](./00-MASTER-CONTROLLER/workflows/SR24-RACING-GAME.md) |
| **10** | `/sr24-ai [task]` | AI & Agent Systems | Production AI systems, MCP servers, prompt injection defense, hybrid RAG vector indexes. | `prompt-injection-security-engineer`, `agency-specialized-mcp-builder` ([agency-agents](https://github.com/msitarzewski/agency-agents), [SR24plus-engineering-toolkit](https://github.com/sahil24raj/SR24plus-engineering-toolkit/tree/main/skills/sr24-custom-engineering)) | [`SR24-AI.md`](./00-MASTER-CONTROLLER/workflows/SR24-AI.md) |
| **11** | `/sr24-design [task]` | UI/UX & Design Systems | Bespoke design system, 4px/8px tokens, anti-AI-slop audit, finish-gate critique. | `impeccable`, `antislop-ui`, `taste-skill`, `ui-ux-pro-max` ([impeccable](https://github.com/pbakaus/impeccable), [anti-slop](https://github.com/miqdadbadjuber/anti-slop), [taste-skill](https://github.com/Leonxlnx/taste-skill), [ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)) | [`SR24-DESIGN.md`](./00-MASTER-CONTROLLER/workflows/SR24-DESIGN.md) |
| **12** | `/sr24-security [task]` | Security & Hardening | AppSec, OWASP Top 10 hardening, secret scanning, dependency CVE audits, CSP/CORS. | `owasp-zap-scanner`, `gitleaks-secret-detection`, `trivy-security-scanner` ([zaproxy](https://github.com/zaproxy/zaproxy), [gitleaks](https://github.com/gitleaks/gitleaks), [trivy](https://github.com/aquasecurity/trivy), [osv-scanner](https://github.com/google/osv-scanner)) | [`SR24-SECURITY.md`](./00-MASTER-CONTROLLER/workflows/SR24-SECURITY.md) |
| **13** | `/sr24-research [task]` | Evidence & Research | Literature search, market sizing, competitive crawl, empirical synthesis, telemetry. | `firecrawl-scraper`, `tavily-search-intelligence`, `agency-research-synthesist` ([firecrawl](https://github.com/firecrawl/firecrawl), [tavily-python](https://github.com/tavily-ai/tavily-python), [agency-agents](https://github.com/msitarzewski/agency-agents)) | [`SR24-RESEARCH.md`](./00-MASTER-CONTROLLER/workflows/SR24-RESEARCH.md) |
| **14** | `/sr24-ship [task]` | DevOps & Release | Production Dockerization, GitHub Actions CI/CD, health check endpoints, zero downtime. | `docker-containerization`, `github-actions-ci`, `sentry-monitoring` ([docs](https://github.com/docker/docs), [runner](https://github.com/actions/runner), [sentry](https://github.com/getsentry/sentry), [opentofu](https://github.com/opentofu/opentofu)) | [`SR24-SHIP.md`](./00-MASTER-CONTROLLER/workflows/SR24-SHIP.md) |

### Core Intelligence Operations:
- **`/sr24-orchestrate [dir]`** — Inspects directory, detects tech stack, classifies into 12 archetypes, and outputs an activation matrix.
- **`/sr24-audit-prod [dir]`** — Conducts an 8-dimension forensic audit producing `reports/SR24-PRODUCTION-AUDIT.md`.
- **`/sr24-heal [test_cmd]`** — Executes a controlled 6-step closed-loop repair cycle (max 3 retries) with strict safety boundaries.
- **`/sr24-full-check`** — Autonomous end-to-end certification pipeline: Orchestration ➔ Audit ➔ Self-Healing ➔ Regression ➔ Release.

---

## 2. How Master Commands Work

When you trigger any master command or natural-language request, the toolkit executes a deterministic engineering pipeline:

```
[User Task]
    │
    ▼
[Workspace Analysis] ──────── Static scan of packages, configs, lockfiles, and folder structure
    │
    ▼
[Technology Detection] ────── Inference of framework, language, styling, ORM, and physics engine
    │
    ▼
[Skill Selection] ─────────── Mobilization of specific canonical skills with confidence rankings
    │
    ▼
[Engineering Execution] ───── Execution of phase-by-phase deliverables with strict typing & contracts
    │
    ▼
[Production Audit] ────────── Forensic inspection across 8 quality dimensions with zero synthetic scoring
    │
    ▼
[Self-Healing Loop] ───────── Controlled 6-step repair cycle if test failures or defects are discovered
    │
    ▼
[Release Certification] ───── Docker container verification, CI/CD pipeline, and green test proof
```

---

## 3. Core Intelligence Layer

The **Core Intelligence Layer** acts as the operational brain of SR24Plus, uniting all 479 canonical skills into an autonomous closed-loop quality system:

```
┌────────────────────────────────────────────────────────────────────────┐
│                        SR24 INTELLIGENCE ENGINE                        │
│   • Traverses filesystem & reads package manifests                     │
│   • Detects languages (TS/JS/Py/Rust/Go/C#) and frameworks             │
│   • Classifies project into 12 archetypes (SaaS, 3D Game, AI, etc.)    │
│   • Generates priority-scored skill activation plans                   │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│                       SR24 PRODUCTION AUDITOR                          │
│   • Audits 8 verified production dimensions with non-synthetic scoring │
│   • Checks Architecture, UI/UX Anti-Slop, Frontend, Backend, DB,       │
│     Security, Game Loop/Physics, and Deployment                        │
│   • Generates forensic defect register: reports/SR24-PRODUCTION-AUDIT  │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│                      SR24 SELF-HEALING ENGINEER                        │
│   • Closed-Loop Repair: Detect ➔ Diagnose ➔ Plan ➔ Repair ➔ Test       │
│   • Strict Safety Guardrails: Blocks rm -rf, DROP TABLE, force push    │
│   • Capped at maximum 3 attempts with automatic rollback on failure    │
└────────────────────────────────────────────────────────────────────────┘
```

### Core Subsystems & Upstream Tool Integration:

1. **SR24 Intelligence Engine (`sr24-intelligence-engine`)**:
   - **Internal Implementation**: [`skills/sr24-custom-engineering/sr24-intelligence-engine/scripts/intelligence_engine.py`](./skills/sr24-custom-engineering/sr24-intelligence-engine/scripts/intelligence_engine.py)
   - **Skill Manifest**: [`skills/sr24-custom-engineering/sr24-intelligence-engine/SKILL.md`](./skills/sr24-custom-engineering/sr24-intelligence-engine/SKILL.md)
   - **Runbook**: [`00-MASTER-CONTROLLER/workflows/SR24-AUTO.md`](./00-MASTER-CONTROLLER/workflows/SR24-AUTO.md)
   - **Subsystem Manual**: [`docs/SR24PLUS-INTELLIGENCE-ENGINE.md`](./docs/SR24PLUS-INTELLIGENCE-ENGINE.md)
   - **Architectural Scope**: Original SR24Plus custom architecture. Statically scans codebase dependencies (`package.json`, `Cargo.toml`, `requirements.txt`, `ProjectSettings.asset`), classifies workspaces into 12 distinct production archetypes, and emits dynamic skill execution plans.

2. **SR24 Production Auditor (`sr24-production-auditor`)**:
   - **Internal Implementation**: [`skills/sr24-custom-engineering/sr24-production-auditor/scripts/production_auditor.py`](./skills/sr24-custom-engineering/sr24-production-auditor/scripts/production_auditor.py)
   - **Skill Manifest**: [`skills/sr24-custom-engineering/sr24-production-auditor/SKILL.md`](./skills/sr24-custom-engineering/sr24-production-auditor/SKILL.md)
   - **Subsystem Manual**: [`docs/SR24PLUS-PRODUCTION-AUDITOR.md`](./docs/SR24PLUS-PRODUCTION-AUDITOR.md)
   - **Integrated Tool Repositories**:
     - Secret Leak Detection: [gitleaks/gitleaks](https://github.com/gitleaks/gitleaks)
     - Dynamic Security Fuzzing (DAST): [zaproxy/zaproxy](https://github.com/zaproxy/zaproxy)
     - Vulnerability Database Scanning: [google/osv-scanner](https://github.com/google/osv-scanner)
     - Container & IaC Security: [aquasecurity/trivy](https://github.com/aquasecurity/trivy)
     - Design Anti-Slop & WCAG Contrast: [miqdadbadjuber/anti-slop](https://github.com/miqdadbadjuber/anti-slop) and [dequelabs/axe-core](https://github.com/dequelabs/axe-core)
     - Payload & API DTO Validation: [colinhacks/zod](https://github.com/colinhacks/zod)
     - Container Configuration: [docker/docs](https://github.com/docker/docs)

3. **SR24 Self-Healing Engineer (`sr24-self-healing-engineer`)**:
   - **Internal Implementation**: [`skills/sr24-custom-engineering/sr24-self-healing-engineer/scripts/self_healing_engineer.py`](./skills/sr24-custom-engineering/sr24-self-healing-engineer/scripts/self_healing_engineer.py)
   - **Skill Manifest**: [`skills/sr24-custom-engineering/sr24-self-healing-engineer/SKILL.md`](./skills/sr24-custom-engineering/sr24-self-healing-engineer/SKILL.md)
   - **Subsystem Manual**: [`docs/SR24PLUS-SELF-HEALING-ENGINEER.md`](./docs/SR24PLUS-SELF-HEALING-ENGINEER.md)
   - **Integrated Verification Tools**:
     - Browser E2E Automation: [microsoft/playwright](https://github.com/microsoft/playwright)
     - Strict Linting & AST Checking: [typescript-eslint/typescript-eslint](https://github.com/typescript-eslint/typescript-eslint)
   - **Architectural Scope**: Original SR24Plus closed-loop repair engine (Detect ➔ Diagnose ➔ Plan ➔ Repair ➔ Test ➔ Verify) with non-destructive guardrails blocking force pushes, unauthorized table drops, and unbacked filesystem truncations.

Detailed architecture manual: [`docs/SR24PLUS-CORE-INTELLIGENCE.md`](./docs/SR24PLUS-CORE-INTELLIGENCE.md).

---

## 4. Flagship Engineering Packs

<p align="center">
  <img src="./assets/sr24plus-deep-dive.jpg" alt="SR24Plus Deep Dive Banner" width="100%" />
</p>

### Pack A: `SR24-WEB-DEV` (58 Verified Skills • Rating: 10.0 / 10)
Enforces a comprehensive **12-Phase Web Application & SaaS Lifecycle** to eliminate generic templates and deliver hardened, production-grade web systems. Every phase mobilizes verified internal skills backed by upstream open-source repositories:

| Phase | Phase Name | Focus & Scope | Core Skills Mobilized | Upstream Sources |
|:---:|---|---|---|---|
| **01** | Research & Discovery | Market sizing, competitor crawl, pricing extraction | [`firecrawl-scraper`](./skills/sr24-custom-engineering/firecrawl-scraper/SKILL.md), [`tavily-search-intelligence`](./skills/sr24-custom-engineering/tavily-search-intelligence/SKILL.md), [`posthog-analytics`](./skills/sr24-custom-engineering/posthog-analytics/SKILL.md) | [firecrawl](https://github.com/firecrawl/firecrawl), [tavily-python](https://github.com/tavily-ai/tavily-python), [posthog](https://github.com/PostHog/posthog) |
| **02** | Planning & Specifications | PRD authoring, user stories, C4 visual architecture | [`c4-architecture-model`](./skills/sr24-custom-engineering/c4-architecture-model/SKILL.md), [`mermaid-diagrams`](./skills/sr24-custom-engineering/mermaid-diagrams/SKILL.md), [`spec-driven-development`](./skills/addyosmani-agent-skills/spec-driven-development/SKILL.md) | [C4-PlantUML](https://github.com/plantuml-stdlib/C4-PlantUML), [mermaid](https://github.com/mermaid-js/mermaid), [agent-skills](https://github.com/addyosmani/agent-skills) |
| **03** | Branding & Identity | Self-hosted typography, color scales, 24px icons | [`taste-skill`](./skills/ui-design-suite/taste-skill/SKILL.md), [`lucide-icons`](./skills/sr24-custom-engineering/lucide-icons/SKILL.md), [`fontsource-typography`](./skills/sr24-custom-engineering/fontsource-typography/SKILL.md) | [taste-skill](https://github.com/Leonxlnx/taste-skill), [lucide](https://github.com/lucide-icons/lucide), [fontsource](https://github.com/fontsource/fontsource) |
| **04** | UI/UX & Anti-Slop Gate | Hard gate banning purple gradients, WCAG AA contrast | [`impeccable`](./skills/ui-design-suite/impeccable/SKILL.md), [`ui-ux-pro-max`](./skills/ui-design-suite/ui-ux-pro-max/SKILL.md), [`antislop-ui`](./skills/ui-design-suite/antislop-ui/SKILL.md), [`component-intelligence`](./skills/sr24-custom-engineering/component-intelligence/SKILL.md) | [impeccable](https://github.com/pbakaus/impeccable), [ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill), [anti-slop](https://github.com/miqdadbadjuber/anti-slop), [aceternity-ui](https://github.com/aceternity/aceternity-ui) |
| **05** | Frontend Development | Modular React/Next.js features, strict typing, motion | [`bulletproof-react`](./skills/sr24-custom-engineering/bulletproof-react/SKILL.md), [`typescript-eslint`](./skills/sr24-custom-engineering/typescript-eslint/SKILL.md), [`react-testing-library`](./skills/sr24-custom-engineering/react-testing-library/SKILL.md), [`gsap-animations`](./skills/sr24-custom-engineering/gsap-animations/SKILL.md) | [bulletproof-react](https://github.com/alan2207/bulletproof-react), [typescript-eslint](https://github.com/typescript-eslint/typescript-eslint), [react-testing-library](https://github.com/testing-library/react-testing-library), [GSAP](https://github.com/greensock/GSAP) |
| **06** | Backend & Realtime | Distributed APIs, WebSockets, background job queues | [`supabase-engineering`](./skills/sr24-custom-engineering/supabase-engineering/SKILL.md), [`node-best-practices`](./skills/sr24-custom-engineering/node-best-practices/SKILL.md), [`socketio-realtime`](./skills/sr24-custom-engineering/socketio-realtime/SKILL.md), [`bullmq-job-queues`](./skills/sr24-custom-engineering/bullmq-job-queues/SKILL.md) | [agent-skills](https://github.com/supabase/agent-skills), [nodebestpractices](https://github.com/goldbergyoni/nodebestpractices), [socket.io](https://github.com/socketio/socket.io), [bullmq](https://github.com/taskforcesh/bullmq) |
| **07** | Database & Storage | Normalized schemas (3NF), zero-downtime migrations | [`prisma-orm`](./skills/sr24-custom-engineering/prisma-orm/SKILL.md), [`drizzle-orm`](./skills/sr24-custom-engineering/drizzle-orm/SKILL.md), [`dbml-schema-design`](./skills/sr24-custom-engineering/dbml-schema-design/SKILL.md), [`redis-in-memory-datastore`](./skills/sr24-custom-engineering/redis-in-memory-datastore/SKILL.md) | [prisma](https://github.com/prisma/prisma), [drizzle-orm](https://github.com/drizzle-team/drizzle-orm), [dbml](https://github.com/holistics/dbml), [redis](https://github.com/redis/redis) |
| **08** | SaaS & Fintech | Razorpay Orders, UPI QR, Indian GST math, Lago | [`razorpay-upi-specialist`](./skills/sr24-custom-engineering/razorpay-upi-specialist/SKILL.md), [`indian-gst-billing-engineer`](./skills/sr24-custom-engineering/indian-gst-billing-engineer/SKILL.md), [`lago-billing`](./skills/sr24-custom-engineering/lago-billing/SKILL.md) | [SR24plus-engineering-toolkit](https://github.com/sahil24raj/SR24plus-engineering-toolkit/tree/main/skills/sr24-custom-engineering), [lago](https://github.com/getlago/lago) |
| **09** | Security & Hardening | OWASP Top 10 defenses, secret scanning, CVE audits | [`owasp-zap-scanner`](./skills/sr24-custom-engineering/owasp-zap-scanner/SKILL.md), [`gitleaks-secret-detection`](./skills/sr24-custom-engineering/gitleaks-secret-detection/SKILL.md), [`trivy-security-scanner`](./skills/sr24-custom-engineering/trivy-security-scanner/SKILL.md) | [zaproxy](https://github.com/zaproxy/zaproxy), [gitleaks](https://github.com/gitleaks/gitleaks), [trivy](https://github.com/aquasecurity/trivy) |
| **10** | Testing & QA | Flake-free E2E browser tests, visual pixel diffing | [`playwright-testing`](./skills/sr24-custom-engineering/playwright-testing/SKILL.md), [`lost-pixel-visual-regression`](./skills/sr24-custom-engineering/lost-pixel-visual-regression/SKILL.md), [`k6-load-testing`](./skills/sr24-custom-engineering/k6-load-testing/SKILL.md) | [playwright](https://github.com/microsoft/playwright), [lost-pixel](https://github.com/lost-pixel/lost-pixel), [k6](https://github.com/grafana/k6) |
| **11** | DevOps & CI/CD | Multi-stage Docker, OpenTofu cloud IaC, Sentry APM | [`docker-containerization`](./skills/sr24-custom-engineering/docker-containerization/SKILL.md), [`opentofu-iac`](./skills/sr24-custom-engineering/opentofu-iac/SKILL.md), [`github-actions-ci`](./skills/sr24-custom-engineering/github-actions-ci/SKILL.md), [`sentry-monitoring`](./skills/sr24-custom-engineering/sentry-monitoring/SKILL.md) | [docs](https://github.com/docker/docs), [opentofu](https://github.com/opentofu/opentofu), [runner](https://github.com/actions/runner), [sentry](https://github.com/getsentry/sentry) |
| **12** | Analytics & Launch | Telemetry funnels, session heatmaps, programmatic SEO | [`posthog-analytics`](./skills/sr24-custom-engineering/posthog-analytics/SKILL.md), [`microsoft-clarity`](./skills/sr24-custom-engineering/microsoft-clarity/SKILL.md), [`programmatic-seo-engineer`](./skills/sr24-custom-engineering/programmatic-seo-engineer/SKILL.md) | [posthog](https://github.com/PostHog/posthog), [clarity](https://github.com/microsoft/clarity), [SR24plus-engineering-toolkit](https://github.com/sahil24raj/SR24plus-engineering-toolkit/tree/main/skills/sr24-custom-engineering) |

*Deep-Dive Manual*: [`docs/README-SR24-WEB-DEV.md`](./docs/README-SR24-WEB-DEV.md)

---

### Pack B: `SR24-GAME-DEV` (52 Verified Skills • Rating: 10.0 / 10)
Powers high-performance, deterministic game engineering across **Browser 2D/3D Canvas/WebGL**, **Rapier/Jolt Physics**, **Authoritative Multiplayer**, and **Native Unity 3D**. Every phase links internal skill manifests directly to their upstream open-source engines and specifications:

| Phase | Phase Name | Focus & Scope | Core Skills Mobilized | Upstream Sources |
|:---:|---|---|---|---|
| **01** | Concept & GDD | 2-minute core loops, GDD specs, economy sinks/sources | [`game-programming-patterns`](./skills/sr24-custom-engineering/game-programming-patterns/SKILL.md), [`awesome-gamedev-skills`](./skills/sr24-custom-engineering/awesome-gamedev-skills/SKILL.md), [`agency-game-development-game-designer`](./skills/agency-agents/agency-game-development-game-designer/SKILL.md) | [game-programming-patterns](https://github.com/munificent/game-programming-patterns), [magictools](https://github.com/ellisonleao/magictools), [agency-agents](https://github.com/msitarzewski/agency-agents) |
| **02** | Architecture & ECS | Zero-GC TypedArray ECS, state machines, ScriptableObjects | [`bitecs-architecture`](./skills/sr24-custom-engineering/bitecs-architecture/SKILL.md), [`game-programming-patterns`](./skills/sr24-custom-engineering/game-programming-patterns/SKILL.md), [`new-unity-project`](./skills/unity-skills/new-unity-project/SKILL.md) | [bitECS](https://github.com/NateLevin1/bitECS), [game-programming-patterns](https://github.com/munificent/game-programming-patterns), [com.unity.entities](https://github.com/Unity-Technologies/com.unity.entities) |
| **03** | In-Game HUD & Audio | Dual-camera HUD, minimap, combo counters, 3D audio | [`threejs-ui-hud`](./skills/sr24-custom-engineering/threejs-ui-hud/SKILL.md), [`gsap-animations`](./skills/sr24-custom-engineering/gsap-animations/SKILL.md), [`howler-js-audio`](./skills/sr24-custom-engineering/howler-js-audio/SKILL.md), [`ui-uitk`](./skills/unity-skills/ui-uitk/SKILL.md) | [three.js](https://github.com/mrdoob/three.js), [GSAP](https://github.com/greensock/GSAP), [howler.js](https://github.com/goldfire/howler.js), [com.unity.entities](https://github.com/Unity-Technologies/com.unity.entities) |
| **04** | Web Game Engines | Three.js PBR, R3F declarative scenes, Phaser 3 arcade | [`threejs-game-engine`](./skills/sr24-custom-engineering/threejs-game-engine/SKILL.md), [`react-three-fiber`](./skills/sr24-custom-engineering/react-three-fiber/SKILL.md), [`pixijs-engine`](./skills/sr24-custom-engineering/pixijs-engine/SKILL.md), [`phaser-game-engine`](./skills/sr24-custom-engineering/phaser-game-engine/SKILL.md) | [three.js](https://github.com/mrdoob/three.js), [react-three-fiber](https://github.com/pmndrs/react-three-fiber), [pixijs](https://github.com/pixijs/pixijs), [phaser](https://github.com/phaserjs/phaser) |
| **05** | Gameplay & Physics | Rapier 3D/2D, Jolt vehicles, 80ms hitstop, frame data | [`rapier-physics`](./skills/sr24-custom-engineering/rapier-physics/SKILL.md), [`react-three-rapier`](./skills/sr24-custom-engineering/react-three-rapier/SKILL.md), [`jolt-physics`](./skills/sr24-custom-engineering/jolt-physics/SKILL.md), [`combat-mechanics-engineer`](./skills/sr24-custom-engineering/combat-mechanics-engineer/SKILL.md) | [rapier](https://github.com/dimforge/rapier), [react-three-rapier](https://github.com/pmndrs/react-three-rapier), [JoltPhysics](https://github.com/jrouwe/JoltPhysics), [SR24plus-engineering-toolkit](https://github.com/sahil24raj/SR24plus-engineering-toolkit/tree/main/skills/sr24-custom-engineering) |
| **06** | Authoritative Multiplayer | 60Hz server tick, prediction, reconciliation, anti-cheat | [`colyseus-multiplayer`](./skills/sr24-custom-engineering/colyseus-multiplayer/SKILL.md), [`nakama-backend`](./skills/sr24-custom-engineering/nakama-backend/SKILL.md), [`browser-game-anti-cheat-engineer`](./skills/sr24-custom-engineering/browser-game-anti-cheat-engineer/SKILL.md) | [colyseus](https://github.com/colyseus/colyseus), [nakama](https://github.com/heroiclabs/nakama), [SR24plus-engineering-toolkit](https://github.com/sahil24raj/SR24plus-engineering-toolkit/tree/main/skills/sr24-custom-engineering) |
| **07** | Unity 3D & URP | DOTS/ECS Burst jobs, custom HLSL Shader Graph nodes | [`unity-entities-ecs`](./skills/sr24-custom-engineering/unity-entities-ecs/SKILL.md), [`agency-game-development-unity-unity-architect`](./skills/agency-agents/agency-game-development-unity-unity-architect/SKILL.md), [`urp-postprocessing`](./skills/unity-skills/urp-postprocessing/SKILL.md) | [com.unity.entities](https://github.com/Unity-Technologies/com.unity.entities), [agency-agents](https://github.com/msitarzewski/agency-agents) |
| **08** | Vehicle Physics | 16-wheeler heavy trucks (12,000kg), Pacejka slip, ghats | [`truck-physics-engineer`](./skills/sr24-custom-engineering/truck-physics-engineer/SKILL.md), [`realistic-car-controller-engineer`](./skills/sr24-custom-engineering/realistic-car-controller-engineer/SKILL.md), [`racing-track-design-engineer`](./skills/sr24-custom-engineering/racing-track-design-engineer/SKILL.md) | [SR24plus-engineering-toolkit](https://github.com/sahil24raj/SR24plus-engineering-toolkit/tree/main/skills/sr24-custom-engineering) |
| **09** | 3D Asset & glTF Pipeline | glTF DRACO compression, KTX2 transcoding, Blender CLI | [`gltf-transform-pipeline`](./skills/sr24-custom-engineering/gltf-transform-pipeline/SKILL.md), [`blender-pipeline`](./skills/sr24-custom-engineering/blender-pipeline/SKILL.md), [`agency-game-development-blender-blender-addon-engineer`](./skills/agency-agents/agency-game-development-blender-blender-addon-engineer/SKILL.md) | [glTF-Transform](https://github.com/donmccurdy/glTF-Transform), [blender](https://projects.blender.org/blender/blender), [agency-agents](https://github.com/msitarzewski/agency-agents) |
| **10** | Testing & Profiling | InstancedMesh, draw call batching, canvas E2E testing | [`threejs-optimization-profiling`](./skills/sr24-custom-engineering/threejs-optimization-profiling/SKILL.md), [`gameplay-regression-testing`](./skills/sr24-custom-engineering/gameplay-regression-testing/SKILL.md), [`unity-performance-testing`](./skills/sr24-custom-engineering/unity-performance-testing/SKILL.md) | [three.js](https://github.com/mrdoob/three.js), [playwright](https://github.com/microsoft/playwright), [com.unity.entities](https://github.com/Unity-Technologies/com.unity.entities) |
| **11** | Build & Release | Headless Unity CLI builds, WebGL Brotli packaging | [`game-build-and-release`](./skills/sr24-custom-engineering/game-build-and-release/SKILL.md), [`unity-cli`](./skills/unity-skills/unity-cli/SKILL.md), [`optimize-web`](./skills/unity-skills/optimize-web/SKILL.md) | [SR24plus-engineering-toolkit](https://github.com/sahil24raj/SR24plus-engineering-toolkit/tree/main/skills/sr24-custom-engineering), [com.unity.entities](https://github.com/Unity-Technologies/com.unity.entities) |
| **12** | Analytics & Retention | Telemetry events, economy balancing, churn reduction | [`game-analytics-sdk`](./skills/sr24-custom-engineering/game-analytics-sdk/SKILL.md), [`umami-game-analytics`](./skills/sr24-custom-engineering/umami-game-analytics/SKILL.md), [`agency-game-development-economy-designer`](./skills/agency-agents/agency-game-development-economy-designer/SKILL.md) | [GA-SDK-JAVASCRIPT](https://github.com/gameanalytics/GA-SDK-JAVASCRIPT), [umami](https://github.com/umami-software/umami), [agency-agents](https://github.com/msitarzewski/agency-agents) |

*Deep-Dive Manual*: [`docs/README-SR24-GAME-DEV.md`](./docs/README-SR24-GAME-DEV.md)

---

## 5. Master Production Profiles

For enterprise implementations, the toolkit includes pre-configured production blueprints combining multi-phase squads:

### Profile 1: Full-Stack SaaS Platforms (`FULLSTACK-SAAS-PROFILE.md`)
- **Target Applications**: E-Commerce, B2B SaaS, Offline POS (e.g., *Dukan Sathi*, *ExamLoop*).
- **Core Architecture**: [Next.js](https://github.com/vercel/next.js) App Router, PostgreSQL ([Supabase](https://github.com/supabase/supabase)), [Drizzle ORM](https://github.com/drizzle-team/drizzle-orm), [Zod](https://github.com/colinhacks/zod) runtime parsing, [Razorpay](https://github.com/sahil24raj/SR24plus-engineering-toolkit/tree/main/skills/sr24-custom-engineering/razorpay-upi-specialist) dynamic UPI QR, [Indian GST](https://github.com/sahil24raj/SR24plus-engineering-toolkit/tree/main/skills/sr24-custom-engineering/indian-gst-billing-engineer) tax calculations, and [Lago](https://github.com/getlago/lago) metered billing.
- **Blueprint Location**: [`00-MASTER-CONTROLLER/projects/FULLSTACK-SAAS-PROFILE.md`](./00-MASTER-CONTROLLER/projects/FULLSTACK-SAAS-PROFILE.md)

### Profile 2: High-Performance Browser Gaming (`BROWSER-GAMING-PROFILE.md`)
- **Target Applications**: Real-Time Multiplayer, 3D Highway Runners, Esports (e.g., *Vibe Arena*, *GullyVerse*).
- **Core Architecture**: Deterministic 60 FPS accumulator loop (`dt = 1/60s`), [Three.js](https://github.com/mrdoob/three.js) / [React Three Fiber](https://github.com/pmndrs/react-three-fiber) WebGL, [Rapier](https://github.com/dimforge/rapier) 3D physics, [Colyseus](https://github.com/colyseus/colyseus) authoritative 60Hz server tick with client prediction, [anti-cheat](https://github.com/sahil24raj/SR24plus-engineering-toolkit/tree/main/skills/sr24-custom-engineering/browser-game-anti-cheat-engineer) memory XOR obfuscation, and [Howler.js](https://github.com/goldfire/howler.js) spatial audio.
- **Blueprint Location**: [`00-MASTER-CONTROLLER/projects/BROWSER-GAMING-PROFILE.md`](./00-MASTER-CONTROLLER/projects/BROWSER-GAMING-PROFILE.md)

---

## 6. Quick Start Guide

You do not need to manually configure or install individual skills. All 479 skills are pre-indexed and ready for autonomous dispatch:

### Step 1: Clone Repository
```bash
git clone https://github.com/sahil24raj/SR24plus-engineering-toolkit.git
cd SR24plus-engineering-toolkit
```

### Step 2: Invoke via CLI or AI Agent Prompt
Inside Google Antigravity, Cursor, Claude, or any modern agent environment, issue your command:

```text
/sr24-auto
```
*Or execute a specialized workflow:*
```text
/sr24-web-dev Build an offline-first inventory SaaS with GST invoices and UPI QR payments
```
```text
/sr24-game-dev Create a 3D highway runner with obstacle lanes, dynamic speed curves, and boss fights
```

---

## 7. Supported Technology Ecosystem

| Domain | Supported Technologies & Official Repositories | Core Architectural Role |
|---|---|---|
| **Web Development** | [Next.js](https://github.com/vercel/next.js), [React](https://github.com/facebook/react), [TypeScript](https://github.com/microsoft/TypeScript), [Tailwind CSS](https://github.com/tailwindlabs/tailwindcss) | App Router, Server Actions, strict type checking, and mathematical 4px/8px styling tokens. |
| **Databases & ORMs** | [Supabase](https://github.com/supabase/supabase), [Drizzle ORM](https://github.com/drizzle-team/drizzle-orm), [Prisma](https://github.com/prisma/prisma), [DBML](https://github.com/holistics/dbml) | PostgreSQL Row Level Security (RLS), type-safe zero-overhead queries, automated migration pipelines. |
| **Queues & Caching** | [BullMQ](https://github.com/taskforcesh/bullmq), [Redis](https://github.com/redis/redis) | Distributed background workers, rate limiting, and high-speed in-memory state caching. |
| **Game Engines (2D/3D)**| [Three.js](https://github.com/mrdoob/three.js), [React Three Fiber](https://github.com/pmndrs/react-three-fiber), [Phaser 3](https://github.com/phaserjs/phaser), [PixiJS](https://github.com/pixijs/pixijs) | PBR shaders, scene graphs, declarative React canvas pipelines, and 2D sprite batching. |
| **Game Physics** | [Rapier](https://github.com/dimforge/rapier), [Jolt Physics](https://github.com/jrouwe/JoltPhysics), [Matter.js](https://github.com/liabru/matter-js) | WASM deterministic 2D/3D rigid body dynamics, multi-threaded vehicle physics, and 2D constraints. |
| **Game Networking** | [Colyseus](https://github.com/colyseus/colyseus), [Nakama](https://github.com/heroiclabs/nakama), [Socket.IO](https://github.com/socketio/socket.io) | Authoritative 60Hz server tick, schema state synchronization, and room matchmaking. |
| **Game Audio & DCC** | [Howler.js](https://github.com/goldfire/howler.js), [glTF-Transform](https://github.com/donmccurdy/glTF-Transform), [Blender](https://projects.blender.org/blender/blender) | Positional 3D Web Audio sprites, glTF DRACO compression, KTX2 transcoding, and headless DCC scripts. |
| **Native Game Engine** | [Unity Technologies (DOTS/ECS)](https://github.com/Unity-Technologies/com.unity.entities) | Burst-compiled jobs, ScriptableObject event architectures, and URP Volume post-processing. |
| **AI & Agent Systems** | [Model Context Protocol](https://github.com/modelcontextprotocol), [Agency Agents](https://github.com/msitarzewski/agency-agents), [Google Antigravity](https://github.com/google-deepmind) | 301 autonomous personas, multi-agent swarms, AST transformers, and MCP integration. |
| **Security & DevSecOps**| [Gitleaks](https://github.com/gitleaks/gitleaks), [OWASP ZAP](https://github.com/zaproxy/zaproxy), [Trivy](https://github.com/aquasecurity/trivy), [OSV-Scanner](https://github.com/google/osv-scanner) | Leaked secret detection, DAST vulnerability fuzzing, container audits, and CVE lockfile scanning. |
| **Testing & Quality** | [Playwright](https://github.com/microsoft/playwright), [React Testing Library](https://github.com/testing-library/react-testing-library), [Lost Pixel](https://github.com/lost-pixel/lost-pixel), [Grafana k6](https://github.com/grafana/k6) | Cross-browser auto-waiting E2E, accessible unit tests, visual regression diffs, and high-concurrency API load tests. |
| **DevOps & Telemetry** | [Docker](https://github.com/docker/docs), [GitHub Actions](https://github.com/actions/runner), [OpenTofu](https://github.com/opentofu/opentofu), [Sentry](https://github.com/getsentry/sentry), [PostHog](https://github.com/PostHog/posthog) | Multi-stage Alpine builds, automated CI/CD runners, declarative IaC, real-time APM, and event replay. |

Detailed ecosystem manual: [`docs/SR24PLUS-TECH-STACK.md`](./docs/SR24PLUS-TECH-STACK.md).

---

## 8. Source Attribution & Provenance

The **SR24Plus Engineering Toolkit** strictly adheres to open-source licensing standards and transparent author attribution. Every upstream open-source project contributing skills, agents, workflows, or architectures is documented and directly accessible:

- [**`msitarzewski/agency-agents`**](https://github.com/msitarzewski/agency-agents) (301 skills • MIT License): Comprehensive autonomous agent personas covering frontend, backend, security, game design, GIS, and DevOps.
- [**`addyosmani/agent-skills`**](https://github.com/addyosmani/agent-skills) (25 skills • MIT License): Engineering craft standards, specification-driven development, context engineering, ADRs, and performance optimization.
- [**`Unity-Technologies/com.unity.entities`**](https://github.com/Unity-Technologies/com.unity.entities) (32 skills • Unity Companion / Apache-2.0): Official Unity engine skills for Entities DOTS/ECS, URP Shader Graph, NavMesh AI, and headless build pipelines.
- [**`vercel-labs/agent-skills`**](https://github.com/vercel-labs/agent-skills) (9 skills • MIT License): Modern React Server Component composition, Next.js Server Actions, and React Compiler optimizations.
- **UI/UX, Anti-Slop & Design Systems Suite**:
  - [pbakaus/impeccable](https://github.com/pbakaus/impeccable) (Apache-2.0): Typographic scale, spacing rhythm, and high-precision design critique.
  - [miqdadbadjuber/anti-slop](https://github.com/miqdadbadjuber/anti-slop) (MIT): Anti-AI generic slop filter enforcing WCAG AA contrast and token contracts.
  - [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) (MIT): Aesthetic curation, color palette harmonizers, and typography pairings.
  - [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) (MIT): 48+ curated visual design systems, design contracts, and accessible layouts.
  - [aceternity/aceternity-ui](https://github.com/aceternity/aceternity-ui) (MIT): Modern Bento grids, spotlight borders, and 3D card pin components.
  - [greensock/GSAP](https://github.com/greensock/GSAP) (Standard Open-Source): 60 FPS timeline animations, ScrollTrigger, and vector morphing.
  - [motiondivision/motion](https://github.com/motiondivision/motion) (MIT): Framer Motion layout animations, spring physics, and gesture recognition.
  - [dequelabs/axe-core](https://github.com/dequelabs/axe-core) (MPL-2.0): Automated accessibility audit engine enforcing WCAG 2.1 AA/AAA.
  - [fontsource/fontsource](https://github.com/fontsource/fontsource) (MIT): Self-hosted variable typography eliminating Cumulative Layout Shift (CLS).
  - [lucide-icons/lucide](https://github.com/lucide-icons/lucide) (ISC): Tree-shaken 24px SVG icon system.
- **Core Game Engines, Physics & DCC Repositories**:
  - [mrdoob/three.js](https://github.com/mrdoob/three.js) (MIT): WebGL 3D scene engine, PBR materials, instancing, and camera projections.
  - [pmndrs/react-three-fiber](https://github.com/pmndrs/react-three-fiber) (MIT): Declarative Three.js in React/Next.js with Drei helpers.
  - [dimforge/rapier](https://github.com/dimforge/rapier) (Apache-2.0): High-performance WebAssembly 2D/3D rigid body physics and kinematic controllers.
  - [pmndrs/react-three-rapier](https://github.com/pmndrs/react-three-rapier) (MIT): Declarative Rapier physics wrappers for React Three Fiber.
  - [jrouwe/JoltPhysics](https://github.com/jrouwe/JoltPhysics) (MIT): Multi-threaded AAA vehicle, character, and ragdoll physics for WebAssembly.
  - [liabru/matter-js](https://github.com/liabru/matter-js) (MIT): 2D rigid body physics, composite bodies, and constraint chains for browser games.
  - [phaserjs/phaser](https://github.com/phaserjs/phaser) (MIT): 2D arcade physics, sprite animation, tilemaps, and game lifecycles.
  - [pixijs/pixijs](https://github.com/pixijs/pixijs) (MIT): High-speed 2D WebGL sprite batching and rendering engine.
  - [colyseus/colyseus](https://github.com/colyseus/colyseus) (MIT): Authoritative multiplayer game server with schema-based binary state synchronization.
  - [heroiclabs/nakama](https://github.com/heroiclabs/nakama) (Apache-2.0): Production game backend, matchmaking, leaderboards, and user storage.
  - [goldfire/howler.js](https://github.com/goldfire/howler.js) (MIT): Web Audio API management, audio sprites, and 3D positional sound.
  - [NateLevin1/bitECS](https://github.com/NateLevin1/bitECS) (MIT): High-performance, zero-garbage TypedArray Entity Component System for JavaScript.
  - [munificent/game-programming-patterns](https://github.com/munificent/game-programming-patterns) (MIT): Game programming architecture (State, Command, Spatial Partition).
  - [ellisonleao/magictools](https://github.com/ellisonleao/magictools) (CC0-1.0): Curated game development patterns and mathematical formulas.
  - [donmccurdy/glTF-Transform](https://github.com/donmccurdy/glTF-Transform) (MIT): glTF 2.0 DRACO mesh compression and KTX2 texture transcoding.
  - [blender/blender](https://projects.blender.org/blender/blender) (GPL-3.0): Headless 3D mesh processing, Python add-on automation, and LOD generation.
  - [gameanalytics/GA-SDK-JAVASCRIPT](https://github.com/gameanalytics/GA-SDK-JAVASCRIPT) (MIT): Player retention, design, and progression event telemetry.
  - [umami-software/umami](https://github.com/umami-software/umami) (MIT): Privacy-focused, self-hosted web game metrics.
- **Backend, Database, DevSecOps & Deployment Repositories**:
  - [supabase/agent-skills](https://github.com/supabase/agent-skills) (MIT): PostgreSQL Row Level Security (RLS), Supabase Auth, and Edge Functions.
  - [prisma/prisma](https://github.com/prisma/prisma) (Apache-2.0): Declarative database modeling and automated migration pipelines.
  - [drizzle-team/drizzle-orm](https://github.com/drizzle-team/drizzle-orm) (Apache-2.0): Zero-overhead type-safe SQL query builder and schema management.
  - [holistics/dbml](https://github.com/holistics/dbml) (Apache-2.0): Database Markup Language visual schema design and SQL DDL synchronization.
  - [colinhacks/zod](https://github.com/colinhacks/zod) (MIT): TypeScript-first runtime schema validation and DTO parsing.
  - [taskforcesh/bullmq](https://github.com/taskforcesh/bullmq) (MIT): Redis-backed distributed message queues and background job processors.
  - [redis/redis](https://github.com/redis/redis) (BSD-3-Clause): In-memory caching, ephemeral lobby states, and rate limiters.
  - [socketio/socket.io](https://github.com/socketio/socket.io) (MIT): Low-latency bidirectional WebSockets and room multiplexing.
  - [zaproxy/zaproxy](https://github.com/zaproxy/zaproxy) (Apache-2.0): OWASP ZAP dynamic application security testing (DAST) scanner.
  - [gitleaks/gitleaks](https://github.com/gitleaks/gitleaks) (MIT): Secret detection engine preventing leaked API keys and tokens.
  - [google/osv-scanner](https://github.com/google/osv-scanner) (Apache-2.0): Vulnerability scanner matching lockfiles against the OSV database.
  - [aquasecurity/trivy](https://github.com/aquasecurity/trivy) (Apache-2.0): Container image and Infrastructure-as-Code vulnerability scanner.
  - [microsoft/playwright](https://github.com/microsoft/playwright) (Apache-2.0): Cross-browser E2E automation with auto-waiting locators.
  - [testing-library/react-testing-library](https://github.com/testing-library/react-testing-library) (MIT): Accessible user-centric React component testing.
  - [lost-pixel/lost-pixel](https://github.com/lost-pixel/lost-pixel) (MIT): Visual screenshot regression diffing with pixel thresholds.
  - [grafana/k6](https://github.com/grafana/k6) (AGPL-3.0 / MIT runner): High-throughput load, spike, and stress testing.
  - [usebruno/bruno](https://github.com/usebruno/bruno) (MIT): Git-friendly offline-first API exploration and automated test collections.
  - [docker/docs](https://github.com/docker/docs) (Apache-2.0): Multi-stage containerization and non-root security.
  - [opentofu/opentofu](https://github.com/opentofu/opentofu) (MPL-2.0): Open-source Infrastructure-as-Code cloud provisioning.
  - [actions/runner](https://github.com/actions/runner) (MIT): GitHub Actions automated CI/CD runners.
  - [getsentry/sentry](https://github.com/getsentry/sentry) (FSL-1.1-MIT): Real-time APM, crash tracking, and error diagnostics.
  - [PostHog/posthog](https://github.com/PostHog/posthog) (MIT): Product analytics, event telemetry, and session replays.
  - [microsoft/clarity](https://github.com/microsoft/clarity) (MIT): Heatmaps, rage-click telemetry, and scroll depth tracking.
  - [growthbook/growthbook](https://github.com/growthbook/growthbook) (MIT): Feature flag management and multi-variant A/B experimentation.
  - [getlago/lago](https://github.com/getlago/lago) (AGPL-3.0): Usage-based metering and subscription billing engine.
  - [vendure-ecommerce/vendure](https://github.com/vendure-ecommerce/vendure) (MIT): Headless e-commerce, shopping carts, and order workflows.
- [**`google-deepmind`**](https://github.com/google-deepmind) (13 skills • Apache-2.0): Google Antigravity IDE agent swarms, workflow migrations, and generative UI.
- [**`SR24Plus Custom Engineering`**](https://github.com/sahil24raj/SR24plus-engineering-toolkit/tree/main/skills/sr24-custom-engineering) (85 skills • MIT License): Core Intelligence layer (Intelligence Engine, Production Auditor, Self-Healing Engineer), Indian fintech (Razorpay Orders, UPI QR, Indian GST math, offline Kirana), heavy truck physics (16-wheelers, Pacejka curves), and 60Hz anti-cheat memory protection.

Complete registries:
- [`registry/SR24PLUS-UPSTREAM-SOURCES.md`](./registry/SR24PLUS-UPSTREAM-SOURCES.md)
- [`docs/SR24PLUS-SOURCE-ATTRIBUTION.md`](./docs/SR24PLUS-SOURCE-ATTRIBUTION.md)
- [`docs/SR24PLUS-SKILL-PROVENANCE.md`](./docs/SR24PLUS-SKILL-PROVENANCE.md)

---

## 9. Quality Verification & Automated Test Suite

The Core Intelligence Layer, documentation integrity, and upstream repository hyperlinks are validated by three automated test suites:

```bash
# 1. Validate Core Intelligence orchestration, audit, and self-healing loop
python tests/test_core_intelligence.py

# 2. Validate documentation files, 14 master commands, 24 phases, and relative links
python tests/validate_documentation.py

# 3. Validate 650+ upstream GitHub repository hyperlinks and canonical sources
python tests/validate_github_links.py
```

### Verification Results:
```
[1/5] Validating 14 Master Commands...
  ✓ All 14 Master Commands and runbooks verified.
[2/5] Validating Required Documentation Files...
  ✓ All 12 critical documentation files present.
[3/5] Validating Internal Relative Markdown Links in Root README...
  ✓ All relative links in README.md resolve to existing files.
[4/5] Validating 12-Phase Coverage for Web Dev and Game Dev...
  ✓ All 12 Web Dev phases and 12 Game Dev phases fully documented.
[5/5] Validating Markdown Table Delimiters across Documentation...
  ✓ All Markdown table structures syntactically valid.

✅ ALL DOCUMENTATION VALIDATION CHECKS PASSED SUCCESSFULLY!

Ran 6 tests in 2.630s
OK
✓ TEST 1 PASSED: Browser game platform correctly classified with 3D & multiplayer skills.
✓ TEST 2 PASSED: SaaS application correctly routed to database, auth & architecture skills.
✓ TEST 3 PASSED: Production auditor captured security token & XSS with evidence.
✓ TEST 4 PASSED: Self-healing closed loop successfully diagnosed and repaired defect.
✓ TEST 5 PASSED: Defect repaired with zero regression to existing functionality.
✓ TEST 6 PASSED: Strict production safety guardrails actively enforced.

============================================================
SR24Plus Global GitHub Hyperlink Audit
============================================================
  • Total Active GitHub Hyperlinks: 651+
  • Total Unique Upstream Repositories: 70
  • Central Registry Matches: 66
✅ 100% GITHUB HYPERLINK VALIDATION PASSED!
```

---

## 10. Inviolable Quality Gates & Execution Rules

1. **Zero Hallucinations**: Never generate non-existent package dependencies, fabricated API methods, or phantom file paths.
2. **Anti-AI-Slop Hard Gate**: Prohibits unmotivated purple-to-cyan gradient landing pages, illegible floating glass cards, and fake static charts.
3. **Deterministic Physics**: All game update loops must decouple physics simulation (`dt = 1/60s`) from variable rendering framerates using an accumulator.
4. **Safety Boundaries**: Destructive commands (`rm -rf /`, `DROP TABLE`, `git push --force`) are intercepted and blocked automatically.
5. **Verified Builds**: Every phase deliverable must pass static compilation (`npm run build`, `tsc --noEmit`, or `python -m py_compile`) and test verification.

---

## 11. Contributing & Community Guidelines

Contributions of high-taste design patterns, game physics models, and engineering skills are welcome:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/new-skill`).
3. Ensure every new skill follows the canonical 12-section `SKILL.md` structure with explicit dependencies, operational boundaries, and upstream attribution.
4. Verify tests pass cleanly (`python tests/test_core_intelligence.py && python tests/validate_documentation.py`).
5. Submit a descriptive Pull Request.

---

## 12. License & Legal Attribution

- The SR24Plus toolkit architecture, custom skills, and Core Intelligence engines are licensed under the **[MIT License](#12-license--legal-attribution)**.
- Upstream imported skills retain their original open-source licenses (MIT, Apache-2.0, Unity Companion License, BSD-2-Clause, MPL-2.0).
- All trademarks, logos, and brand names are the property of their respective owners.
