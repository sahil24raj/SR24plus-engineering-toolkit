# SR24Plus Technology Ecosystem & Supported Stack Reference
### Technical Capabilities, Framework Integrations, Engines, and Tooling Tiers

> **Ecosystem Standard**: 100% Tested & Verified • Zero Marketing Hallucinations  
> **Repository**: [https://github.com/sahil24raj/SR24plus-engineering-toolkit.git](https://github.com/sahil24raj/SR24plus-engineering-toolkit.git)  
> **Maintainer**: Sahil Raj (SR24Plus)  

---

## 1. Ecosystem Overview & Support Tiers

The **SR24Plus Engineering Toolkit** categorizes its technology integrations into three distinct operational tiers to prevent confusion between fully verified code systems and optional references:

- **Tier 1: Fully Integrated & Verified** — Supported by dedicated skills, operational scripts, automated unit tests, and production blueprints in the repository.
- **Tier 2: Supported via Upstream Integration** — Mobilized through canonical skills with pre-configured schemas, linters, or engine bridges.
- **Tier 3: Architectural Reference / Planned** — Documented integration paths and architectural recommendations for future engine expansions.

---

## 2. Web Development Stack

```
                               WEB STACK
   ┌───────────────────────────────┼──────────────────────────────┐
   ▼                               ▼                              ▼
FRONTEND                        BACKEND                       DATABASE
Next.js 14/15 (App Router)      Node.js (LTS) & TypeScript    PostgreSQL (15/16)
React 18/19                     FastAPI (Python 3.11+)        Supabase (RLS & Realtime)
TypeScript 5.x (Strict)         Express.js                    Drizzle ORM & Prisma
Tailwind CSS & 8px Tokens       BullMQ (Redis Queues)         Redis (In-Memory / PubSub)
Motion (Framer) & GSAP          Zod (Runtime Validation)      SQLite (WASM / Offline)
```

| Technology | Support Tier | Primary Skills Responsible | Operational Scope |
|---|:---:|---|---|
| **Next.js (App Router)** | **Tier 1** | `bulletproof-react`, `composition-patterns`, `react-best-practices` | Server Components, Server Actions, Route Handlers, Streaming Suspense. |
| **React 18 / 19** | **Tier 1** | `bulletproof-react`, `react-testing-library`, `component-intelligence` | Concurrent features, hooks, strict mode, state management. |
| **TypeScript (Strict)** | **Tier 1** | `typescript-eslint`, `zod-schema-validation` | Strict typing, `no-explicit-any`, exhaustive pattern matching. |
| **Tailwind CSS** | **Tier 1** | `antislop-ui`, `impeccable`, `component-intelligence` | Utility styling, design tokens, mathematical 4px/8px rhythm. |
| **Motion / Framer** | **Tier 1** | `motion-animations` | Layout animations, spring physics, exit transitions. |
| **GSAP (GreenSock)** | **Tier 1** | `gsap-animations` | 60 FPS timeline choreography, ScrollTrigger, GPU tweens. |
| **Node.js** | **Tier 1** | `node-best-practices` | Layered backend architecture, process lifecycles, error handlers. |
| **FastAPI** | **Tier 2** | `agency-engineering-backend-architect` | High-throughput async REST endpoints, Pydantic schemas. |
| **PostgreSQL** | **Tier 1** | `supabase-engineering`, `drizzle-orm`, `prisma-orm` | Normalized relational tables, indexed foreign keys, RLS policies. |
| **Supabase** | **Tier 1** | `supabase-engineering` | PostgreSQL Row Level Security, Edge Functions, realtime events. |
| **Drizzle ORM** | **Tier 1** | `drizzle-orm` | Zero-overhead type-safe SQL queries for Serverless & Edge. |
| **Prisma ORM** | **Tier 1** | `prisma-orm`, `dbml-schema-design` | Declarative `schema.prisma` models, migrations, client queries. |
| **Redis** | **Tier 1** | `redis-in-memory-datastore`, `bullmq-job-queues` | Key-value caching, distributed job queues, rate limiters. |
| **Razorpay / UPI** | **Tier 1** | `razorpay-upi-specialist` | Dynamic UPI QR generation, Orders API, HMAC webhook verification. |
| **Indian GST Math**| **Tier 1** | `indian-gst-billing-engineer` | Exact CGST, SGST, IGST calculations and thermal receipt formatting. |
| **Lago** | **Tier 1** | `lago-billing` | Open-source usage metering and hybrid subscription billing. |

---

## 3. Game Development & 3D Physics Stack

```
                              GAMEDEV STACK
   ┌───────────────────────────────┼──────────────────────────────┐
   ▼                               ▼                              ▼
ENGINES & RENDERING             PHYSICS ENGINES               MULTIPLAYER
Three.js (WebGL PBR)            Rapier 3D / 2D (WASM)         Colyseus (Authoritative 60Hz)
React Three Fiber (R3F)         Jolt Physics (AAA Vehicles)   Nakama (Matchmaking & State)
Phaser 3 & PixiJS               Matter.js (2D Rigid Bodies)   WebSockets & Socket.IO
Unity Engine (URP & DOTS)       Unity PhysX 3D                Redis (Matchmaking Lobbies)
```

| Technology | Support Tier | Primary Skills Responsible | Operational Scope |
|---|:---:|---|---|
| **Three.js** | **Tier 1** | `threejs-game-engine`, `threejs-optimization-profiling` | WebGL 3D scenes, PBR materials, instancing, shadow maps. |
| **React Three Fiber (R3F)** | **Tier 1** | `react-three-fiber`, `threejs-ui-hud` | Declarative 3D components, Drei helpers, Suspense loading. |
| **Phaser 3** | **Tier 1** | `phaser-game-engine` | 2D arcade physics, tilemap renderers, sprite sheets, game loops. |
| **PixiJS** | **Tier 1** | `pixijs-engine` | High-speed 2D WebGL sprite batching and canvas rendering. |
| **Unity Engine 2022/6**| **Tier 1** | `unity-cli`, `urp-postprocessing`, `unity-entities-ecs` | C# ScriptableObjects, URP Volume shaders, DOTS/ECS, builds. |
| **Rapier (2D & 3D)** | **Tier 1** | `rapier-physics`, `react-three-rapier` | WASM-accelerated deterministic physics, kinematic controllers. |
| **Jolt Physics** | **Tier 1** | `jolt-physics` | Multithreaded vehicle physics, suspension raycasts, ragdolls. |
| **Matter.js** | **Tier 1** | `matter-js-physics` | 2D rigid bodies, constraint chains, collision filters. |
| **Colyseus** | **Tier 1** | `colyseus-multiplayer` | Authoritative 60Hz server tick, schema-based state sync. |
| **Nakama** | **Tier 1** | `nakama-backend` | Distributed multiplayer, matchmaking, chat, user storage. |
| **Howler.js** | **Tier 1** | `howler-js-audio` | Web Audio API management, 3D spatial audio, audio sprites. |
| **bitECS** | **Tier 1** | `bitecs-architecture` | Zero-GC TypedArray Entity Component System for JavaScript. |
| **glTF-Transform** | **Tier 1** | `gltf-transform-pipeline` | DRACO geometry compression, KTX2/Basis texture transcoding. |
| **Blender (Headless)**| **Tier 1** | `blender-pipeline` | Headless Python scripting, LOD baking, model batch exports. |

---

## 4. AI, Agents & Autonomous Systems

```
                                AI & ORCHESTRATION
   ┌───────────────────────────────────┼──────────────────────────────────┐
   ▼                                   ▼                                  ▼
CORE INTELLIGENCE                   AGENT PERSONAS                    AI DEFENSE
SR24 Intelligence Engine            301 Agency Personas               Prompt Injection Defense
SR24 Production Auditor             Addy Osmani Engineering Skills     MCP Server Builder
SR24 Self-Healing Engineer          Google Antigravity Swarms          Structured Zod Outputs
```

| Technology | Support Tier | Primary Skills Responsible | Operational Scope |
|---|:---:|---|---|
| **SR24 Core Intelligence**| **Tier 1** | `sr24-intelligence-engine`, `sr24-production-auditor`, `sr24-self-healing-engineer` | Codebase discovery, 8-dimension audit, 6-step closed-loop repair. |
| **Model Context Protocol (MCP)**| **Tier 1** | `agency-specialized-mcp-builder`, `mcp-server-developer` | Custom tool creation, resource endpoints, agent MCP contracts. |
| **Prompt Injection Defense**| **Tier 1** | `prompt-injection-security-engineer` | Delimiter defense, jailbreak detection, input sanitization. |
| **RAG & Search Intelligence**| **Tier 1** | `tavily-search-intelligence`, `firecrawl-scraper` | Real-time factual web search, clean markdown extraction. |
| **Agent Swarms** | **Tier 1** | `antigravity-core` (`swarm`) | Shared message board multi-agent coordination. |

---

## 5. Quality Engineering, DevOps & SRE Stack

```
                              QUALITY & DEVOPS
   ┌───────────────────────────────────┼──────────────────────────────────┐
   ▼                                   ▼                                  ▼
TESTING & QA                        DEVSECOPS                         DEPLOYMENT & SRE
Playwright (Cross-Browser E2E)      OWASP ZAP (DAST Scans)            Docker Multi-Stage
Lost Pixel (Visual Diffing)         Gitleaks (Secret Detection)       GitHub Actions CI/CD
Grafana k6 (Load & Stress)          Aqua Trivy & Google OSV (CVEs)    OpenTofu (IaC Cloud)
Bruno (Offline API Tests)           Axe-Core (WCAG Accessibility)     Sentry APM & PostHog
```

| Technology | Support Tier | Primary Skills Responsible | Operational Scope |
|---|:---:|---|---|
| **Playwright** | **Tier 1** | `playwright-testing`, `gameplay-regression-testing` | Headless/headed E2E tests, network mocking, canvas interactions. |
| **Lost Pixel** | **Tier 1** | `lost-pixel-visual-regression` | Automated screenshot regression diffing with pixel thresholds. |
| **Grafana k6** | **Tier 1** | `k6-load-testing` | High-concurrency virtual user HTTP/WebSocket load benchmarks. |
| **Bruno** | **Tier 1** | `bruno-api-testing` | Git-friendly offline-first API collection test automation. |
| **OWASP ZAP** | **Tier 1** | `owasp-zap-scanner` | Dynamic application security testing & vulnerability fuzzing. |
| **Gitleaks** | **Tier 1** | `gitleaks-secret-detection` | Pre-commit Git commit history and working tree secret scanning. |
| **Aqua Trivy & OSV**| **Tier 1** | `trivy-security-scanner`, `osv-scanner` | Lockfile CVE auditing, container image and IaC misconfiguration. |
| **Docker** | **Tier 1** | `docker-containerization` | Optimized multi-stage builds, Alpine base images, compose stacks. |
| **GitHub Actions** | **Tier 1** | `github-actions-ci`, `ci-cd-and-automation` | Matrix build runners, test execution, automated deployments. |
| **OpenTofu / Terraform**| **Tier 1** | `opentofu-iac` | Declarative Infrastructure-as-Code state locking and cloud provisioning. |
| **Sentry** | **Tier 1** | `sentry-monitoring` | Error crash alerting, performance APM, sourcemap resolution. |
| **PostHog & Clarity**| **Tier 1** | `posthog-analytics`, `microsoft-clarity` | User event telemetry, session recordings, scroll & heatmaps. |
