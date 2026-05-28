# Changelog

All notable changes to Marketing Atlas are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned
- LLM-as-judge: parallel execution to reduce eval runtime
- Trigger eval runner integration with Anthropic skill-creator
- Optional skill: SMS/messaging flows
- Optional skill: ASO (app store optimization)
- More languages in trigger queries (DE, ES)

## [1.0.0] — 2026-05-28

### Added
- Initial release: 17 skills organized in 5 categories.
- **Foundation:** `calibrator` — meta-skill that builds `marketing-context.md` for all other skills.
- **Discover (3):** `audience-discovery`, `market-intel`, `brand-positioning`.
- **Create (4):** `copy-craft`, `content-engine`, `visual-design`, `video-script`.
- **Distribute (5):** `organic-search`, `paid-media`, `social-presence`, `email-flows`, `partnerships-pr`.
- **Optimize (4):** `conversion-optimization`, `analytics-stack`, `retention-system`, `growth-experiments`.
- Bilingual (EN + PL) trigger descriptions on every skill.
- Optional Polish-market regulatory and tooling layer (RODO, UOKiK Omnibus, AI Act art. 50, EAA/WCAG 2.2, dyr. 2023/2673; BLIK, InPost, Allegro, Senuto, Brand24, SALESmanago, GetResponse, Piwik PRO).
- `validate.sh` for structural validation.
- `tools/run-behavior-evals.py` — LLM-as-judge runner using the Anthropic API.
- `tools/coverage-stats.py` — coverage metrics generator that updates README badges.
- `.github/workflows/validate.yml` — CI gating on every push and PR.
- `.github/workflows/release.yml` — auto-build `.skill` bundles on tag push.
- 176 trigger queries, 35 negative cases, 19 behavior cases, 107 assertions across all skills.
- MIT license.

[Unreleased]: https://github.com/piotrkotulski/marketing-atlas/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/piotrkotulski/marketing-atlas/releases/tag/v1.0.0
