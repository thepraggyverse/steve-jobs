#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd -P)"

python3 - "$ROOT" <<'PY'
import csv
import json
import re
import sys
from pathlib import Path

root = Path(sys.argv[1])
errors = []

skill_dirs = sorted(path.name for path in (root / "skills").iterdir() if path.is_dir() and path.name.startswith("sj-"))
skill_set = set(skill_dirs)

skills_sh = json.loads((root / "skills.sh.json").read_text())
grouped = []
for group in skills_sh.get("groupings", []):
    grouped.extend(group.get("skills", []))

with (root / "assets" / "sj-skills.csv").open(newline="") as handle:
    csv_names = [row["name"] for row in csv.DictReader(handle)]

claude = json.loads((root / ".claude-plugin" / "plugin.json").read_text())
claude_names = [Path(path).name for path in claude.get("skills", [])]

catalog_text = (root / "references" / "sj-skill-catalog.md").read_text()
catalog_names = re.findall(r"`\$(sj-[^`]+)`", catalog_text)

reference_names = []
for line in (root / "docs" / "SKILL_REFERENCE.md").read_text().splitlines():
    match = re.match(r"^\|\s*`\$(sj-[^`]+)`\s*\|", line)
    if match:
        reference_names.append(match.group(1))

surfaces = {
    "skills.sh.json": grouped,
    "assets/sj-skills.csv": csv_names,
    ".claude-plugin/plugin.json": claude_names,
    "references/sj-skill-catalog.md": catalog_names,
    "docs/SKILL_REFERENCE.md": reference_names,
}

for label, names in surfaces.items():
    if len(names) != len(skill_dirs):
        errors.append(f"{label} count mismatch: expected {len(skill_dirs)}, found {len(names)}")
    if set(names) != skill_set:
        missing = sorted(skill_set - set(names))
        extra = sorted(set(names) - skill_set)
        if missing:
            errors.append(f"{label} missing: {', '.join(missing)}")
        if extra:
            errors.append(f"{label} extra: {', '.join(extra)}")
    if len(names) != len(set(names)):
        duplicates = sorted(name for name in set(names) if names.count(name) > 1)
        errors.append(f"{label} duplicates: {', '.join(duplicates)}")

if grouped != csv_names:
    errors.append("assets/sj-skills.csv order must match skills.sh.json grouping order")
if grouped != catalog_names:
    errors.append("references/sj-skill-catalog.md order must match skills.sh.json grouping order")
if grouped != reference_names:
    errors.append("docs/SKILL_REFERENCE.md order must match skills.sh.json grouping order")

if errors:
    for error in errors:
        print(f"ERROR: {error}")
    raise SystemExit(1)

print("Inventory check passed")
print(f"skills: {len(skill_dirs)}")
print(f"groups: {len(skills_sh.get('groupings', []))}")
PY
