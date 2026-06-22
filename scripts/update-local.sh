#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd -P)"

if git -C "$ROOT" rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  git -C "$ROOT" pull --ff-only
else
  echo "Skipping git pull because $ROOT is not a git checkout." >&2
fi

"$ROOT/scripts/install-local.sh"
"$ROOT/scripts/validate.sh"

echo
echo "Updated local Steve Jobs plugin checkout."
echo "Restart the agent session or reinstall from the plugin UI so cached skills reload."
