# SR24PLUS CORE INTELLIGENCE ARCHITECTURE
### Master Orchestration Blueprint Connecting Intelligence, Packs, Auditing, and Self-Healing

> **Architecture Version**: v3.0  
> **Master Router**: `/sr24-auto` • `/sr24-full-check`  
> **Total Canonical Skills**: 479 Verified In-Repo Skills

---

## 1. Unified End-to-End Execution Pipeline

```mermaid
flowchart TD
    TRIGGER["Developer Request / Master Command: /sr24-full-check"] --> ROUTER["00-MASTER-CONTROLLER"]
    
    subgraph STAGE1["Stage 1: Autonomous Discovery"]
        ROUTER --> INTEL["SR24 Intelligence Engine"]
        INTEL --> SCAN["Static Codebase & Manifest Scan"]
        SCAN --> CLASS["12-Archetype Classification"]
        CLASS --> MATRIX["Relevance-Scored Skill Matrix"]
    end
    
    subgraph STAGE2["Stage 2: Pack Execution"]
        MATRIX --> PACKS{"Selected Pack"}
        PACKS -->|"Web Application / SaaS"| WEB["SR24-WEB-DEV (12 Phases)"]
        PACKS -->|"Browser / 3D / Unity Game"| GAME["SR24-GAME-DEV (12 Phases)"]
    end
    
    subgraph STAGE3["Stage 3: Production Quality Gate"]
        WEB & GAME --> AUDIT["SR24 Production Auditor"]
        AUDIT --> M_ARCH["Architecture Audit"]
        AUDIT --> M_UI["UI/UX & Anti-Slop Audit"]
        AUDIT --> M_FE["Frontend Audit"]
        AUDIT --> M_BE["Backend & API Audit"]
        AUDIT --> M_DB["Database & Index Audit"]
        AUDIT --> M_SEC["Security & Secrets Audit"]
        AUDIT --> M_GAME["Game Loop & Physics Audit"]
        AUDIT --> M_DEP["Deployment & CI/CD Audit"]
        
        M_ARCH & M_UI & M_FE & M_BE & M_DB & M_SEC & M_GAME & M_DEP --> REPORT["reports/SR24-PRODUCTION-AUDIT.md"]
    end
    
    subgraph STAGE4["Stage 4: Autonomous Closed-Loop Self-Healing"]
        REPORT --> EVAL{"Any Critical / High Defects?"}
        EVAL -->|"Defects Found"| HEAL["SR24 Self-Healing Engineer"]
        HEAL --> LOOP["6-Step Loop: Detect ➔ Diagnose ➔ Plan ➔ Repair ➔ Test ➔ Verify"]
        LOOP -->|"Max 3 Retries"| RETEST{"Verified Green?"}
        RETEST -->|"Yes"| AUDIT
        RETEST -->|"No"| BLOCKER["Halt with Blocker Report"]
    end
    
    EVAL -->|"Zero Critical Defects (Score >= 9.0)"| RELEASE["Production Release Ready (10.0 / 10)"]
```

---

## 2. Core Master Commands

| Master Command | Scope & Mission | Underlying Subsystems |
|---|---|---|
| **`/sr24-auto [task]`** | Fully autonomous project analysis and matching skill activation | Intelligence Engine ➔ Skill Selection |
| **`/sr24-intelligence [dir]`** | Run static codebase discovery, archetype classification, and skill plan | `sr24-intelligence-engine` |
| **`/sr24-audit [dir]`** | Run 8-module full-spectrum production audit and generate structured report | `sr24-production-auditor` |
| **`/sr24-heal [test_cmd]`** | Autonomous 6-step closed-loop debugging and minimal repair | `sr24-self-healing-engineer` |
| **`/sr24-full-check`** | End-to-end pipeline: Intelligence ➔ Audit ➔ Heal ➔ Verify ➔ Release | All Core Subsystems |
| **`/sr24-web-audit`** | Targeted audit for Web/SaaS stacks (Modules A-F, H) | Production Auditor (Web Profile) |
| **`/sr24-game-audit`** | Targeted audit for Browser/Unity game stacks (Modules A-C, G-H) | Production Auditor (Game Profile) |
| **`/sr24-production-ready`** | Evaluates whether all quality dimensions score $\ge 9.0/10$ | Quality Gate Validator |