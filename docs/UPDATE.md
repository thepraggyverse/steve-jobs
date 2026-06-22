# Update Guide

Agent harnesses often cache skill text at session start. Updating the files on disk is only half the job; you also need a fresh agent session or a plugin reinstall step so the updated skill text is loaded.

## Local Codex Plugin Update

```bash
cd ~/plugins/steve-jobs
./scripts/update-local.sh
```

That script runs:

1. `git pull --ff-only`
2. `scripts/install-local.sh`
3. `scripts/validate.sh`

Then restart Codex or reinstall from the `/plugins` UI if your profile still has an older cached plugin copy.

## GitHub Marketplace Update

If you installed from the GitHub marketplace:

1. Pull the latest marketplace source in the plugin UI if your harness exposes that action.
2. Reinstall or update `steve-jobs` from `/plugins`.
3. Start a new session.

Codex CLI marketplace registration usually does not need to be repeated unless the source repository changed:

```bash
codex plugin marketplace add thepraggyverse/steve-jobs
```

## Loose Symlink Update

```bash
cd /path/to/steve-jobs
git pull --ff-only
./scripts/validate.sh
```

The harness points at the checkout, so the file update is immediate on disk. Start a new session to refresh cached skill text.

## Loose Copy Update

```bash
cd /path/to/steve-jobs
git pull --ff-only
SKILL_COPY_OVERWRITE=1 ./scripts/copy-skills.sh ~/.codex/skills
```

Replace `~/.codex/skills` with the target harness skill directory.

## Verify After Update

```bash
./scripts/validate.sh
find skills -mindepth 1 -maxdepth 1 -type d | wc -l
```

Expected count:

```text
80
```

Then test one router prompt:

```text
Use $sj-core-catalog to choose the right SJ skill for this product problem.
```
