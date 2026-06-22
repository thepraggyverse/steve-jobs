#!/usr/bin/env bash
set -euo pipefail

SOURCE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd -P)"
TARGET_DIR="${1:-$HOME/.codex/skills}"
FILTER="${2:-sj-*}"
OVERWRITE="${SKILL_COPY_OVERWRITE:-0}"

mkdir -p "$TARGET_DIR"

count=0
failed=0

shopt -s nullglob
for skill in "$SOURCE_DIR"/skills/$FILTER; do
  [ -d "$skill" ] || continue
  name="$(basename "$skill")"
  dest="$TARGET_DIR/$name"

  if [ -e "$dest" ] && [ "$OVERWRITE" != "1" ]; then
    echo "Refusing to overwrite existing path: $dest" >&2
    echo "Set SKILL_COPY_OVERWRITE=1 to replace copied skills intentionally." >&2
    failed=1
    continue
  fi

  if [ -e "$dest" ] || [ -L "$dest" ]; then
    rm -rf "$dest"
  fi

  cp -R "$skill" "$dest"
  count=$((count + 1))
done

if [ "$failed" -ne 0 ]; then
  echo "Some skills were not copied because of collisions." >&2
  exit 1
fi

echo "Copied $count skill(s) into $TARGET_DIR"
