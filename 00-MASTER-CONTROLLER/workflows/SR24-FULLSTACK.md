# WORKFLOW: /sr24-fullstack — COMPLETE FULLSTACK ENGINEERING SQUAD

> **Command**: `/sr24-fullstack [task]`  
> **Natural Language Trigger**: `"Build fullstack feature"`, `"Implement end-to-end app"`, `"Create frontend and backend"`  
> **Mission**: Execute cohesive, end-to-end feature implementations across database schema, backend API routes, and frontend user interfaces with tight contract synchronization.

---

## FULLSTACK SPECIALIST SQUAD

| Role | Skill | Focus |
|---|---|---|
| **System Architect** | `agency-engineering-software-architect` | Domain-driven design, module boundaries, unified system architecture |
| **Backend Architect** | `agency-engineering-backend-architect` | REST/GraphQL/tRPC endpoints, service layer, transactional business logic |
| **Database Specialist** | `agency-engineering-database-optimizer` | Schema migrations, indices, query performance, relational integrity |
| **Frontend Engineer** | `agency-engineering-frontend-developer` | React/Next.js UI components, responsive layout, client-side caching |
| **API Contract Specialist** | `api-and-interface-design` | OpenAPI specs, TypeScript types shared between client and server |
| **Fullstack Reviewer** | `agency-engineering-senior-developer` | Code review, error propagation, network resilience, end-to-end verification |

---

## 5-STEP END-TO-END IMPLEMENTATION PIPELINE

1. **Step 1: Interface & Schema Contract**:
   - Define TypeScript data types and API contracts before writing implementation code.
   - Example:
     ```typescript
     export interface OrderPayload {
       customerId: string;
       items: Array<{ productId: string; quantity: number }>;
       paymentMethod: 'CASH' | 'UPI' | 'UDHAAR';
     }
     ```
2. **Step 2: Database Migration & Repository**:
   - Write SQL migration or ORM schema update with proper constraints (`NOT NULL`, `FOREIGN KEY`, `CHECK`).
   - Add database indices on high-frequency query fields (`customer_id`, `created_at`).
3. **Step 3: Backend Controller & Business Logic**:
   - Implement route handler with strict input validation (e.g. Zod or Pydantic).
   - Wrap mutations in database transactions (`BEGIN ... COMMIT`).
   - Return structured HTTP status codes (`201 Created`, `400 Bad Request`, `404 Not Found`, `500 Server Error`).
4. **Step 4: Frontend UI & State Integration**:
   - Implement frontend service call with loading, error, and success state handling.
   - Use optimistic updates or cache invalidation (React Query / SWR / Zustand).
   - Display clear feedback toasts and validation messages to the user.
5. **Step 5: Fullstack Verification**:
   - Test the flow end-to-end: user action in UI -> network request -> DB commit -> UI update.
   - Verify zero unhandled promise rejections or console errors.
