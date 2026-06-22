#!/usr/bin/env bash
set -euo pipefail

SOURCE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd -P)"
TARGET_DIR="${1:-$HOME/.codex/skills}"
FILTER="${2:-sj-*}"

if [ -L "$TARGET_DIR" ]; then
  resolved="$(python3 - "$TARGET_DIR" <<'PY'
from pathlib import Path
import sys

print(Path(sys.argv[1]).resolve())
PY
)"
  case "$resolved" in
    "$SOURCE_DIR"|"$SOURCE_DIR"/*)
      echo "Refusing to link into $TARGET_DIR because it resolves inside this repo: $resolved" >&2
      echo "Replace it with a real directory, then rerun the script." >&2
      exit 1
      ;;
  esac
fi

mkdir -p "$TARGET_DIR"

count=0
failed=0

shopt -s nullglob
for skill in "$SOURCE_DIR"/skills/$FILTER; do
  [ -d "$skill" ] || continue
  name="$(basename "$skill")"
  dest="$TARGET_DIR/$name"

  if [ -e "$dest" ] && [ ! -L "$dest" ]; then
    echo "Refusing to replace existing non-symlink: $dest" >&2
    failed=1
    continue
  fi

  ln -sfn "$skill" "$dest"
  count=$((count + 1))
done

if [ "$failed" -ne 0 ]; then
  echo "Some skills were not linked because of collisions." >&2
  exit 1
fi

echo "Linked $count skill(s) into $TARGET_DIR"
