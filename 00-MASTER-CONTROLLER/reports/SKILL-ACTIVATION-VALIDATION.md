# SR24PLUS SKILL ACTIVATION & RUNTIME VALIDATION PROTOCOL

**Document Purpose**: Define the mandatory validation rules to ensure every skill invocation within the SR24Plus Engineering Toolkit is authentic, verified, and grounded in actual `SKILL.md` instructions.

---

## 1. The Zero-Pretense Principle

In accordance with Antigravity Behavioral Guidelines and the SR24Plus Quality Charter:
1. **Never claim a skill was activated unless its instructions were physically loaded**:
   - The agent must invoke `read_file` or reference the installed skill path before claiming specialist execution.
2. **Never invent non-existent CLI tools or subagent types**:
   - If a capability is missing or requires manual user action, state it honestly.
3. **Never skip quality gates**:
   - Anti-AI-slop critiques, security reviews, and unit test verifications must output concrete evidence (diffs, test logs, terminal outputs) rather than empty affirmative statements.

---

## 2. Runtime Skill Activation Verification Matrix

When any SR24 command (such as `/sr24-web-dev` or `/sr24-game-dev`) executes, each phase must follow this 4-step verification loop:

```
[Phase Trigger] 
       │
       ▼
[1. Path Resolution] ──── Verify skill directory & SKILL.md exists on disk
       │
       ▼
[2. Instruction Load] ─── Read SKILL.md using read_file / active system context
       │
       ▼
[3. Execution Gate] ───── Apply persona constraints, templates, and CLI standards
       │
       ▼
[4. Output Evidence] ──── Produce concrete deliverables (PRD, code, test log, diff)
```

---

## 3. Evidence Standards by Phase

| Phase | Assigned Specialists | Mandatory Verification Output |
|---|---|---|
| **Discovery & Planning** | Product Manager, UX Researcher | Structured `PRD.md` with explicit non-goals and MVP scope |
| **Brand Identity** | Brand Guardian, Visual Storyteller | Color palette tokens (HEX/RGB), font pairings, tone guidelines |
| **UX Architecture** | UX Architect | Screen hierarchy, user journey flow, error & empty state specs |
| **Visual Design Gate** | UI Designer, UI Finish-Gate Reviewer, Impeccable, Anti-Slop | Explicit Anti-Slop critique checklist (contrast, no generic purple gradients, spacing audit) |
| **Frontend Engineering** | Frontend Developer, Senior Developer | Clean component hierarchy, TypeScript strict typing, responsive layout |
| **Backend & Database** | Backend Architect, Database Optimizer | ER diagram / schema, REST/tRPC API endpoints, input validation |
| **AI Integration** | AI Engineer, Prompt Engineer | Prompt template, rate limiting, fallbacks, token cost budget |
| **Security Audit** | AppSec Engineer, Security Architect | Threat analysis matrix (OWASP Top 10, auth validation, secret scan) |
| **QA & Verification** | Test Automation Engineer, Reality Checker | Passing test runner output (`npm test`, `pytest`, `npm run build`) |
| **Ship & DevOps** | DevOps Automator, SRE | Deployment configuration, environment variable manifest, healthcheck |

---

## 4. Anti-Slop Validation Gate Checklist

Before any web or game UI is marked complete, the following checklist must pass:
- [ ] No generic AI purple/blue gradient backgrounds.
- [ ] No decorative floating cards without functional utility.
- [ ] No emoji-based icon systems where SVGs or Lucide icons are appropriate.
- [ ] No arbitrary glassmorphism without high contrast readability.
- [ ] Typography follows a strictly defined mathematical scale (e.g. 1.25 Major Third).
- [ ] All interactive elements possess explicit hover, focus, active, and disabled states.
- [ ] Responsive layouts verified across mobile (375px), tablet (768px), and desktop (1280px+).

---

## 5. Summary Log Output Convention

At the conclusion of each orchestrated command, the Master Router prints a verification summary:
```markdown
### 🛡️ SR24Plus Specialist Execution Summary
- **Command Invoked**: `/sr24-web-dev`
- **Active Project**: Dukaan Saathi POS
- **Specialists Loaded**:
  1. `agency-product-manager` (Scope: PRD & MVP definition) — ✅ Verified
  2. `agency-design-brand-guardian` (Scope: Dark Kirana Visual Identity) — ✅ Verified
  3. `ui-ux-pro-max` + `antislop` (Scope: Anti-Slop Design Gate) — ✅ Verified
  4. `agency-engineering-frontend-developer` (Scope: Three.js Spatial Background) — ✅ Verified
  5. `agency-security-appsec-engineer` (Scope: API Secret Protection) — ✅ Verified
- **Quality Gate Status**: PASS (Zero build errors, 100% test integrity)
```
