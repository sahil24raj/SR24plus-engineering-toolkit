# SR24PLUS MASTER SKILL ROUTER (v2.0)
## Multi-Specialist Autonomous Orchestration Engine

The **SR24Plus Master Skill Router** is the intelligent command router and autonomous multi-agent orchestration layer for all 443 canonical engineering skills installed in the Google Antigravity environment.

Instead of running isolated prompts or invoking single narrow skills, the Master Router interprets user engineering requests, inspects existing workspaces, selects the minimum sufficient squad of specialists, loads their actual `SKILL.md` instructions, and coordinates execution through strict dependency-ordered phases.

---

## 1. Primary Commands & Dedicated Workflows

The Master Router supports 9 dedicated engineering commands. Each command is bound to an executable workflow runbook in `00-MASTER-CONTROLLER/workflows/`:

| Primary Command | Target Workflow Runbook | Squad Composition | Core Deliverables |
|---|---|---|---|
| **`/sr24-web-dev [task]`** | [`SR24-WEB-DEV.md`](./workflows/SR24-WEB-DEV.md) | Product + Branding + UX + UI + Anti-Slop + Frontend + Backend + Security + QA + DevOps | Complete production web app, PRD, zero AI slop, clean responsive UI, fullstack code |
| **`/sr24-game-dev [task]`** | [`SR24-GAME-DEV.md`](./workflows/SR24-GAME-DEV.md) | Game Design + Narrative + Tech Art + Engine (Unity/UE/Godot/Web) + Gameplay + Audio + QA | Playable core loop, GDD, custom shaders/VFX, responsive HUD, 60+ FPS |
| **`/sr24-saas [task]`** | [`SR24-SAAS.md`](./workflows/SR24-SAAS.md) | Product + Enterprise Brand + High-Density UI + Multi-Tenancy + Auth + Stripe + SRE | Production SaaS platform, tenant isolation, billing webhooks, RBAC |
| **`/sr24-design [task]`** | [`SR24-DESIGN.md`](./workflows/SR24-DESIGN.md) | UI Designer + Finish-Gate Reviewer + Impeccable + Anti-Slop + Whimsy + Design Tokens | Custom design system, contrast audit, mathematical spacing, anti-slop pass |
| **`/sr24-ai [task]`** | [`SR24-AI.md`](./workflows/SR24-AI.md) | AI Engineer + Prompt Engineer + RAG Architect + Data Remediation + AI Security | Robust LLM/Vision/Speech integration, structured JSON outputs, rule fallback |
| **`/sr24-security [task]`** | [`SR24-SECURITY.md`](./workflows/SR24-SECURITY.md) | AppSec Engineer + Security Architect + Cloud Security + Pen Tester + Code Auditor | OWASP Top 10 remediation, secret leak scanning, auth validation, hardened headers |
| **`/sr24-research [task]`** | [`SR24-RESEARCH.md`](./workflows/SR24-RESEARCH.md) | Research Synthesist + Statistician + ArXiv/PubMed + Bioinformatics + Reverse Eng | Peer-reviewed citations, empirical evidence matrix, market TAM/SAM analysis |
| **`/sr24-ship [task]`** | [`SR24-SHIP.md`](./workflows/SR24-SHIP.md) | DevOps Automator + SRE + CI/CD Automator + Launch Strategist + Technical Writer | Automated CI/CD pipeline, Docker/Vercel config, healthchecks, rollback plan |
| **`/sr24-fullstack [task]`** | [`SR24-FULLSTACK.md`](./workflows/SR24-FULLSTACK.md) | System Architect + Backend Architect + Database Optimizer + Frontend Dev + Senior Dev | Cohesive end-to-end features, strict TypeScript API contracts, database migrations |

---

## 2. Dynamic Stack & Workspace Detection Protocol

Before executing any code changes, the Master Router executes the following automated workspace inspection:

```
[User Command Received]
         │
         ▼
[Step 1: Workspace Scan] ──────── Inspect directory tree, package.json, configs
         │
         ▼
[Step 2: Stack Detection] ─────── Identify Framework (React/Vite/Next/FastAPI/Unity)
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

### Stack Detection Matrix:
- **Node.js / React / Next.js / Vite**: Detected via `package.json`. Activates `agency-engineering-frontend-developer` + `ui-ux-pro-max`.
- **Python / FastAPI / Django / Flask**: Detected via `requirements.txt`, `pyproject.toml`, `main.py`. Activates `agency-engineering-backend-architect` + `api-and-interface-design`.
- **Unity Engine**: Detected via `Assets/`, `ProjectSettings/`. Activates Unity architecture, shaders, and physics skills.
- **Godot Engine**: Detected via `project.godot`. Activates Godot gameplay scripter and shader skills.
- **Unreal Engine**: Detected via `*.uproject`. Activates Unreal systems engineer and technical artist skills.

---

## 3. Genuine Antigravity Invocation Mechanisms

To ensure transparent execution without inventing non-existent features:

1. **Prompt Interception**:
   - The user triggers commands either by typing the exact command (e.g. `/sr24-web-dev build a billing dashboard`) or natural language equivalent (`"Build a professional billing website"`).
   - The assistant intercepts this command, loads the corresponding workflow file from `00-MASTER-CONTROLLER/workflows/`, and announces the active squad.
2. **Native Subagent Delegation (`invoke_subagent`)**:
   - Where deep independent exploration or review is required, the Master Router launches native subagents:
     - `research`: Broad codebase or documentation surveys.
     - `code-reviewer`: Architectural, correctness, and security code reviews.
     - `security-auditor`: Deep OWASP and vulnerability scans.
     - `test-engineer`: Test strategy, unit test authoring, and coverage.
     - `web-performance-auditor`: Core Web Vitals and performance audits.
3. **Instruction Grounding (`read_file`)**:
   - Skills are physically loaded by reading their installed `SKILL.md` paths. The instructions in the `SKILL.md` govern the constraints and output format of that phase.

---

## 4. Quality Gates & Anti-Slop Guarantees

Every workflow enforced by the Master Router contains mandatory, non-bypassable quality gates:
1. **The Anti-AI-Slop Gate**: Rejects unmotivated purple gradients, gratuitous glassmorphism, emoji icons, and generic 3-card layouts.
2. **The Security Gate**: Rejects hardcoded secrets, open CORS with credentials, and unparameterized SQL queries.
3. **The Build & Verification Gate**: Code must compile with 0 TypeScript/bundler errors (`npm run build`, `tsc`). No tasks are marked complete without real verification output.
