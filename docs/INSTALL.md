# Install Guide

This repository can be used in three ways:

1. As a native Codex plugin.
2. As loose `SKILL.md` folders linked or copied into a harness skill directory.
3. As a source catalog for installers that read `.claude-plugin/plugin.json` or `skills.sh.json`.

Use the native plugin path when your harness supports `.codex-plugin/plugin.json`. Use loose skills when the harness scans a skill directory. Use copy mode when the harness does not follow symlinks.

## Compatibility Matrix

| Harness | Recommended path | Status | Notes |
|---|---|---|---|
| Codex App | GitHub marketplace -> native plugin install | Supported | Add `thepraggyverse/steve-jobs` as a custom marketplace, install `steve-jobs`, restart Codex. |
| Codex CLI | `codex plugin marketplace add` plus `/plugins` | Supported | Marketplace registration makes it visible; the `/plugins` UI activates it. |
| Local Codex plugin | `scripts/install-local.sh` | Supported | Creates or refreshes `~/plugins/steve-jobs` and `~/.agents/plugins/marketplace.json`. |
| Codex loose skills | `scripts/link-skills.sh ~/.codex/skills` | Supported | Useful when you want direct skill folders. |
| Claude Code loose skills | `scripts/link-skills.sh ~/.claude/skills` | Supported | Skills are self-contained and use local references. |
| Claude plugin-aware loaders | `.claude-plugin/plugin.json` | Manifest included | Use if your loader accepts a local Claude plugin manifest. |
| Cursor, OpenCode, Gemini, Qwen, Pi, Copilot-style harnesses | Link or copy `skills/sj-*` into that harness skill directory | Portable | These docs avoid claiming a native plugin format unless the harness documents one. |
| skills.sh-style catalogs | `skills.sh.json` | Manifest included | Grouped by skill family for browsing and installer experiments. |

## Option A: Codex App From GitHub

In the Codex app, add this repository as a custom plugin marketplace:

| Field | Value |
|---|---|
| Source | `thepraggyverse/steve-jobs` |
| Git ref | `main` |
| Sparse paths | leave blank |

Then install the **Steve Jobs** plugin from that marketplace and restart Codex.

Invoke:

```text
Use $sj-core-catalog to choose the right Steve Jobs operating skill for this task.
```

## Option B: Codex CLI Marketplace

Register the GitHub repository as a marketplace:

```bash
codex plugin marketplace add thepraggyverse/steve-jobs
```

Then launch Codex, open `/plugins`, select the **Steve Jobs** marketplace, install `steve-jobs`, and restart Codex.

For a non-default Codex profile, keep the marketplace and install steps on the same `CODEX_HOME`:

```bash
CODEX_HOME="$HOME/.codex/profiles/work" codex plugin marketplace add thepraggyverse/steve-jobs
CODEX_HOME="$HOME/.codex/profiles/work" codex
```

Inside Codex, run `/plugins` from that profile and install `steve-jobs`.

## Option C: Local Codex Plugin

Clone directly into the default personal plugin location:

```bash
git clone https://github.com/thepraggyverse/steve-jobs.git ~/plugins/steve-jobs
cd ~/plugins/steve-jobs
./scripts/install-local.sh
codex plugin add steve-jobs@personal
```

If you keep source repos elsewhere:

```bash
git clone https://github.com/thepraggyverse/steve-jobs.git ~/Developer/steve-jobs
cd ~/Developer/steve-jobs
./scripts/install-local.sh
codex plugin add steve-jobs@personal
```

## What The Local Installer Does

`scripts/install-local.sh`:

- ensures `~/plugins/steve-jobs` points at this checkout
- creates or updates `~/.agents/plugins/marketplace.json`
- preserves existing marketplace entries
- adds or refreshes the `steve-jobs` entry
- refuses to overwrite a real, non-symlink directory at `~/plugins/steve-jobs`

## Option D: Loose Skill Symlinks

```bash
./scripts/link-skills.sh ~/.codex/skills
./scripts/link-skills.sh ~/.claude/skills
./scripts/link-skills.sh /path/to/skills
```

Only one group:

```bash
./scripts/link-skills.sh ~/.codex/skills 'sj-product-*'
./scripts/link-skills.sh ~/.codex/skills 'sj-ive-*'
./scripts/link-skills.sh ~/.codex/skills 'sj-story-*'
./scripts/link-skills.sh ~/.codex/skills 'sj-strategy-*'
```

## Option E: Copy Skills Instead Of Symlink

Use copy mode when a harness does not follow symlinks or when you want a frozen snapshot.

```bash
./scripts/copy-skills.sh ~/.codex/skills
./scripts/copy-skills.sh ~/.claude/skills
./scripts/copy-skills.sh /path/to/skills 'sj-product-*'
```

Copy mode refuses to overwrite existing folders by default. To replace a previous copy intentionally:

```bash
SKILL_COPY_OVERWRITE=1 ./scripts/copy-skills.sh ~/.codex/skills
```

## Manual Plugin Install

```bash
mkdir -p ~/plugins ~/.agents/plugins
ln -sfn "$PWD" ~/plugins/steve-jobs
```

Then add this entry to `~/.agents/plugins/marketplace.json` under `plugins[]`:

```json
{
  "name": "steve-jobs",
  "source": {
    "source": "local",
    "path": "./plugins/steve-jobs"
  },
  "policy": {
    "installation": "AVAILABLE",
    "authentication": "ON_INSTALL"
  },
  "category": "Productivity"
}
```

Then run:

```bash
codex plugin add steve-jobs@personal
```

## Validate Install

One-command check:

```bash
./scripts/check-install.sh --refresh
```

Add `--live` to run a read-only `codex exec` smoke test:

```bash
./scripts/check-install.sh --refresh --live
```

Manual checks:

```bash
./scripts/validate.sh
find skills -mindepth 1 -maxdepth 1 -type d | wc -l
find references -maxdepth 1 -name 'sj-*.md' | wc -l
```

Expected:

```text
91 skills
9 root references
```

For a native Codex plugin install, also verify the installed cache:

```bash
codex plugin list | rg 'steve-jobs@personal|PLUGIN|Marketplace `personal`' -C 2
"$HOME/.codex/plugins/cache/personal/steve-jobs/0.2.0/scripts/validate.sh"
```

For a live harness test, use the plugin-only `codex exec` recipe in [`docs/HANDOFF.md`](HANDOFF.md).

## Update

```bash
cd ~/plugins/steve-jobs
./scripts/update-local.sh
```

For copied loose skills:

```bash
git pull --ff-only
SKILL_COPY_OVERWRITE=1 ./scripts/copy-skills.sh ~/.codex/skills
```

Start a new agent session after updating so cached skill text reloads.

## Skill Profiles

Use profiles when you want a smaller loose-skill install:

```bash
./scripts/list-skills.sh profiles
./scripts/install-profile.sh product ~/.codex/skills
./scripts/install-profile.sh ive ~/.codex/skills
./scripts/install-profile.sh story ~/.codex/skills
./scripts/install-profile.sh strategy ~/.codex/skills
```

For copy mode:

```bash
./scripts/install-profile.sh ive ~/.codex/skills --copy
```

The lower-level scripts still accept raw patterns:

```bash
./scripts/link-skills.sh ~/.codex/skills 'sj-product-*'
SKILL_COPY_OVERWRITE=1 ./scripts/copy-skills.sh ~/.codex/skills 'sj-ive-*'
```

## Uninstall

Remove the plugin symlink or checkout:

```bash
rm -f ~/plugins/steve-jobs
```

If you linked loose skills:

```bash
./scripts/unlink-skills.sh ~/.codex/skills 'sj-*'
./scripts/unlink-skills.sh ~/.claude/skills 'sj-*'
```

If you copied loose skills:

```bash
find ~/.codex/skills -maxdepth 1 -type d -name 'sj-*' -exec rm -rf {} +
find ~/.claude/skills -maxdepth 1 -type d -name 'sj-*' -exec rm -rf {} +
```

If you want to remove the marketplace entry too, delete the `steve-jobs` object from `~/.agents/plugins/marketplace.json`.
