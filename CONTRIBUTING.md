# Contributing

Contributions are welcome if they keep the package practical, compact, and public-safe.

## Principles

- Keep every skill name prefixed with `sj-`.
- Prefer small composable skills over one giant skill.
- Put broad background in `references/`, not in every `SKILL.md`.
- Use paraphrase and operating principles instead of long source quotations.
- Keep install steps simple for Codex and symlink-based harnesses.

## Before Opening A PR

Run:

```bash
./scripts/validate.sh
```

Check that:

- the skill count is intentional
- the reference count is intentional
- every skill has `SKILL.md`
- every skill has `agents/openai.yaml`
- no copyrighted source text was added

## Adding A Skill

1. Choose a name like `sj-product-example-skill`.
2. Add `skills/<name>/SKILL.md`.
3. Add `skills/<name>/agents/openai.yaml`.
4. Link to one or two shared references.
5. Add the skill to `references/sj-skill-catalog.md`.
6. Add the skill to `assets/sj-skills.csv`.
7. Run `./scripts/validate.sh`.
