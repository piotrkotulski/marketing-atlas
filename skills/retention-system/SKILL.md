---
name: retention-system
description: "Use for churn prevention, loyalty programs, win-back campaigns, referrals, customer lifecycle. Trigger on: 'reduce churn', 'retention', 'win-back', 'loyalty program', 'lifetime value', 'LTV', 'customer lifecycle', 'cancellation flow', 'save offer', 'referral program', 'churn', 'redukcja churn', 'retencja', 'lifetime value', 'win-back', 'program lojalnościowy', 'program poleceń', 'cancellation flow'. Use for any conversation about keeping customers and increasing their value over time."
---

# Retention system

A new customer costs more than a kept one.

## When to use

Read `.agents/marketing-context.md`. Model (subscription, transactional, marketplace) shapes the strategy.

## Core frameworks

### The retention hierarchy
1. **Product fit** — if the product doesn't deliver, no campaign saves it
2. **Activation** — first value within minutes or first session
3. **Habit** — repeated use within first 30 days
4. **Expansion** — cross-sell, upgrade, deeper use
5. **Advocacy** — referral, review, case study

Don't optimize step 5 if step 2 is broken.

### Churn diagnosis
- **Voluntary churn** — they chose to leave. Why? (Survey at cancellation.)
- **Involuntary churn** — payment failed. (Dunning, smart retry, alternative payment.)
- **Silent churn** — they stopped using but didn't cancel. (Usage-based health score, re-engagement.)

Different problems, different fixes.

### Cancellation flow (compliant)
- Honest reason capture (3–5 options + open field)
- Save offer only when relevant and not coercive
- Cancel must be one click; no "are you sure" loops; no "please call us"
- Confirmation email is the goodbye, not the trap

### Loyalty programs that work
- Points-for-purchase (simple, marketplace and retail)
- Tier-based (status motivates more than discount above some price level)
- Community-based (access, events, exclusive content)
- Referral built into loyalty (point bonus for invites)

Programs that don't work: overly complex tiers, points that expire mysteriously, "exclusive" offers that everyone gets.

### Referral program design
- Reward both sides (referrer + referred); double-sided beats one-sided by 2–3×
- Reward proportional to value (free trial extension, credit, cash)
- Make tracking trivial (unique link)
- Promote at the moment of highest delight (post-purchase, post-success)

### Lifecycle email — see email-flows for sequences
- Onboarding maps to activation events, not days
- Post-purchase educates, doesn't just confirm
- Re-engagement runs at 60–90 days inactive

### LTV math, simply
- LTV = average order value × purchase frequency × customer lifespan (or margin × tenure for subs)
- Compare to CAC; LTV/CAC ≥3 is a healthy benchmark for most models
- Track CAC payback period — when does the customer pay back their acquisition cost?

## Compliance and limits

- **Dyr. 2023/2673 (from 2026-06-19 in EU)**: cancellation must be as easy as signup; no dark patterns. Kara do 10% obrotu.
- Loyalty terms must be clear and not change retroactively.
- Referral rewards may be taxable income for the referrer (PIT in Poland, similar elsewhere).
- GDPR/RODO: lawful basis for retention messaging; honor unsubscribes.

## Polish market notes (active when Polish layer is enabled in calibrator)

- Polish stack defaults documented in `.agents/marketing-context-pl.md` (BLIK, InPost, Allegro, SALESmanago, GetResponse, Senuto, Brand24, Piwik PRO).
- Active regulations: Omnibus (lowest-price-from-30-days on every promotion), AI Act art. 50 (AI labeling from 2026-08-02), EAA/WCAG 2.2 (accessibility, since 2025-06-28), dyr. 2023/2673 (visible withdrawal button, no dark patterns, from 2026-06-19), GDPR/RODO baseline. Regulator: UOKiK and UODO.
- Polish consumers are research-driven and price-sensitive; social proof in Polish and trust signals (Sprawdzona Opinia, Ceneo reviews, BLIK + InPost as defaults) lift conversion materially.

## Questions to ask the user

1. Business model — subscription, transactional, marketplace, service?
2. Current churn rate or repurchase rate?
3. Do you have a cancellation flow today? What does it do?
4. Existing loyalty or referral mechanic — or building from scratch?

## Related skills

email-flows, conversion-optimization, analytics-stack.
