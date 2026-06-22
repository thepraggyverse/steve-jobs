# Privacy

This repository has no telemetry, no hosted service, and no runtime network dependency.

The install scripts only modify local plugin or skill directories that you choose:

- `scripts/install-local.sh` can update `~/.agents/plugins/marketplace.json` and create `~/plugins/steve-jobs` as a symlink.
- `scripts/link-skills.sh` creates symlinks in a target skill directory.
- `scripts/copy-skills.sh` copies skill folders into a target skill directory.
- `scripts/update-local.sh` runs `git pull --ff-only`, reinstalls the local plugin pointer, and validates the checkout.

The skills do not collect data. The agent harness you run them inside may read your project files according to that harness's normal permissions.
