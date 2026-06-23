#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd -P)"
export ROOT

python3 <<'PYVALIDATE'
import json
import os
import re
import csv
from pathlib import Path

root = Path(os.environ['ROOT'])
skills_dir = root / 'skills'
refs_dir = root / 'references'
expected_skill_count = 91
max_description_chars = 260

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
    'docs/PLAYBOOKS.md',
    'docs/COMPOUNDING.md',
    'docs/MEMORY_AND_LOGS.md',
    'docs/HANDOFF.md',
    'docs/PLUGIN_ARCHITECTURE.md',
    'docs/DEVELOPMENT.md',
    'templates/sj-learning.md',
    'scripts/check-install.sh',
]

errors = []
for rel in required_files:
    if not (root / rel).exists():
        errors.append(f'missing required file: {rel}')

skills = sorted(p for p in skills_dir.iterdir() if p.is_dir() and p.name.startswith('sj-'))
refs = sorted(refs_dir.glob('sj-*.md'))

skill_names = [p.name for p in skills]

if len(skills) != expected_skill_count:
    errors.append(f'expected {expected_skill_count} skills, found {len(skills)}')
if len(refs) != 9:
    errors.append(f'expected 9 root references, found {len(refs)}')

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
    else:
        description = desc_re.search(text).group(1)
        if len(description) > max_description_chars:
            errors.append(f'frontmatter description too long ({len(description)} chars): {skill_md}')
    if '[TODO:' in text or 'TODO:' in text:
        errors.append(f'skill still contains TODO placeholder: {skill_md}')
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
    with (root / 'assets' / 'sj-skills.csv').open(newline='') as handle:
        rows = list(csv.DictReader(handle))
except Exception as exc:
    errors.append(f'assets/sj-skills.csv could not be read: {exc}')
else:
    csv_names = [row.get('name', '') for row in rows]
    if len(csv_names) != expected_skill_count or sorted(csv_names) != sorted(skill_names):
        errors.append('assets/sj-skills.csv must list exactly the skill folders')

try:
    claude_manifest = json.loads((root / '.claude-plugin' / 'plugin.json').read_text())
except Exception as exc:
    errors.append(f'Claude plugin manifest is not valid JSON: {exc}')
else:
    skills_list = claude_manifest.get('skills')
    if claude_manifest.get('name') != 'steve-jobs':
        errors.append('Claude plugin manifest name must be steve-jobs')
    expected_paths = [f'./skills/{name}' for name in skill_names]
    if not isinstance(skills_list, list) or sorted(skills_list) != sorted(expected_paths):
        errors.append(f'Claude plugin manifest must list exactly the {expected_skill_count} skill folders')

try:
    skills_sh = json.loads((root / 'skills.sh.json').read_text())
except Exception as exc:
    errors.append(f'skills.sh.json is not valid JSON: {exc}')
else:
    listed = []
    for group in skills_sh.get('groupings', []):
        listed.extend(group.get('skills', []))
    if len(listed) != expected_skill_count or sorted(listed) != sorted(skill_names):
        errors.append(f'skills.sh.json must list exactly the {expected_skill_count} skill folders')

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

inventory_files = [
    'README.md',
    'docs/SKILL_REFERENCE.md',
    'references/sj-skill-catalog.md',
]
for rel in inventory_files:
    path = root / rel
    if not path.exists():
        continue
    content = path.read_text()
    for name in skill_names:
        if name not in content:
            errors.append(f'{rel} is missing skill reference: {name}')

numbered_catalogs = [
    'references/sj-skill-catalog.md',
    'skills/sj-core-catalog/references/sj-skill-catalog.md',
    'skills/sj-core-compound-learning/references/sj-skill-catalog.md',
]
numbered_skill_re = re.compile(r'^(\d+)\.\s+`\$sj-[^`]+`', re.MULTILINE)
for rel in numbered_catalogs:
    path = root / rel
    if not path.exists():
        errors.append(f'missing numbered skill catalog: {rel}')
        continue
    numbers = [int(match.group(1)) for match in numbered_skill_re.finditer(path.read_text())]
    expected_numbers = list(range(1, expected_skill_count + 1))
    if numbers != expected_numbers:
        errors.append(f'{rel} must number skills sequentially 1..{expected_skill_count}')

known_skill_tokens = set(skill_names)
known_non_skill_tokens = {
    'sj-core',
    'sj-core-',
    'sj-product',
    'sj-product-',
    'sj-ive',
    'sj-ive-',
    'sj-story',
    'sj-story-',
    'sj-people',
    'sj-people-',
    'sj-strategy',
    'sj-strategy-',
    'sj-learning',
    'sj-learning-',
    'sj-anti',
    'sj-anti-',
    'sj-prefixed',
}
stale_ref_re = re.compile(r'\bsj-[a-z0-9-]+')
scan_roots = [
    root / 'README.md',
    root / 'AGENTS.md',
    root / 'docs',
    root / 'references',
    root / 'assets',
    root / 'skills.sh.json',
    root / '.claude-plugin' / 'plugin.json',
]
for scan_root in scan_roots:
    candidates = [scan_root] if scan_root.is_file() else sorted(scan_root.rglob('*'))
    for path in candidates:
        if not path.is_file() or path.suffix not in {'', '.md', '.json', '.csv'}:
            continue
        rel = path.relative_to(root)
        content = path.read_text(errors='ignore')
        for token in stale_ref_re.findall(content):
            if token.endswith('-plugin') or token in known_skill_tokens:
                continue
            if token in known_non_skill_tokens:
                continue
            if token.startswith(('sj-source', 'sj-skill', 'sj-product-craft', 'sj-ive-design-studio', 'sj-story-selling', 'sj-people-leadership', 'sj-strategy-failure', 'sj-learning-practice', 'sj-anti-patterns')):
                continue
            errors.append(f'stale or unknown sj-* reference in {rel}: {token}')
        if '/Users/praggy' in content:
            errors.append(f'author-local absolute path leaked into public file: {rel}')

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
