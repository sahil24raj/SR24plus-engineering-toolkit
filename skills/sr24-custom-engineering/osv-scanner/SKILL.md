---
name: osv-scanner
description: >-
  Specialist in Google OSV Scanner — open-source vulnerability database audits, lockfile vulnerability detection, transitive dependency scanning, and CVE remediation.
---

# Google OSV Scanner Dependency Vulnerability & CVE Remediation

## 1. When to Activate
Activate this skill whenever a project or prompt requires specialist in google osv scanner — open-source vulnerability database audits, lockfile vulnerability detection, transitive dependency scanning, and cve remediation.. It is assigned to official engineering phases in the **SR24Plus Engineering Toolkit**.

## 2. When Not to Activate
- Do not activate when the task does not involve osv-scanner.
- Do not activate as a substitute for simple static mockups where deeper engineering is unnecessary.

## 3. Core Capabilities
- Fast lockfile scanning (`package-lock.json`, `pnpm-lock.yaml`, `Cargo.lock`) against Google OSV database
- Precise commit-level vulnerability matching eliminating false-positive CVE alerts
- Remediation path suggestions for upgrading specific vulnerable dependency versions
- Docker container filesystem dependency scanning
- Integration into pre-commit git hooks and CI/CD pull request security gates

## 4. Engineering Workflow
1. **Discovery & Architecture**: Inspect technical constraints, performance requirements, and data contracts.
2. **Setup & Configuration**: Install official package dependencies and configure environment variables.
3. **Implementation**: Author production-grade code using clean architecture, strict TypeScript types, and error handling.
4. **Validation & Testing**: Run unit and integration tests confirming zero regressions.
5. **Production Deployment**: Verify build bundle impact, tree-shaking, and observability telemetry.

## 5. Implementation Instructions & Code Patterns

```typescript
# OSV-Scanner Execution Command
# Install: go install github.com/google/osv-scanner/cmd/osv-scanner@v1

# 1. Scan root project lockfiles recursively:
# osv-scanner -r .

# 2. Output detailed JSON vulnerability report:
# osv-scanner --json -r . > osv-report.json

# 3. GitHub Action configuration:
name: OSV Dependency Vulnerability Audit
on: [pull_request]
jobs:
  scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: google/osv-scanner-action@v1.9.0
        with:
          scan-args: |-
            -r
            --skip-git
            .
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
- **Repository**: [https://github.com/google/osv-scanner](https://github.com/google/osv-scanner)
- **Category**: SR24-WEB-DEV Canonical Engineering Skill

## 10. License & Attribution
- **License**: Apache-2.0
- **Maintained By**: SR24Plus Autonomous Engineering Architecture
