---
name: tavily-search-intelligence
description: >-
  Specialist in Tavily Search API integration for real-time web discovery, grounded AI citations, competitor pricing intelligence, and market validation.
---

# Tavily Search Intelligence & Agent Web Research

## 1. When to Activate
Activate this skill whenever a project or prompt requires specialist in tavily search api integration for real-time web discovery, grounded ai citations, competitor pricing intelligence, and market validation.. It is assigned to official engineering phases in the **SR24Plus Engineering Toolkit**.

## 2. When Not to Activate
- Do not activate when the task does not involve tavily-search-intelligence.
- Do not activate as a substitute for simple static mockups where deeper engineering is unnecessary.

## 3. Core Capabilities
- Agent-optimized real-time search returning direct answers, excerpts, and raw content
- Domain filtering, time-range restriction (day/week/month), and topical clustering
- Competitor pricing and feature matrix extraction with verifiable source URLs
- Q&A synthesis reducing hallucination by feeding factual web context to LLMs
- Multi-query fan-out search orchestration for comprehensive product discovery

## 4. Engineering Workflow
1. **Discovery & Architecture**: Inspect technical constraints, performance requirements, and data contracts.
2. **Setup & Configuration**: Install official package dependencies and configure environment variables.
3. **Implementation**: Author production-grade code using clean architecture, strict TypeScript types, and error handling.
4. **Validation & Testing**: Run unit and integration tests confirming zero regressions.
5. **Production Deployment**: Verify build bundle impact, tree-shaking, and observability telemetry.

## 5. Implementation Instructions & Code Patterns

```typescript
import { tavily } from '@tavily/core';

const tvly = tavily({ apiKey: process.env.TAVILY_API_KEY });

export async function researchCompetitorMarket(query: string) {
  const response = await tvly.search(query, {
    searchDepth: 'advanced',
    includeAnswer: true,
    includeRawContent: false,
    maxResults: 8,
    includeDomains: ['techcrunch.com', 'producthunt.com', 'github.com', 'ycombinator.com']
  });

  return {
    summary: response.answer,
    sources: response.results.map((r) => ({
      title: r.title,
      url: r.url,
      snippet: r.content,
      score: r.score
    }))
  };
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
- **Repository**: [https://github.com/tavily-ai/tavily-python](https://github.com/tavily-ai/tavily-python)
- **Category**: SR24-WEB-DEV Canonical Engineering Skill

## 10. License & Attribution
- **License**: MIT
- **Maintained By**: SR24Plus Autonomous Engineering Architecture
