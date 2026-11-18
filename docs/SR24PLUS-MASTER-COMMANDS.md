# SR24Plus Master Command Center & Runbook Directory
### Exhaustive Operational Reference for All 14 Primary Master Commands & Core Intelligence Triggers

> **Toolkit Version**: v3.0 Enterprise  
> **Repository**: [https://github.com/sahil24raj/SR24plus-engineering-toolkit.git](https://github.com/sahil24raj/SR24plus-engineering-toolkit.git)  
> **Maintainer**: Sahil Raj (SR24Plus)  
> **Enforcement**: Zero Hallucinations • TypeScript Verification • Inviolable Quality Gates  

---

## 1. How Master Commands Work

Every master command in the SR24Plus Engineering Toolkit is an autonomous multi-agent pipeline orchestrator. Rather than triggering generic unstructured code generation, commands execute a deterministic lifecycle:

```
                  USER TASK OR CLI PROMPT
                             │
                             ▼
                    WORKSPACE DISCOVERY
       (File trees, package.json, configs, lockfiles)
                             │
                             ▼
                    TECHNOLOGY DETECTION
   (Framework, CSS system, DB ORM, state manager, engine)
                             │
                             ▼
                 12-ARCHETYPE CLASSIFICATION
   (Fullstack SaaS, 3D Game, AI Agent, Mobile App, etc.)
                             │
                             ▼
                      SKILL SELECTION
     (Mobilize specialized skills with confidence scores)
                             │
                             ▼
                   ENGINEERING EXECUTION
  (PRD/GDD ➔ Design System ➔ Core Engine ➔ API & DB ➔ Security)
                             │
                             ▼
                  PRODUCTION VERIFICATION
     (8-Dimension Production Audit & Playwright E2E)
                             │
                             ▼
                  AUTONOMOUS SELF-HEALING
          (6-Step closed loop repair if tests fail)
                             │
                             ▼
                     PRODUCTION RELEASE
             (Docker, CI/CD, Zero-Downtime Deploy)
```

---

## 2. Master Command Center: Unified Matrix

The following table documents all 14 Primary Workflow Commands, their operational scope, mobilized skills, source repository attribution, and dedicated runbooks:

| No. | Master Command | Category | Operational Scope & Mission | Key Skills Mobilized | Upstream Source Repositories | Target Runbook |
|:---:|---|---|---|---|---|:---:|
| **01** | `/sr24-auto [task]` | Orchestration | Inspects workspace, identifies stack & archetype, activates matching squad | `sr24-intelligence-engine`, `sr24-production-auditor`, `sr24-self-healing-engineer` | [agency-agents](https://github.com/msitarzewski/agency-agents), [agent-skills](https://github.com/addyosmani/agent-skills), [SR24Plus](https://github.com/sahil24raj/SR24plus-engineering-toolkit/tree/main/skills/sr24-custom-engineering) | [`SR24-AUTO.md`](../00-MASTER-CONTROLLER/workflows/SR24-AUTO.md) |
| **02** | `/sr24-web-dev [task]` | Web Development | Executes complete 12-phase web application lifecycle from PRD to cloud deploy | `bulletproof-react`, `supabase-engineering`, `drizzle-orm`, `antislop-ui`, `lago-billing` | [bulletproof-react](https://github.com/alan2207/bulletproof-react), [agent-skills](https://github.com/vercel-labs/agent-skills), [agent-skills](https://github.com/addyosmani/agent-skills) | [`README-SR24-WEB-DEV.md`](./README-SR24-WEB-DEV.md) |
| **03** | `/sr24-game-dev [task]` | Game Development | End-to-end 12-phase game development across WebGL 2D/3D, Rapier, and Unity 3D | `rapier-physics`, `colyseus-multiplayer`, `threejs-game-engine`, `truck-physics-engineer` | [three.js](https://github.com/mrdoob/three.js), [rapier](https://github.com/dimforge/rapier), [colyseus](https://github.com/colyseus/colyseus) | [`README-SR24-GAME-DEV.md`](./README-SR24-GAME-DEV.md) |
| **04** | `/sr24-saas [task]` | SaaS Platforms | Multi-tenant SaaS, subscription billing, multi-tier auth, dashboard HUD, SRE | `razorpay-upi-specialist`, `indian-gst-billing-engineer`, `lago-billing`, `prisma-orm` | [lago](https://github.com/getlago/lago), [prisma](https://github.com/prisma/prisma), [SR24Plus](https://github.com/sahil24raj/SR24plus-engineering-toolkit/tree/main/skills/sr24-custom-engineering) | [`SR24-SAAS.md`](../00-MASTER-CONTROLLER/workflows/SR24-SAAS.md) |
| **05** | `/sr24-fullstack [task]` | Fullstack Engineering | TypeScript contracts, database schemas, REST/tRPC APIs, responsive interfaces | `zod-schema-validation`, `drizzle-orm`, `node-best-practices`, `component-intelligence` | [zod](https://github.com/colinhacks/zod), [drizzle-orm](https://github.com/drizzle-team/drizzle-orm), [nodebestpractices](https://github.com/goldbergyoni/nodebestpractices) | [`SR24-FULLSTACK.md`](../00-MASTER-CONTROLLER/workflows/SR24-FULLSTACK.md) |
| **06** | `/sr24-browser-game [task]` | Browser Gaming | 60 FPS HTML5/WebGL games, fixed-timestep loop, mobile virtual controls, game feel | `browser-game-architect`, `threejs-game-engine`, `matter-js-physics`, `howler-js-audio` | [three.js](https://github.com/mrdoob/three.js), [matter-js](https://github.com/liabru/matter-js), [howler.js](https://github.com/goldfire/howler.js) | [`SR24-BROWSER-GAME.md`](../00-MASTER-CONTROLLER/workflows/SR24-BROWSER-GAME.md) |
| **07** | `/sr24-multiplayer [task]` | Multiplayer Networking | Authoritative low-latency game servers, client prediction, reconciliation, rooms | `colyseus-multiplayer`, `socketio-realtime`, `redis-in-memory-datastore`, `gaffer-on-games-networking` | [colyseus](https://github.com/colyseus/colyseus), [socket.io](https://github.com/socketio/socket.io), [redis](https://github.com/redis/redis) | [`SR24-MULTIPLAYER.md`](../00-MASTER-CONTROLLER/workflows/SR24-MULTIPLAYER.md) |
| **08** | `/sr24-unity [task]` | Native 3D Engines | Unity 2D/3D development, ScriptableObjects, URP shaders, audio mixers, builds | `unity-cli`, `urp-postprocessing`, `initialize-ai-navigation`, `setup-multiplayer-services` | [Unity Technologies](https://unity.com), [agency-agents](https://github.com/msitarzewski/agency-agents) | [`SR24-UNITY.md`](../00-MASTER-CONTROLLER/workflows/SR24-UNITY.md) |
| **09** | `/sr24-racing-game [task]` | Vehicle Simulation | Heavy truck & vehicle physics, WheelColliders, Ackermann steering, banked tracks | `truck-physics-engineer`, `realistic-car-controller-engineer`, `racing-track-design-engineer` | [SR24Plus](https://github.com/sahil24raj/SR24plus-engineering-toolkit/tree/main/skills/sr24-custom-engineering), [Unity](https://unity.com) | [`SR24-RACING-GAME.md`](../00-MASTER-CONTROLLER/workflows/SR24-RACING-GAME.md) |
| **10** | `/sr24-ai [task]` | AI & Agent Systems | Production AI systems, MCP servers, prompt injection defense, hybrid RAG | `prompt-injection-security-engineer`, `agency-specialized-mcp-builder`, `agency-engineering-prompt-engineer` | [agency-agents](https://github.com/msitarzewski/agency-agents), [SR24Plus](https://github.com/sahil24raj/SR24plus-engineering-toolkit/tree/main/skills/sr24-custom-engineering) | [`SR24-AI.md`](../00-MASTER-CONTROLLER/workflows/SR24-AI.md) |
| **11** | `/sr24-design [task]` | UI/UX & Design Systems | Bespoke design system, 4px/8px tokens, anti-AI-slop audit, finish-gate critique | `impeccable`, `antislop-ui`, `taste-skill`, `ui-ux-pro-max`, `axe-core-accessibility` | [impeccable](https://github.com/pbakaus/impeccable), [anti-slop](https://github.com/miqdadbadjuber/anti-slop), [taste-skill](https://github.com/Leonxlnx/taste-skill), [ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | [`SR24-DESIGN.md`](../00-MASTER-CONTROLLER/workflows/SR24-DESIGN.md) |
| **12** | `/sr24-security [task]` | Security & Hardening | AppSec, OWASP Top 10 hardening, secret scanning, dependency audit, CSP/CORS | `owasp-zap-scanner`, `gitleaks-secret-detection`, `trivy-security-scanner`, `osv-scanner` | [zaproxy](https://github.com/zaproxy/zaproxy), [gitleaks](https://github.com/gitleaks/gitleaks), [trivy](https://github.com/aquasecurity/trivy), [osv-scanner](https://github.com/google/osv-scanner) | [`SR24-SECURITY.md`](../00-MASTER-CONTROLLER/workflows/SR24-SECURITY.md) |
| **13** | `/sr24-research [task]` | Evidence & Research | Literature search, market sizing, competitive analysis, empirical synthesis | `firecrawl-scraper`, `tavily-search-intelligence`, `agency-research-synthesist` | [firecrawl](https://github.com/firecrawl/firecrawl), [tavily-python](https://github.com/tavily-ai/tavily-python), [agency-agents](https://github.com/msitarzewski/agency-agents) | [`SR24-RESEARCH.md`](../00-MASTER-CONTROLLER/workflows/SR24-RESEARCH.md) |
| **14** | `/sr24-ship [task]` | DevOps & Release | Production containerization, GitHub Actions CI, health checks, zero-downtime deploy | `docker-containerization`, `github-actions-ci`, `sentry-monitoring`, `opentofu-iac` | [docker-docs](https://github.com/docker/docs), [actions-runner](https://github.com/actions/runner), [sentry](https://github.com/getsentry/sentry), [opentofu](https://github.com/opentofu/opentofu) | [`SR24-SHIP.md`](../00-MASTER-CONTROLLER/workflows/SR24-SHIP.md) |

---

## 3. Core Intelligence Layer Commands

In addition to the 14 Primary Workflow Commands, the toolkit exposes 4 operational commands powered by the Core Intelligence Layer:

| Command | Purpose | Output / Artifact |
|---|---|---|
| **`/sr24-orchestrate [dir]`** | Statically audits codebase, detects tech stack, classifies into 12 archetypes, and generates ranked skill plan. | CLI Matrix + JSON Plan |
| **`/sr24-audit-prod [dir]`** | Audits 8 production dimensions (Architecture, UI/UX, Frontend, Backend, DB, Security, Game, DevOps). | `reports/SR24-PRODUCTION-AUDIT.md` |
| **`/sr24-heal [test_cmd]`** | Autonomous 6-step closed-loop repair engine (Detect ➔ Diagnose ➔ Plan ➔ Repair ➔ Test ➔ Verify). Capped at 3 retries. | Minimal Git Patch & Clean Test Run |
| **`/sr24-full-check`** | Autonomous orchestrator: Intelligence Scan ➔ Production Audit ➔ Self-Healing ➔ Regression Test ➔ Ship Gate. | Comprehensive Release Certification |

---

## 4. Deep-Dive Command Specifications

### 01. `/sr24-auto [task]`
- **Mission**: Universal entry point for any engineering request. Analyzes existing workspace files (e.g. `package.json`, `Cargo.toml`, `go.mod`, Unity project configs) and dynamically routes to the highest-scoring squad.
- **Example**:
  ```text
  /sr24-auto Refactor multiplayer matchmaking to support 8-player room lobbies with Redis caching
  ```
- **Execution Runbook**: [`00-MASTER-CONTROLLER/workflows/SR24-AUTO.md`](../00-MASTER-CONTROLLER/workflows/SR24-AUTO.md)

### 02. `/sr24-web-dev [task]`
- **Mission**: Orchestrates the entire 12-phase web application lifecycle. Enforces design contracts, anti-slop rules, server-side data fetching, normalized schemas, and zero-flake E2E tests.
- **Example**:
  ```text
  /sr24-web-dev Build a remote team sprint retrospective SaaS with real-time voting and PDF exports
  ```
- **Execution Runbook**: [`docs/README-SR24-WEB-DEV.md`](./README-SR24-WEB-DEV.md)

### 03. `/sr24-game-dev [task]`
- **Mission**: Flagship 12-phase game development squad. Spans deterministic 60Hz physics loops, WebGL shaders, Rapier 3D colliders, authoritative networking, and native Unity 3D scenes.
- **Example**:
  ```text
  /sr24-game-dev Develop a 3D highway runner with obstacle lanes, dynamic speed curves, and boss fights
  ```
- **Execution Runbook**: [`docs/README-SR24-GAME-DEV.md`](./README-SR24-GAME-DEV.md)

### 04. `/sr24-saas [task]`
- **Mission**: Targeted SaaS platform engineering. Implements multi-tenant organizational isolation, Stripe/Razorpay subscription webhooks, usage-based metering via Lago, and audit logs.
- **Example**:
  ```text
  /sr24-saas Implement multi-tenant B2B billing with tiered usage limits and GST invoices
  ```
- **Execution Runbook**: [`00-MASTER-CONTROLLER/workflows/SR24-SAAS.md`](../00-MASTER-CONTROLLER/workflows/SR24-SAAS.md)

### 05. `/sr24-fullstack [task]`
- **Mission**: End-to-end fullstack feature delivery. Bridges frontend forms with backend validation via Zod schemas, executes safe database migrations via Drizzle/Prisma, and secures API endpoints.
- **Example**:
  ```text
  /sr24-fullstack Create a user profile settings page with avatar upload and two-factor auth toggle
  ```
- **Execution Runbook**: [`00-MASTER-CONTROLLER/workflows/SR24-FULLSTACK.md`](../00-MASTER-CONTROLLER/workflows/SR24-FULLSTACK.md)

### 06. `/sr24-browser-game [task]`
- **Mission**: 60 FPS HTML5 Canvas and WebGL game development. Implements accumulator timestep loops, mobile virtual joypads, sprite sheet animation, audio management with Howler.js, and asset preloading.
- **Example**:
  ```text
  /sr24-browser-game Create an arcade space combat game with particle thrusters and sound FX
  ```
- **Execution Runbook**: [`00-MASTER-CONTROLLER/workflows/SR24-BROWSER-GAME.md`](../00-MASTER-CONTROLLER/workflows/SR24-BROWSER-GAME.md)

### 07. `/sr24-multiplayer [task]`
- **Mission**: Authoritative server architecture for real-time multiplayer titles. Features client-side prediction, entity reconciliation, binary message serialization, and room matchmaking.
- **Example**:
  ```text
  /sr24-multiplayer Set up Colyseus state synchronization for 4-player arena combat with lag compensation
  ```
- **Execution Runbook**: [`00-MASTER-CONTROLLER/workflows/SR24-MULTIPLAYER.md`](../00-MASTER-CONTROLLER/workflows/SR24-MULTIPLAYER.md)

### 08. `/sr24-unity [task]`
- **Mission**: Professional Unity 2D/3D development. Integrates ScriptableObjects for decoupled event architecture, URP post-processing volumes, NavMesh agents, and headless command-line builds.
- **Example**:
  ```text
  /sr24-unity Configure URP bloom post-processing and create a patrol state machine for enemy AI
  ```
- **Execution Runbook**: [`00-MASTER-CONTROLLER/workflows/SR24-UNITY.md`](../00-MASTER-CONTROLLER/workflows/SR24-UNITY.md)

### 09. `/sr24-racing-game [task]`
- **Mission**: High-fidelity vehicle physics simulation. Models 16-wheeler heavy trucks, Ackermann steering angles, Pacejka slip curves, engine RPM torque curves, and mountain hairpin tracks.
- **Example**:
  ```text
  /sr24-racing-game Calibrate truck suspension damping, air brake friction, and road banking for ghat roads
  ```
- **Execution Runbook**: [`00-MASTER-CONTROLLER/workflows/SR24-RACING-GAME.md`](../00-MASTER-CONTROLLER/workflows/SR24-RACING-GAME.md)

### 10. `/sr24-ai [task]`
- **Mission**: Enterprise AI and agent engineering. Builds MCP (Model Context Protocol) servers, guards against prompt injection attacks, formats structured output with Zod, and creates RAG vector indexes.
- **Example**:
  ```text
  /sr24-ai Implement an MCP server for semantic database queries with strict query sanitization
  ```
- **Execution Runbook**: [`00-MASTER-CONTROLLER/workflows/SR24-AI.md`](../00-MASTER-CONTROLLER/workflows/SR24-AI.md)

### 11. `/sr24-design [task]`
- **Mission**: Senior design engineering and anti-AI-slop gating. Audits interfaces for generic templates, enforces mathematical 4px/8px layout grids, validates WCAG AA contrast, and curates typography.
- **Example**:
  ```text
  /sr24-design Audit the landing page hero section for AI slop and align spacing to an 8px grid
  ```
- **Execution Runbook**: [`00-MASTER-CONTROLLER/workflows/SR24-DESIGN.md`](../00-MASTER-CONTROLLER/workflows/SR24-DESIGN.md)

### 12. `/sr24-security [task]`
- **Mission**: Rigorous DevSecOps and AppSec auditing. Scans for hardcoded API keys via Gitleaks, validates dependencies with OSV/Trivy, checks OWASP Top 10 vulnerabilities, and configures CSP headers.
- **Example**:
  ```text
  /sr24-security Run a full-spectrum security audit on API routes and sanitize SQL injection attack vectors
  ```
- **Execution Runbook**: [`00-MASTER-CONTROLLER/workflows/SR24-SECURITY.md`](../00-MASTER-CONTROLLER/workflows/SR24-SECURITY.md)

### 13. `/sr24-research [task]`
- **Mission**: Evidence-backed academic, competitive, and technological research. Synthesizes literature, scrapes documentation with Firecrawl, conducts market discovery, and validates claims.
- **Example**:
  ```text
  /sr24-research Benchmark database performance between Supabase PostgreSQL and PlanetScale MySQL
  ```
- **Execution Runbook**: [`00-MASTER-CONTROLLER/workflows/SR24-RESEARCH.md`](../00-MASTER-CONTROLLER/workflows/SR24-RESEARCH.md)

### 14. `/sr24-ship [task]`
- **Mission**: Autonomous production shipping. Generates multi-stage Dockerfiles, sets up GitHub Actions CI pipelines, configures Sentry error monitoring, and verifies green healthcheck endpoints.
- **Example**:
  ```text
  /sr24-ship Package the Next.js frontend and Node.js backend into production Docker containers with CI/CD
  ```
- **Execution Runbook**: [`00-MASTER-CONTROLLER/workflows/SR24-SHIP.md`](../00-MASTER-CONTROLLER/workflows/SR24-SHIP.md)
