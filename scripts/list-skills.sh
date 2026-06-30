#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd -P)"
MODE="${1:-table}"

case "$MODE" in
  table|names|profiles|-h|--help)
    ;;
  *)
    echo "Unknown mode: $MODE" >&2
    echo "Usage: scripts/list-skills.sh [table|names|profiles]" >&2
    exit 2
    ;;
esac

if [ "$MODE" = "-h" ] || [ "$MODE" = "--help" ]; then
  cat <<'EOF'
Usage: scripts/list-skills.sh [table|names|profiles]

table     Show skills grouped by profile with counts.
names     Print one skill name per line.
profiles  Show supported install profiles and patterns.
EOF
  exit 0
fi

python3 - "$ROOT/skills.sh.json" "$MODE" <<'PY'
import json
import sys
from pathlib import Path

manifest = json.loads(Path(sys.argv[1]).read_text())
mode = sys.argv[2]

profiles = {
    "all": "sj-*",
    "core": "sj-core-*",
    "product": "sj-product-*",
    "ive": "sj-ive-*",
    "story": "sj-story-*",
    "people": "sj-people-*",
    "strategy": "sj-strategy-*",
    "learning": "sj-learning-*",
    "anti": "sj-anti-*",
}

if mode == "profiles":
    for name, pattern in profiles.items():
        print(f"{name}\t{pattern}")
    raise SystemExit(0)

total = 0
for group in manifest["groupings"]:
    skills = group["skills"]
    total += len(skills)
    if mode == "table":
        print(f"{group['label']} ({len(skills)})")
        for skill in skills:
            print(f"  ${skill}")
        print()
    else:
        for skill in skills:
            print(skill)

if mode == "table":
    print(f"Total: {total}")
PY
