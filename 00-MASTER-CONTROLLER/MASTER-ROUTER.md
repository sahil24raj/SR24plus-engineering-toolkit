# SR24PLUS MASTER SKILL ROUTER (v2.5)
## Multi-Specialist Autonomous Orchestration Engine

The **SR24Plus Master Skill Router** is the intelligent routing engine and autonomous multi-agent orchestration layer for all 443+ engineering skills in Google Antigravity.

Instead of running isolated prompts or invoking single narrow skills, the Master Router interprets user engineering requests, inspects existing workspaces, selects the minimum sufficient squad of specialists, loads their actual `SKILL.md` instructions, and coordinates execution through strict dependency-ordered phases.

---

## 1. Primary Commands & Dedicated Workflows

The Master Router supports 14 dedicated engineering commands. Each command is bound to an executable workflow runbook in `00-MASTER-CONTROLLER/workflows/`:

| Primary Command | Target Workflow Runbook | Squad Composition | Core Deliverables |
|---|---|---|---|
| **`/sr24-auto [task]`** | [`SR24-AUTO.md`](./workflows/SR24-AUTO.md) | Dynamic Inspector + Auto-Selected Squad | Workspace diagnosis, stack detection, automatic squad deployment |
| **`/sr24-web-dev [task]`** | [`README-SR24-WEB-DEV.md`](../docs/README-SR24-WEB-DEV.md) | 12-Phase SaaS Squad: Product + Frontend + Backend + DB + Anti-Slop + QA | Complete web application, clean TypeScript contracts, responsive UI |
| **`/sr24-game-dev [task]`** | [`README-SR24-GAME-DEV.md`](../docs/README-SR24-GAME-DEV.md) | Game Designer + WebGL Architect + Netcode Lead + Physics + Audio + Anti-Cheat | Professional game development (HTML5/WebGL, Browser Arena, Unity 3D) |
| **`/sr24-saas [task]`** | [`SR24-SAAS.md`](./workflows/SR24-SAAS.md) | Product + Multi-Tenancy + Auth + Razorpay/Stripe + Offline Store + SRE | Production SaaS platform, tenant isolation, billing webhooks, RBAC |
| **`/sr24-fullstack [task]`** | [`SR24-FULLSTACK.md`](./workflows/SR24-FULLSTACK.md) | System Architect + Backend Architect + Database Optimizer + Frontend Dev | Cohesive end-to-end features, strict TypeScript API contracts, DB migrations |
| **`/sr24-browser-game [task]`**| [`SR24-BROWSER-GAME.md`](./workflows/SR24-BROWSER-GAME.md) | Browser Game Architect + Combat Mechanics + Game Feel + Asset Optimizer + Audio | 60 FPS HTML5/WebGL game, fixed timestep loop, mobile virtual controls |
| **`/sr24-multiplayer [task]`** | [`SR24-MULTIPLAYER.md`](./workflows/SR24-MULTIPLAYER.md) | WebSocket Multiplayer Engineer + Anti-Cheat Engineer + Realtime Systems | Authoritative server, client prediction, reconciliation, room lobbies |
| **`/sr24-unity [task]`** | [`SR24-UNITY.md`](./workflows/SR24-UNITY.md) | Unity Architect + Editor Tooling + Shader Graph Artist + Audio + Profiler | Complete Unity 2D/3D project, ScriptableObjects, URP shaders, builds |
| **`/sr24-racing-game [task]`** | [`SR24-RACING-GAME.md`](./workflows/SR24-RACING-GAME.md) | Truck Physics Engineer + Car Controller + Circuit Designer + Audio + VFX | Multi-axle truck physics, WheelColliders, ghat road circuits, tire smoke |
| **`/sr24-ai [task]`** | [`SR24-AI.md`](./workflows/SR24-AI.md) | AI Engineer + Prompt Engineer + RAG Architect + Data Remediation + AI Security | Robust LLM/Vision/Speech integration, structured JSON outputs, rule fallback |
| **`/sr24-design [task]`** | [`SR24-DESIGN.md`](./workflows/SR24-DESIGN.md) | UI Designer + Finish-Gate Reviewer + Impeccable + Anti-Slop + Whimsy | Custom design system, contrast audit, mathematical spacing, anti-slop pass |
| **`/sr24-security [task]`** | [`SR24-SECURITY.md`](./workflows/SR24-SECURITY.md) | AppSec Engineer + Security Architect + Cloud Security + Pen Tester + Code Auditor | OWASP Top 10 remediation, secret leak scanning, auth validation, hardened headers |
| **`/sr24-qa [task]`** | [`SR24-SHIP.md`](./workflows/SR24-SHIP.md) | Code Reviewer + Playwright Test Automator + Systematic Debugger + Reality Checker | Flake-free Playwright E2E tests, visual regression, passing build evidence |
| **`/sr24-ship [task]`** | [`SR24-SHIP.md`](./workflows/SR24-SHIP.md) | DevOps Automator + SRE + CI/CD Automator + Launch Strategist + Technical Writer | Automated CI/CD pipeline, Docker/Vercel config, healthchecks, rollback plan |

---

## 2. Dedicated Master Production Profiles

When working on user-specific initiatives, the Master Router deploys specialized production squad profiles from `00-MASTER-CONTROLLER/projects/`:
- **Profile 1: Full-Stack Production SaaS & Web Applications** (Dukan Sathi, ExamLoop, B2B SaaS): [`00-MASTER-CONTROLLER/projects/FULLSTACK-SAAS-PROFILE.md`](./projects/FULLSTACK-SAAS-PROFILE.md)
- **Profile 2: Browser-Based Multiplayer 3D/2D Gaming Platform** (Vibe Arena, Multiplayer WebGL/Canvas): [`00-MASTER-CONTROLLER/projects/BROWSER-GAMING-PROFILE.md`](./projects/BROWSER-GAMING-PROFILE.md)

---

## 3. Dynamic Stack & Workspace Detection Protocol

Before executing any code changes, the Master Router executes the following automated workspace inspection:

```
[User Command Received]
         │
         ▼
[Step 1: Workspace Scan] ──────── Inspect directory tree, package.json, configs
         │
         ▼
[Step 2: Stack Detection] ─────── Identify Framework (React/Vite/Next/FastAPI/Unity/Godot)
         │
         ▼
[Step 3: Specialist Selection] ── Match project requirements to exact SKILL.md paths
         │
         ▼
[Step 4: Instruction Loading] ─── Read actual SKILL.md files into reasoning context
         │
         ▼
[Step 5: Sequential Execution] ── Run Phase 1 -> Phase N with intermediate quality gates
```

---

## 4. Quality Gates & Anti-Slop Guarantees

Every workflow enforced by the Master Router contains mandatory, non-bypassable quality gates:
1. **The Anti-AI-Slop Gate**: Rejects unmotivated purple gradients, gratuitous glassmorphism, emoji icons, and generic 3-card layouts.
2. **The Security Gate**: Rejects hardcoded secrets, open CORS with credentials, and unparameterized SQL queries.
3. **The Build & Verification Gate**: Code must compile with 0 TypeScript/bundler errors (`npm run build`, `tsc`). No tasks are marked complete without real verification output.
