---
name: sr24-production-auditor
description: Full-spectrum automated production audit engine covering Architecture, UI/UX, Frontend, Backend, Database, Security, Game Systems, and CI/CD deployment.
---

# SR24 Production Auditor (`sr24-production-auditor`)

## 1. Overview & Operational Mandate
The **`sr24-production-auditor`** is an automated quality gate that systematically inspects projects from top to bottom. It enforces production-grade rigor across 8 distinct architectural modules, logs structured findings with concrete evidence, and generates non-fabricated scores out of 10.0.

## 2. The 8 Audit Modules
1. **Module A — Architecture Audit**: Clean separation of concerns, modular boundaries, cyclic dependency checks, API contracts.
2. **Module B — UI/UX & Anti-Slop**: Visual hierarchy, responsive viewport safety, accessibility standards, elimination of generic AI slop.
3. **Module C — Frontend Performance**: React re-render optimization, unmemoized calculations, bundle bloat, memory leak patterns.
4. **Module D — Backend & APIs**: Route handler safety, validation, error encapsulation, rate limiting, idempotent mutations.
5. **Module E — Database & Data Integrity**: Schema indexing, foreign key constraints, migration traceability, N+1 query detection.
6. **Module F — Security & Secrets**: Regex scanning for API keys/tokens, OWASP Top 10 vulnerabilities, XSS/SQLi vectors, CSP/CORS headers.
7. **Module G — Game Development Systems**: Deterministic 60Hz accumulator loop, collision layers, physics stability, asset memory budgeting.
8. **Module H — Deployment & Operations**: Production build flags, Dockerfile optimization, CI/CD pipeline integrity, health monitoring.

## 3. Report Output Structure
Generates: `reports/SR24-PRODUCTION-AUDIT.md` containing:
- Individual Dimension Scores (/10.0)
- Finding ID (`SEC-001`, `FE-001`, `GAME-001`)
- Category & Severity (`CRITICAL`, `HIGH`, `MEDIUM`, `LOW`, `INFO`)
- Concrete Code Evidence & Affected Files
- Recommended Solution & Verification Method

## 4. CLI Usage
```bash
python skills/sr24-custom-engineering/sr24-production-auditor/scripts/production_auditor.py [project_path]
```

## 5. Upstream Attribution & License
- Upstream: SR24Plus Core Architecture (`sahil24raj/SR24plus-engineering-toolkit`)
- License: MIT