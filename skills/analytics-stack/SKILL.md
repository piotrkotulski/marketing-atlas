---
name: analytics-stack
description: "Use to design or audit measurement: GA4, events, conversions, attribution, consent, dashboards, e-commerce tracking. Trigger on: 'GA4 setup', 'tracking', 'measurement plan', 'attribution', 'analytics audit', 'consent mode', 'dashboard', 'cookie consent', 'data layer', 'GA4', 'śledzenie konwersji', 'analityka', 'pomiar', 'atrybucja', 'cookie consent', 'dashboardy'. Use whenever measurement is being set up, audited, or revised."
metadata:
  version: 1.0.0
  category: optimize
  pack: marketing-atlas
---

# Analytics stack

Measure what matters, respect consent.

## When to use

Read `.agents/marketing-context.md`. Polish-market layer enabled? Consider privacy-first stack (Piwik PRO) as alternative to GA4.

## Core frameworks

### Measurement plan (build this first)
For every business goal, define:
- **Goal** (e.g., "increase sign-ups")
- **Metric** (e.g., "sign-up conversion rate")
- **Event** (e.g., `sign_up` with parameters)
- **Owner** (who watches it)
- **Threshold** (when to act)

If you can't fill all five rows, you don't have a measurement plan, you have wishes.

### E-commerce tracking essentials
- `view_item`
- `add_to_cart`
- `begin_checkout`
- `add_payment_info` (with payment method as parameter — BLIK, card, BNPL)
- `add_shipping_info` (with shipping method — InPost, courier, pickup)
- `purchase` (revenue, items, transaction ID, tax, shipping)

Use enhanced ecommerce / GA4 ecommerce schema consistently.

### Attribution choices
- **Last click** — easy, lies about reality
- **Data-driven** (GA4 default) — better, still imperfect
- **Position-based or time-decay** — fine for sanity-checking
- **Marketing mix modeling (MMM)** — for budgets above ~$50k/mo, when iOS/cookie limits matter

No model is right; compare and triangulate.

### Privacy-first stack option
- **Piwik PRO** — first-party data, EU hosting, GDPR-by-design
- **Plausible / Fathom / Simple Analytics** — lightweight, no cookies
- **Server-side tagging** — improves accuracy after Consent Mode v2 reductions

### Consent Mode v2 (EU)
- Without it, expect 20–40% data loss in ad platforms after consent rejection
- Required for ad attribution to work in EU after March 2024
- Configure with your CMP (Cookiebot, OneTrust, Iubenda, CookieYes, CookieScript)

### Dashboards that get used
- One page per audience: executive (revenue, CAC, payback), marketing ops (channel, funnel), product (activation, retention)
- Refresh weekly; review monthly
- 5–7 metrics per dashboard, not 50

## Compliance and limits

- **GDPR/RODO** — consent before tracking, Consent Mode v2 for ad platforms, right to deletion, lawful basis documented. Polish regulator: UODO.
- Cookie consent: equal-weight buttons for "Accept" and "Reject" (Polish UOKiK has begun enforcing).
- AI Act art. 50: AI-driven personalization (recommendations, dynamic pricing) must be disclosed to users.
- Server-side and first-party tagging respect consent the same way client-side does.

## Polish market notes (active when Polish layer is enabled in calibrator)

- Polish stack defaults documented in `.agents/marketing-context-pl.md` (BLIK, InPost, Allegro, SALESmanago, GetResponse, Senuto, Brand24, Piwik PRO).
- Active regulations: Omnibus (lowest-price-from-30-days on every promotion), AI Act art. 50 (AI labeling from 2026-08-02), EAA/WCAG 2.2 (accessibility, since 2025-06-28), dyr. 2023/2673 (visible withdrawal button, no dark patterns, from 2026-06-19), GDPR/RODO baseline. Regulator: UOKiK and UODO.
- Polish consumers are research-driven and price-sensitive; social proof in Polish and trust signals (Sprawdzona Opinia, Ceneo reviews, BLIK + InPost as defaults) lift conversion materially.

## Questions to ask the user

1. What are the top 3 business outcomes to measure?
2. Current analytics setup (GA4? GTM? Piwik PRO? Other?)
3. Consent management in place?
4. Marketing channels and ad platforms connected?

## Related skills

conversion-optimization, paid-media, growth-experiments.
