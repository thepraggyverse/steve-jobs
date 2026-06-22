# Harness Compatibility

The portable unit in this repo is a complete skill folder: `skills/sj-*/SKILL.md` plus its local `references/` and `agents/` files.

## Support Matrix

| Harness family | Works as native plugin? | Works as loose skills? | Recommended install |
|---|---|---|---|
| Codex App | Yes, via `.codex-plugin/plugin.json` | Yes | GitHub marketplace for plugin use, `scripts/link-skills.sh ~/.codex/skills` for loose skills. |
| Codex CLI | Yes, after marketplace registration and `/plugins` install | Yes | `codex plugin marketplace add thepraggyverse/steve-jobs`, then install from `/plugins`. |
| Claude Code | Manifest included for plugin-aware loaders | Yes | `scripts/link-skills.sh ~/.claude/skills` or `scripts/copy-skills.sh ~/.claude/skills`. |
| Cursor-style agents | Not claimed | Usually, if the agent scans skill folders | Link or copy `skills/sj-*` into the documented skill location. |
| OpenCode-style agents | Not claimed | Usually, if the agent scans skill folders | Link or copy `skills/sj-*` into the documented skill location. |
| Gemini/Qwen/Pi/Factory/Copilot-style agents | Not claimed | Usually, if the agent scans skill folders | Link or copy skill folders; use `skills.sh.json` as a catalog if helpful. |
| Custom harness | Depends on its plugin API | Yes, if it reads `SKILL.md` folders | Use `scripts/link-skills.sh /path/to/skills` or `scripts/copy-skills.sh /path/to/skills`. |

## Why Loose Skills Are The Common Denominator

Native plugin formats differ across harnesses. A self-contained `SKILL.md` folder is the smallest reliable unit that can move across systems. This repo therefore keeps each skill folder portable:

- no absolute paths
- no `../` references from runtime skills
- no dependency on a root repo file at runtime
- local `references/` files inside each skill that needs grounding
- a short `agents/openai.yaml` stub for harnesses that read agent metadata

## Native Manifests Included

| File | Purpose |
|---|---|
| `.codex-plugin/plugin.json` | Codex native plugin manifest. |
| `.claude-plugin/plugin.json` | Simple Claude-style manifest listing all skill folders. |
| `.agents/plugins/marketplace.json` | Repo-local marketplace metadata for Codex/custom marketplace installs. |
| `skills.sh.json` | Grouped catalog for skills.sh-style browsing and installer workflows. |

## Installation Pattern For Unknown Harnesses

1. Find the harness's skill directory.
2. Symlink the skills if the harness follows symlinks:

```bash
./scripts/link-skills.sh /path/to/harness/skills
```

3. Copy the skills if it does not:

```bash
./scripts/copy-skills.sh /path/to/harness/skills
```

4. Start a new session so the harness reloads skill metadata.
5. Test with:

```text
Use $sj-core-catalog to choose the right Steve Jobs operating skill for this task.
```

For Codex plugin installs, the stronger live proof is in [`docs/HANDOFF.md`](HANDOFF.md): it starts a fresh read-only `codex exec` session and verifies that `$sj-core-learning-refresh` loads from the installed plugin cache.

## What This Repo Does Not Claim

This repo does not claim official native plugin support for every harness. It claims portable skill-folder support and ships the manifests that are currently useful. When a harness publishes a stable plugin schema, add that manifest with validation rather than guessing.
