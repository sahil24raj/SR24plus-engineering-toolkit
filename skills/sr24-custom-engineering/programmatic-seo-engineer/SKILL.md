---
name: programmatic-seo-engineer
description: Architect of programmatic SEO (pSEO) — dynamic template generation, JSON-LD structured data, XML sitemaps, internal linking graphs, and Core Web Vitals optimization.
---

# Programmatic SEO (pSEO) & Organic Growth Engineer

## Role & Mission
The **Programmatic SEO & Organic Growth Engineer** designs and implements scalable programmatic SEO engines that generate thousands of high-quality, high-converting, indexable landing pages targeting long-tail commercial queries with structured data and instant load times.

---

## 1. Activation Conditions
Invoke this skill whenever:
- Designing programmatic landing pages (e.g., city-based retail landing pages, HSN code calculators, tool directories).
- Implementing dynamic sitemap index generation (`sitemap.xml`) handling 10,000+ URLs.
- Authoring JSON-LD schema markup (`SoftwareApplication`, `LocalBusiness`, `FAQPage`).
- Optimizing internal linking topologies and PageRank distribution for SR24Plus or SaaS products.

---

## 2. Programmatic SEO Architecture

```
[Curated Dataset (JSON / PostgreSQL)] ──── E.g. 500 Indian Cities / 2,000 Kirana Categories
              │
              ▼
[Dynamic Static Regeneration (ISR / Next.js)] ─── generateStaticParams()
              │
              ▼
[High-Value Template Component] ────────── Rich Content, FAQs, City Stats, Real CTAs
              │
              ▼
[Automated Sitemap & Inter-linking Graph] ── Sitemaps split into 5,000 URL chunks
```

---

## 3. Implementation: Next.js Dynamic pSEO Route
```typescript
import { Metadata } from 'next';

interface PageProps {
  params: { city: string; category: string };
}

// 1. Dynamic Meta Tags & Open Graph
export async function generateMetadata({ params }: PageProps): Promise<Metadata> {
  const cityName = capitalize(params.city);
  const categoryName = capitalize(params.category);

  return {
    title: `Best ${categoryName} Billing Software in ${cityName} (2026) | Dukaan Saathi`,
    description: `Fastest Hindi voice POS and GST billing software for ${categoryName} retailers in ${cityName}. 100% offline-ready, thermal printing & udhaar khata.`,
    alternates: {
      canonical: `https://dukaansaathi.in/pos/${params.city}/${params.category}`,
    },
    openGraph: {
      title: `${categoryName} POS & Billing Software in ${cityName}`,
      description: `Upgrade your retail counter with voice AI billing.`,
      images: [{ url: `/og/pos-${params.city}.png` }],
    },
  };
}

// 2. Structured JSON-LD Schema (SoftwareApplication + BreadcrumbList)
export function generateJsonLd(cityName: string, categoryName: string) {
  return {
    '@context': 'https://schema.org',
    '@type': 'SoftwareApplication',
    name: `Dukaan Saathi ${categoryName} POS (${cityName})`,
    operatingSystem: 'Web, Android, Windows',
    applicationCategory: 'BusinessApplication',
    offers: {
      '@type': 'Offer',
      price: '0',
      priceCurrency: 'INR',
    },
    aggregateRating: {
      '@type': 'AggregateRating',
      ratingValue: '4.9',
      reviewCount: '1240',
    },
  };
}
```

---

## 4. Quality Checklist
- [ ] No "thin content" penalties: Every programmatic page must include unique local data points, customized FAQs, and interactive calculators.
- [ ] Canonical URLs explicitly defined on 100% of generated pages.
- [ ] Automated sitemap pinging on new content generation (`/sitemap.xml`).
- [ ] Google PageSpeed score > 90 on mobile viewports for all template routes.
