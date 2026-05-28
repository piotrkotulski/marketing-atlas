# Contributing to Marketing Atlas

Thanks for considering a contribution. Marketing Atlas is community-maintained, and good contributions make every user's life better.

## Ground rules

- Skills must be useful in real marketing work, not theoretical
- Quality > coverage — better to have 17 great skills than 50 mediocre ones
- Every new skill needs evals (see TESTING.md)
- Polish-market and global-market work both welcome; mark which applies

## Workflow

1. **Open an issue first** for non-trivial changes — saves time on both sides
2. Fork the repo
3. Create or edit a skill in `skills/<name>/SKILL.md`
4. Add or update `skills/<name>/evals/evals.json`
5. Run `./validate.sh` locally — must pass with zero errors
6. Open a PR with:
   - Rationale (what problem does this solve)
   - Example prompts and outputs
   - Any breaking changes to existing skills called out

## What a good skill looks like

- **Frontmatter description (under 1024 chars)** that says when to use, what to do, what to avoid, with explicit trigger phrases in both EN and PL
- **SKILL.md under 500 lines** — load time matters
- **Frameworks > tactics** — explain how to think, not just what to do
- **Compliance section** when relevant (GDPR, regulatory)
- **Questions to ask the user** when input is needed
- **Related skills** cross-reference

## What we won't merge

- Skills that duplicate existing scope without clear differentiation
- Skills that promote dark patterns, fake scarcity, or non-compliant tactics
- Skills with no evals
- Skills that fail `./validate.sh`

## Code of conduct

Be kind. Disagree honestly. Don't waste people's time.
