#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd -P)"
SOURCE_SKILLS="$ROOT/skills"
TARGET_DIR="$HOME/.codex/skills"
FILTER="sj-*"
DRY_RUN=0

usage() {
  cat <<'EOF'
Usage: scripts/unlink-skills.sh [target-dir] [filter] [--dry-run]

Safely removes only symlinks whose resolved target is inside this repo's skills/
directory. It never removes real directories, copied skills, or symlinks owned by
another checkout.
EOF
}

if [ "${1:-}" = "-h" ] || [ "${1:-}" = "--help" ]; then
  usage
  exit 0
fi

target_set=0
filter_set=0
while [ "$#" -gt 0 ]; do
  case "$1" in
    --dry-run)
      DRY_RUN=1
      ;;
    -*)
      echo "Unknown argument: $1" >&2
      usage >&2
      exit 2
      ;;
    *)
      if [ "$target_set" -eq 0 ]; then
        TARGET_DIR="$1"
        target_set=1
      elif [ "$filter_set" -eq 0 ]; then
        FILTER="$1"
        filter_set=1
      else
        echo "Unexpected extra argument: $1" >&2
        usage >&2
        exit 2
      fi
      ;;
  esac
  shift
done

if [ ! -d "$TARGET_DIR" ]; then
  if [ "$DRY_RUN" -eq 1 ]; then
    echo "Target directory does not exist: $TARGET_DIR"
    echo "Matched repo-owned symlink(s): 0"
    echo "Skipped path(s): 0"
    exit 0
  fi
  echo "Target directory does not exist: $TARGET_DIR" >&2
  exit 1
fi

count=0
skipped=0

shopt -s nullglob
# shellcheck disable=SC2086 # FILTER is intentionally a caller-provided glob.
for path in "$TARGET_DIR"/$FILTER; do
  [ -L "$path" ] || {
    skipped=$((skipped + 1))
    continue
  }

  resolved="$(python3 - "$path" <<'PY'
from pathlib import Path
import sys

print(Path(sys.argv[1]).resolve())
PY
)"

  case "$resolved" in
    "$SOURCE_SKILLS"/*)
      if [ "$DRY_RUN" -eq 1 ]; then
        echo "Would remove $path -> $resolved"
      else
        rm "$path"
        echo "Removed $path"
      fi
      count=$((count + 1))
      ;;
    *)
      echo "Skipped foreign symlink: $path -> $resolved"
      skipped=$((skipped + 1))
      ;;
  esac
done

echo "Matched repo-owned symlink(s): $count"
echo "Skipped path(s): $skipped"
