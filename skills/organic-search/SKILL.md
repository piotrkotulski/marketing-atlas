---
name: organic-search
description: "Use for SEO audit, technical SEO, on-page optimization, AI search visibility, schema/structured data. Trigger on: 'SEO audit', 'fix our SEO', 'why no Google traffic', 'technical SEO', 'AI search', 'AI Overviews', 'schema', 'structured data', 'rich snippets', 'audyt SEO', 'pozycjonowanie', 'widoczność w Google', 'dane strukturalne', 'JSON-LD', 'SEO sklepu', 'AI SEO'. Use for any conversation about getting found organically in Google or AI search engines."
---

# Organic search

Found by humans and by AI.

## When to use

Read `.agents/marketing-context.md`. Polish-market layer? Then primary target is google.pl + Polish AI Overviews. Otherwise local Google.

## Core frameworks

### SEO audit, in order
1. **Technical** — indexability (robots, sitemap, canonical), Core Web Vitals, mobile, HTTPS
2. **On-page** — title, meta description, H1, internal links, schema
3. **Content** — does the page match the search intent (informational vs commercial vs transactional)?
4. **Off-page** — link profile health
5. **E-commerce specifics** — faceted navigation, parameter handling, duplicate product pages (common Magento/WooCommerce trap)

Fix in order: technical first (you can't rank if you can't be indexed), then on-page, then content gap, then links.

### On-page that works in 2026
- Title and H1: include primary intent, written for a human
- Match intent — if the SERP shows comparison posts, don't publish a product page
- Cover the topic, not just the keyword
- Use schema (see schema patterns below)
- E-E-A-T signals: author, dates, citations, evidence

### Schema patterns to ship
- **Product / Offer / AggregateRating** for e-commerce
- **Article / Person / Organization** for content
- **FAQPage** for FAQ blocks
- **BreadcrumbList** for navigation
- **LocalBusiness** for local
- Always validate in Google Rich Results Test
- Match what's visible on the page — discrepancies get penalized

### AI search optimization (GEO)
- Answer questions directly in 1–2 sentences, then expand
- Use Q&A and definitions
- Strong entities (consistent brand name, products, people)
- Citable statistics with sources
- Schema makes your content easier to extract
- Monitor mentions: Peec AI, Otterly, Brand Radar

### What still doesn't work
- Keyword stuffing
- Pages without internal links
- "Thin" auto-generated content without value
- Buying low-quality links

## Compliance and limits

- AI-generated content must be labeled (AI Act art. 50 from 2026-08-02 in EU).
- Accessibility helps SEO: heading structure, alt text, contrast (EAA/WCAG 2.2 in EU).
- Don't fake schema (e.g., showing reviews you don't have) — Google penalizes; can also violate consumer law.

## Polish market notes (active when Polish layer is enabled in calibrator)

- Polish stack defaults documented in `.agents/marketing-context-pl.md` (BLIK, InPost, Allegro, SALESmanago, GetResponse, Senuto, Brand24, Piwik PRO).
- Active regulations: Omnibus (lowest-price-from-30-days on every promotion), AI Act art. 50 (AI labeling from 2026-08-02), EAA/WCAG 2.2 (accessibility, since 2025-06-28), dyr. 2023/2673 (visible withdrawal button, no dark patterns, from 2026-06-19), GDPR/RODO baseline. Regulator: UOKiK and UODO.
- Polish consumers are research-driven and price-sensitive; social proof in Polish and trust signals (Sprawdzona Opinia, Ceneo reviews, BLIK + InPost as defaults) lift conversion materially.

## Questions to ask the user

1. URL and platform (Shopify, WooCommerce, Magento/Adobe Commerce, WordPress, custom)?
2. Do I have access to Search Console and analytics?
3. Main categories or topics and 2–3 competitors in search?
4. Primary market and language?

## Related skills

content-engine, conversion-optimization, analytics-stack.
