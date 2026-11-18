---
name: owasp-zap-scanner
description: >-
  Specialist in OWASP ZAP (Zed Attack Proxy) automated security testing — dynamic vulnerability scanning, baseline checks, SQL injection, XSS, and security reports.
---

# OWASP ZAP Dynamic Application Security Testing (DAST)

## 1. When to Activate
Activate this skill whenever a project or prompt requires specialist in owasp zap (zed attack proxy) automated security testing — dynamic vulnerability scanning, baseline checks, sql injection, xss, and security reports.. It is assigned to official engineering phases in the **SR24Plus Engineering Toolkit**.

## 2. When Not to Activate
- Do not activate when the task does not involve owasp-zap-scanner.
- Do not activate as a substitute for simple static mockups where deeper engineering is unnecessary.

## 3. Core Capabilities
- Automated baseline dynamic scanning of web endpoints and staging deployments
- Active vulnerability fuzzing for Cross-Site Scripting (XSS), SQLi, and Path Traversal
- HTTP security header compliance auditing (CSP, HSTS, X-Content-Type-Options)
- Authentication session spidering across protected web routes
- CI/CD pipeline automated security gates blocking releases on High/Critical findings

## 4. Engineering Workflow
1. **Discovery & Architecture**: Inspect technical constraints, performance requirements, and data contracts.
2. **Setup & Configuration**: Install official package dependencies and configure environment variables.
3. **Implementation**: Author production-grade code using clean architecture, strict TypeScript types, and error handling.
4. **Validation & Testing**: Run unit and integration tests confirming zero regressions.
5. **Production Deployment**: Verify build bundle impact, tree-shaking, and observability telemetry.

## 5. Implementation Instructions & Code Patterns

```typescript
# OWASP ZAP Baseline Scan GitHub Action
name: OWASP ZAP Security Audit
on:
  push:
    branches: [main]

jobs:
  zap_scan:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Run ZAP Baseline Scan
        uses: zaproxy/action-baseline@v0.12.0
        with:
          target: 'https://staging.gullyverse.com'
          rules_file_name: '.zap/rules.tsv'
          fail_action: true
```

## 6. Best Practices
- **Strict Typing**: Never use `any`; use strict interface and generic contracts.
- **Error Boundaries**: Handle all edge cases, offline drops, and network timeouts gracefully.
- **Performance Budget**: Avoid blocking main thread operations; optimize bundle sizes and lazy-load where appropriate.
- **Security**: Never expose private keys, credentials, or sensitive customer data in client-side bundles.

## 7. Common Anti-Patterns to Avoid
- Hardcoding credentials or API endpoints directly into source files.
- Ignoring promise rejections and async exceptions.
- Creating monolithic un-testable files instead of modular single-responsibility units.
- Introducing layout shifts or un-optimized re-renders.

## 8. Verification & Testing Checklist
- [ ] TypeScript compiles cleanly with zero errors (`tsc --noEmit`).
- [ ] Unit tests pass verifying expected behavior and edge cases.
- [ ] Environment variables documented in `.env.example`.
- [ ] Build artifact size verified with tree-shaking confirmed.

## 9. Official Source Repository & Upstream Reference
- **Repository**: [https://github.com/zaproxy/zaproxy](https://github.com/zaproxy/zaproxy)
- **Category**: SR24-WEB-DEV Canonical Engineering Skill

## 10. License & Attribution
- **License**: Apache-2.0
- **Maintained By**: SR24Plus Autonomous Engineering Architecture
