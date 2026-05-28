---
name: email-flows
description: "Use to design email sequences and campaigns: welcome series, cart abandonment, onboarding, lifecycle, win-back, newsletters, transactional. Trigger on: 'email sequence', 'welcome email', 'cart abandonment', 'newsletter strategy', 'lifecycle email', 'win-back', 'email automation', 'email marketing', 'sekwencja powitalna', 'porzucony koszyk', 'newsletter', 'email lifecycle', 'win-back', 'email automation', 'kampania mailowa'. Use for both content and automation logic of email; for SMS see this skill too (it handles short-form messaging principles)."
metadata:
  version: 1.0.0
  category: distribute
  pack: marketing-atlas
---

# Email flows

Compliant, well-timed, written for one person.

## When to use

Read `.agents/marketing-context.md`. Choose tool based on market: PL — GetResponse, MailerLite, edrone, SALESmanago; global — Klaviyo (e-commerce), HubSpot, Customer.io, ConvertKit, Beehiiv (newsletters).

## Core frameworks

### Core sequences for most businesses
**Welcome (1–3 emails)** — within first 24h after opt-in
- Email 1 (immediate): confirm value, deliver the magnet, set expectation
- Email 2 (day 2): story or insight, no ask
- Email 3 (day 5): soft CTA or invitation

**Cart abandonment (e-commerce, 3 emails)**
- 30 min: reminder + cart link
- 4–24 h: address top objection (shipping, returns, social proof)
- 48–72 h: offer or last-chance — only if margin allows

**Onboarding (SaaS or service, 5–10 emails over 14 days)**
- Map to activation events ("aha moment"), not days
- Each email teaches one thing and asks for one action

**Lifecycle / post-purchase**
- Day 0: order confirmation
- Day 2–3: shipping update + how to use
- Day 7: ask for review
- Day 30: cross-sell / restock
- Day 60: re-engagement

**Win-back**
- Trigger: no engagement for 60–90 days
- 2–3 emails: "We miss you", value reminder, last-call offer with a clear "unsubscribe is fine"

### Newsletter that survives
- Pick a cadence and hold it (weekly works for most)
- One main idea per issue
- Personality > information (information is everywhere)
- Single CTA, even if it's "reply and tell me X"
- Track replies and clicks, not just opens (open rates are unreliable since iOS 15)

### Design for the inbox
- Subject line: <50 characters, specific, no clickbait
- Preview text: complement, don't repeat subject
- Plain-text or simple HTML beats complex layouts in deliverability
- One link per email if you can (more dilutes the action)
- Mobile-first: short paragraphs

### Deliverability discipline
- Authenticate: SPF, DKIM, DMARC
- Clean list: remove non-openers after 90–180 days
- Don't send to purchased lists (kills domain reputation)

## Compliance and limits

- **GDPR/RODO + ePrivacy + ust. o świadczeniu usług drogą elektroniczną (PL)**: explicit opt-in; double opt-in recommended; separate consent for marketing.
- One-click unsubscribe must work; honor within 10 days.
- B2B cold email to personal addresses is risky in PL/EU — prefer role addresses + legitimate interest.
- CAN-SPAM (US): physical address, opt-out, no deceptive subjects.
- AI Act art. 50: AI-generated email content — internal log; for transparency-required interactions, disclose.
- Don't send to children without parental consent.

## Polish market notes (active when Polish layer is enabled in calibrator)

- Polish stack defaults documented in `.agents/marketing-context-pl.md` (BLIK, InPost, Allegro, SALESmanago, GetResponse, Senuto, Brand24, Piwik PRO).
- Active regulations: Omnibus (lowest-price-from-30-days on every promotion), AI Act art. 50 (AI labeling from 2026-08-02), EAA/WCAG 2.2 (accessibility, since 2025-06-28), dyr. 2023/2673 (visible withdrawal button, no dark patterns, from 2026-06-19), GDPR/RODO baseline. Regulator: UOKiK and UODO.
- Polish consumers are research-driven and price-sensitive; social proof in Polish and trust signals (Sprawdzona Opinia, Ceneo reviews, BLIK + InPost as defaults) lift conversion materially.

## Questions to ask the user

1. Which sequence and what's the goal?
2. Email tool already in use?
3. List size and consent status (double opt-in?)
4. Brand voice and any examples of recent emails to match?

## Related skills

copy-craft, retention-system, conversion-optimization, content-engine.
