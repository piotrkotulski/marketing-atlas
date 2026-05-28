---
name: conversion-optimization
description: "Use to diagnose and improve conversion across landing pages, product pages, checkouts, signup flows, forms. Trigger on: 'CRO', 'improve conversion', 'page not converting', 'checkout optimization', 'cart abandonment', 'signup flow', 'reduce friction', 'A/B test', 'conversion audit', 'optymalizacja konwersji', 'CRO', 'niska konwersja', 'porzucony koszyk', 'popraw checkout', 'uprość formularz', 'test A/B'. Use whenever conversion math needs to improve at a specific point in the funnel."
metadata:
  version: 1.0.0
  category: optimize
  pack: marketing-atlas
---

# Conversion optimization

Find the friction. Remove it. Prove the impact.

## When to use

Read `.agents/marketing-context.md`. Identify which step you're optimizing — strategies differ.

## Core frameworks

### Diagnose before you optimize
- **Quantitative**: analytics funnel — where are people dropping?
- **Qualitative**: session recordings, heatmaps, surveys
- **Comparative**: how do similar pages convert in your industry?

Top-of-funnel optimization fixes the wrong problem if checkout is the leak.

### Conversion hierarchy (apply in order)
1. **Right traffic** — wrong audience never converts
2. **Right message match** — ad promised X, page must deliver X
3. **Clear hero** — one promise, one CTA above the fold
4. **Proof** — numbers, names, screenshots, reviews
5. **Friction reduction** — fewer fields, fewer clicks, fewer required choices
6. **Trust signals** — security, returns, guarantee, contact

### Checkout optimization
- Guest checkout
- One column, mobile-first
- Show shipping cost and delivery time early — never surprise at the end
- Preferred local payment methods visible (BLIK in Poland is non-negotiable)
- Preferred delivery options visible (InPost Paczkomaty in Poland for most e-commerce)
- Progress indicator
- Errors inline, not on submit
- No required fields that aren't needed (phone number is often optional)

### Form optimization
- Cut every field you don't immediately need
- Single column
- Match input type (date picker, number, etc.)
- Autofill enabled
- Inline validation

### A/B testing rules
- Calculate sample size before starting
- One variable changed at a time (or clean MVT)
- Minimum one full business cycle (usually 1–2 weeks)
- Don't peek; statistical significance ≥95% before deciding
- Don't run tests during major sales periods (Black Week, holidays)
- Document the hypothesis, result, and learning — even on losers

### Common diagnoses
- **High traffic, low conversion** = message mismatch or trust gap
- **High form starts, low completes** = friction in the form
- **High cart adds, low purchases** = checkout friction or unexpected costs

## Compliance and limits

- Accessibility (EAA/WCAG 2.2 in EU): forms, checkout, navigation must be usable by everyone (kara do 10% obrotu in PL).
- Dark patterns prohibited: dyr. 2023/2673 (from 2026-06-19 in EU) — cancellation as easy as signup, visible withdrawal button. Kara do 10% obrotu.
- Consent before tracking (GDPR/RODO + Consent Mode v2).
- No false scarcity, urgency, or social proof — UOKiK enforces.
- Pricing in promotions: lowest price from 30 days must be shown (Omnibus).

## Polish market notes (active when Polish layer is enabled in calibrator)

- Polish stack defaults documented in `.agents/marketing-context-pl.md` (BLIK, InPost, Allegro, SALESmanago, GetResponse, Senuto, Brand24, Piwik PRO).
- Active regulations: Omnibus (lowest-price-from-30-days on every promotion), AI Act art. 50 (AI labeling from 2026-08-02), EAA/WCAG 2.2 (accessibility, since 2025-06-28), dyr. 2023/2673 (visible withdrawal button, no dark patterns, from 2026-06-19), GDPR/RODO baseline. Regulator: UOKiK and UODO.
- Polish consumers are research-driven and price-sensitive; social proof in Polish and trust signals (Sprawdzona Opinia, Ceneo reviews, BLIK + InPost as defaults) lift conversion materially.

## Questions to ask the user

1. Which step in the funnel and what's the current conversion rate?
2. Do you have analytics + heatmap/recording data?
3. What testing tool, and what's the daily traffic on this page?
4. Any constraints (no checkout changes, no design system changes, etc.)?

## Related skills

copy-craft, analytics-stack, growth-experiments.
