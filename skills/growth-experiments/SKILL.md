---
name: growth-experiments
description: "Use to plan, prioritize, and run a marketing experiment program: hypothesis design, ICE/RICE scoring, experiment templates, launch plans. Trigger on: 'experiment program', 'growth experiments', 'how to prioritize tests', 'ICE scoring', 'RICE', 'growth hacking', 'launch plan', 'go-to-market', 'eksperymenty marketingowe', 'priorytetyzacja testów', 'plan launchu', 'go-to-market', 'growth experimentation'. Use for testing programs broader than a single A/B test (those belong to conversion-optimization)."
metadata:
  version: 1.0.0
  category: optimize
  pack: marketing-atlas
---

# Growth experiments

Test fast, kill faster, document always.

## When to use

Read `.agents/marketing-context.md`. Match experiment cadence to team size and traffic.

## Core frameworks

### Hypothesis template
**Because** [observation or data]
**We believe that** [change]
**Will result in** [outcome]
**We will know we are right when** [signal + threshold]
**This will be a learning even if it fails because** [what we learn either way]

If "we'll know" can't be filled with a number and a timeframe, it's not testable yet.

### Prioritization
**ICE** (fast)
- Impact (1–10)
- Confidence (1–10)
- Ease (1–10)
- Score = average

**RICE** (more rigorous)
- Reach × Impact × Confidence ÷ Effort

Pick one and stick with it. Mixing methods makes prioritization a debate, not a tool.

### Experiment design rules
- One variable, or clean MVT
- Statistical power before starting (use a calculator)
- Pre-register the metric and the threshold for success
- Document hypothesis, result, learning — even losers
- Maintain a public-to-the-team experiment log

### Launch planning (for product launches, campaigns, big initiatives)
**T-minus 30 days**: positioning locked, assets in production, partner outreach starts
**T-minus 14 days**: assets shipped to channels, paid setup, email sequences loaded
**T-minus 7 days**: dry run, retail/partner check-in, PR pitches landed
**T-minus 1 day**: final go/no-go, on-call setup
**Launch day**: ship, monitor, respond
**T+7 days**: post-mortem, share results

### Common experiment failures
- Testing button colors instead of meaningful changes
- Running on traffic too low to reach significance
- Stopping early because "we saw a trend"
- Forgetting to document
- Running too many tests at once and contaminating data

## Compliance and limits

- A/B testing tools require consent (GDPR/RODO + Consent Mode v2).
- Don't test illegal or coercive variations (dark patterns under dyr. 2023/2673 in EU).
- Disclose AI personalization to test subjects if relevant (AI Act art. 50).

## Polish market notes (active when Polish layer is enabled in calibrator)

- Polish stack defaults documented in `.agents/marketing-context-pl.md` (BLIK, InPost, Allegro, SALESmanago, GetResponse, Senuto, Brand24, Piwik PRO).
- Active regulations: Omnibus (lowest-price-from-30-days on every promotion), AI Act art. 50 (AI labeling from 2026-08-02), EAA/WCAG 2.2 (accessibility, since 2025-06-28), dyr. 2023/2673 (visible withdrawal button, no dark patterns, from 2026-06-19), GDPR/RODO baseline. Regulator: UOKiK and UODO.
- Polish consumers are research-driven and price-sensitive; social proof in Polish and trust signals (Sprawdzona Opinia, Ceneo reviews, BLIK + InPost as defaults) lift conversion materially.

## Questions to ask the user

1. Team size and current experiment cadence (per month)?
2. What's the priority area (acquisition, activation, retention, monetization)?
3. Traffic levels on the key pages — can you reach significance in a reasonable window?
4. What does "won" or "lost" look like for the top experiments queued?

## Related skills

conversion-optimization, analytics-stack, paid-media.
