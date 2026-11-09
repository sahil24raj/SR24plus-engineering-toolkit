# SR24Plus Production Project Profiles
### Dedicated Architecture Blueprints for SaaS Web Apps & Real-Time Browser Games

[![Profiles](https://img.shields.io/badge/Production%20Profiles-2%20Consolidated%20Blueprints-blue.svg)](./PROJECT-USE-CASES.md)
[![SaaS](https://img.shields.io/badge/Profile%201-Full--Stack%20Production%20SaaS%20(Dukan%20Sathi%20%26%20ExamLoop)-emerald.svg)](#1-master-profile-full-stack-production-saas--web-applications)
[![Gaming](https://img.shields.io/badge/Profile%202-Real--Time%20Browser%20Multiplayer%20(Vibe%20Arena)-purple.svg)](#2-master-profile-browser-based-multiplayer-3d2d-gaming-platform)

---

## 1. Master Profile: Full-Stack Production SaaS & Web Applications
*(Used for **Dukan Sathi**, **ExamLoop**, Vernacular Commerce & B2B SaaS)*

- **Domain**: Production Full-Stack Web Applications, Offline-First Kirana Voice POS, AI Adaptive Testing Engines, and B2B Subscription Platforms.
- **Reference Runbook**: [`00-MASTER-CONTROLLER/projects/FULLSTACK-SAAS-PROFILE.md`](../00-MASTER-CONTROLLER/projects/FULLSTACK-SAAS-PROFILE.md)
- **Primary Commands**: `/sr24-saas [project]` or `/sr24-web-dev [project]` or `/sr24-fullstack [feature]`

### Target Project Implementations:
1. **Dukan Sathi (Vernacular Kirana Voice POS)**:
   - Vernacular Hindi speech billing (sub-300ms latency via Gnani Prisma v2.5 with local regex fallback).
   - 100% offline-first resilience: IndexedDB / SQLite WASM local storage with background FIFO sync queue when internet reconnects.
   - Indian GST calculation (CGST/SGST/IGST), HSN codes, and 80mm/58mm thermal receipt printing.
   - Razorpay dynamic UPI QR codes (`upi://pay`) and HMAC-SHA256 webhook reconciliation.
   - Dark glassmorphic aesthetic (`bg-zinc-900/60 backdrop-blur-xl`) with full-screen interactive 3D acoustic sphere background.
2. **ExamLoop (AI Adaptive Testing Engine)**:
   - Computer Adaptive Testing (CAT) algorithm driven by Item Response Theory (1PL Rasch Model) calibrating test difficulty to student ability ($\theta$).
   - Flawless mathematical and chemical symbol rendering via KaTeX with zero layout shift.
   - Sandboxed proctoring telemetry auditing window blurs and suspicious device switches.
   - Scalable question bank integration with JSON-RPC schemas and automated score reports.

### Specialist Squad & Upstream GitHub Sources:
| Responsibility | Specialist Skill | Upstream GitHub Repository |
|---|---|---|
| **SaaS System Architecture** | `agency-engineering-software-architect` + `saas-architect` | [`msitarzewski/agency-agents`](https://github.com/msitarzewski/agency-agents) |
| **Anti-AI-Slop Visuals** | `impeccable` + `antislop-ui` + `ui-ux-pro-max` | [`pbakaus/impeccable`](https://github.com/pbakaus/impeccable) & [`miqdadbadjuber/anti-slop`](https://github.com/miqdadbadjuber/anti-slop) |
| **Frontend Engineering** | `agency-engineering-frontend-developer` + `agency-engineering-senior-developer` | [`msitarzewski/agency-agents`](https://github.com/msitarzewski/agency-agents) |
| **Backend & API Routes** | `agency-engineering-backend-architect` | [`msitarzewski/agency-agents`](https://github.com/msitarzewski/agency-agents) |
| **Offline-First Storage** | `offline-first-kirana-architect` | `SR24Plus Custom Engineering` |
| **Database Tuning & Indexing**| `agency-engineering-database-optimizer` | [`msitarzewski/agency-agents`](https://github.com/msitarzewski/agency-agents) |
| **Indian Payments (UPI)** | `razorpay-upi-specialist` | `SR24Plus Custom Engineering` |
| **Indian GST Invoicing** | `indian-gst-billing-engineer` | `SR24Plus Custom Engineering` |
| **Adaptive Testing & Math** | `assessment-engine-architect` + `agency-academic-statistician` | `SR24Plus Custom Engineering` & [`msitarzewski/agency-agents`](https://github.com/msitarzewski/agency-agents) |
| **AppSec & Prompt Defense** | `agency-security-appsec-engineer` + `prompt-injection-security-engineer` | [`msitarzewski/agency-agents`](https://github.com/msitarzewski/agency-agents) & `SR24Plus Custom Engineering` |
| **E2E Test Automation** | `playwright-automation-engineer` + `test-driven-development` | `SR24Plus Custom Engineering` & [`addyosmani/agent-skills`](https://github.com/addyosmani/agent-skills) |
| **CI/CD & Deployment** | `agency-engineering-devops-automator` + `ci-cd-and-automation` | [`msitarzewski/agency-agents`](https://github.com/msitarzewski/agency-agents) & [`addyosmani/agent-skills`](https://github.com/addyosmani/agent-skills) |

### Copy-Paste Prompt for AI:
> *"Act as the SR24Plus Principal SaaS Architect & Full-Stack Squad. Build a production-grade full-stack SaaS application for [Dukan Sathi / ExamLoop / Web App]. Follow the 12-phase pipeline with strict TypeScript contracts, anti-AI-slop design, database migrations, authentication, billing, and automated Playwright test coverage with build evidence."*

---

## 2. Master Profile: Browser-Based Multiplayer 3D/2D Gaming Platform
*(Used for **Vibe Arena**, HTML5/WebGL Real-Time Multiplayer Games)*

- **Domain**: Real-Time Competitive Browser Gaming, 60 FPS HTML5 Canvas / Three.js WebGL, Authoritative Multiplayer Servers, Frictionless Room Lobbies, and Anti-Cheat.
- **Reference Runbook**: [`00-MASTER-CONTROLLER/projects/BROWSER-GAMING-PROFILE.md`](../00-MASTER-CONTROLLER/projects/BROWSER-GAMING-PROFILE.md)
- **Primary Commands**: `/sr24-browser-game [game-concept]` or `/sr24-multiplayer [task]`

### Target Project Implementation:
1. **Vibe Arena (Real-Time Browser Esports Platform)**:
   - Deterministic 60Hz accumulator game loop (`dt = 1/60s`) with sub-frame state interpolation for buttery smooth movement.
   - Authoritative Node.js WebSocket backend executing 60Hz physics ticks and broadcasting 20-30Hz delta-compressed state snapshots.
   - Client-side prediction with entity reconciliation: zero rubberbanding over 4G cellular connections.
   - Anti-Cheat Engine: server-authoritative movement delta distance caps preventing speedhacks, plus memory XOR variable masking preventing client tampering.
   - Frictionless social matchmaking via 4-character room codes (`#A9K4`) with zero signup required.
   - Visceral game feel: active hitbox/hurtbox frame data, 80ms hitstop impact freezes, and dynamic camera shake.
   - Universal controls: responsive on desktop (WASD + mouse) and mobile (on-screen virtual joystick and touch action buttons).

### Specialist Squad & Upstream GitHub Sources:
| Responsibility | Specialist Skill | Upstream GitHub Repository |
|---|---|---|
| **Deterministic 60Hz Loop** | `browser-game-architect` | `SR24Plus Custom Engineering` |
| **Authoritative WebSockets** | `websocket-multiplayer-engineer` | `SR24Plus Custom Engineering` |
| **Anti-Cheat & XOR Masking** | `browser-game-anti-cheat-engineer` | `SR24Plus Custom Engineering` |
| **Combat Feel & Hitstop** | `combat-mechanics-engineer` | `SR24Plus Custom Engineering` |
| **Dynamic Web Audio FX** | `agency-game-development-game-audio-engineer` | [`msitarzewski/agency-agents`](https://github.com/msitarzewski/agency-agents) |
| **Juice & Visual Feedback** | `agency-design-whimsy-injector` | [`msitarzewski/agency-agents`](https://github.com/msitarzewski/agency-agents) |
| **High-FPS HUD & Room UI** | `agency-design-ui-designer` + `ui-ux-pro-max` | [`msitarzewski/agency-agents`](https://github.com/msitarzewski/agency-agents) & [`nextlevelbuilder/ui-ux-pro-max-skill`](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) |
| **Headless Multi-Client QA**| `playwright-automation-engineer` | `SR24Plus Custom Engineering` |

### Copy-Paste Prompt for AI:
> *"Act as the SR24Plus Principal Game Architect & Realtime Netcode Specialist. Build a 60 FPS browser-based multiplayer gaming platform for Vibe Arena. Implement a deterministic fixed-timestep game loop, authoritative Node.js WebSocket game server with 4-character room codes, client-side prediction, server-authoritative delta-distance anti-cheat, mobile virtual controls, and 80ms hitstop impact freezes."*

---

## 3. Summary Comparison

| Dimension | Profile 1: Full-Stack SaaS (Dukan Sathi / ExamLoop) | Profile 2: Browser Gaming (Vibe Arena) |
|---|---|---|
| **Primary Domain** | High-utility web applications, retail POS, adaptive testing | Real-time competitive multiplayer esports, WebGL/Canvas games |
| **Frontend Core** | Next.js / React 18 / Tailwind CSS / Dark Glassmorphism | HTML5 Canvas / Three.js / Fixed 60Hz Accumulator Loop |
| **Backend Core** | FastAPI / Node.js REST + WebSockets + SQLite/Postgres | Authoritative Node.js / Bun WebSocket Server (60Hz Tick) |
| **Persistence** | IndexedDB local + cloud PostgreSQL with composite indexes | Redis in-memory match state + PostgreSQL Elo ratings |
| **Specialized IP** | Voice AI fallback, UPI QR codes, GST tax math, IRT models | Delta-distance anti-cheat, XOR memory protection, hitstop |
| **Primary Command** | `/sr24-saas` or `/sr24-web-dev` | `/sr24-browser-game` or `/sr24-multiplayer` |
