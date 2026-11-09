# SR24PLUS MASTER COMMAND REFERENCE & USER MANUAL

This document is the exhaustive operational reference for invoking, routing, and executing all **13 Primary Workflow Commands**, **6 Project Profiles**, and **14 Category Shorthand Triggers** in the SR24Plus Engineering Toolkit.

---

## 1. Primary Workflow Commands (`/sr24-*`)

### 1. `/sr24-auto [task]`
- **Intent**: Autonomous project inspection and squad deployment.
- **Workflow**: [`00-MASTER-CONTROLLER/workflows/SR24-AUTO.md`](../workflows/SR24-AUTO.md)
- **Heuristic**: Scans files, detects framework (`React`, `Next`, `Unity`, `FastAPI`), matches against known project profiles, and launches the exact specialist team.
- **Example**: `/sr24-auto analyze the current project and implement the pending feature`

### 2. `/sr24-saas [task]`
- **Intent**: Complete SaaS product engineering from monetization to multi-tenancy.
- **Workflow**: [`00-MASTER-CONTROLLER/workflows/SR24-SAAS.md`](../workflows/SR24-SAAS.md)
- **Phases**: SaaS Pricing & PRD -> Enterprise Brand -> Multi-Tenant UX -> High-Density UI -> Stripe/Razorpay Billing -> RLS Security -> SRE Launch.
- **Example**: `/sr24-saas build a multi-tenant inventory tracking platform with role-based access`

### 3. `/sr24-fullstack [task]`
- **Intent**: End-to-end synchronized feature implementation across database, API, and UI.
- **Workflow**: [`00-MASTER-CONTROLLER/workflows/SR24-FULLSTACK.md`](../workflows/SR24-FULLSTACK.md)
- **Phases**: Shared TypeScript Contract -> SQL Migration -> Transactional API Route -> Responsive UI Component -> E2E Flow Test.
- **Example**: `/sr24-fullstack create an udhaar credit ledger mutation with optimistic frontend updates`

### 4. `/sr24-browser-game [task]`
- **Intent**: 60 FPS HTML5, Canvas, WebGL, PixiJS, or Phaser browser games.
- **Workflow**: [`00-MASTER-CONTROLLER/workflows/SR24-BROWSER-GAME.md`](../workflows/SR24-BROWSER-GAME.md)
- **Phases**: Fixed Timestep Loop -> Universal Input (Touch/Keys) -> Combat/Mechanics -> Hitstop/Feel -> Texture Atlasing -> 60 FPS Audit.
- **Example**: `/sr24-browser-game build a fast-paced pixel art arena brawler with on-screen touch controls`

### 5. `/sr24-multiplayer [task]`
- **Intent**: Real-time networked multiplayer architectures with authoritative server validation.
- **Workflow**: [`00-MASTER-CONTROLLER/workflows/SR24-MULTIPLAYER.md`](../workflows/SR24-MULTIPLAYER.md)
- **Phases**: 60Hz Server Tick -> Client Prediction & Reconciliation -> 100ms Entity Interpolation -> Room Codes -> Latency Throttling Test.
- **Example**: `/sr24-multiplayer implement 1v1 matchmaking with 4-letter room codes and authoritative hit detection`

### 6. `/sr24-unity [task]`
- **Intent**: Complete Unity 2D/3D game development.
- **Workflow**: [`00-MASTER-CONTROLLER/workflows/SR24-UNITY.md`](../workflows/SR24-UNITY.md)
- **Phases**: ScriptableObject Architecture -> URP Volumes -> Input Actions -> Audio Routing -> 60 FPS Profiling -> Multi-Platform Build.
- **Example**: `/sr24-unity setup URP lighting and ScriptableObject event system for main game loop`

### 7. `/sr24-racing-game [task]`
- **Intent**: High-fidelity vehicle handling and circuit racing simulation in Unity.
- **Workflow**: [`00-MASTER-CONTROLLER/workflows/SR24-RACING-GAME.md`](../workflows/SR24-RACING-GAME.md)
- **Phases**: Rigidbody Mass & CoM -> WheelColliders & Anti-Roll -> Spline Track with Camber -> Checkpoint Loops -> Diesel Audio & Smoke VFX.
- **Example**: `/sr24-racing-game calibrate 16-wheeler truck WheelColliders for mountain ghat hairpins`

### 8. `/sr24-ai [task]`
- **Intent**: Production-grade AI systems, MCP tools, and deterministic RAG.
- **Workflow**: [`00-MASTER-CONTROLLER/workflows/SR24-AI.md`](../workflows/SR24-AI.md)
- **Phases**: Model Selection -> Prompt Schema -> Hybrid RAG -> Deterministic Offline Fallbacks -> Prompt Injection Defense -> Token Cost Evals.
- **Example**: `/sr24-ai build an MCP server that generates standardized CBSE Class 12 chemistry questions`

### 9. `/sr24-ui [task]`
- **Intent**: Bespoke visual design system, mathematical tokens, and anti-AI-slop audit.
- **Workflow**: [`00-MASTER-CONTROLLER/workflows/SR24-DESIGN.md`](../workflows/SR24-DESIGN.md)
- **Phases**: Slop Detection -> Design Tokens (4px/8px scale) -> Component Hierarchy & Contrast -> Spring Motion Budget -> Finish-Gate Review.
- **Example**: `/sr24-ui redesign the settings dashboard to eliminate generic purple gradients and floating cards`

### 10. `/sr24-security [task]`
- **Intent**: Comprehensive application security audit and vulnerability remediation.
- **Workflow**: [`00-MASTER-CONTROLLER/workflows/SR24-SECURITY.md`](../workflows/SR24-SECURITY.md)
- **Phases**: Secret Scanning -> Auth Cookie Flags -> BOLA/IDOR Defense -> Parameterized SQL -> CSP/CORS Whitelisting -> Rate Limiting -> CVE Audit.
- **Example**: `/sr24-security audit API endpoints for IDOR vulnerabilities and hardcoded tokens`

### 11. `/sr24-qa [task]`
- **Intent**: Automated testing, visual regression, and systematic debugging.
- **Workflow**: [`00-MASTER-CONTROLLER/workflows/SR24-SHIP.md`](../workflows/SR24-SHIP.md)
- **Phases**: Playwright E2E Suites -> Accessible Role Locators -> Visual Snapshots -> Heap Memory Leak Analysis -> Build Evidence.
- **Example**: `/sr24-qa write a Playwright E2E test suite for the complete customer billing checkout journey`

### 12. `/sr24-ship [task]`
- **Intent**: Production release gating, CI/CD pipeline, and SRE readiness.
- **Workflow**: [`00-MASTER-CONTROLLER/workflows/SR24-SHIP.md`](../workflows/SR24-SHIP.md)
- **Phases**: Compiler & Build Check (`npm run build`) -> Env Var Audit -> DB Migration Test -> Staging Smoke Test -> SRE Healthchecks.
- **Example**: `/sr24-ship prepare Dockerfile, GitHub Actions workflow, and production healthcheck endpoints`

### 13. `/sr24-research [task]`
- **Intent**: Deep evidence synthesis, literature reviews, and competitor analysis.
- **Workflow**: [`00-MASTER-CONTROLLER/workflows/SR24-RESEARCH.md`](../workflows/SR24-RESEARCH.md)
- **Phases**: Hypothesis Framing -> ArXiv/PubMed/PubChem -> Statistical Significance Check -> Decision-Ready Synthesis Report.
- **Example**: `/sr24-research analyze local speech-to-text models (Whisper vs Vosk) for offline Hindi recognition`

---

## 2. Dedicated Project Triggers

Quick triggers for user's actual project workspaces:
- `/sr24-auto vibe-arena`
- `/sr24-auto truck-racing`
- `/sr24-auto politics-arena`
- `/sr24-auto dukan-sathi`
- `/sr24-auto exam-loop`
- `/sr24-auto sr24plus`

---

## 3. Category Squad Shorthand Triggers

- `/sr24 ui`: 01 - UI/UX Design & Anti-Slop
- `/sr24 game`: 02 - Game Development
- `/sr24 frontend`: 03 - Modern Frontend, WebGL & Motion
- `/sr24 backend`: 04 - Scalable APIs, Databases & Auth
- `/sr24 ai`: 05 - AI/ML Engineering
- `/sr24 mobile`: 06 - Mobile App Development
- `/sr24 devops`: 07 - DevOps and Cloud
- `/sr24 qa`: 08 - Quality Engineering
- `/sr24 research`: 09 - Research and Analytics
- `/sr24 branding`: 10 - Branding and Creative
- `/sr24 product`: 11 - Product Engineering
- `/sr24 science`: 12 - Science and Bioinformatics
- `/sr24 agy`: 13 - Antigravity Automation
- `/sr24 general`: 14 - General Engineering

