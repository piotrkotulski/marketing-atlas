---
name: audience-discovery
description: "Use to understand who the customer really is — personas, jobs-to-be-done, voice-of-customer extraction from reviews, interviews, surveys, support tickets. Trigger on: 'who is my customer', 'build personas', 'jobs to be done', 'analyze reviews', 'voice of customer', 'customer interviews', 'kim jest mój klient', 'persony', 'analiza recenzji', 'badanie klientów', 'voice of customer', 'wywiady z klientami', 'co mówią klienci'. Use whenever decisions need to be grounded in real customer language and behavior, not assumptions."
metadata:
  version: 1.0.0
  category: discover
  pack: marketing-atlas
---

# Audience discovery

Understand who you are really talking to.

## When to use

Two modes:
1. **Extraction mode** — user has raw material (reviews, transcripts, surveys, support tickets). Pull patterns, language, and segments from it.
2. **Discovery mode** — user has no material yet. Help them find where to look and what to ask.

Always read `.agents/marketing-context.md` first if it exists.

## Core frameworks

### Jobs-to-be-done (JTBD) lens
For each customer, find:
- **Situation:** what was happening when they started looking
- **Motivation:** what they were trying to accomplish (functional, emotional, social)
- **Outcome:** how they defined success
- **Alternatives:** what they tried or considered before you

### Voice-of-customer extraction
From raw text (reviews, transcripts), tag:
- **Pains** — exact words for frustration ("waited 3 days for support")
- **Gains** — exact words for value ("saved me 4 hours a week")
- **Triggers** — what made them search/buy
- **Objections** — what almost stopped them
- **Surprises** — unexpected use cases or values

Keep direct quotes. Direct quotes become headlines later (see `copy-craft`).

### Segment by behavior, not demographics
Better segments: by job-to-be-done, by stage of awareness, by trigger event. Demographics are a poor proxy in most markets — use them as last resort.

## Where to look

- **Review platforms** relevant to the product (G2, Capterra, Trustpilot for SaaS; Amazon/marketplace reviews for physical goods; Yelp/Google for local)
- **Support tickets and chat logs**
- **Sales calls** (recorded with consent)
- **Communities** (Reddit, Discord, Facebook Groups, industry forums)
- **Search queries** in Search Console, Google autocomplete
- **Surveys** for what you can't find — keep them short, open-ended where it matters

## Compliance and limits

- Consent for recording interviews; anonymize transcripts.
- GDPR/RODO: data minimization, lawful basis, right to deletion if subjects are in EU.
- Avoid scraping platforms whose Terms of Service forbid it.

## Polish market notes (active when Polish layer is enabled in calibrator)

- Polish stack defaults documented in `.agents/marketing-context-pl.md` (BLIK, InPost, Allegro, SALESmanago, GetResponse, Senuto, Brand24, Piwik PRO).
- Active regulations: Omnibus (lowest-price-from-30-days on every promotion), AI Act art. 50 (AI labeling from 2026-08-02), EAA/WCAG 2.2 (accessibility, since 2025-06-28), dyr. 2023/2673 (visible withdrawal button, no dark patterns, from 2026-06-19), GDPR/RODO baseline. Regulator: UOKiK and UODO.
- Polish consumers are research-driven and price-sensitive; social proof in Polish and trust signals (Sprawdzona Opinia, Ceneo reviews, BLIK + InPost as defaults) lift conversion materially.

## Questions to ask the user

1. Do you have raw material to analyze, or are we starting from zero?
2. What decision will these insights drive (positioning, messaging, product, pricing)?
3. Are there specific segments you suspect exist but can't confirm?

## Related skills

brand-positioning, market-intel, copy-craft, content-engine.
