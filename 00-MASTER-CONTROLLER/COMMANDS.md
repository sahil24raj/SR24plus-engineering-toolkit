# SR24PLUS MASTER COMMAND REFERENCE (v2.5)

The SR24Plus Engineering Toolkit provides **14 Primary Workflow Commands** for end-to-end multi-agent execution, **2 Dedicated Master Production Profiles**, and **14 Category Squad Shorthand Triggers**.

---

## 1. Primary Engineering Workflow Commands

| # | Primary Command | Scope & Mission | Target Runbook |
|---|---|---|---|
| **1** | **`/sr24-auto [task]`** | Automatically inspects project workspace, detects framework & stack, and selects matching squad | [`SR24-AUTO.md`](./workflows/SR24-AUTO.md) |
| **2** | **`/sr24-web-dev [task]`** | Complete 12-phase squad for modern web applications from PRD to production deploy | [`README-SR24-WEB-DEV.md`](../docs/README-SR24-WEB-DEV.md) |
| **3** | **`/sr24-game-dev [task]`** | Professional end-to-end game development squad (Browser WebGL, HTML5 Canvas & Unity 3D) | [`README-SR24-GAME-DEV.md`](../docs/README-SR24-GAME-DEV.md) |
| **4** | **`/sr24-saas [task]`** | Multi-tenant SaaS platform, subscription billing, multi-tier auth, dashboard HUD, SRE launch | [`SR24-SAAS.md`](./workflows/SR24-SAAS.md) |
| **5** | **`/sr24-fullstack [task]`** | End-to-end feature engineering: TypeScript contracts, SQL migrations, API routes, responsive UI | [`SR24-FULLSTACK.md`](./workflows/SR24-FULLSTACK.md) |
| **6** | **`/sr24-browser-game [task]`**| 60 FPS HTML5/WebGL browser games, fixed timestep loop, mobile virtual controls, game feel | [`SR24-BROWSER-GAME.md`](./workflows/SR24-BROWSER-GAME.md) |
| **7** | **`/sr24-multiplayer [task]`** | Low-latency authoritative game servers, client prediction, reconciliation, 4-character room codes | [`SR24-MULTIPLAYER.md`](./workflows/SR24-MULTIPLAYER.md) |
| **8** | **`/sr24-unity [task]`** | Complete Unity 2D/3D game development, ScriptableObjects, URP shaders, audio mixers, builds | [`SR24-UNITY.md`](./workflows/SR24-UNITY.md) |
| **9** | **`/sr24-racing-game [task]`** | Heavy truck & car physics, WheelColliders, Ackermann steering, ghat road tracks, audio | [`SR24-RACING-GAME.md`](./workflows/SR24-RACING-GAME.md) |
| **10**| **`/sr24-ai [task]`** | Production AI systems, MCP servers, prompt injection defense, hybrid RAG, offline rule fallbacks | [`SR24-AI.md`](./workflows/SR24-AI.md) |
| **11**| **`/sr24-design [task]`** | Bespoke design system, 4px/8px mathematical tokens, anti-AI-slop audit, finish-gate critique | [`SR24-DESIGN.md`](./workflows/SR24-DESIGN.md) |
| **12**| **`/sr24-security [task]`** | Comprehensive AppSec, OWASP Top 10, secret scanning, SQL injection, CSP/CORS hardening | [`SR24-SECURITY.md`](./workflows/SR24-SECURITY.md) |
| **13**| **`/sr24-qa [task]`** | Automated Playwright E2E suites, visual regression, systematic debugging, test evidence | [`SR24-SHIP.md`](./workflows/SR24-SHIP.md) |
| **14**| **`/sr24-ship [task]`** | Production build verification, Docker, CI/CD pipeline, healthchecks, rollback strategy | [`SR24-SHIP.md`](./workflows/SR24-SHIP.md) |

---

## 2. Dedicated Master Production Profiles

| Project Command | Target Production Profile | Activated Specialist Squad |
|---|---|---|
| `/sr24-saas [dukan-sathi / exam-loop / saas]` | [`FULLSTACK-SAAS-PROFILE.md`](./projects/FULLSTACK-SAAS-PROFILE.md) | SaaS Architect + Offline Kirana Lead + Indian GST Specialist + Razorpay UPI + Assessment Lead + Anti-Slop UI |
| `/sr24-browser-game [vibe-arena / game]` | [`BROWSER-GAMING-PROFILE.md`](./projects/BROWSER-GAMING-PROFILE.md) | Browser Game Architect + WebSocket Multiplayer + Anti-Cheat Engineer + Combat Mechanics + Web Audio Lead |

---

## 3. Category Squad Shorthand Triggers

| Shorthand Trigger | Natural Language Command | Activated Domain |
|---|---|---|
| `/sr24 ui` | *"Activate UI Design Toolkit"* | 01 - UI/UX Design & Anti-Slop |
| `/sr24 game` | *"Activate Game Development Toolkit"* | 02 - Game Development (Unity/UE/Godot/Web) |
| `/sr24 frontend` | *"Activate Frontend Development Toolkit"* | 03 - Modern Frontend, WebGL & Motion |
| `/sr24 backend` | *"Activate Backend Development Toolkit"* | 04 - Scalable APIs, Databases & Auth |
| `/sr24 ai` | *"Activate AI/ML Engineering Toolkit"* | 05 - LLM Training, Prompting & RAG |
| `/sr24 mobile` | *"Activate Mobile App Toolkit"* | 06 - Native Android/iOS & Desktop |
| `/sr24 devops` | *"Activate DevOps & Cloud Toolkit"* | 07 - CI/CD Pipelines, SRE & Docker |
