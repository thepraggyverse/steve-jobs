# Contributing

Contributions are welcome if they keep the package practical, compact, portable, and public-safe.

## Principles

- Keep every skill name prefixed with `sj-`.
- Prefer small composable skills over one giant skill.
- Keep each runtime skill self-contained.
- Put broad background in compact reference files, not in every `SKILL.md`.
- Use paraphrase and operating principles instead of long source quotations.
- Keep install steps simple for Codex and symlink/copy-based harnesses.

## Before Opening A PR

Run:

```bash
./scripts/validate.sh
```

Check that the skill count is intentional, the root reference count is intentional, every skill has `SKILL.md` and `agents/openai.yaml`, runtime reference paths stay inside the skill folder, and no copyrighted source text was added.

## Adding A Skill

1. Choose a name like `sj-product-example-skill`.
2. Add `skills/<name>/SKILL.md`.
3. Add `skills/<name>/agents/openai.yaml`.
4. Add local supporting references under `skills/<name>/references/`.
5. Add or update root maintainer references under `references/` if needed.
6. Add the skill to `references/sj-skill-catalog.md`.
7. Add the skill to `assets/sj-skills.csv`.
8. Add the skill to `skills.sh.json` and `.claude-plugin/plugin.json`.
9. Update `README.md` and `docs/SKILL_REFERENCE.md`.
10. Run `./scripts/validate.sh`.
