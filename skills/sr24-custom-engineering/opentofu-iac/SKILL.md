---
name: opentofu-iac
description: >-
  Specialist in OpenTofu open-source infrastructure-as-code — declarative cloud provisioning, state management, module design, and immutable deployments.
---

# OpenTofu Infrastructure-as-Code & Cloud Automation

## 1. When to Activate
Activate this skill whenever a project or prompt requires specialist in opentofu open-source infrastructure-as-code — declarative cloud provisioning, state management, module design, and immutable deployments.. It is assigned to official engineering phases in the **SR24Plus Engineering Toolkit**.

## 2. When Not to Activate
- Do not activate when the task does not involve opentofu-iac.
- Do not activate as a substitute for simple static mockups where deeper engineering is unnecessary.

## 3. Core Capabilities
- Declarative cloud infrastructure provisioning (AWS, DigitalOcean, GCP, Cloudflare)
- State locking with S3 buckets and DynamoDB table locks preventing concurrent race conditions
- Reusable module architecture for VPCs, ECS/EKS clusters, and managed PostgreSQL databases
- Secret parameter injection via AWS SSM or Vault without committing credentials
- Plan and apply automation integrated into GitHub Actions pull request reviews

## 4. Engineering Workflow
1. **Discovery & Architecture**: Inspect technical constraints, performance requirements, and data contracts.
2. **Setup & Configuration**: Install official package dependencies and configure environment variables.
3. **Implementation**: Author production-grade code using clean architecture, strict TypeScript types, and error handling.
4. **Validation & Testing**: Run unit and integration tests confirming zero regressions.
5. **Production Deployment**: Verify build bundle impact, tree-shaking, and observability telemetry.

## 5. Implementation Instructions & Code Patterns

```typescript
# main.tofu
terraform {
  required_version = ">= 1.6.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
  backend "s3" {
    bucket         = "sr24plus-tofu-state"
    key            = "production/terraform.tfstate"
    region         = "ap-south-1"
    encrypt        = true
    dynamodb_table = "tofu-state-lock"
  }
}

resource "aws_s3_bucket" "game_assets" {
  bucket = "gullyverse-production-assets"
}

resource "aws_s3_bucket_public_access_block" "game_assets_block" {
  bucket = aws_s3_bucket.game_assets.id
  block_public_acls       = false
  block_public_policy     = false
  ignore_public_acls      = false
  restrict_public_buckets = false
}
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
- **Repository**: [https://github.com/opentofu/opentofu](https://github.com/opentofu/opentofu)
- **Category**: SR24-WEB-DEV Canonical Engineering Skill

## 10. License & Attribution
- **License**: MPL-2.0
- **Maintained By**: SR24Plus Autonomous Engineering Architecture
