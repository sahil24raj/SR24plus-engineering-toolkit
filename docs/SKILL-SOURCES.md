# SR24Plus Skill Sources & Repository Attribution
### Exhaustive Open-Source Provenance & Upstream Repository Directory

[![Attribution](https://img.shields.io/badge/Attribution-Verified%20Upstream-blue.svg)](./SKILL-SOURCES.md)
[![Licenses](https://img.shields.io/badge/Licenses-MIT%20%7C%20Apache--2.0%20%7C%20Unity-lightgrey.svg)](#license-compliance-matrix)
[![Repository](https://img.shields.io/badge/Toolkit-SR24Plus-emerald.svg)](../README.md)

---

## 1. Provenance Investigation Methodology

To ensure 100% factual accuracy and eliminate guesswork, every skill in the **SR24Plus Engineering Toolkit** was verified across multiple forensic sources:
1. **`plugin.json` and `package.json` manifests** in the system's Antigravity plugin ecosystem (`C:\Users\sr24s\.gemini\config\plugins`).
2. **Git remote configurations** (`.git/config`) of local plugin clones.
3. **YAML frontmatter headers** within each individual `SKILL.md`.
4. **License texts** (`LICENSE`, `LICENSE.md`, `COPYING`) bundled with each skill suite.
5. **Upstream author commits** and official repository readmes.

---

## 2. Upstream Source Repositories Directory

The following table documents all external repositories that contributed skills to the SR24Plus ecosystem:

| Upstream Repository | Author / Organization | Local Directory in Repo | Skills Count | License | Domain / Capability |
|---|---|---|:---:|:---:|---|
| [**`msitarzewski/agency-agents`**](https://github.com/msitarzewski/agency-agents) | msitarzewski / The Agency | `skills/agency-agents/` | **301** | MIT | 300+ autonomous AI agent personas across software engineering, architecture, design, security, GIS, sales, marketing, and operations. |
| [**`addyosmani/agent-skills`**](https://github.com/addyosmani/agent-skills) | Addy Osmani (Engineering Lead, Google Chrome) | `skills/addyosmani-agent-skills/` | **25** | MIT | Software engineering craft: Context engineering, CI/CD, TDD, code review, systematic debugging, ADRs, performance optimization, and API design. |
| [**`Unity Technologies Official`**](https://unity.com) | Unity Technologies | `skills/unity-skills/` | **32** | Unity Companion / Apache-2.0 | Engine engineering: 2D/3D physics, URP/HDRP shaders, Render Graph features, NavMesh AI, Vivox voice, Netcode multiplayer, Sprite Atlases, and live games. |
| [**`SR24Plus Custom Engineering`**](https://github.com/sahil24raj/SR24plus-engineering-toolkit) | Sahil Raj (SR24Plus) | `skills/sr24-custom-engineering/` | **17** | MIT | Original custom architecture: Razorpay/UPI dynamic QR, Indian GST billing, Offline-First Kirana IndexedDB/SQLite, WebSockets, Truck Physics, Anti-Cheat, Combat 60Hz. |
| [**`google-antigravity-sdk`**](https://github.com/google-deepmind) | Google DeepMind | `skills/antigravity-core/` | **13** | Apache-2.0 | Core Antigravity IDE capabilities: agent swarms, workflow migrations, runtime plugins, generative UI, and automation controllers. |
| [**`vercel-labs/agent-skills`**](https://github.com/vercel-labs/agent-skills) & [**`vercel-labs/skills`**](https://github.com/vercel-labs/skills) | Vercel Labs | `skills/vercel-skills/` | **9** | MIT | Modern web engineering: React composition patterns, React Compiler rules, View Transitions API, Vercel deployments, and web design guidelines. |
| [**`Android Developer Tools`**](https://developer.android.com) | Android Open Source Project (Google) | `skills/android-mobile/` | **5** | Apache-2.0 | Native mobile tooling: Android CLI, ADB device hub, Compose previews, and mobile build pipelines. |
| [**`pbakaus/impeccable`**](https://github.com/pbakaus/impeccable) | Paul Bakaus | `skills/ui-design-suite/impeccable/` | **1** | Apache-2.0 | Design critique engine: typography scales, spacing rhythm, layout density, and interface refinement. |
| [**`miqdadbadjuber/anti-slop`**](https://github.com/miqdadbadjuber/anti-slop) | Miqdad Badjuber | `skills/ui-design-suite/antislop/` | **2** | MIT | Anti-AI-slop design gates: filters out generic purple SaaS gradients, illegible glassmorphism, and cartoon emoji icons. |
| [**`Leonxlnx/taste-skill`**](https://github.com/Leonxlnx/taste-skill) | Leon (Leonxlnx) | `skills/ui-design-suite/taste-skill/` | **1** | MIT | Aesthetic direction, color palette selection, brand positioning, and typography curation. |
| [**`nextlevelbuilder/ui-ux-pro-max-skill`**](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | NextLevelBuilder | `skills/ui-design-suite/ui-ux-pro-max/` | **1** | MIT | UI/UX design intelligence: 48+ curated design styles, design contracts, and accessible layouts. |
| [**`custom-skills / REA`**](https://github.com/sahil24raj/SR24plus-engineering-toolkit) | REA & Agent Reach Contributors | `skills/custom-skills/` | **6** | MIT | Reverse engineering anything, codebase archaeology, runtime observation, and tool design. |
| **Total In-Repo Verified Skills** | **Multi-Source Engineering Ecosystem** | **`skills/`** | **413** | **Fully Audited** | **Complete Fullstack, Game, SaaS & Startup Coverage** |

---

## 3. License Compliance Matrix

All imported skills maintain their original open-source licenses:
- **MIT License**: Governs `agency-agents`, `addyosmani-agent-skills`, `vercel-skills`, `anti-slop`, `taste-skill`, `ui-ux-pro-max`, `custom-skills`, and all `sr24-custom-engineering` files. Allows unrestricted commercial use, modification, and redistribution with copyright notice preservation.
- **Apache 2.0 License**: Governs `antigravity-core`, `impeccable`, and `android-mobile`. Grants explicit patent rights and open redistribution with attribution.
- **Unity Companion License**: Governs `unity-skills`. Grants permission to build and run Unity-based titles in accordance with Unity Terms of Service.

---

## 4. Preservation of Intellectual Property

No copyright headers, author attributions, or original `SKILL.md` instructions were removed or modified during the repository organization. Every skill is cited with its exact upstream author and repository link.
