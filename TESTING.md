# Testing Marketing Atlas

Marketing Atlas has three layers of testing.

## Layer 1: Structural validation (fast, local + CI)

```bash
./validate.sh
```

Per skill, checks:
- Valid YAML frontmatter at the top of `SKILL.md`
- `name` matches the directory name
- `description` present and within Anthropic's 1024-char limit
- `SKILL.md` under 500 lines (load-time recommendation)
- `evals/evals.json` exists and is valid JSON with at least 3 trigger evals

Runs automatically on every push and PR via `.github/workflows/validate.yml`.

## Layer 2: Coverage stats (CI-gated)

```bash
python3 tools/coverage-stats.py                  # print stats
python3 tools/coverage-stats.py --update-readme  # update badges
python3 tools/coverage-stats.py --json           # machine-readable
```

CI fails if README badges are out of sync with the actual eval counts. To fix:

```bash
python3 tools/coverage-stats.py --update-readme
git add README.md && git commit -m "Update coverage badges"
```

## Layer 3: Behavior evals (LLM-as-judge)

```bash
pip install -r requirements-dev.txt
export ANTHROPIC_API_KEY=sk-ant-...
python3 tools/run-behavior-evals.py --all              # all skills
python3 tools/run-behavior-evals.py --skill copy-craft # one skill
```

For each behavior eval:
1. Loads the skill's `SKILL.md` into the system message.
2. Sends the eval prompt to Claude (the **actor** model).
3. Sends the actor's response to a second Claude call (the **judge**) with the list of assertions.
4. The judge returns per-assertion PASS/FAIL with brief reasoning.

Output: `eval-results.json` with per-skill, per-assertion verdicts.

Exit code 0 if all assertions pass, 1 otherwise.

### Models

By default, both actor and judge use `claude-sonnet-4-5`. Override:

```bash
python3 tools/run-behavior-evals.py --all \
    --actor-model claude-opus-4-7 \
    --judge-model claude-sonnet-4-5
```

The judge is intentionally not the same instance as the actor — separate calls avoid self-grading bias.

### Running in CI

The release pipeline (`.github/workflows/release.yml`) does **not** run behavior evals automatically (they cost API credits). The validate workflow runs them only when:
- `ANTHROPIC_API_KEY` is configured as a repo secret
- Triggered by manual `workflow_dispatch` or push to `main`

PRs from forks do not get API access, so behavior evals are gated to maintainer-triggered runs.

## Layer 4: Trigger evals (manual)

Trigger evals — does the skill description actually cause Claude to activate the skill on a given prompt — require the Anthropic skill-creator runner (it depends on Claude Code CLI).

```bash
# Once: install Claude Code
# Then per skill:
python -m scripts.run_eval --skill skills/copy-craft \
    --queries skills/copy-craft/evals/evals.json
```

If a query in `should_trigger` does not activate the skill, the description is too narrow or missing keywords. If a query in `should_not_trigger` does activate, the description is too broad.

## Adding a new skill — testing checklist

When adding a skill:

1. Place `SKILL.md` under `skills/<your-skill-name>/SKILL.md`
2. Add `skills/<your-skill-name>/evals/evals.json` with:
   - At least 5 `should_trigger` queries (mix EN and PL where relevant)
   - At least 2 `should_not_trigger` queries
   - At least 1 `behavior_evals` case with 3+ assertions
3. Run `./validate.sh` locally
4. Run `python3 tools/coverage-stats.py --update-readme` to refresh badges
5. (Optional) Run behavior evals locally for the new skill: `python3 tools/run-behavior-evals.py --skill <your-skill-name>`
6. Push, open PR, CI gates the rest
