# SR24PLUS CATEGORY & WORKFLOW ARCHITECTURE MAP

The SR24Plus Engineering Toolkit organizes 443 canonical skills into **14 Specialized Domains** interconnected with **9 Cross-Domain Workflows**.

---

## 1. Cross-Domain Workflows & Primary Commands

```
                              ┌────────────────────────────────────────┐
                              │       SR24PLUS MASTER ROUTER           │
                              │    00-MASTER-CONTROLLER/MASTER-ROUTER  │
                              └──────────────────┬─────────────────────┘
                                                 │
   ┌───────────────┬───────────────┬─────────────┴─┬───────────────┬───────────────┬───────────────┐
   ▼               ▼               ▼               ▼               ▼               ▼               ▼
/sr24-web-dev  /sr24-game-dev  /sr24-saas     /sr24-design     /sr24-ai     /sr24-security   /sr24-fullstack
  (10 Phases)    (10 Phases)   (8 Stages)      (5 Steps)      (6 Stages)      (7 Points)       (5 Steps)
```

| Primary Command | Activated Category Squads | Workflow File |
|---|---|---|
| **`/sr24-web-dev`** | 01 (UI/UX) + 03 (Frontend) + 04 (Backend) + 07 (DevOps) + 08 (QA) + 10 (Branding) + 11 (Product) | [`SR24-WEB-DEV.md`](./workflows/SR24-WEB-DEV.md) |
| **`/sr24-game-dev`** | 02 (Game Dev) + 01 (UI/UX) + 08 (QA) + 10 (Branding & Lore) + 14 (Performance) | [`SR24-GAME-DEV.md`](./workflows/SR24-GAME-DEV.md) |
| **`/sr24-saas`** | 11 (Product) + 01 (UI/UX) + 04 (Backend) + 07 (DevOps) + 08 (QA) + Multi-Tenancy & Billing | [`SR24-SAAS.md`](./workflows/SR24-SAAS.md) |
| **`/sr24-design`** | 01 (UI/UX) + `antislop` + `impeccable` + `ui-ux-pro-max` + Finish-Gate Reviewer | [`SR24-DESIGN.md`](./workflows/SR24-DESIGN.md) |
| **`/sr24-ai`** | 05 (AI/ML) + 04 (Backend) + AI Security Auditor + Prompt Engineering | [`SR24-AI.md`](./workflows/SR24-AI.md) |
| **`/sr24-security`** | 04 (Backend) + 07 (Cloud) + AppSec Engineer + Pen Tester + Threat Detection | [`SR24-SECURITY.md`](./workflows/SR24-SECURITY.md) |
| **`/sr24-research`** | 09 (Research & Analytics) + 12 (Science) + Academic Statisticians + ArXiv | [`SR24-RESEARCH.md`](./workflows/SR24-RESEARCH.md) |
| **`/sr24-ship`** | 07 (DevOps) + 08 (QA) + SRE + CI/CD Automator + Launch Strategist | [`SR24-SHIP.md`](./workflows/SR24-SHIP.md) |
| **`/sr24-fullstack`** | 03 (Frontend) + 04 (Backend) + Software Architect + DB Optimizer + API Contracts | [`SR24-FULLSTACK.md`](./workflows/SR24-FULLSTACK.md) |

---

## 2. The 14 Specialized Skill Domains

| ID | Domain Name | Skills | Key Capabilities | Directory |
|:---:|---|:---:|---|---|
| **01** | **UI/UX Design** | `65` | Design systems, anti-AI-slop gates, typography, accessibility, responsive UI | [`01-UI-UX-DESIGN/`](../01-UI-UX-DESIGN/README.md) |
| **02** | **Game Development** | `57` | GDD design, Unity, Unreal, Godot, shaders, 2D/3D physics, game audio, HUDs | [`02-GAME-DEVELOPMENT/`](../02-GAME-DEVELOPMENT/README.md) |
| **03** | **Frontend Development** | `32` | Modern React/Next.js/Vue, WebGL, Three.js, motion animations, Core Web Vitals | [`03-FRONTEND-DEVELOPMENT/`](../03-FRONTEND-DEVELOPMENT/README.md) |
| **04** | **Backend Development** | `48` | Scalable microservices, PostgreSQL/SQLite, database indexing, REST/tRPC APIs | [`04-BACKEND-DEVELOPMENT/`](../04-BACKEND-DEVELOPMENT/README.md) |
| **05** | **AI/ML Engineering** | `58` | LLM fine-tuning, prompt engineering, RAG pipelines, synthetic data, AI evaluation | [`05-AIML-ENGINEERING/`](../05-AIML-ENGINEERING/README.md) |
| **06** | **Mobile App Development** | `13` | Native Android/iOS, Flutter, React Native, Electron desktop, app store ASO | [`06-MOBILE-APP-DEVELOPMENT/`](../06-MOBILE-APP-DEVELOPMENT/README.md) |
| **07** | **DevOps and Cloud** | `26` | CI/CD pipelines, Docker, Kubernetes, Terraform, zero-downtime deployment, SRE | [`07-DEVOPS-AND-CLOUD/`](../07-DEVOPS-AND-CLOUD/README.md) |
| **08** | **Quality Engineering** | `39` | Reality checkers, visual evidence collection, automated E2E tests, code reviews | [`08-QUALITY-ENGINEERING/`](../08-QUALITY-ENGINEERING/README.md) |
| **09** | **Research & Analytics** | `91` | Cross-source evidence synthesis, academic methodologies, GIS spatial analysis | [`09-RESEARCH-AND-ANALYTICS/`](../09-RESEARCH-AND-ANALYTICS/README.md) |
| **10** | **Branding & Creative** | `45` | Brand strategy, visual storytelling, lore architecture, marketing copy | [`10-BRANDING-AND-CREATIVE/`](../10-BRANDING-AND-CREATIVE/README.md) |
| **11** | **Product Engineering** | `212` | PRDs, sprint prioritization, executive coordination, domain-driven architecture | [`11-PRODUCT-ENGINEERING/`](../11-PRODUCT-ENGINEERING/README.md) |
| **12** | **Science & Bioinformatics**| `39` | PubChem, ChEMBL, AlphaFold 3D structures, ClinVar, GTEx expression data | [`12-SCIENCE-AND-BIOINFORMATICS/`](../12-SCIENCE-AND-BIOINFORMATICS/README.md) |
| **13** | **Antigravity Automation** | `29` | Custom MCP builders, swarm orchestration, workflow migrations, platform tooling | [`13-ANTIGRAVITY-AND-AUTOMATION/`](../13-ANTIGRAVITY-AND-AUTOMATION/README.md) |
| **14** | **General Engineering** | `60` | Git workflows, performance profiling, error recovery, architectural ADRs | [`14-GENERAL-ENGINEERING/`](../14-GENERAL-ENGINEERING/README.md) |
