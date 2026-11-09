# SR24PLUS COMMAND DIRECTORY & TRIGGER REFERENCE

The SR24Plus Engineering Toolkit supports both **Primary Workflow Commands** (`/sr24-*`) for complete end-to-end multi-disciplinary projects, and **Category Squad Triggers** (`/sr24 <domain>`) for domain-specific tasks.

---

## 1. Primary Workflow Commands (Complete Squads)

| Primary Command | Description | Example Usage | Target Workflow Runbook |
|---|---|---|---|
| **`/sr24-web-dev [task]`** | Launches 10-phase website & web app squad | `/sr24-web-dev build an offline-first POS for retail store` | [`SR24-WEB-DEV.md`](./workflows/SR24-WEB-DEV.md) |
| **`/sr24-game-dev [task]`** | Launches 10-phase game development squad | `/sr24-game-dev build a 3D truck runner game in Unity` | [`SR24-GAME-DEV.md`](./workflows/SR24-GAME-DEV.md) |
| **`/sr24-saas [task]`** | Launches multi-tenant SaaS startup squad | `/sr24-saas create an AI invoice management platform` | [`SR24-SAAS.md`](./workflows/SR24-SAAS.md) |
| **`/sr24-design [task]`** | Launches visual design system & anti-slop audit | `/sr24-design audit landing page and remove AI slop` | [`SR24-DESIGN.md`](./workflows/SR24-DESIGN.md) |
| **`/sr24-ai [task]`** | Launches AI/ML & RAG intelligent systems squad | `/sr24-ai implement RAG vector search with hybrid BM25` | [`SR24-AI.md`](./workflows/SR24-AI.md) |
| **`/sr24-security [task]`** | Launches offensive & defensive security audit squad | `/sr24-security audit OWASP vulnerabilities and API secrets` | [`SR24-SECURITY.md`](./workflows/SR24-SECURITY.md) |
| **`/sr24-research [task]`** | Launches deep evidence synthesis & research squad | `/sr24-research compare local speech-to-text models vs cloud` | [`SR24-RESEARCH.md`](./workflows/SR24-RESEARCH.md) |
| **`/sr24-ship [task]`** | Launches production release, CI/CD & SRE squad | `/sr24-ship prepare Docker, CI/CD pipeline and healthchecks` | [`SR24-SHIP.md`](./workflows/SR24-SHIP.md) |
| **`/sr24-fullstack [task]`** | Launches fullstack feature engineering squad | `/sr24-fullstack add udhaar credit payment flow with DB schema` | [`SR24-FULLSTACK.md`](./workflows/SR24-FULLSTACK.md) |

---

## 2. Category Squad Shorthand Triggers

| Shorthand Trigger | Natural Language Command | Activated Domain | Included Specialists |
|---|---|---|---|
| `/sr24 ui` | *"Activate UI Design Toolkit"* | 01 - UI/UX Design | `antislop`, `impeccable`, `ui-ux-pro-max`, `taste-skill`, UI Designer |
| `/sr24 game` | *"Activate Game Development Toolkit"* | 02 - Game Development | Game Designer, Level Designer, Tech Artist, Engine Specialists |
| `/sr24 frontend` | *"Activate Frontend Development Toolkit"* | 03 - Frontend Development | Frontend Developer, Senior Developer, Performance Auditor |
| `/sr24 backend` | *"Activate Backend Development Toolkit"* | 04 - Backend Development | Backend Architect, DB Optimizer, Identity Engineer |
| `/sr24 ai` | *"Activate AI/ML Engineering Toolkit"* | 05 - AI/ML Engineering | AI Engineer, Prompt Engineer, RAG Pipeline Engineer |
| `/sr24 mobile` | *"Activate Mobile App Toolkit"* | 06 - Mobile App Development | Mobile Builder, Android CLI, App Store Optimizer |
| `/sr24 devops` | *"Activate DevOps & Cloud Toolkit"* | 07 - DevOps and Cloud | DevOps Automator, SRE, Cloud Security Architect |
| `/sr24 qa` | *"Activate Quality Engineering Toolkit"* | 08 - Quality Engineering | Code Reviewer, Test Automator, Reality Checker |
| `/sr24 research` | *"Activate Research & Analytics Toolkit"* | 09 - Research and Analytics | Research Synthesist, Statistician, ArXiv, PubMed |
| `/sr24 branding` | *"Activate Branding & Creative Toolkit"* | 10 - Branding and Creative | Brand Guardian, Content Creator, Narrative Designer |
| `/sr24 product` | *"Activate Product Engineering Toolkit"* | 11 - Product Engineering | Product Manager, Sprint Prioritizer, Task Breakdown |
| `/sr24 science` | *"Activate Science & Bioinformatics Toolkit"* | 12 - Science and Bioinformatics | ChEMBL, PubChem, AlphaFold, ClinVar, GTEx |
| `/sr24 agy` | *"Activate Antigravity Automation Toolkit"* | 13 - Antigravity & Automation | Custom MCPs, Workflow Migrator, Antigravity Customizations |
| `/sr24 general` | *"Activate General Engineering Toolkit"* | 14 - General Engineering | Git Workflow, Performance Opt, Debugging & Error Recovery |

---

## 3. How to Invoke in Antigravity

Type the command directly into the conversation:
```text
/sr24-web-dev Build a responsive Hindi-first Kirana POS billing interface with Three.js interactive background
```
Or use natural language:
```text
Activate the Web Development Toolkit to build a responsive Hindi-first Kirana POS billing interface
```

The Master Router will intercept the request, inspect the project workspace, load the corresponding `SKILL.md` instruction files, announce the active squad, and begin execution.
