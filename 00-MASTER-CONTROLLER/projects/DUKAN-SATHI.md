# PROJECT WORKFLOW PROFILE: DUKAN SATHI
## Offline-First Retail & Kirana SaaS Platform

> **Project Identity**: DUKAN SATHI (दुकान साथी)  
> **Domain**: Indian Retail POS, Voice Billing, Udhaar Khata, and GST Compliance  
> **Primary Command**: `/sr24-saas dukan-sathi` or `/sr24-fullstack dukan-sathi`

---

## 1. Specialist Squad Roster

| Role | Assigned Skill(s) | Primary Mission |
|---|---|---|
| **SaaS Architect** | `agency-engineering-software-architect` + `saas-architect` | Multi-tenant architecture, offline-first sync pipelines |
| **Full-Stack Lead** | `agency-engineering-senior-developer` + `agency-engineering-frontend-developer` | React 18, Vite, Three.js 3D acoustic canvas, FastAPI backend |
| **Fintech Specialist** | `razorpay-upi-specialist` | UPI dynamic QR codes, Intent checkout, webhook HMAC verification |
| **GST Tax Specialist** | `indian-gst-billing-engineer` | CGST/SGST/IGST calculation, HSN summaries, 80mm thermal slips |
| **Offline-First Lead** | `offline-first-kirana-architect` | IndexedDB local storage, background sync queue, conflict resolution |
| **Database Architect** | `agency-engineering-database-optimizer` | SQLite local DB, PostgreSQL cloud, composite indexes on orders |
| **Design & Anti-Slop** | `antislop-ui` + `ui-ux-pro-max` + `agency-design-ui-finish-gate-reviewer` | Premium dark glass theme, 3D spatial acoustic sphere, zero AI slop |
| **Speech AI Lead** | `agency-engineering-ai-engineer` | Hindi/Hinglish natural speech parsing, local fallback matching |
| **Security Engineer** | `agency-security-appsec-engineer` | Tenant data isolation, API secret protection, input sanitization |

---

## 2. System Architecture & Dual-Engine Pipeline

```
[Retail Merchant Counter (Mobile / Tablet / PC)]
      │
      ├── Input: Hindi Natural Speech ("2 kg chawal, 1L refined tel")
      │     └── Voice Engine: Gnani Prisma v2.5 / Local Offline Regex Fallback
      │
      ├── Local Fast Store (IndexedDB / SQLite WASM)
      │     └── Sub-10ms Bill Generation & Thermal Print
      │
      └── Background Sync Queue (Auto-Syncs on 4G Reconnect)
            └── Cloud Backend: FastAPI + PostgreSQL + Razorpay Webhooks
```

---

## 3. Mandatory Quality Gates

1. **Sub-3-Second Voice Billing**: Order spoken in natural Hindi -> Itemized bill with total generated in under 3 seconds.
2. **100% Offline Survival**: Full POS billing, stock lookup, and Udhaar ledger accessible with zero internet.
3. **Exact GST Math**: B2B and B2C tax breakdowns accurate to 2 decimal places with annual serial number sequencing.
4. **Dark Glass Aesthetics**: Consistent dark frosted glass styling (`bg-zinc-900/60 backdrop-blur-xl`) across all 11 tabs.

