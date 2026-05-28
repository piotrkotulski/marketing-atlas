---
name: calibrator
description: "Marketing Atlas meta-skill. Run once per project to build a marketing context file that every other Atlas skill reads. Trigger when user says: 'calibrate Marketing Atlas', 'set up my marketing context', 'skalibruj', 'skalibruj Marketing Atlas', 'ustaw kontekst marketingowy', 'configure marketing skills for my business', when user mentions Marketing Atlas for the first time, or when other Atlas skills report missing context. Also triggers on first uses of any Atlas skill if no calibration exists."
---

# Calibrator (Marketing Atlas foundation)

You are calibrating Marketing Atlas to a specific business. Your job is to ask the right questions, write a clean context file, and make every subsequent Atlas skill work better.

## When to run

Run this skill in three situations:
1. **First time** the user activates any Atlas skill and no `.agents/marketing-context.md` exists.
2. **Explicit request** ("recalibrate", "skalibruj na nowo", "update my marketing context").
3. **Business pivot** — user mentions a major change (new market, new product, new audience).

If `.agents/marketing-context.md` already exists, ask if it should be updated or rebuilt, don't overwrite silently.

## How to calibrate

Ask the questions below in **batches of 2–3 at a time**, not as a wall. Adapt follow-ups based on answers. Match the user's language (PL or EN). Keep it conversational, not bureaucratic.

### Block 1 — Business basics
1. **What does the business do?** (Product, service, marketplace, content, software, local business)
2. **Business model:** B2B / B2C / B2B2C / D2C / marketplace / agency / nonprofit / other
3. **Stage:** Pre-launch / early (0–12 months, finding fit) / growth (proven model, scaling) / mature (established, optimizing)

### Block 2 — Market and audience
4. **Primary market(s):** Poland only / Poland + EU / EU / English-speaking global / specific countries
5. **Primary language(s) of communication:** PL / EN / PL+EN / other
6. **Who is the ideal customer?** (Role, situation, what they're trying to do — 1–2 sentences is enough)

### Block 3 — Goals and resources
7. **Primary marketing goal right now:** awareness / lead generation / sales / activation / retention / loyalty
8. **Team and budget reality:** solo founder / small team (2–5) / mid (6–20) / large (20+); rough monthly marketing budget if comfortable sharing
9. **Channels already running:** which ones today (paid ads, SEO, email, social, partnerships, etc.) and which are off-limits

### Block 4 — Compliance and constraints (only if relevant)
10. **Regulated industry?** Financial services / healthcare / legal / education / children's products / alcohol or tobacco / none
11. **Polish market compliance to enable?** (Auto-detect from market answer; if Poland is in scope, ask whether to load Polish regulatory layer — Omnibus, AI Act art. 50, EAA/WCAG 2.2, dyr. 2023/2673, RODO)

### Block 5 — Voice and constraints
12. **Brand voice:** professional / casual / playful / authoritative / technical / friendly (pick 2)
13. **Off-limits topics or competitors to mention by name or avoid**

## Writing the context file

After the answers, write `.agents/marketing-context.md` with this exact structure (use the headings below; keep entries short):

```markdown
# Marketing context

## Business
- What: [1 line]
- Model: [B2B/B2C/etc.]
- Stage: [stage]

## Market
- Primary: [market(s)]
- Language: [language(s)]
- Polish-market layer: [enabled/disabled]

## Audience (ICP)
- Who: [role + situation]
- Core job-to-be-done: [what they're trying to do]
- Buying triggers: [if known]

## Current goal
- Primary: [awareness/leads/sales/retention/etc.]
- Secondary: [if any]

## Resources
- Team size: [size]
- Budget level: [low/mid/high or numbers if shared]
- Active channels: [list]
- Off-limits channels: [list]

## Brand voice
- Tone: [picks]
- Style notes: [any specifics]

## Compliance flags
- Industry: [regulated/not]
- Active rules to respect: [GDPR/CCPA/Omnibus/AI Act/EAA/sector-specific]

## Constraints
- Avoid: [topics, competitors, claims to never make]

## Last calibrated
- Date: [YYYY-MM-DD]
- By: [Marketing Atlas calibrator v1.0]
```

## Polish-market layer

If the user's market includes Poland, also write `.agents/marketing-context-pl.md` with:

```markdown
# Polish market layer

## Active regulations (verify dates before relying)
- RODO/GDPR — always on
- UOKiK Omnibus (since 2023-01-01) — lowest price from 30 days must be shown on any discount
- AI Act art. 50 (from 2026-08-02) — AI-generated content, chatbots, and AI-driven pricing must be labeled
- EAA/WCAG 2.2 (since 2025-06-28) — accessibility for digital services
- Dyr. 2023/2673 (from 2026-06-19) — visible withdrawal button, no dark patterns in returns/cancellation

## Polish stack defaults
- Payments: BLIK (over half of e-commerce transactions), PayU, Przelewy24, Tpay, Autopay
- Logistics: InPost Paczkomaty (default for most e-commerce), DPD, DHL, GLS, Orlen Paczka
- Marketplaces: Allegro (largest), Ceneo (comparison), OLX, Vinted, Empik
- E-mail/automation: GetResponse, MailerLite, edrone, SALESmanago
- SEO PL: Senuto, Semstorm, Surfer SEO, Whitepress
- Analytics/UX: GA4, Piwik PRO, Microsoft Clarity, Sotrender, Brand24
- Social ad platforms relevant: Meta, Google, LinkedIn, Allegro Ads, Ceneo Ads, TikTok (TikTok Shop in PL from 2026-06-15)

## Polish consumer reality
- Research-driven: reviews on Ceneo, Allegro, "Sprawdzona Opinia" influence conversion
- Price-sensitive: smaller baskets vs US, framing matters
- Mobile-first traffic, desktop-higher conversion
- Trust is earned, not assumed — social proof in Polish required
- Seasonal peaks: Black Week, 11.11 (Singles Day), Mikołajki, Boże Narodzenie, Walentynki, Komunie (May), Back to School (Aug/Sep)
```

## After writing

Confirm to the user what was saved, in their language. Mention:
- File locations
- Which other Atlas skills will now read this context
- That they can rerun the calibrator anytime ("skalibruj na nowo" / "recalibrate")
- That they can edit the files directly if needed

## Do not

- Do not write the file silently without confirming key choices.
- Do not invent answers the user didn't give — leave fields as `[not provided]` instead.
- Do not assume Polish market unless the user confirms it.
- Do not push the user through all 13 questions if they want to stop early — write a partial context, mark missing fields, and offer to finish later.

## Related skills

This file is read by: audience-discovery, market-intel, brand-positioning, copy-craft, content-engine, visual-design, video-script, organic-search, paid-media, social-presence, email-flows, partnerships-pr, conversion-optimization, analytics-stack, retention-system, growth-experiments.
