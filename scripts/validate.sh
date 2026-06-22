#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd -P)"
export ROOT

python3 <<'PYVALIDATE'
import json
import os
import re
from pathlib import Path

root = Path(os.environ['ROOT'])
skills_dir = root / 'skills'
refs_dir = root / 'references'

required_files = [
    'README.md',
    'AGENTS.md',
    'CLAUDE.md',
    'GEMINI.md',
    'CONTEXT.md',
    'CHANGELOG.md',
    'PRIVACY.md',
    'SECURITY.md',
    'CONTRIBUTING.md',
    'NOTICE.md',
    'LICENSE',
    'skills.sh.json',
    '.codex-plugin/plugin.json',
    '.claude-plugin/plugin.json',
    '.agents/plugins/marketplace.json',
    'docs/INSTALL.md',
    'docs/SYMLINKS.md',
    'docs/HARNESSES.md',
    'docs/UPDATE.md',
    'docs/AUDIT.md',
    'docs/SKILL_REFERENCE.md',
    'docs/EXAMPLES.md',
    'docs/COMPOUNDING.md',
    'docs/PLUGIN_ARCHITECTURE.md',
    'docs/DEVELOPMENT.md',
]

errors = []
for rel in required_files:
    if not (root / rel).exists():
        errors.append(f'missing required file: {rel}')

skills = sorted(p for p in skills_dir.iterdir() if p.is_dir() and p.name.startswith('sj-'))
refs = sorted(refs_dir.glob('sj-*.md'))

if len(skills) != 80:
    errors.append(f'expected 80 skills, found {len(skills)}')
if len(refs) != 8:
    errors.append(f'expected 8 root references, found {len(refs)}')

name_re = re.compile(r'^name:\s*([a-z0-9-]+)\s*$', re.MULTILINE)
desc_re = re.compile(r'^description:\s*"(.+)"\s*$', re.MULTILINE)
local_ref_re = re.compile(r'`(references/[^`]+)`')
seen_names = set()
for skill in skills:
    skill_md = skill / 'SKILL.md'
    openai_yaml = skill / 'agents' / 'openai.yaml'
    if not skill_md.exists():
        errors.append(f'missing SKILL.md: {skill}')
        continue
    text = skill_md.read_text()
    match = name_re.search(text)
    if not match:
        errors.append(f'missing frontmatter name: {skill_md}')
    elif match.group(1) != skill.name:
        errors.append(f'frontmatter name mismatch in {skill_md}: {match.group(1)}')
    elif match.group(1) in seen_names:
        errors.append(f'duplicate frontmatter name: {match.group(1)}')
    else:
        seen_names.add(match.group(1))
    if not desc_re.search(text):
        errors.append(f'missing quoted frontmatter description: {skill_md}')
    if '../../references/' in text or '../' in text:
        errors.append(f'skill has non-local reference traversal: {skill_md}')
    for ref in local_ref_re.findall(text):
        if not (skill / ref).exists():
            errors.append(f'missing skill-local reference {ref}: {skill_md}')
    if not openai_yaml.exists():
        errors.append(f'missing agents/openai.yaml: {skill}')
    else:
        yaml_text = openai_yaml.read_text()
        if f'${skill.name}' not in yaml_text:
            errors.append(f'default prompt does not mention ${skill.name}: {openai_yaml}')

try:
    manifest = json.loads((root / '.codex-plugin' / 'plugin.json').read_text())
except Exception as exc:
    errors.append(f'plugin manifest is not valid JSON: {exc}')
else:
    if manifest.get('name') != 'steve-jobs':
        errors.append('plugin manifest name must be steve-jobs')
    if manifest.get('skills') != './skills/':
        errors.append('plugin manifest skills path must be ./skills/')

try:
    claude_manifest = json.loads((root / '.claude-plugin' / 'plugin.json').read_text())
except Exception as exc:
    errors.append(f'Claude plugin manifest is not valid JSON: {exc}')
else:
    skills_list = claude_manifest.get('skills')
    if claude_manifest.get('name') != 'steve-jobs':
        errors.append('Claude plugin manifest name must be steve-jobs')
    if not isinstance(skills_list, list) or len(skills_list) != 80:
        errors.append('Claude plugin manifest must list 80 skills')

try:
    skills_sh = json.loads((root / 'skills.sh.json').read_text())
except Exception as exc:
    errors.append(f'skills.sh.json is not valid JSON: {exc}')
else:
    listed = []
    for group in skills_sh.get('groupings', []):
        listed.extend(group.get('skills', []))
    if len(listed) != 80 or sorted(listed) != sorted(p.name for p in skills):
        errors.append('skills.sh.json must list exactly the 80 skill folders')

try:
    marketplace = json.loads((root / '.agents' / 'plugins' / 'marketplace.json').read_text())
except Exception as exc:
    errors.append(f'marketplace manifest is not valid JSON: {exc}')
else:
    if marketplace.get('name') != 'steve-jobs-plugin':
        errors.append('marketplace name must be steve-jobs-plugin')
    entries = marketplace.get('plugins')
    if not isinstance(entries, list):
        errors.append('marketplace plugins must be an array')
    elif not any(entry.get('name') == 'steve-jobs' for entry in entries if isinstance(entry, dict)):
        errors.append('marketplace must include steve-jobs plugin entry')

if errors:
    for error in errors:
        print(f'ERROR: {error}')
    raise SystemExit(1)

print('Basic validation passed')
print(f'skills: {len(skills)}')
print(f'root references: {len(refs)}')
PYVALIDATE

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
