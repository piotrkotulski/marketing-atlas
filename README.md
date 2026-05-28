# Marketing Atlas

<!-- BADGES START -->
![skills](https://img.shields.io/badge/skills-17-blue)
![trigger evals](https://img.shields.io/badge/trigger%20evals-176-blue)
![negative cases](https://img.shields.io/badge/negative%20cases-35-blue)
![behavior cases](https://img.shields.io/badge/behavior%20cases-19-blue)
![assertions](https://img.shields.io/badge/assertions-107-blue)
![eval coverage](https://img.shields.io/badge/eval%20coverage-17/17-brightgreen)
![behavior coverage](https://img.shields.io/badge/behavior%20coverage-17/17-brightgreen)
![license](https://img.shields.io/badge/license-MIT-green)
<!-- BADGES END -->

**An open-source Claude Skills pack for marketing work — from positioning to retention.**

Marketing Atlas is a curated set of 17 AI skills that turn Claude into a marketing collaborator that adapts to *your* business — not a generic playbook. Each skill activates on natural language ("write me a landing page", "audyt SEO sklepu", "what should I email churned users") and brings frameworks, checklists, and compliance-aware guidance.

## What makes this different

Most marketing skill packs are flat lists of tactics. Marketing Atlas is built around three ideas:

1. **Calibration before execution.** A meta-skill (`calibrator`) asks 6–8 questions about your business, market, and stage, then writes `.agents/marketing-context.md`. Every other skill reads this file first, so you stop re-explaining your context every conversation.

2. **Lifecycle grouping, not tactic dumping.** Skills are organized by *what they do for the business*: Discover, Create, Distribute, Optimize. Easier to find, less overlap, fewer "which one do I use" moments.

3. **Multi-market by design.** Examples and references work for global English-speaking markets, with optional Polish-market layers (regulations, tools, payment/logistics specifics) you can enable via the calibrator.

## The 17 skills

### Foundation
- **calibrator** — Run once per project. Builds `marketing-context.md` used by every other skill.

### Discover (understand the market)
- **audience-discovery** — Personas, jobs-to-be-done, language extraction from reviews/interviews
- **market-intel** — Competitive analysis, positioning maps, pricing benchmarks
- **brand-positioning** — Value proposition, differentiators, messaging hierarchy

### Create (produce assets)
- **copy-craft** — Headlines, landing pages, hero copy, CTAs
- **content-engine** — Content strategy, topic clusters, editorial calendar
- **visual-design** — Image creative briefs, brand consistency, ad creative
- **video-script** — Short-form video, YouTube, live shopping scripts

### Distribute (reach the audience)
- **organic-search** — SEO audit, technical SEO, AI search visibility, schema
- **paid-media** — Paid acquisition strategy across platforms (Google, Meta, LinkedIn, marketplaces)
- **social-presence** — Platform-specific content, personal brand, community
- **email-flows** — Welcome, cart abandonment, lifecycle, win-back sequences
- **partnerships-pr** — Co-marketing, affiliates, PR, influencer collaborations

### Optimize (measure and improve)
- **conversion-optimization** — CRO methodology, A/B testing, funnel diagnosis
- **analytics-stack** — Measurement plan, attribution, consent, dashboards
- **retention-system** — Churn prevention, loyalty, referrals, win-back
- **growth-experiments** — Hypothesis design, prioritization, experiment programs

## How to use

1. **Install all skills** via Claude.ai Settings → Capabilities → Skills → Upload (one `.skill` per file, or all at once from `marketing-atlas-all.zip`).
2. **Run the calibrator first**: "Skalibruj Marketing Atlas pod mój biznes" / "Calibrate Marketing Atlas for my business". Answer 6–8 questions. Output is saved automatically.
3. **Use other skills naturally**: "Napisz mi sekwencję powitalną" / "Draft me a welcome email sequence" — the relevant skill triggers and reads your context.

## Polish market support

Marketing Atlas includes optional Polish-market layers covering:
- Regulations (RODO, UOKiK Omnibus, AI Act, EAA/WCAG 2.2, dyr. 2023/2673)
- Polish tools (BLIK, InPost, Allegro Ads, SALESmanago, GetResponse, Brand24, Senuto, Piwik PRO)
- Polish case studies and consumer behavior patterns

Enable via calibrator by setting market to "Poland" or "Poland + EU".

## License

MIT — see LICENSE file. Use freely, fork freely, contribute back if you can.

## Contributing

Skills are written in standard Anthropic Skills format (YAML frontmatter + Markdown body). To contribute a new skill or improve an existing one:
1. Fork the repo
2. Create or edit a skill in `skills/{name}/SKILL.md`
3. Test it in Claude.ai
4. Submit a PR with rationale

## Versioning

Marketing Atlas uses semantic versioning. Current: **1.0.0**.

---

*Marketing Atlas is community-built and is not affiliated with Anthropic.*

## Testing

Marketing Atlas ships with two layers of testing:

- **Structural validation** (`./validate.sh`) — runs in CI on every push and PR
- **Trigger and behavior evals** — `skills/<name>/evals/evals.json` for each skill

See [TESTING.md](TESTING.md) for details and [CONTRIBUTING.md](CONTRIBUTING.md) for how to add a new skill with proper evals.

## Repo status

- ✅ 17 skills, all valid
- ✅ 176 trigger queries + 35 negative cases
- ✅ 19 behavior eval cases
- ✅ CI gating on PRs (.github/workflows/validate.yml)
- 🚧 LLM-as-judge automation for behavior evals (planned for v1.1)
