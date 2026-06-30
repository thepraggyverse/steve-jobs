# Symlink And Copy Guide

Symlinks let one checkout serve many agent harnesses. Update the repo once with `git pull`, and every linked harness sees the new skill files after a fresh session.

Copy mode is for harnesses that do not follow symlinks or when you want a frozen snapshot.

## Plugin Symlink

The default local Codex plugin path is:

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

```bash
./scripts/link-skills.sh ~/.codex/skills
./scripts/link-skills.sh ~/.claude/skills
./scripts/link-skills.sh /path/to/custom/skills
```

The script creates links like:

```text
~/.codex/skills/sj-product-simplify-to-one -> /path/to/repo/skills/sj-product-simplify-to-one
```

## Link One Group

The profile installer is the easiest path:

```bash
./scripts/install-profile.sh product ~/.codex/skills
./scripts/install-profile.sh ive ~/.codex/skills
./scripts/install-profile.sh story ~/.codex/skills
```

The lower-level linker accepts raw patterns:

```bash
./scripts/link-skills.sh ~/.codex/skills 'sj-core-*'
./scripts/link-skills.sh ~/.codex/skills 'sj-product-*'
./scripts/link-skills.sh ~/.codex/skills 'sj-ive-*'
./scripts/link-skills.sh ~/.codex/skills 'sj-story-*'
./scripts/link-skills.sh ~/.codex/skills 'sj-people-*'
./scripts/link-skills.sh ~/.codex/skills 'sj-strategy-*'
./scripts/link-skills.sh ~/.codex/skills 'sj-learning-*'
./scripts/link-skills.sh ~/.codex/skills 'sj-anti-*'
```

## Collision Policy

`scripts/link-skills.sh` refuses to replace an existing real directory or file. It may replace an existing symlink because symlinks are install pointers.

## Copy Instead Of Symlink

```bash
./scripts/copy-skills.sh ~/.codex/skills
./scripts/copy-skills.sh ~/.claude/skills
./scripts/copy-skills.sh /path/to/custom/skills
```

Copy one group:

```bash
./scripts/copy-skills.sh ~/.codex/skills 'sj-product-*'
```

Overwrite a previous copy intentionally:

```bash
SKILL_COPY_OVERWRITE=1 ./scripts/copy-skills.sh ~/.codex/skills
```

Copying is less convenient because `git pull` will not update the copied skill folders. Rerun copy mode after updates.

## Remove Skill Symlinks

Use the safe remover so only symlinks pointing into this checkout are removed:

```bash
./scripts/unlink-skills.sh ~/.codex/skills 'sj-*'
./scripts/unlink-skills.sh ~/.claude/skills 'sj-*'
./scripts/unlink-skills.sh ~/.codex/skills 'sj-ive-*' --dry-run
```

## Remove Copied Skills

```bash
find ~/.codex/skills -maxdepth 1 -type d -name 'sj-*' -exec rm -rf {} +
find ~/.claude/skills -maxdepth 1 -type d -name 'sj-*' -exec rm -rf {} +
```
