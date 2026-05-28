#!/usr/bin/env bash
# Marketing Atlas — local validation
# Checks structure, frontmatter, and evals JSON for every skill.
# Run: ./validate.sh
set -u

SKILLS_DIR="skills"
ISSUES=0
WARNINGS=0
PASSED=0

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

echo "🔍 Validating Marketing Atlas skills"
echo "===================================="
echo ""

for skill_dir in "$SKILLS_DIR"/*/; do
    skill_name=$(basename "$skill_dir")
    skill_file="$skill_dir/SKILL.md"
    skill_errors=()
    skill_warnings=()

    if [[ ! -f "$skill_file" ]]; then
        skill_errors+=("missing SKILL.md")
    else
        # Frontmatter present
        if ! head -1 "$skill_file" | grep -q "^---$"; then
            skill_errors+=("frontmatter not at top of file")
        fi
        # name field
        if ! grep -q "^name: " "$skill_file"; then
            skill_errors+=("missing 'name' in frontmatter")
        else
            fm_name=$(grep "^name: " "$skill_file" | head -1 | sed 's/^name: *//;s/[\" ]//g')
            if [[ "$fm_name" != "$skill_name" ]]; then
                skill_errors+=("'name' in frontmatter ($fm_name) does not match directory ($skill_name)")
            fi
        fi
        # description field present
        if ! grep -q "^description: " "$skill_file"; then
            skill_errors+=("missing 'description' in frontmatter")
        else
            desc_len=$(grep "^description: " "$skill_file" | head -1 | wc -c)
            if (( desc_len < 50 )); then
                skill_warnings+=("description very short ($desc_len chars) — may hurt triggering")
            elif (( desc_len > 1024 )); then
                skill_errors+=("description over 1024 chars (Anthropic spec limit)")
            fi
        fi
        # Length check
        line_count=$(wc -l < "$skill_file")
        if (( line_count > 500 )); then
            skill_warnings+=("SKILL.md is $line_count lines (>500 may be slow to load)")
        fi
    fi

    # Evals
    evals_file="$skill_dir/evals/evals.json"
    if [[ -f "$evals_file" ]]; then
        if ! python3 -c "import json,sys; json.load(open('$evals_file'))" 2>/dev/null; then
            skill_errors+=("evals.json is not valid JSON")
        else
            trigger_count=$(python3 -c "import json; d=json.load(open('$evals_file')); print(len(d.get('trigger_evals',{}).get('should_trigger',[])))" 2>/dev/null || echo 0)
            if (( trigger_count < 3 )); then
                skill_warnings+=("only $trigger_count trigger evals (recommend 5+)")
            fi
        fi
    else
        skill_warnings+=("no evals/evals.json")
    fi

    # Verdict
    if (( ${#skill_errors[@]} > 0 )); then
        echo -e "${RED}✗ $skill_name${NC}"
        for err in "${skill_errors[@]}"; do
            echo "    error: $err"
            ((ISSUES++))
        done
        for w in "${skill_warnings[@]}"; do
            echo "    warning: $w"
            ((WARNINGS++))
        done
    elif (( ${#skill_warnings[@]} > 0 )); then
        echo -e "${YELLOW}⚠ $skill_name${NC}"
        for w in "${skill_warnings[@]}"; do
            echo "    $w"
            ((WARNINGS++))
        done
        ((PASSED++))
    else
        echo -e "${GREEN}✓ $skill_name${NC}"
        ((PASSED++))
    fi
done

echo ""
echo "===================================="
echo -e "${GREEN}Passed: $PASSED${NC}    ${YELLOW}Warnings: $WARNINGS${NC}    ${RED}Errors: $ISSUES${NC}"

if (( ISSUES > 0 )); then
    exit 1
fi
exit 0
