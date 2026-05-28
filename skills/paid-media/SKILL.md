---
name: paid-media
description: "Use for paid acquisition strategy across platforms: Google Ads, Meta Ads, LinkedIn Ads, TikTok Ads, marketplace ads (Allegro, Amazon), programmatic. Trigger on: 'paid ads', 'Google Ads', 'Meta Ads', 'LinkedIn Ads', 'TikTok Ads', 'Allegro Ads', 'ad strategy', 'PPC', 'ROAS', 'scaling ads', 'campaign structure', 'reklama płatna', 'kampania reklamowa', 'Google Ads', 'Meta Ads', 'Allegro Ads', 'skalowanie reklam', 'struktura kont reklamowych'. Use for any paid acquisition question that is not specifically about creative (creative belongs to visual-design and copy-craft)."
metadata:
  version: 1.0.0
  category: distribute
  pack: marketing-atlas
---

# Paid media

Spend where the math works.

## When to use

Read `.agents/marketing-context.md`. Match goal (awareness vs leads vs sales) to platforms.

## Core frameworks

### Channel selection by goal
- **Awareness, broad** — Meta, TikTok, YouTube, programmatic display
- **Demand capture (intent-led)** — Google Search, Bing, marketplace search (Allegro Ads, Amazon Ads)
- **B2B leads** — LinkedIn, Google Search, niche industry placements
- **Retargeting** — Meta, Google, programmatic
- **Local** — Google (Performance Max for local), Meta with radius targeting

### Account structure that scales
- One campaign per goal
- Ad sets segmented by audience or intent, not by creative
- Creative is rotated within ad sets, tested fast
- Use platform's optimization (smart bidding, advantage+) once you have signal; not on day one

### Budget allocation framework
- 70% on proven channels and audiences
- 20% on scaling proven hypotheses (new lookalikes, new keywords)
- 10% on net-new experiments
- Re-evaluate monthly

### KPI hierarchy (in order)
1. CAC (or CPL for lead gen) vs target
2. ROAS (for e-commerce)
3. CPC, CTR, conversion rate as diagnostic, not primary
4. View-through and assisted conversions in the attribution model

### Common scaling traps
- Scaling spend faster than the algorithm can learn (rule of thumb: max +20–30% per week per ad set)
- Killing campaigns before they hit statistical significance
- Optimizing for clicks instead of conversions
- Ignoring creative fatigue (CTR drops, frequency rises — refresh)

## Compliance and limits

- Consent Mode v2 (EU) — without it, ad platforms lose ~30% signal.
- DSA: transparency on who paid for the ad, especially for marketplaces.
- Sector rules: financial services (RRSO + representative example in Poland), pharmaceuticals (prescription rules), gambling, alcohol — sector-specific.
- AI Act art. 50: AI-generated ad content labeled.
- Omnibus (PL/EU): "before" prices in ads must reflect the lowest price from the past 30 days.

## Polish market notes (active when Polish layer is enabled in calibrator)

- Polish stack defaults documented in `.agents/marketing-context-pl.md` (BLIK, InPost, Allegro, SALESmanago, GetResponse, Senuto, Brand24, Piwik PRO).
- Active regulations: Omnibus (lowest-price-from-30-days on every promotion), AI Act art. 50 (AI labeling from 2026-08-02), EAA/WCAG 2.2 (accessibility, since 2025-06-28), dyr. 2023/2673 (visible withdrawal button, no dark patterns, from 2026-06-19), GDPR/RODO baseline. Regulator: UOKiK and UODO.
- Polish consumers are research-driven and price-sensitive; social proof in Polish and trust signals (Sprawdzona Opinia, Ceneo reviews, BLIK + InPost as defaults) lift conversion materially.

## Questions to ask the user

1. Primary objective for the next 90 days (leads, sales, awareness)?
2. Monthly budget range and current platforms?
3. CAC target or ROAS target — what does "working" mean?
4. Existing assets (creative, audiences, conversion tracking) we can build on?

## Related skills

copy-craft, visual-design, video-script, analytics-stack, conversion-optimization.
