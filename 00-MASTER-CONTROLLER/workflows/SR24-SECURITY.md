# WORKFLOW: /sr24-security — COMPREHENSIVE SECURITY & APPSEC SQUAD

> **Command**: `/sr24-security [task]`  
> **Natural Language Trigger**: `"Audit security"`, `"Penetration test"`, `"Check vulnerabilities"`, `"Fix OWASP flaws"`  
> **Mission**: Conduct exhaustive offensive and defensive security audits, threat modeling, dependency vulnerability analysis, secret exfiltration scanning, and cloud hardening.

---

## SECURITY SPECIALIST SQUAD

| Role | Skill | Focus |
|---|---|---|
| **AppSec Lead** | `agency-security-appsec-engineer` | OWASP Top 10, static/dynamic code analysis, secure coding practices |
| **Security Architect** | `agency-security-architect` | Threat modeling (STRIDE), zero trust boundaries, cryptographic standards |
| **Cloud Security Architect** | `agency-security-cloud-security-architect` | IAM least privilege, VPC peering, KMS encryption, S3/bucket policies |
| **Penetration Tester** | `agency-security-penetration-tester` | Ethical exploit simulation, authorization bypass, parameter fuzzing |
| **AI Code Auditor** | `agency-security-ai-generated-code-auditor` | Hallucinated package vulnerabilities, insecure defaults in AI code |
| **Compliance Auditor** | `agency-security-compliance-auditor` | SOC 2, ISO 27001, GDPR, HIPAA data protection requirements |

---

## 7-POINT SECURITY AUDIT PROTOCOL

1. **Point 1: Secret & Credential Scanning**:
   - Scan git tree, `.env*`, config files, and client-side bundles for exposed API keys, tokens, or private keys.
   - Verify `.gitignore` comprehensively blocks all local credentials.
2. **Point 2: Authentication & Session Integrity**:
   - Verify passwords use secure hashing (Argon2id or bcrypt with work factor >= 12).
   - Ensure session tokens use `HttpOnly`, `Secure`, `SameSite=Lax/Strict` cookie flags.
   - Check password reset flows against token reuse and timing attacks.
3. **Point 3: Authorization & Multi-Tenant Access Control (BOLA/IDOR)**:
   - Audit every mutation endpoint (`POST`, `PUT`, `DELETE`): does it verify that the requesting user owns the target record?
   - Prevent Broken Object-Level Authorization (IDOR).
4. **Point 4: Injection & Input Sanitization**:
   - Verify 100% of database queries use parameterized SQL/ORM bindings. Zero raw string concatenation.
   - Check DOM rendering against Cross-Site Scripting (XSS).
5. **Point 5: Network, Headers & CORS**:
   - Enforce strict Content Security Policy (`CSP`), `X-Frame-Options: DENY`, `X-Content-Type-Options: nosniff`.
   - Ensure CORS whitelist specifies explicit authorized origins (never `Access-Control-Allow-Origin: *` with credentials).
6. **Point 6: Rate Limiting & DoS Hardening**:
   - Apply rate limiters on login, registration, OTP generation, and resource-heavy endpoints.
7. **Point 7: Dependency Vulnerability Audit**:
   - Run dependency audit (`npm audit`, `pip-audit`, `cargo audit`) and document remediation for known CVEs.
