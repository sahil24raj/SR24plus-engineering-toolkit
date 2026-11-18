---
name: firecrawl-scraper
description: >-
  Expert in Firecrawl web scraping, JS-rendered crawling, and clean Markdown extraction for AI agent research, competitor analysis, and product discovery.
---

# Firecrawl Web Scraping & Deep Crawl Intelligence

## 1. When to Activate
Activate this skill whenever a project or prompt requires expert in firecrawl web scraping, js-rendered crawling, and clean markdown extraction for ai agent research, competitor analysis, and product discovery.. It is assigned to official engineering phases in the **SR24Plus Engineering Toolkit**.

## 2. When Not to Activate
- Do not activate when the task does not involve firecrawl-scraper.
- Do not activate as a substitute for simple static mockups where deeper engineering is unnecessary.

## 3. Core Capabilities
- Deep recursive crawling of competitor SaaS domains with rate-limit backoff
- Full JavaScript hydration handling for SPAs and React/Vue client-rendered pages
- Clean markdown output generation with metadata, headers, tables, and image references preserved
- Structured JSON extraction using LLM schema extraction over scraped page content
- Anti-bot and proxy rotation management for reliable product data extraction

## 4. Engineering Workflow
1. **Discovery & Architecture**: Inspect technical constraints, performance requirements, and data contracts.
2. **Setup & Configuration**: Install official package dependencies and configure environment variables.
3. **Implementation**: Author production-grade code using clean architecture, strict TypeScript types, and error handling.
4. **Validation & Testing**: Run unit and integration tests confirming zero regressions.
5. **Production Deployment**: Verify build bundle impact, tree-shaking, and observability telemetry.

## 5. Implementation Instructions & Code Patterns

```typescript
import FirecrawlApp from '@mendable/firecrawl-js';

const app = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

// 1. Scrape single competitor landing page into clean Markdown
export async function scrapeCompetitorPage(url: string) {
  const scrapeResult = await app.scrapeUrl(url, {
    formats: ['markdown'],
    onlyMainContent: true,
    waitFor: 2000,
  });

  if (!scrapeResult.success) {
    throw new Error(`Scrape failed: ${scrapeResult.error}`);
  }

  return {
    title: scrapeResult.metadata?.title,
    description: scrapeResult.metadata?.description,
    markdown: scrapeResult.markdown,
  };
}

// 2. Crawl competitor documentation or blog recursively
export async function crawlDocumentation(baseUrl: string, maxPages = 15) {
  const crawlResponse = await app.crawlUrl(baseUrl, {
    limit: maxPages,
    scrapeOptions: {
      formats: ['markdown'],
      onlyMainContent: true,
    },
  });

  return crawlResponse;
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
- **Repository**: [https://github.com/firecrawl/firecrawl](https://github.com/firecrawl/firecrawl)
- **Category**: SR24-WEB-DEV Canonical Engineering Skill

## 10. License & Attribution
- **License**: Apache-2.0
- **Maintained By**: SR24Plus Autonomous Engineering Architecture
