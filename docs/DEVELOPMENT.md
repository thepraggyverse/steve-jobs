# Development Notes

## Naming

Every skill must start with `sj-`.

Use this category shape:

```text
sj-core-*
sj-product-*
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

Shared references live in `references/` and are loaded only when useful.

Current reference set:

```text
sj-source-map.md
sj-skill-catalog.md
sj-product-craft.md
sj-story-selling.md
sj-people-leadership.md
sj-strategy-failure.md
sj-learning-practice.md
sj-anti-patterns.md
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

## Public Safety

This repository should contain:

- skill workflows
- paraphrased operating principles
- source titles
- compact references
- install scripts

It should not contain:

- full books
- full transcripts
- long copyrighted excerpts
- private notes the user did not intend to publish
- local machine secrets
