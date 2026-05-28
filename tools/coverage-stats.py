#!/usr/bin/env python3
"""
Marketing Atlas — coverage statistics generator.

Walks all skills, counts evals, and either prints stats or updates
the badges section of README.md (between <!-- BADGES START --> and
<!-- BADGES END --> markers).

Usage:
    python tools/coverage-stats.py              # print stats
    python tools/coverage-stats.py --update-readme   # update README badges
"""
from __future__ import annotations
import argparse
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = REPO_ROOT / "skills"
README = REPO_ROOT / "README.md"

BADGE_START = "<!-- BADGES START -->"
BADGE_END = "<!-- BADGES END -->"


def gather_stats() -> dict:
    skills = sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir())
    total_skills = len(skills)
    skills_with_evals = 0
    skills_with_behavior_evals = 0
    total_triggers = 0
    total_negatives = 0
    total_behavior_cases = 0
    total_assertions = 0
    by_category: dict[str, int] = {}

    for skill_dir in skills:
        # Category from frontmatter
        skill_md = skill_dir / "SKILL.md"
        if skill_md.exists():
            content = skill_md.read_text(encoding="utf-8")
            m = re.search(r"^\s*category:\s*(\S+)", content, re.MULTILINE)
            if m:
                cat = m.group(1).strip()
                by_category[cat] = by_category.get(cat, 0) + 1

        # Evals
        evals_path = skill_dir / "evals" / "evals.json"
        if not evals_path.exists():
            continue
        skills_with_evals += 1
        try:
            data = json.loads(evals_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue

        triggers = data.get("trigger_evals", {})
        total_triggers += len(triggers.get("should_trigger", []))
        total_negatives += len(triggers.get("should_not_trigger", []))

        behavior_evals = data.get("behavior_evals", {}).get("evals", [])
        if behavior_evals:
            skills_with_behavior_evals += 1
        total_behavior_cases += len(behavior_evals)
        for bev in behavior_evals:
            total_assertions += len(bev.get("assertions", []))

    return {
        "total_skills": total_skills,
        "skills_with_evals": skills_with_evals,
        "skills_with_behavior_evals": skills_with_behavior_evals,
        "total_triggers": total_triggers,
        "total_negatives": total_negatives,
        "total_behavior_cases": total_behavior_cases,
        "total_assertions": total_assertions,
        "by_category": by_category,
    }


def make_badges(stats: dict) -> str:
    """Generate shields.io static badge URLs in markdown form."""

    def badge(label: str, value: str, color: str) -> str:
        # URL-encode the spaces and dashes
        label_u = label.replace(" ", "%20").replace("-", "--")
        value_u = value.replace(" ", "%20").replace("-", "--")
        return f"![{label}](https://img.shields.io/badge/{label_u}-{value_u}-{color})"

    eval_coverage = stats["skills_with_evals"]
    behavior_coverage = stats["skills_with_behavior_evals"]
    total = stats["total_skills"]

    coverage_color = "brightgreen" if eval_coverage == total else "yellow"
    behavior_color = "brightgreen" if behavior_coverage == total else "yellow"

    return "\n".join([
        BADGE_START,
        badge("skills", str(total), "blue"),
        badge("trigger evals", f"{stats['total_triggers']}", "blue"),
        badge("negative cases", f"{stats['total_negatives']}", "blue"),
        badge("behavior cases", f"{stats['total_behavior_cases']}", "blue"),
        badge("assertions", f"{stats['total_assertions']}", "blue"),
        badge("eval coverage", f"{eval_coverage}/{total}", coverage_color),
        badge("behavior coverage", f"{behavior_coverage}/{total}", behavior_color),
        badge("license", "MIT", "green"),
        BADGE_END,
    ])


def update_readme(stats: dict) -> bool:
    if not README.exists():
        print("README.md not found", file=sys.stderr)
        return False
    content = README.read_text(encoding="utf-8")
    new_block = make_badges(stats)

    if BADGE_START in content and BADGE_END in content:
        # Replace existing block
        pattern = re.compile(
            re.escape(BADGE_START) + r".*?" + re.escape(BADGE_END),
            re.DOTALL,
        )
        new_content = pattern.sub(new_block, content)
    else:
        # Insert after the first heading
        lines = content.split("\n")
        for i, line in enumerate(lines):
            if line.startswith("# "):
                lines.insert(i + 1, "")
                lines.insert(i + 2, new_block)
                break
        new_content = "\n".join(lines)

    README.write_text(new_content, encoding="utf-8")
    return True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--update-readme", action="store_true", help="Update README badges in place")
    parser.add_argument("--json", action="store_true", help="Output stats as JSON")
    args = parser.parse_args()

    stats = gather_stats()

    if args.json:
        print(json.dumps(stats, indent=2))
        return

    print("=== Marketing Atlas coverage ===")
    print(f"Skills total: {stats['total_skills']}")
    print(f"  by category: {', '.join(f'{k}={v}' for k, v in sorted(stats['by_category'].items()))}")
    print(f"Skills with evals.json: {stats['skills_with_evals']}/{stats['total_skills']}")
    print(f"Skills with behavior evals: {stats['skills_with_behavior_evals']}/{stats['total_skills']}")
    print(f"Trigger queries: {stats['total_triggers']}")
    print(f"Negative cases: {stats['total_negatives']}")
    print(f"Behavior cases: {stats['total_behavior_cases']}")
    print(f"Assertions: {stats['total_assertions']}")

    if args.update_readme:
        if update_readme(stats):
            print("\nREADME.md badges updated.")
        else:
            print("\nREADME.md update failed.", file=sys.stderr)


if __name__ == "__main__":
    main()
