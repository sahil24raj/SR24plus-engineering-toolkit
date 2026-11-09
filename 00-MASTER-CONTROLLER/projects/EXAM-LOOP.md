# PROJECT WORKFLOW PROFILE: EXAM LOOP
## AI-Powered Adaptive Educational Testing Platform

> **Project Identity**: EXAM LOOP  
> **Domain**: Computer Adaptive Testing (CAT), Item Response Theory (IRT), AI Question Generation  
> **Primary Command**: `/sr24-ai exam-loop` or `/sr24-saas exam-loop`

---

## 1. Specialist Squad Roster

| Role | Assigned Skill(s) | Primary Mission |
|---|---|---|
| **Assessment Architect** | `assessment-engine-architect` | IRT 1PL/2PL adaptive difficulty engine, test session state |
| **AI Systems Lead** | `agency-engineering-ai-engineer` + `mcp-server-developer` | MCP question generator tools, Bloom's taxonomy classifier |
| **AI Security Specialist**| `prompt-injection-security-engineer` | Prompt leak defense, XML delimiters, untrusted input containment |
| **Full-Stack Engineer** | `agency-engineering-frontend-developer` + `agency-engineering-backend-architect` | React KaTeX math renderer, question cache, student portal |
| **Database Architect** | `agency-engineering-database-optimizer` | Normalized question bank schema, student response audit log |
| **Proctoring Engineer** | `agency-security-appsec-engineer` | Tab-switch telemetry, fullscreen locks, copy-paste defense |
| **Analytics Lead** | `agency-support-analytics-reporter` | Percentile ranking, difficulty-weighted scoring, topic heatmaps |
| **QA Automation** | `playwright-automation-engineer` | Timed examination smoke tests, automated answer submission |

---

## 2. Assessment Engine Architecture

- **Item Response Theory (IRT)**: Student theta ($\theta$) ability updated dynamically after every answer.
- **Formulas & Diagrams**: Native KaTeX formatting for complex mathematical integrals, chemical reactions, and physics diagrams.
- **Proctoring Integrity**: Real-time logging of focus-loss events, browser resize triggers, and screenshot attempts.
- **Instant Diagnostic Analytics**: Diagnostic report showing time spent per question, topic-level weakness radar, and predicted rank.

---

## 3. Mandatory Quality Gates

1. **Deterministic Timing**: Test countdown timer runs server-side to prevent local device clock tampering.
2. **Zero Latex Clipping**: All mathematical equations rendered with responsive line-breaking and KaTeX fonts.
3. **Prompt Hardening**: MCP question generation tools reject system prompt exfiltration and out-of-curriculum requests.
