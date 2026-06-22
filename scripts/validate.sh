#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd -P)"
export ROOT

python3 <<'PY'
import json
import os
import re
from pathlib import Path

root = Path(os.environ["ROOT"])

skills_dir = root / "skills"
refs_dir = root / "references"
plugin_json = root / ".codex-plugin" / "plugin.json"

skills = sorted(p for p in skills_dir.iterdir() if p.is_dir() and p.name.startswith("sj-"))
refs = sorted(refs_dir.glob("sj-*.md"))

errors = []
if len(skills) != 80:
    errors.append(f"expected 80 skills, found {len(skills)}")
if len(refs) != 8:
    errors.append(f"expected 8 references, found {len(refs)}")

name_re = re.compile(r"^name:\s*([a-z0-9-]+)\s*$", re.MULTILINE)
for skill in skills:
    skill_md = skill / "SKILL.md"
    openai_yaml = skill / "agents" / "openai.yaml"
    if not skill_md.exists():
        errors.append(f"missing SKILL.md: {skill}")
        continue
    text = skill_md.read_text()
    match = name_re.search(text)
    if not match:
        errors.append(f"missing frontmatter name: {skill_md}")
    elif match.group(1) != skill.name:
        errors.append(f"frontmatter name mismatch in {skill_md}: {match.group(1)}")
    if not openai_yaml.exists():
        errors.append(f"missing agents/openai.yaml: {skill}")
    else:
        yaml_text = openai_yaml.read_text()
        if f"${skill.name}" not in yaml_text:
            errors.append(f"default prompt does not mention ${skill.name}: {openai_yaml}")

try:
    manifest = json.loads(plugin_json.read_text())
except Exception as exc:
    errors.append(f"plugin manifest is not valid JSON: {exc}")
else:
    if manifest.get("name") != "steve-jobs":
        errors.append("plugin manifest name must be steve-jobs")
    if manifest.get("skills") != "./skills/":
        errors.append("plugin manifest skills path must be ./skills/")

if errors:
    for error in errors:
        print(f"ERROR: {error}")
    raise SystemExit(1)

print("Basic validation passed")
print(f"skills: {len(skills)}")
print(f"references: {len(refs)}")
PY

QUICK_VALIDATE="$HOME/.codex/skills/.system/skill-creator/scripts/quick_validate.py"
PLUGIN_VALIDATE="$HOME/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py"

if [ -f "$QUICK_VALIDATE" ]; then
  for skill in "$ROOT"/skills/sj-*; do
    python3 "$QUICK_VALIDATE" "$skill" >/dev/null
  done
  echo "Codex skill validation passed"
else
  echo "Codex skill validator not found; skipped"
fi

if [ -f "$PLUGIN_VALIDATE" ]; then
  python3 "$PLUGIN_VALIDATE" "$ROOT"
else
  echo "Codex plugin validator not found; skipped"
fi
