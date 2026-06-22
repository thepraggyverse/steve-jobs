# Context

This file defines vocabulary used in the Steve Jobs operating skills repo.

## Terms

**SJ skill**: A runtime skill whose folder name starts with `sj-`.

**Operating lens**: A compact method derived from Steve Jobs-related books, interviews, and podcast notes. It should create a clearer artifact or decision, not imitate a personality.

**Root reference**: A maintainer copy under `references/`. Root references are useful for docs and generation, but runtime skills should not point to them directly.

**Skill-local reference**: A small copied note under `skills/<skill>/references/`. This is the portable runtime form because converters and loose-skill installs can move one skill folder without breaking its supporting files.

**Loose skill install**: An install where a harness scans folders such as `~/.codex/skills` or `~/.claude/skills`.

**Native plugin install**: An install where the harness reads a plugin manifest, such as `.codex-plugin/plugin.json`.

**Compound capture**: Ending a useful run by writing down the reusable lesson so a future session starts smarter.

## Avoided Terms

- Do not describe the skills as a Steve Jobs simulator.
- Do not lead public docs with affiliation disclaimers; keep those in `NOTICE.md` and the README disclaimer.
- Do not call root references shared runtime dependencies. Runtime dependencies are skill-local.
