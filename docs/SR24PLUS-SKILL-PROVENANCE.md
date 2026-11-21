# SR24Plus Unified Skill Provenance Matrix
### Complete Lineage, Upstream Repository, Engineering Pack, Phase, and Verification Status

> **Lineage Standard**: Forensic Audit • Authentic Origin Verification • Zero Unaccounted Assets  
> **Repository**: [https://github.com/sahil24raj/SR24plus-engineering-toolkit.git](https://github.com/sahil24raj/SR24plus-engineering-toolkit.git)  
> **Maintainer**: Sahil Raj (SR24Plus)  
> **Total Audited Canonical Skills**: **480**  

---

## 1. Provenance Classification Criteria

Every skill in the toolkit is evaluated against strict forensic provenance criteria:

- **Integrated**: Fully imported or authored skill with canonical `SKILL.md`, operational boundaries, code samples, and tests in the repository.
- **Customized**: Derived from an upstream open-source specification and adapted/hardened for SR24Plus architectures.
- **Referenced**: Canonical ecosystem skill referenced for inter-agent delegation and tool invocation.
- **Recommended**: External open-source package or tool recommended for production scaling.
- **Planned**: Documented architectural roadmap capability scheduled for future engine releases.
- **Unverified**: Candidate skill undergoing provenance verification. *(Currently 0)*

---

## 2. Flagship Skill Provenance Register

The following unified matrix details the core production skills actively mobilizing the 24 phases of Web and Game development, Core Intelligence, and specialized engineering packs. Every skill links to its canonical repository source and internal skill manual:

| Skill Name | Original GitHub Repository | Pack | Phase | Used By Commands | Status |
|---|---|:---:|:---:|---|:---:|
| [`sr24-intelligence-engine`](../skills/sr24-custom-engineering/sr24-intelligence-engine/SKILL.md) | [SR24plus-engineering-toolkit](https://github.com/sahil24raj/SR24plus-engineering-toolkit/tree/main/skills/sr24-custom-engineering/sr24-intelligence-engine) | Core | Phase 1.5 | `/sr24-auto` | **Integrated** |
| [`sr24-production-auditor`](../skills/sr24-custom-engineering/sr24-production-auditor/SKILL.md) | [SR24plus-engineering-toolkit](https://github.com/sahil24raj/SR24plus-engineering-toolkit/tree/main/skills/sr24-custom-engineering/sr24-production-auditor) | Core | Phase 7.5 | `/sr24-auto`, `/sr24-ship` | **Integrated** |
| [`sr24-self-healing-engineer`](../skills/sr24-custom-engineering/sr24-self-healing-engineer/SKILL.md) | [SR24plus-engineering-toolkit](https://github.com/sahil24raj/SR24plus-engineering-toolkit/tree/main/skills/sr24-custom-engineering/sr24-self-healing-engineer) | Core | Phase 8.5 | `/sr24-auto`, `/sr24-heal` | **Integrated** |
| [`firecrawl-scraper`](../skills/sr24-custom-engineering/firecrawl-scraper/SKILL.md) | [firecrawl](https://github.com/firecrawl/firecrawl) | Web Dev | Phase 01 | `/sr24-web-dev`, `/sr24-research` | **Integrated** |
| [`tavily-search-intelligence`](../skills/sr24-custom-engineering/tavily-search-intelligence/SKILL.md) | [tavily-python](https://github.com/tavily-ai/tavily-python) | Web Dev | Phase 01 | `/sr24-web-dev`, `/sr24-research` | **Integrated** |
| [`agency-product-trend-researcher`](../skills/agency-agents/agency-product-trend-researcher/SKILL.md) | [agency-agents](https://github.com/msitarzewski/agency-agents) | Web Dev | Phase 01 | `/sr24-web-dev`, `/sr24-research` | **Integrated** |
| [`reverse-engineer-anything`](../skills/sr24-custom-engineering/reverse-engineer-anything/SKILL.md) | [agent-reach](https://github.com/sahil24raj/SR24plus-engineering-toolkit) | Web Dev / Game | Phase 01 | `/sr24-web-dev`, `/sr24-game-dev` | **Customized** |
| [`spec-driven-development`](../skills/addyosmani-agent-skills/spec-driven-development/SKILL.md) | [agent-skills](https://github.com/addyosmani/agent-skills) | Web Dev | Phase 02 | `/sr24-web-dev`, `/sr24-saas` | **Integrated** |
| [`c4-architecture-model`](../skills/sr24-custom-engineering/c4-architecture-model/SKILL.md) | [C4-PlantUML](https://github.com/plantuml-stdlib/C4-PlantUML) | Web Dev | Phase 02 | `/sr24-web-dev`, `/sr24-saas` | **Integrated** |
| [`mermaid-diagrams`](../skills/sr24-custom-engineering/mermaid-diagrams/SKILL.md) | [mermaid](https://github.com/mermaid-js/mermaid) | Web Dev | Phase 02 | `/sr24-web-dev`, `/sr24-saas` | **Integrated** |
| [`taste-skill`](../skills/sr24-custom-engineering/taste-skill/SKILL.md) | [taste-skill](https://github.com/Leonxlnx/taste-skill) | Web Dev | Phase 03 | `/sr24-web-dev`, `/sr24-design` | **Integrated** |
| [`lucide-icons`](../skills/sr24-custom-engineering/lucide-icons/SKILL.md) | [lucide](https://github.com/lucide-icons/lucide) | Web Dev | Phase 03 | `/sr24-web-dev`, `/sr24-design` | **Integrated** |
| [`fontsource-typography`](../skills/sr24-custom-engineering/fontsource-typography/SKILL.md) | [fontsource](https://github.com/fontsource/fontsource) | Web Dev | Phase 03 | `/sr24-web-dev`, `/sr24-design` | **Integrated** |
| [`impeccable`](../skills/sr24-custom-engineering/impeccable/SKILL.md) | [impeccable](https://github.com/pbakaus/impeccable) | Web Dev | Phase 04 | `/sr24-web-dev`, `/sr24-design` | **Integrated** |
| [`ui-ux-pro-max`](../skills/sr24-custom-engineering/ui-ux-pro-max/SKILL.md) | [ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | Web Dev | Phase 04 | `/sr24-web-dev`, `/sr24-design` | **Integrated** |
| [`antislop`](../skills/sr24-custom-engineering/antislop/SKILL.md) | [anti-slop](https://github.com/miqdadbadjuber/anti-slop) | Web Dev | Phase 04 | `/sr24-web-dev`, `/sr24-design` | **Integrated** |
| [`antislop-ui`](../skills/sr24-custom-engineering/antislop-ui/SKILL.md) | [anti-slop](https://github.com/miqdadbadjuber/anti-slop) | Web Dev | Phase 04 | `/sr24-web-dev`, `/sr24-design` | **Integrated** |
| [`component-intelligence`](../skills/sr24-custom-engineering/component-intelligence/SKILL.md) | [aceternity-ui](https://github.com/aceternity/aceternity-ui) | Web Dev | Phase 04 | `/sr24-web-dev`, `/sr24-design` | **Integrated** |
| [`motion-animations`](../skills/sr24-custom-engineering/motion-animations/SKILL.md) | [motion](https://github.com/motiondivision/motion) | Web Dev | Phase 04 | `/sr24-web-dev`, `/sr24-design` | **Integrated** |
| [`axe-core-accessibility`](../skills/sr24-custom-engineering/axe-core-accessibility/SKILL.md) | [axe-core](https://github.com/dequelabs/axe-core) | Web Dev | Phase 04 | `/sr24-web-dev`, `/sr24-design` | **Integrated** |
| [`bulletproof-react`](../skills/sr24-custom-engineering/bulletproof-react/SKILL.md) | [bulletproof-react](https://github.com/alan2207/bulletproof-react) | Web Dev | Phase 05 | `/sr24-web-dev`, `/sr24-fullstack` | **Integrated** |
| [`typescript-eslint`](../skills/sr24-custom-engineering/typescript-eslint/SKILL.md) | [typescript-eslint](https://github.com/typescript-eslint/typescript-eslint) | Web Dev | Phase 05 | `/sr24-web-dev`, `/sr24-fullstack` | **Integrated** |
| [`react-testing-library`](../skills/sr24-custom-engineering/react-testing-library/SKILL.md) | [react-testing-library](https://github.com/testing-library/react-testing-library) | Web Dev | Phase 05 | `/sr24-web-dev`, `/sr24-fullstack` | **Integrated** |
| [`gsap-animations`](../skills/sr24-custom-engineering/gsap-animations/SKILL.md) | [GSAP](https://github.com/greensock/GSAP) | Web Dev / Game | Phase 05 / 03 | `/sr24-web-dev`, `/sr24-browser-game` | **Integrated** |
| [`supabase-engineering`](../skills/sr24-custom-engineering/supabase-engineering/SKILL.md) | [agent-skills](https://github.com/supabase/agent-skills) | Web Dev | Phase 06 | `/sr24-web-dev`, `/sr24-fullstack` | **Integrated** |
| [`node-best-practices`](../skills/sr24-custom-engineering/node-best-practices/SKILL.md) | [nodebestpractices](https://github.com/goldbergyoni/nodebestpractices) | Web Dev | Phase 06 | `/sr24-web-dev`, `/sr24-fullstack` | **Integrated** |
| [`socketio-realtime`](../skills/sr24-custom-engineering/socketio-realtime/SKILL.md) | [socket.io](https://github.com/socketio/socket.io) | Web Dev / Game | Phase 06 / 06 | `/sr24-web-dev`, `/sr24-multiplayer` | **Integrated** |
| [`zod-schema-validation`](../skills/sr24-custom-engineering/zod-schema-validation/SKILL.md) | [zod](https://github.com/colinhacks/zod) | Web Dev | Phase 06 | `/sr24-web-dev`, `/sr24-fullstack` | **Integrated** |
| [`bullmq-job-queues`](../skills/sr24-custom-engineering/bullmq-job-queues/SKILL.md) | [bullmq](https://github.com/taskforcesh/bullmq) | Web Dev | Phase 06 | `/sr24-web-dev`, `/sr24-fullstack` | **Integrated** |
| [`prisma-orm`](../skills/sr24-custom-engineering/prisma-orm/SKILL.md) | [prisma](https://github.com/prisma/prisma) | Web Dev | Phase 07 | `/sr24-web-dev`, `/sr24-fullstack` | **Integrated** |
| [`drizzle-orm`](../skills/sr24-custom-engineering/drizzle-orm/SKILL.md) | [drizzle-orm](https://github.com/drizzle-team/drizzle-orm) | Web Dev | Phase 07 | `/sr24-web-dev`, `/sr24-fullstack` | **Integrated** |
| [`dbml-schema-design`](../skills/sr24-custom-engineering/dbml-schema-design/SKILL.md) | [dbml](https://github.com/holistics/dbml) | Web Dev | Phase 07 | `/sr24-web-dev`, `/sr24-fullstack` | **Integrated** |
| [`redis-in-memory-datastore`](../skills/sr24-custom-engineering/redis-in-memory-datastore/SKILL.md) | [redis](https://github.com/redis/redis) | Web Dev / Game | Phase 07 / 06 | `/sr24-web-dev`, `/sr24-multiplayer` | **Integrated** |
| [`razorpay-upi-specialist`](../skills/sr24-custom-engineering/razorpay-upi-specialist/SKILL.md) | [SR24plus-engineering-toolkit](https://github.com/sahil24raj/SR24plus-engineering-toolkit/tree/main/skills/sr24-custom-engineering/razorpay-upi-specialist) | Web Dev | Phase 08 | `/sr24-web-dev`, `/sr24-saas` | **Integrated** |
| [`indian-gst-billing-engineer`](../skills/sr24-custom-engineering/indian-gst-billing-engineer/SKILL.md) | [SR24plus-engineering-toolkit](https://github.com/sahil24raj/SR24plus-engineering-toolkit/tree/main/skills/sr24-custom-engineering/indian-gst-billing-engineer) | Web Dev | Phase 08 | `/sr24-web-dev`, `/sr24-saas` | **Integrated** |
| [`lago-billing`](../skills/sr24-custom-engineering/lago-billing/SKILL.md) | [lago](https://github.com/getlago/lago) | Web Dev | Phase 08 | `/sr24-web-dev`, `/sr24-saas` | **Integrated** |
| [`growthbook-experimentation`](../skills/sr24-custom-engineering/growthbook-experimentation/SKILL.md) | [growthbook](https://github.com/growthbook/growthbook) | Web Dev | Phase 08 | `/sr24-web-dev`, `/sr24-saas` | **Integrated** |
| [`vendure-ecommerce`](../skills/sr24-custom-engineering/vendure-ecommerce/SKILL.md) | [vendure](https://github.com/vendure-ecommerce/vendure) | Web Dev | Phase 08 | `/sr24-web-dev`, `/sr24-saas` | **Integrated** |
| [`owasp-zap-scanner`](../skills/sr24-custom-engineering/owasp-zap-scanner/SKILL.md) | [zaproxy](https://github.com/zaproxy/zaproxy) | Web Dev | Phase 09 | `/sr24-web-dev`, `/sr24-security` | **Integrated** |
| [`gitleaks-secret-detection`](../skills/sr24-custom-engineering/gitleaks-secret-detection/SKILL.md) | [gitleaks](https://github.com/gitleaks/gitleaks) | Web Dev | Phase 09 | `/sr24-web-dev`, `/sr24-security` | **Integrated** |
| [`trivy-security-scanner`](../skills/sr24-custom-engineering/trivy-security-scanner/SKILL.md) | [trivy](https://github.com/aquasecurity/trivy) | Web Dev | Phase 09 | `/sr24-web-dev`, `/sr24-security` | **Integrated** |
| [`osv-scanner`](../skills/sr24-custom-engineering/osv-scanner/SKILL.md) | [osv-scanner](https://github.com/google/osv-scanner) | Web Dev | Phase 09 | `/sr24-web-dev`, `/sr24-security` | **Integrated** |
| [`playwright-testing`](../skills/sr24-custom-engineering/playwright-testing/SKILL.md) | [playwright](https://github.com/microsoft/playwright) | Web Dev / Game | Phase 10 / 10 | `/sr24-web-dev`, `/sr24-game-dev` | **Integrated** |
| [`lost-pixel-visual-regression`](../skills/sr24-custom-engineering/lost-pixel-visual-regression/SKILL.md) | [lost-pixel](https://github.com/lost-pixel/lost-pixel) | Web Dev | Phase 10 | `/sr24-web-dev` | **Integrated** |
| [`k6-load-testing`](../skills/sr24-custom-engineering/k6-load-testing/SKILL.md) | [k6](https://github.com/grafana/k6) | Web Dev | Phase 10 | `/sr24-web-dev`, `/sr24-saas` | **Integrated** |
| [`bruno-api-testing`](../skills/sr24-custom-engineering/bruno-api-testing/SKILL.md) | [bruno](https://github.com/usebruno/bruno) | Web Dev | Phase 10 | `/sr24-web-dev`, `/sr24-fullstack` | **Integrated** |
| [`docker-containerization`](../skills/sr24-custom-engineering/docker-containerization/SKILL.md) | [docs](https://github.com/docker/docs) | Web Dev | Phase 11 | `/sr24-web-dev`, `/sr24-ship` | **Integrated** |
| [`opentofu-iac`](../skills/sr24-custom-engineering/opentofu-iac/SKILL.md) | [opentofu](https://github.com/opentofu/opentofu) | Web Dev | Phase 11 | `/sr24-web-dev`, `/sr24-ship` | **Integrated** |
| [`github-actions-ci`](../skills/sr24-custom-engineering/github-actions-ci/SKILL.md) | [runner](https://github.com/actions/runner) | Web Dev | Phase 11 | `/sr24-web-dev`, `/sr24-ship` | **Integrated** |
| [`sentry-monitoring`](../skills/sr24-custom-engineering/sentry-monitoring/SKILL.md) | [sentry](https://github.com/getsentry/sentry) | Web Dev | Phase 11 | `/sr24-web-dev`, `/sr24-ship` | **Integrated** |
| [`posthog-analytics`](../skills/sr24-custom-engineering/posthog-analytics/SKILL.md) | [posthog](https://github.com/PostHog/posthog) | Web Dev | Phase 12 | `/sr24-web-dev`, `/sr24-ship` | **Integrated** |
| [`microsoft-clarity`](../skills/sr24-custom-engineering/microsoft-clarity/SKILL.md) | [clarity](https://github.com/microsoft/clarity) | Web Dev | Phase 12 | `/sr24-web-dev`, `/sr24-ship` | **Integrated** |
| [`game-programming-patterns`](../skills/sr24-custom-engineering/game-programming-patterns/SKILL.md) | [game-programming-patterns](https://github.com/munificent/game-programming-patterns) | Game Dev | Phase 01 | `/sr24-game-dev`, `/sr24-browser-game` | **Integrated** |
| [`awesome-gamedev-skills`](../skills/sr24-custom-engineering/awesome-gamedev-skills/SKILL.md) | [magictools](https://github.com/ellisonleao/magictools) | Game Dev | Phase 01 | `/sr24-game-dev` | **Integrated** |
| [`bitecs-architecture`](../skills/sr24-custom-engineering/bitecs-architecture/SKILL.md) | [bitECS](https://github.com/NateLevin1/bitECS) | Game Dev | Phase 02 | `/sr24-game-dev`, `/sr24-browser-game` | **Integrated** |
| [`threejs-ui-hud`](../skills/sr24-custom-engineering/threejs-ui-hud/SKILL.md) | [three.js](https://github.com/mrdoob/three.js) | Game Dev | Phase 03 | `/sr24-game-dev`, `/sr24-browser-game` | **Integrated** |
| [`howler-js-audio`](../skills/sr24-custom-engineering/howler-js-audio/SKILL.md) | [howler.js](https://github.com/goldfire/howler.js) | Game Dev | Phase 03 | `/sr24-game-dev`, `/sr24-browser-game` | **Integrated** |
| [`web-game-engine`](../skills/sr24-custom-engineering/web-game-engine/SKILL.md) | [SR24plus-engineering-toolkit](https://github.com/sahil24raj/SR24plus-engineering-toolkit/tree/main/skills/sr24-custom-engineering/web-game-engine) | Game Dev | Phase 04 | `/sr24-game-dev`, `/sr24-browser-game` | **Integrated** |
| [`threejs-game-engine`](../skills/sr24-custom-engineering/threejs-game-engine/SKILL.md) | [three.js](https://github.com/mrdoob/three.js) | Game Dev | Phase 04 | `/sr24-game-dev`, `/sr24-browser-game` | **Integrated** |
| [`react-three-fiber`](../skills/sr24-custom-engineering/react-three-fiber/SKILL.md) | [react-three-fiber](https://github.com/pmndrs/react-three-fiber) | Game Dev | Phase 04 | `/sr24-game-dev`, `/sr24-browser-game` | **Integrated** |
| [`pixijs-engine`](../skills/sr24-custom-engineering/pixijs-engine/SKILL.md) | [pixijs](https://github.com/pixijs/pixijs) | Game Dev | Phase 04 | `/sr24-game-dev`, `/sr24-browser-game` | **Integrated** |
| [`phaser-game-engine`](../skills/sr24-custom-engineering/phaser-game-engine/SKILL.md) | [phaser](https://github.com/phaserjs/phaser) | Game Dev | Phase 04 | `/sr24-game-dev`, `/sr24-browser-game` | **Integrated** |
| [`browser-game-architect`](../skills/sr24-custom-engineering/browser-game-architect/SKILL.md) | [SR24plus-engineering-toolkit](https://github.com/sahil24raj/SR24plus-engineering-toolkit/tree/main/skills/sr24-custom-engineering/browser-game-architect) | Game Dev | Phase 04 | `/sr24-game-dev`, `/sr24-browser-game` | **Integrated** |
| [`rapier-physics`](../skills/sr24-custom-engineering/rapier-physics/SKILL.md) | [rapier](https://github.com/dimforge/rapier) | Game Dev | Phase 05 | `/sr24-game-dev`, `/sr24-browser-game` | **Integrated** |
| [`react-three-rapier`](../skills/sr24-custom-engineering/react-three-rapier/SKILL.md) | [react-three-rapier](https://github.com/pmndrs/react-three-rapier) | Game Dev | Phase 05 | `/sr24-game-dev`, `/sr24-browser-game` | **Integrated** |
| [`jolt-physics`](../skills/sr24-custom-engineering/jolt-physics/SKILL.md) | [JoltPhysics](https://github.com/jrouwe/JoltPhysics) | Game Dev | Phase 05 | `/sr24-game-dev`, `/sr24-racing-game` | **Integrated** |
| [`matter-js-physics`](../skills/sr24-custom-engineering/matter-js-physics/SKILL.md) | [matter-js](https://github.com/liabru/matter-js) | Game Dev | Phase 05 | `/sr24-game-dev`, `/sr24-browser-game` | **Integrated** |
| [`combat-mechanics-engineer`](../skills/sr24-custom-engineering/combat-mechanics-engineer/SKILL.md) | [SR24plus-engineering-toolkit](https://github.com/sahil24raj/SR24plus-engineering-toolkit/tree/main/skills/sr24-custom-engineering/combat-mechanics-engineer) | Game Dev | Phase 05 | `/sr24-game-dev`, `/sr24-browser-game` | **Integrated** |
| [`colyseus-multiplayer`](../skills/sr24-custom-engineering/colyseus-multiplayer/SKILL.md) | [colyseus](https://github.com/colyseus/colyseus) | Game Dev | Phase 06 | `/sr24-game-dev`, `/sr24-multiplayer` | **Integrated** |
| [`nakama-backend`](../skills/sr24-custom-engineering/nakama-backend/SKILL.md) | [nakama](https://github.com/heroiclabs/nakama) | Game Dev | Phase 06 | `/sr24-game-dev`, `/sr24-multiplayer` | **Integrated** |
| [`gaffer-on-games-networking`](../skills/sr24-custom-engineering/gaffer-on-games-networking/SKILL.md) | [libyojimbo](https://github.com/networkprotocol/libyojimbo) | Game Dev | Phase 06 | `/sr24-game-dev`, `/sr24-multiplayer` | **Integrated** |
| [`browser-game-anti-cheat-engineer`](../skills/sr24-custom-engineering/browser-game-anti-cheat-engineer/SKILL.md) | [SR24plus-engineering-toolkit](https://github.com/sahil24raj/SR24plus-engineering-toolkit/tree/main/skills/sr24-custom-engineering/browser-game-anti-cheat-engineer) | Game Dev | Phase 06 | `/sr24-game-dev`, `/sr24-multiplayer` | **Integrated** |
| [`unity-entities-ecs`](../skills/sr24-custom-engineering/unity-entities-ecs/SKILL.md) | [com.unity.entities](https://github.com/Unity-Technologies/com.unity.entities) | Game Dev | Phase 07 | `/sr24-game-dev`, `/sr24-unity` | **Integrated** |
| [`urp-postprocessing`](../skills/unity-skills/urp-postprocessing/SKILL.md) | [com.unity.entities](https://github.com/Unity-Technologies/com.unity.entities) | Game Dev | Phase 07 | `/sr24-game-dev`, `/sr24-unity` | **Integrated** |
| [`truck-physics-engineer`](../skills/sr24-custom-engineering/truck-physics-engineer/SKILL.md) | [SR24plus-engineering-toolkit](https://github.com/sahil24raj/SR24plus-engineering-toolkit/tree/main/skills/sr24-custom-engineering/truck-physics-engineer) | Game Dev | Phase 08 | `/sr24-game-dev`, `/sr24-racing-game` | **Integrated** |
| [`realistic-car-controller-engineer`](../skills/sr24-custom-engineering/realistic-car-controller-engineer/SKILL.md) | [SR24plus-engineering-toolkit](https://github.com/sahil24raj/SR24plus-engineering-toolkit/tree/main/skills/sr24-custom-engineering/realistic-car-controller-engineer) | Game Dev | Phase 08 | `/sr24-game-dev`, `/sr24-racing-game` | **Integrated** |
| [`racing-track-design-engineer`](../skills/sr24-custom-engineering/racing-track-design-engineer/SKILL.md) | [SR24plus-engineering-toolkit](https://github.com/sahil24raj/SR24plus-engineering-toolkit/tree/main/skills/sr24-custom-engineering/racing-track-design-engineer) | Game Dev | Phase 08 | `/sr24-game-dev`, `/sr24-racing-game` | **Integrated** |
| [`gltf-transform-pipeline`](../skills/sr24-custom-engineering/gltf-transform-pipeline/SKILL.md) | [glTF-Transform](https://github.com/donmccurdy/glTF-Transform) | Game Dev | Phase 09 | `/sr24-game-dev`, `/sr24-unity` | **Integrated** |
| [`blender-pipeline`](../skills/sr24-custom-engineering/blender-pipeline/SKILL.md) | [blender](https://projects.blender.org/blender/blender) | Game Dev | Phase 09 | `/sr24-game-dev`, `/sr24-unity` | **Integrated** |
| [`threejs-optimization-profiling`](../skills/sr24-custom-engineering/threejs-optimization-profiling/SKILL.md) | [three.js](https://github.com/mrdoob/three.js) | Game Dev | Phase 10 | `/sr24-game-dev`, `/sr24-browser-game` | **Integrated** |
| [`gameplay-regression-testing`](../skills/sr24-custom-engineering/gameplay-regression-testing/SKILL.md) | [playwright](https://github.com/microsoft/playwright) | Game Dev | Phase 10 | `/sr24-game-dev`, `/sr24-browser-game` | **Integrated** |
| [`unity-performance-testing`](../skills/sr24-custom-engineering/unity-performance-testing/SKILL.md) | [com.unity.entities](https://github.com/Unity-Technologies/com.unity.entities) | Game Dev | Phase 10 | `/sr24-game-dev`, `/sr24-unity` | **Integrated** |
| [`game-build-and-release`](../skills/sr24-custom-engineering/game-build-and-release/SKILL.md) | [SR24plus-engineering-toolkit](https://github.com/sahil24raj/SR24plus-engineering-toolkit/tree/main/skills/sr24-custom-engineering/game-build-and-release) | Game Dev | Phase 11 | `/sr24-game-dev`, `/sr24-ship` | **Integrated** |
| [`game-analytics-sdk`](../skills/sr24-custom-engineering/game-analytics-sdk/SKILL.md) | [GA-SDK-JAVASCRIPT](https://github.com/gameanalytics/GA-SDK-JAVASCRIPT) | Game Dev | Phase 12 | `/sr24-game-dev` | **Integrated** |
| [`umami-game-analytics`](../skills/sr24-custom-engineering/umami-game-analytics/SKILL.md) | [umami](https://github.com/umami-software/umami) | Game Dev | Phase 12 | `/sr24-game-dev` | **Integrated** |

---

## 3. Central Upstream Register Cross-Reference
For a complete, verified directory of all 65+ upstream source repositories, licensing metadata, and canonical authors, see [`registry/SR24PLUS-UPSTREAM-SOURCES.md`](../registry/SR24PLUS-UPSTREAM-SOURCES.md).
