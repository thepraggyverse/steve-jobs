# Symlink Guide

Symlinks let one checkout serve many agent harnesses. Update the repo once with `git pull`, and every linked harness sees the new skill files.

## Plugin Symlink

The Codex plugin path is:

```text
~/plugins/steve-jobs
```

If the repository is cloned elsewhere, link it:

```bash
mkdir -p ~/plugins
ln -sfn "$PWD" ~/plugins/steve-jobs
```

Then make sure `~/.agents/plugins/marketplace.json` contains the `steve-jobs` plugin entry. The easiest path is:

```bash
./scripts/install-local.sh
```

## Skill Symlinks

Each skill is a folder under `skills/`. A harness that scans skill folders can link them directly.

```bash
./scripts/link-skills.sh ~/.codex/skills
./scripts/link-skills.sh ~/.claude/skills
```

The script creates links like:

```text
~/.codex/skills/sj-product-simplify-to-one -> /path/to/repo/skills/sj-product-simplify-to-one
```

## Link One Group

```bash
./scripts/link-skills.sh ~/.codex/skills 'sj-core-*'
./scripts/link-skills.sh ~/.codex/skills 'sj-product-*'
./scripts/link-skills.sh ~/.codex/skills 'sj-story-*'
./scripts/link-skills.sh ~/.codex/skills 'sj-people-*'
./scripts/link-skills.sh ~/.codex/skills 'sj-strategy-*'
./scripts/link-skills.sh ~/.codex/skills 'sj-learning-*'
./scripts/link-skills.sh ~/.codex/skills 'sj-anti-*'
```

## Collision Policy

`scripts/link-skills.sh` refuses to replace an existing real directory or file.

If you see a collision:

1. Inspect the existing path.
2. Move or delete it yourself if it is obsolete.
3. Re-run the script.

The script may replace an existing symlink because symlinks are treated as install pointers.

## Copy Instead Of Symlink

If a harness does not follow symlinks, copy the skills:

```bash
mkdir -p ~/.codex/skills
cp -R skills/sj-* ~/.codex/skills/
```

Copying is less convenient because `git pull` will not update the copied skill folders.

## Remove Skill Symlinks

```bash
find ~/.codex/skills -maxdepth 1 -type l -name 'sj-*' -delete
find ~/.claude/skills -maxdepth 1 -type l -name 'sj-*' -delete
```
