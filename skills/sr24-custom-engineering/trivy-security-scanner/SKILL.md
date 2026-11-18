---
name: trivy-security-scanner
description: >-
  Specialist in Aqua Security Trivy — container image vulnerability scanning, misconfiguration checks, SBOM generation, and Kubernetes manifest auditing.
---

# Trivy Container, Filesystem & Cloud Security Scanner

## 1. When to Activate
Activate this skill whenever a project or prompt requires specialist in aqua security trivy — container image vulnerability scanning, misconfiguration checks, sbom generation, and kubernetes manifest auditing.. It is assigned to official engineering phases in the **SR24Plus Engineering Toolkit**.

## 2. When Not to Activate
- Do not activate when the task does not involve trivy-security-scanner.
- Do not activate as a substitute for simple static mockups where deeper engineering is unnecessary.

## 3. Core Capabilities
- Docker container base image CVE scanning (Alpine, Debian, Ubuntu, Node.js)
- Infrastructure-as-Code (IaC) misconfiguration scanning (Terraform, Dockerfile, Kubernetes)
- Software Bill of Materials (SBOM) generation in CycloneDX and SPDX formats
- Severity threshold filtering (exit with code 1 on HIGH or CRITICAL issues)
- Zero-dependency single-binary CLI operation in local terminal and CI runners

## 4. Engineering Workflow
1. **Discovery & Architecture**: Inspect technical constraints, performance requirements, and data contracts.
2. **Setup & Configuration**: Install official package dependencies and configure environment variables.
3. **Implementation**: Author production-grade code using clean architecture, strict TypeScript types, and error handling.
4. **Validation & Testing**: Run unit and integration tests confirming zero regressions.
5. **Production Deployment**: Verify build bundle impact, tree-shaking, and observability telemetry.

## 5. Implementation Instructions & Code Patterns

```typescript
# Scan local project filesystem:
# trivy fs --severity HIGH,CRITICAL .

# Scan built Docker image:
# trivy image --severity HIGH,CRITICAL gullyverse-api:latest

# GitHub Actions Workflow Step:
- name: Run Trivy vulnerability scanner
  uses: aquasecurity/trivy-action@master
  with:
    scan-type: 'fs'
    ignore-unfixed: true
    format: 'table'
    severity: 'CRITICAL,HIGH'
    exit-code: '1'

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
- **Repository**: [https://github.com/aquasecurity/trivy](https://github.com/aquasecurity/trivy)
- **Category**: SR24-WEB-DEV Canonical Engineering Skill

## 10. License & Attribution
- **License**: Apache-2.0
- **Maintained By**: SR24Plus Autonomous Engineering Architecture
