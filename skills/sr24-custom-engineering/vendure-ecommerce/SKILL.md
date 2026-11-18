---
name: vendure-ecommerce
description: >-
  Specialist in Vendure headless e-commerce architecture — product catalogs, variant pricing, cart sessions, checkout pipelines, and order fulfillment.
---

# Vendure Headless E-Commerce & Checkout Architecture

## 1. When to Activate
Activate this skill whenever a project or prompt requires specialist in vendure headless e-commerce architecture — product catalogs, variant pricing, cart sessions, checkout pipelines, and order fulfillment.. It is assigned to official engineering phases in the **SR24Plus Engineering Toolkit**.

## 2. When Not to Activate
- Do not activate when the task does not involve vendure-ecommerce.
- Do not activate as a substitute for simple static mockups where deeper engineering is unnecessary.

## 3. Core Capabilities
- Headless e-commerce architecture decoupling GraphQL storefronts from administrative backend
- Shopping cart session management with tax calculation, promotions, and shipping methods
- Custom payment integration plugins implementing Indian payment rails (Razorpay, UPI)
- Multi-tenant marketplace configuration with discrete vendor catalog partitions
- Inventory reservation preventing overselling during high-velocity flash sales

## 4. Engineering Workflow
1. **Discovery & Architecture**: Inspect technical constraints, performance requirements, and data contracts.
2. **Setup & Configuration**: Install official package dependencies and configure environment variables.
3. **Implementation**: Author production-grade code using clean architecture, strict TypeScript types, and error handling.
4. **Validation & Testing**: Run unit and integration tests confirming zero regressions.
5. **Production Deployment**: Verify build bundle impact, tree-shaking, and observability telemetry.

## 5. Implementation Instructions & Code Patterns

```typescript
import { GraphQLClient, gql } from 'graphql-request';

const client = new GraphQLClient(process.env.VENDURE_SHOP_API || 'http://localhost:3000/shop-api');

const ADD_ITEM_TO_ORDER = gql`
  mutation AddItemToOrder($productVariantId: ID!, $quantity: Int!) {
    addItemToOrder(productVariantId: $productVariantId, quantity: $quantity) {
      ... on Order {
        id
        code
        totalWithTax
        lines {
          id
          quantity
          productVariant {
            name
            priceWithTax
          }
        }
      }
      ... on ErrorResult {
        errorCode
        message
      }
    }
  }
`;
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
- **Repository**: [https://github.com/vendure-ecommerce/vendure](https://github.com/vendure-ecommerce/vendure)
- **Category**: SR24-WEB-DEV Canonical Engineering Skill

## 10. License & Attribution
- **License**: MIT
- **Maintained By**: SR24Plus Autonomous Engineering Architecture
