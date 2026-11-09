# WORKFLOW: /sr24-ai — AI/ML & INTELLIGENT SYSTEMS SQUAD

> **Command**: `/sr24-ai [task]`  
> **Natural Language Trigger**: `"Add AI feature"`, `"Build RAG pipeline"`, `"Integrate LLM"`, `"Create voice agent"`  
> **Mission**: Build production-grade, secure, cost-controlled, and deterministic AI systems with structured outputs, prompt evals, and offline/rule-based fallbacks.

---

## AI SPECIALIST SQUAD

| Role | Skill | Focus |
|---|---|---|
| **AI Systems Lead** | `agency-engineering-ai-engineer` | Model selection, system architecture, latency budgets, API contracts |
| **Prompt Specialist** | `agency-engineering-prompt-engineer` | Few-shot prompting, chain-of-thought, structured JSON extraction, prompt versioning |
| **RAG Architect** | `agency-engineering-rag-pipeline-engineer` | Chunking, embeddings, hybrid vector/keyword search, reranking, source citation |
| **Post-Training Engineer** | `agency-engineering-llm-post-training-engineer` | Fine-tuning, synthetic dataset curation, preference optimization (DPO/RLHF) |
| **Data Remediation** | `agency-engineering-ai-data-remediation-engineer` | Data cleaning, outlier removal, privacy masking, PII scrubbing |
| **AI Security Auditor** | `agency-security-ai-generated-code-auditor` | Prompt injection defense, secret exfiltration prevention, hallucination controls |

---

## 6-STAGE AI PRODUCTION LIFECYCLE

1. **Stage 1: Architecture & Model Selection**:
   - Determine whether task requires a frontier LLM (e.g. Gemini 1.5 Pro), lightweight edge model (Gemini Flash, Llama 3.2), or deterministic rule-based engine.
   - Establish strict latency (< 500ms for voice/autocomplete, < 2s for complex generation) and budget limits.
2. **Stage 2: Prompt Engineering & Schema Enforcement**:
   - Author system prompts with explicit operational bounds, negative constraints, and output JSON schemas (Pydantic / Zod).
   - Implement few-shot examples representing tricky edge cases.
3. **Stage 3: Vector & RAG Pipeline (if contextual)**:
   - Configure semantic chunking (256-512 tokens with 10% overlap).
   - Implement hybrid BM25 + dense embedding retrieval with reciprocal rank fusion (RRF).
4. **Stage 4: Deterministic Guardrails & Fallback Engine**:
   - **Crucial Rule**: Every AI feature must have a deterministic rule-based fallback. If API is down or latency spikes, user workflows must never break.
5. **Stage 5: Security & Prompt Injection Hardening**:
   - Quarantine untrusted user inputs.
   - Validate and sanitize all LLM outputs before storing in database or rendering in DOM (prevent stored XSS via LLM outputs).
6. **Stage 6: Cost Tracking & Evaluation**:
   - Implement token usage metrics and logging per user/tenant.
   - Run automated evaluation suites against gold-standard test prompts.
