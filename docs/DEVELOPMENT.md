# Development Notes

## Naming

Every skill must start with `sj-`.

Use this category shape:

```text
sj-core-*
sj-product-*
sj-ive-*
sj-story-*
sj-people-*
sj-strategy-*
sj-learning-*
sj-anti-*
```

Keep names lowercase, hyphenated, and under 64 characters.

## Skill Shape

Each skill should contain:

```text
skills/<skill-name>/
  SKILL.md
  agents/openai.yaml
  references/
    sj-*.md
```

`SKILL.md` should stay lean:

- frontmatter with `name` and `description`
- core move
- workflow
- reference pointers
- output shape
- guardrails
- example prompt

Do not paste book chapters or long excerpts into skills.

## References

Root reference copies live in `references/` for maintainers and docs.

Runtime skills must reference only files inside their own directory tree, usually `references/<file>.md`. If a skill needs a root reference, copy it into that skill's local `references/` folder.

Current root reference set:

```text
sj-source-map.md
sj-skill-catalog.md
sj-product-craft.md
sj-ive-design-studio.md
sj-story-selling.md
sj-people-leadership.md
sj-strategy-failure.md
sj-learning-practice.md
sj-anti-patterns.md
```

## Updating Skill Lists

When adding, removing, or renaming a skill, update:

```text
assets/sj-skills.csv
references/sj-skill-catalog.md
README.md
docs/SKILL_REFERENCE.md
skills.sh.json
.claude-plugin/plugin.json
```

If the skill is referenced by another skill's local catalog, update that skill-local `references/sj-skill-catalog.md` copy too.

When changing memory or compounding behavior, update:

```text
docs/MEMORY_AND_LOGS.md
templates/sj-learning.md
docs/COMPOUNDING.md
docs/PLUGIN_ARCHITECTURE.md
```

When changing install, validation, live testing, or release closeout behavior, update:

```text
docs/HANDOFF.md
docs/INSTALL.md
docs/UPDATE.md
docs/PLAYBOOKS.md
CHANGELOG.md
scripts/check-install.sh
```

Then run:

```bash
./scripts/validate.sh
```

## Validation

Run:

```bash
./scripts/validate.sh
```

If local Codex authoring validators are available at:

```text
~/.codex/skills/.system/skill-creator/scripts/quick_validate.py
~/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py
```

the validation script will use them automatically.

Validation should catch skill count drift, duplicate names, missing manifest entries, missing README/catalog references, stale skill references, and overlong descriptions.

Before handing work to another agent or publishing, follow `docs/HANDOFF.md`.

## Lifecycle Cleanup

Do not add CE-style install manifests or legacy cleanup while `sj-*` names remain stable. Add lifecycle cleanup only when skills are renamed, removed, or moved in a way that would leave stale loose-skill installs behind.

## Public Safety

This repository should contain skill workflows, paraphrased operating principles, source titles, compact references, and install scripts.

It should not contain full books, full transcripts, long copyrighted excerpts, private notes the user did not intend to publish, local machine secrets, or local absolute paths in runtime skill content.
