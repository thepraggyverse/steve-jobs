#!/usr/bin/env bash
set -euo pipefail

PLUGIN_NAME="steve-jobs"
SOURCE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd -P)"
TARGET_ROOT="${PLUGIN_TARGET_ROOT:-$HOME/plugins}"
TARGET_PATH="${PLUGIN_TARGET_PATH:-$TARGET_ROOT/$PLUGIN_NAME}"
MARKETPLACE_PATH="${MARKETPLACE_PATH:-$HOME/.agents/plugins/marketplace.json}"
MARKETPLACE_NAME="${MARKETPLACE_NAME:-personal}"

mkdir -p "$TARGET_ROOT"

if [ "$SOURCE_DIR" != "$TARGET_PATH" ]; then
  if [ -e "$TARGET_PATH" ] && [ ! -L "$TARGET_PATH" ]; then
    echo "Refusing to replace existing non-symlink: $TARGET_PATH" >&2
    echo "Move it aside or set PLUGIN_TARGET_PATH to another location." >&2
    exit 1
  fi
  ln -sfn "$SOURCE_DIR" "$TARGET_PATH"
fi

mkdir -p "$(dirname "$MARKETPLACE_PATH")"

export MARKETPLACE_PATH MARKETPLACE_NAME PLUGIN_NAME
python3 <<'PY'
import json
import os
from pathlib import Path

path = Path(os.environ["MARKETPLACE_PATH"]).expanduser()
name = os.environ["MARKETPLACE_NAME"]
plugin = os.environ["PLUGIN_NAME"]

if path.exists():
    data = json.loads(path.read_text())
else:
    data = {
        "name": name,
        "interface": {"displayName": name.capitalize()},
        "plugins": [],
    }

data.setdefault("name", name)
data.setdefault("interface", {}).setdefault("displayName", data["name"].capitalize())
plugins = data.setdefault("plugins", [])

entry = {
    "name": plugin,
    "source": {
        "source": "local",
        "path": f"./plugins/{plugin}",
    },
    "policy": {
        "installation": "AVAILABLE",
        "authentication": "ON_INSTALL",
    },
    "category": "Productivity",
}

for index, existing in enumerate(plugins):
    if existing.get("name") == plugin:
        plugins[index] = entry
        break
else:
    plugins.append(entry)

path.write_text(json.dumps(data, indent=2) + "\n")
PY

echo "Installed local plugin source: $TARGET_PATH"
echo "Updated marketplace: $MARKETPLACE_PATH"
echo
echo "Next:"
echo "  codex plugin add ${PLUGIN_NAME}@${MARKETPLACE_NAME}"
echo "  # then start a new Codex thread"
