#!/usr/bin/env python3
"""
Marketing Atlas — behavior eval runner with LLM-as-judge.

For each behavior eval in skills/<name>/evals/evals.json:
1. Loads the skill's SKILL.md
2. Asks Claude to act on the eval prompt, with the skill loaded into the system message
3. Asks a second Claude (the judge) to score the output against each assertion
4. Writes a JSON report

Usage:
    export ANTHROPIC_API_KEY=sk-ant-...
    python tools/run-behavior-evals.py --all
    python tools/run-behavior-evals.py --skill copy-craft
    python tools/run-behavior-evals.py --skill copy-craft --model claude-opus-4-5

Exit code 0 if all assertions pass, 1 if any fail.
"""
from __future__ import annotations
import argparse
import json
import os
import sys
import time
from pathlib import Path
from typing import Any

try:
    from anthropic import Anthropic
except ImportError:
    sys.stderr.write("Missing 'anthropic' SDK. Install: pip install anthropic\n")
    sys.exit(2)

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = REPO_ROOT / "skills"

DEFAULT_ACTOR_MODEL = "claude-sonnet-4-5"
DEFAULT_JUDGE_MODEL = "claude-sonnet-4-5"

# The judge sees a list of assertions and the skill's response. It returns
# a strict JSON object with per-assertion PASS/FAIL and reasoning.
JUDGE_SYSTEM = """You are a strict evaluator of marketing AI skill outputs.

You will receive:
1. The prompt that was given to a skill.
2. The skill's response.
3. A list of assertions the response must satisfy.

For each assertion, decide PASS or FAIL based on whether the response actually demonstrates that property. Be strict but fair:
- PASS only if the response clearly demonstrates the property.
- FAIL if the property is missing, partial, or ambiguous.
- Do not invent properties that were not asserted.
- Do not penalize for things that were not asserted.

Output ONLY a JSON object with this exact shape:
{
  "results": [
    {"assertion": "<text>", "verdict": "PASS" | "FAIL", "reasoning": "<one short sentence>"}
  ],
  "summary": {"passed": <int>, "failed": <int>}
}

No prose outside the JSON. No markdown code fences."""


def load_skill_md(skill_name: str) -> str:
    """Return the SKILL.md body (frontmatter + content) for embedding in system prompt."""
    path = SKILLS_DIR / skill_name / "SKILL.md"
    if not path.exists():
        raise FileNotFoundError(f"SKILL.md not found for skill '{skill_name}'")
    return path.read_text(encoding="utf-8")


def load_evals(skill_name: str) -> dict[str, Any]:
    path = SKILLS_DIR / skill_name / "evals" / "evals.json"
    if not path.exists():
        raise FileNotFoundError(f"evals.json not found for skill '{skill_name}'")
    return json.loads(path.read_text(encoding="utf-8"))


def run_skill_actor(client: Anthropic, skill_md: str, prompt: str, model: str) -> str:
    """Run the skill against a behavior eval prompt. Returns the model's text response."""
    system = (
        "You are Claude. You have the following Marketing Atlas skill loaded. "
        "Apply it when the user's request matches its scope.\n\n"
        "=== SKILL START ===\n"
        f"{skill_md}\n"
        "=== SKILL END ==="
    )
    response = client.messages.create(
        model=model,
        max_tokens=2048,
        system=system,
        messages=[{"role": "user", "content": prompt}],
    )
    parts = [b.text for b in response.content if getattr(b, "type", None) == "text"]
    return "\n".join(parts).strip()


def run_judge(
    client: Anthropic,
    prompt: str,
    skill_response: str,
    assertions: list[str],
    model: str,
) -> dict[str, Any]:
    """Run the judge on a single behavior eval. Returns parsed JSON with per-assertion verdicts."""
    user_msg = (
        f"PROMPT GIVEN TO SKILL:\n{prompt}\n\n"
        f"SKILL RESPONSE:\n{skill_response}\n\n"
        f"ASSERTIONS TO EVALUATE:\n"
        + "\n".join(f"- {a}" for a in assertions)
    )
    response = client.messages.create(
        model=model,
        max_tokens=2048,
        system=JUDGE_SYSTEM,
        messages=[{"role": "user", "content": user_msg}],
    )
    raw = "".join(b.text for b in response.content if getattr(b, "type", None) == "text").strip()
    # Defensive parse: strip any code fences if a model adds them.
    if raw.startswith("```"):
        raw = raw.strip("`")
        if raw.lstrip().startswith("json"):
            raw = raw.split("\n", 1)[1] if "\n" in raw else raw
    try:
        return json.loads(raw)
    except json.JSONDecodeError as e:
        return {
            "results": [
                {"assertion": a, "verdict": "FAIL", "reasoning": f"judge JSON parse error: {e}"}
                for a in assertions
            ],
            "summary": {"passed": 0, "failed": len(assertions)},
        }


def run_eval_for_skill(
    client: Anthropic, skill_name: str, actor_model: str, judge_model: str, verbose: bool
) -> dict[str, Any]:
    skill_md = load_skill_md(skill_name)
    evals_data = load_evals(skill_name)
    behavior_evals = evals_data.get("behavior_evals", {}).get("evals", [])

    skill_results = {
        "skill_name": skill_name,
        "actor_model": actor_model,
        "judge_model": judge_model,
        "behavior_evals": [],
        "summary": {"total_assertions": 0, "passed": 0, "failed": 0},
    }

    for eval_case in behavior_evals:
        eval_id = eval_case.get("id", "?")
        prompt = eval_case["prompt"]
        assertions = eval_case["assertions"]

        if verbose:
            print(f"  [{skill_name}#{eval_id}] running actor...", flush=True)
        try:
            skill_response = run_skill_actor(client, skill_md, prompt, actor_model)
        except Exception as e:
            skill_results["behavior_evals"].append({
                "id": eval_id, "prompt": prompt, "error": f"actor failed: {e}",
                "results": [{"assertion": a, "verdict": "FAIL", "reasoning": "actor failed"} for a in assertions],
            })
            skill_results["summary"]["total_assertions"] += len(assertions)
            skill_results["summary"]["failed"] += len(assertions)
            continue

        if verbose:
            print(f"  [{skill_name}#{eval_id}] running judge...", flush=True)
        try:
            judge_result = run_judge(client, prompt, skill_response, assertions, judge_model)
        except Exception as e:
            judge_result = {
                "results": [{"assertion": a, "verdict": "FAIL", "reasoning": f"judge failed: {e}"} for a in assertions],
                "summary": {"passed": 0, "failed": len(assertions)},
            }

        passed = judge_result.get("summary", {}).get("passed", 0)
        failed = judge_result.get("summary", {}).get("failed", 0)

        skill_results["behavior_evals"].append({
            "id": eval_id,
            "prompt": prompt,
            "skill_response_preview": skill_response[:500] + ("..." if len(skill_response) > 500 else ""),
            "judgments": judge_result.get("results", []),
            "passed": passed,
            "failed": failed,
        })
        skill_results["summary"]["total_assertions"] += len(assertions)
        skill_results["summary"]["passed"] += passed
        skill_results["summary"]["failed"] += failed

        if verbose:
            print(f"  [{skill_name}#{eval_id}] {passed}/{len(assertions)} passed", flush=True)

        time.sleep(0.5)  # Be polite to the API

    return skill_results


def main() -> int:
    parser = argparse.ArgumentParser(description="Run Marketing Atlas behavior evals")
    parser.add_argument("--skill", help="Skill name (e.g. copy-craft). Omit to use --all.")
    parser.add_argument("--all", action="store_true", help="Run all skills with behavior_evals.")
    parser.add_argument("--actor-model", default=DEFAULT_ACTOR_MODEL)
    parser.add_argument("--judge-model", default=DEFAULT_JUDGE_MODEL)
    parser.add_argument("--out", default="eval-results.json", help="Output JSON path.")
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()

    if not args.skill and not args.all:
        parser.error("Pass --skill <name> or --all")

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        sys.stderr.write("ANTHROPIC_API_KEY env var not set\n")
        return 2

    client = Anthropic(api_key=api_key)

    skills_to_run = []
    if args.all:
        skills_to_run = [p.name for p in SKILLS_DIR.iterdir() if p.is_dir()]
    else:
        skills_to_run = [args.skill]

    overall = {
        "actor_model": args.actor_model,
        "judge_model": args.judge_model,
        "skills": [],
        "summary": {"total_assertions": 0, "passed": 0, "failed": 0},
    }

    for skill_name in skills_to_run:
        if not args.quiet:
            print(f"-> {skill_name}", flush=True)
        try:
            result = run_eval_for_skill(client, skill_name, args.actor_model, args.judge_model, not args.quiet)
        except FileNotFoundError as e:
            if not args.quiet:
                print(f"   skip: {e}", flush=True)
            continue
        overall["skills"].append(result)
        for k in ("total_assertions", "passed", "failed"):
            overall["summary"][k] += result["summary"][k]

    Path(args.out).write_text(json.dumps(overall, indent=2, ensure_ascii=False))

    s = overall["summary"]
    pass_rate = (s["passed"] / s["total_assertions"] * 100) if s["total_assertions"] else 0
    print(f"\n=== Marketing Atlas behavior evals ===")
    print(f"Skills run: {len(overall['skills'])}")
    print(f"Assertions: {s['passed']}/{s['total_assertions']} passed ({pass_rate:.1f}%)")
    print(f"Results: {args.out}")
    return 0 if s["failed"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
