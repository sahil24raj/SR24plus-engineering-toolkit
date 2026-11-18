---
name: sr24-intelligence-engine
description: Autonomous project understanding, tech stack inference, classification, and priority-scored skill activation planner for Web and Game Dev packs.
---

# SR24 Intelligence Engine (`sr24-intelligence-engine`)

## 1. Overview & Operational Mandate
The **`sr24-intelligence-engine`** serves as the cognitive dispatch hub for the **SR24Plus Engineering Toolkit**. It statically inspects project files, dependencies, manifests, and directory trees to infer the technology stack, classify the project into one of 12 distinct archetypes, and generate a priority-scored skill activation matrix without bloat.

## 2. When to Use
- At the start of any new software engineering task (`/sr24-auto` or `/sr24-intelligence`).
- When onboarding an unfamiliar codebase or auditing an existing project.
- To eliminate skill activation conflicts between Web Dev and Game Dev packs.

## 3. Supported Project Archetypes
1. Full Stack Web Applications (Next.js, Remix, Vite, SvelteKit)
2. SaaS Platforms (Multi-tenant, Stripe/Razorpay billing, auth, queues)
3. AI/ML Applications (RAG pipelines, LangChain, OpenAI/Gemini SDKs, MCP servers)
4. Browser Games & Esports (60Hz Canvas/WebGL, Pixi.js, Three.js, Phaser)
5. 2D Games & Physics (Matter.js, Rapier 2D, Arcade Physics)
6. 3D Games & Environments (Three.js, React Three Fiber, Rapier 3D)
7. Multiplayer Games (Colyseus, Nakama, Socket.IO, authoritative state)
8. Unity Games (ScriptableObjects, URP, WheelColliders, DOTS/ECS)
9. E-Commerce & Retail (Vendure, Medusa, Cart & Payment flows)
10. Fintech Applications (Razorpay UPI, GST calculations, ledger audit)
11. Developer Tools & CLI (Node CLI, TypeScript compilers, Rust tools)
12. AI Agent Orchestration (Multi-agent workflows, autonomous supervisors)

## 4. Execution Workflow
1. **Static Manifest Inspection**: Scans `package.json`, `Cargo.toml`, `requirements.txt`, or Unity `ProjectSettings`.
2. **Archetype Classification**: Matches detected libraries against weighted archetype signatures.
3. **Relevance Scoring**: Assigns priority scores (0-100) to matching skills from `skills/`.
4. **Conflict Resolution**: Prevents duplicate or conflicting engine activations (e.g., choosing either Three.js or Unity for a given project).
5. **Output Matrix**: Emits a structured activation plan for master agent consumption.

## 5. CLI Usage
```bash
python skills/sr24-custom-engineering/sr24-intelligence-engine/scripts/intelligence_engine.py [project_path]
```

## 6. Upstream Attribution & License
- Upstream: SR24Plus Core Architecture (`sahil24raj/SR24plus-engineering-toolkit`)
- License: MIT