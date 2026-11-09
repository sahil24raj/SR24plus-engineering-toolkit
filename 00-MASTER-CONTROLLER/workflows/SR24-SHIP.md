# WORKFLOW: /sr24-ship — PRODUCTION RELEASE & SRE SQUAD

> **Command**: `/sr24-ship [task]`  
> **Natural Language Trigger**: `"Prepare release"`, `"Ship to production"`, `"Deploy app"`, `"Create CI/CD pipeline"`  
> **Mission**: Ensure high-reliability, zero-downtime releases with verified automated tests, infrastructure-as-code, rollback plans, and observability dashboards.

---

## SHIP & SRE SPECIALIST SQUAD

| Role | Skill | Focus |
|---|---|---|
| **DevOps Automator** | `agency-engineering-devops-automator` | GitHub Actions, Docker builds, release pipelines, infrastructure automation |
| **Site Reliability Engineer** | `agency-engineering-sre` | SLOs, error budgets, health checks, rollback triggers, incident mitigation |
| **Launch Strategist** | `shipping-and-launch` | Pre-launch checklist, smoke testing, feature flags, user onboarding validation |
| **Automation Architect** | `ci-cd-and-automation` | Quality gates, automated test runners, linting, branch protection rules |
| **Technical Writer** | `agency-engineering-technical-writer` | Release changelogs, operational runbooks, API documentation, disaster recovery plans |

---

## 6-STAGE PRODUCTION RELEASE GATE

```
[1. Build & Test Gate] ─── npm run build / pytest / cargo build
           │
           ▼
[2. Env & Secret Audit] ── Verify all env vars defined in .env.example
           │
           ▼
[3. Migration Validation]  Test database schema migrations up and down
           │
           ▼
[4. Staging Smoke Test] ── Verify core user journeys on preview deployment
           │
           ▼
[5. Production Rollout] ── Blue/green or canary release with health monitoring
           │
           ▼
[6. Post-Deploy Observ] ── Monitor error rates, latency (P95/P99), and alerts
```

### Mandatory Pre-Flight Checklist
- [ ] Working tree is clean with all code committed.
- [ ] 100% of unit, integration, and build tests pass with evidence.
- [ ] No hardcoded secrets or environment variables in repository code.
- [ ] Rollback strategy documented (exact command to revert to previous stable SHA).
- [ ] User approval explicitly granted before live production deployment.
