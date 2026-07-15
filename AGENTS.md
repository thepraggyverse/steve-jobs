# Agent Instructions

This repository packages the `steve-jobs` operating skills: 91 `sj-*` skills for product craft, Jony Ive design studio practice, storytelling, hiring, strategy, learning, and failure review.

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
- define a skill-specific workflow, output contract, and at least three failure guardrails
- include a stable claim ID and source IDs under `Source Grounding`
- keep its `agents/openai.yaml` prompt synchronized with its example prompt

`$sj-core-catalog` is the only skill with `allow_implicit_invocation: true`.
All leaf skills remain available through explicit `$sj-*` invocation.
This policy keeps the full 91-skill pack searchable without consuming the model's global implicit-skill budget.

If two skills need the same reference, duplicate the small reference into each skill's own `references/` folder. Root `references/` are source copies for maintainers and docs; runtime skills should read their local copies.

## Documentation Contract

When adding, renaming, or removing a skill, update `assets/sj-skills.csv`, `references/sj-skill-catalog.md`, `README.md`, `docs/SKILL_REFERENCE.md`, `skills.sh.json`, and `.claude-plugin/plugin.json`.

When changing usage chains, scenario guidance, or install profiles, update `docs/PLAYBOOKS.md` and `docs/WHEN_TO_USE_WHAT.md`.

When adding memory, logging, or compounding behavior, update `docs/MEMORY_AND_LOGS.md`, `templates/sj-learning.md`, and validation coverage.

When install behavior changes, update `README.md`, `docs/INSTALL.md`, `docs/SYMLINKS.md`, `docs/HARNESSES.md`, `docs/UPDATE.md`, `scripts/check-install.sh`, `scripts/install-profile.sh`, and `scripts/unlink-skills.sh`.

When live verification, release closeout, or continuation instructions change, update `docs/HANDOFF.md`.

When source grounding changes, update `references/sj-source-map.md`, `scripts/sync-source-grounding.py`, and regenerate the local evidence files.

When a workflow, output, guardrail, example prompt, or metadata policy changes, run all synchronization scripts before validation:

```bash
./scripts/sync-source-grounding.py
./scripts/sync-openai-metadata.py
./scripts/build-behavior-cases.py
```

## Validation

Run this before committing:

```bash
./scripts/validate.sh
```

For release or handoff closeout, also follow `docs/HANDOFF.md`.
Use `scripts/check-install.sh --refresh` when installed-cache truth matters.

The validator checks inventory, unique workflow and output contracts, provenance, metadata policy, 182 behavior cases, router cases, local reference portability, manifests, and system validators when available.

## Public Safety

This repo contains operating workflows and paraphrased reference notes only. Do not add source books, full podcast transcripts, long excerpts, private notes, secrets, or local machine paths.
