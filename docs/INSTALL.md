# Install Guide

This repository can be used in two ways:

1. As a Codex plugin.
2. As loose symlinked skill folders for Codex, Claude Code, or another harness.

Use the plugin install when your harness supports `.codex-plugin/plugin.json`. Use loose skills when the harness only scans a skill directory.

## Option A: Codex Plugin Install

Clone directly into the default personal plugin location:

```bash
git clone https://github.com/thepraggyverse/steve-jobs.git ~/plugins/steve-jobs
cd ~/plugins/steve-jobs
./scripts/install-local.sh
codex plugin add steve-jobs@personal
```

Start a new Codex thread, then invoke:

```text
Use $sj-core-catalog to choose the right Steve Jobs operating skill for this task.
```

## Option B: Codex App From GitHub

In the Codex app, add this repository as a custom plugin marketplace:

| Field | Value |
|---|---|
| Source | `thepraggyverse/steve-jobs` |
| Git ref | `main` |
| Sparse paths | leave blank |

Then install the **Steve Jobs** plugin from that marketplace and restart Codex.

## Option C: Codex CLI Marketplace

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

## What The Local Installer Does

`scripts/install-local.sh`:

- ensures `~/plugins/steve-jobs` points at this checkout
- creates or updates `~/.agents/plugins/marketplace.json`
- preserves existing marketplace entries
- adds or refreshes the `steve-jobs` entry
- refuses to overwrite a real, non-symlink directory at `~/plugins/steve-jobs`

The marketplace entry uses:

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

## Option D: Clone Elsewhere And Symlink The Plugin

If you keep source repos under `~/Developer`:

```bash
git clone https://github.com/thepraggyverse/steve-jobs.git ~/Developer/steve-jobs
cd ~/Developer/steve-jobs
./scripts/install-local.sh
codex plugin add steve-jobs@personal
```

The installer creates:

```text
~/plugins/steve-jobs -> ~/Developer/steve-jobs
```

## Option E: Loose Skill Symlinks

Codex skill home:

```bash
./scripts/link-skills.sh ~/.codex/skills
```

Claude Code skill home:

```bash
./scripts/link-skills.sh ~/.claude/skills
```

Custom skill home:

```bash
./scripts/link-skills.sh /path/to/skills
```

Only product skills:

```bash
./scripts/link-skills.sh ~/.codex/skills 'sj-product-*'
```

Only strategy skills:

```bash
./scripts/link-skills.sh ~/.codex/skills 'sj-strategy-*'
```

## Manual Plugin Install

If you do not want to run the installer:

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

```bash
./scripts/validate.sh
find skills -mindepth 1 -maxdepth 1 -type d | wc -l
find references -maxdepth 1 -name 'sj-*.md' | wc -l
```

Expected:

```text
80 skills
8 references
```

## Update

```bash
cd ~/plugins/steve-jobs
git pull
./scripts/install-local.sh
codex plugin add steve-jobs@personal
```

Start a new Codex thread after reinstalling.

## Uninstall

Remove the plugin symlink or checkout:

```bash
rm -f ~/plugins/steve-jobs
```

If you linked loose skills:

```bash
find ~/.codex/skills -maxdepth 1 -type l -name 'sj-*' -delete
find ~/.claude/skills -maxdepth 1 -type l -name 'sj-*' -delete
```

If you want to remove the marketplace entry too, delete the `steve-jobs` object from `~/.agents/plugins/marketplace.json`.
