# Agent Instructions

This repository packages the `steve-jobs` operating skills: 80 `sj-*` skills for product craft, storytelling, hiring, strategy, learning, and failure review.

`AGENTS.md` is the canonical authoring file for this repo. `CLAUDE.md` and `GEMINI.md` are compatibility shims for harnesses that look for those names.

## Quick Start

```bash
./scripts/validate.sh
./scripts/link-skills.sh ~/.codex/skills
./scripts/link-skills.sh ~/.claude/skills
```

For local Codex plugin development:

```bash
./scripts/install-local.sh
codex plugin add steve-jobs@personal
```

## Repo Surfaces

Changes may affect runtime skills, skill-local references, root reference copies, Codex plugin metadata, Claude/skills manifests, repo marketplace metadata, docs, and install/update scripts.

## Skill Contract

Every runtime skill must:

- start with `sj-`
- live under `skills/<skill-name>/`
- include `SKILL.md`
- include `agents/openai.yaml`
- keep frontmatter to `name` and `description`
- point only to files inside its own directory tree when it references runtime support files
- avoid absolute paths, `../` traversal, and harness-specific variables in core behavior
- avoid full books, full transcripts, and long copyrighted excerpts

If two skills need the same reference, duplicate the small reference into each skill's own `references/` folder. Root `references/` are source copies for maintainers and docs; runtime skills should read their local copies.

## Documentation Contract

When adding, renaming, or removing a skill, update `assets/sj-skills.csv`, `references/sj-skill-catalog.md`, `README.md`, `docs/SKILL_REFERENCE.md`, `skills.sh.json`, and `.claude-plugin/plugin.json`.

When install behavior changes, update `README.md`, `docs/INSTALL.md`, `docs/SYMLINKS.md`, `docs/HARNESSES.md`, and `docs/UPDATE.md`.

## Validation

Run this before committing:

```bash
./scripts/validate.sh
```

The validator checks skill counts, manifest JSON, local reference portability, skill frontmatter, prompt stubs, and system validators when available.

## Public Safety

This repo contains operating workflows and paraphrased reference notes only. Do not add source books, full podcast transcripts, long excerpts, private notes, secrets, or local machine paths.
