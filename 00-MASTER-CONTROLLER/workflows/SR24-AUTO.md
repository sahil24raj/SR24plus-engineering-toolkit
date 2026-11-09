# WORKFLOW: /sr24-auto — AUTONOMOUS PROJECT DETECTION & SQUAD ROUTER

> **Command**: `/sr24-auto [optional task]`  
> **Natural Language Trigger**: `"Auto analyze project"`, `"Select engineering workflow"`, `"Run auto orchestrator"`  
> **Mission**: Autonomously inspect the active project repository, identify the project type and framework, match it to specialized project profiles, and select and activate the optimal engineering squad.

---

## 1. Autonomous Project Detection Heuristics

The `/sr24-auto` command runs the following file inspection:

```
                          ┌─────────────────────────────┐
                          │   WORKSPACE SCAN PROTOCOL   │
                          └──────────────┬──────────────┘
                                         │
        ┌────────────────────────────────┼────────────────────────────────┐
        ▼                                ▼                                ▼
[Check Known Projects]          [Check Game Engines]            [Check Web / Fullstack]
- "Dukaan Saathi" in code       - Assets/ / ProjectSettings/    - package.json + vite/react
  -> DUKAN-SATHI Profile          -> SR24-UNITY                   -> SR24-FULLSTACK / SAAS
- "Vibe Arena" in code          - project.godot                 - requirements.txt / fastapi
  -> VIBE-ARENA Profile           -> SR24-GAME-DEV (Godot)        -> SR24-FULLSTACK
- "Truck Racing" in code        - *.uproject                    - next.config.js
  -> INDIAN-TRUCK-RACING          -> SR24-GAME-DEV (Unreal)       -> SR24-WEB-DEV / SAAS
- "Politics Arena" in code      - Phaser / PixiJS in pkg        - AI / LangChain / RAG in code
  -> INDIAN-POLITICS-ARENA        -> SR24-BROWSER-GAME            -> SR24-AI
```

---

## 2. Decision Tree & Automatic Routing Table

| Detected Workspace Signatures | Auto-Selected Workflow / Profile | Primary Squad Activated |
|---|---|---|
| POS Billing, Hindi speech, Udhaar, SQLite, `P1` | [`DUKAN-SATHI.md`](../projects/DUKAN-SATHI.md) | Fullstack Lead + Indian GST Specialist + Razorpay UPI + Offline Kirana Architect |
| Real-time browser game, canvas, lobby, multiplayer | [`VIBE-ARENA.md`](../projects/VIBE-ARENA.md) | Browser Game Architect + WebSocket Multiplayer + Anti-Cheat Engineer |
| Unity project with vehicle physics, trucks, racing | [`INDIAN-TRUCK-RACING.md`](../projects/INDIAN-TRUCK-RACING.md) | Unity Architect + Truck Physics Engineer + Car Controller + Circuit Designer |
| Browser 2D fighting/combat game, hitboxes, frame data | [`INDIAN-POLITICS-ARENA.md`](../projects/INDIAN-POLITICS-ARENA.md) | Browser Game Architect + Combat Mechanics Engineer + Hitstop/Feel Engineer |
| Adaptive examination, question bank, KaTeX, proctoring | [`EXAM-LOOP.md`](../projects/EXAM-LOOP.md) | Assessment Engine Architect + MCP Server Developer + AI Security Engineer |
| Multi-tenant SaaS, Stripe billing, auth, dashboards | [`SR24-SAAS.md`](./SR24-SAAS.md) | SaaS Architect + Multi-Tenant DB Specialist + AppSec Engineer + SRE |
| Unity 2D/3D project (generic) | [`SR24-UNITY.md`](./SR24-UNITY.md) | Unity Architect + Shader Graph Artist + Audio Engineer + Build Pipeline |
| Web application with LLM / RAG / embeddings | [`SR24-AI.md`](./SR24-AI.md) | AI Systems Lead + Prompt Injection Defense + RAG Pipeline Engineer |
| Standard full-stack web application | [`SR24-FULLSTACK.md`](./SR24-FULLSTACK.md) | System Architect + Frontend Dev + Backend Architect + Database Optimizer |

---

## 3. Execution Output Format

Upon invoking `/sr24-auto`, the Master Router outputs:
```markdown
### ⚡ SR24Plus Autonomous Project Inspection
- **Detected Workspace**: Dukaan Saathi POS Retail System
- **Framework Stack**: React 18 (Vite) + Three.js + Tailwind CSS + Python FastAPI + SQLite
- **Matched Project Profile**: `00-MASTER-CONTROLLER/projects/DUKAN-SATHI.md`
- **Active Specialist Squad**:
  1. `offline-first-kirana-architect` (Local IndexedDB & background sync)
  2. `indian-gst-billing-engineer` (CGST/SGST/IGST compliance & 80mm receipts)
  3. `razorpay-upi-specialist` (Dynamic UPI QR & HMAC-SHA256 webhooks)
  4. `agency-engineering-frontend-developer` (3D Spatial acoustic canvas & dark glass UI)
  5. `agency-security-appsec-engineer` (Data isolation & secret protection)
- **Status**: Squad deployed. Ready for engineering commands.
```
