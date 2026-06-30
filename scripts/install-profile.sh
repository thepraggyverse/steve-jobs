#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd -P)"
PROFILE="${1:-}"
TARGET_DIR="$HOME/.codex/skills"
MODE="link"

usage() {
  cat <<'EOF'
Usage: scripts/install-profile.sh <profile> [target-dir] [--copy]

Profiles:
  all       sj-*
  core      sj-core-*
  product   sj-product-*
  ive       sj-ive-*
  story     sj-story-*
  people    sj-people-*
  strategy  sj-strategy-*
  learning  sj-learning-*
  anti      sj-anti-*

Examples:
  scripts/install-profile.sh ive ~/.codex/skills
  scripts/install-profile.sh product ~/.claude/skills --copy
EOF
}

if [ -z "$PROFILE" ] || [ "$PROFILE" = "-h" ] || [ "$PROFILE" = "--help" ]; then
  usage
  exit 0
fi

shift
while [ "$#" -gt 0 ]; do
  case "$1" in
    --copy)
      MODE="copy"
      ;;
    -*)
      echo "Unknown argument: $1" >&2
      usage >&2
      exit 2
      ;;
    *)
      if [ "$TARGET_DIR" != "$HOME/.codex/skills" ]; then
        echo "Unexpected extra target directory: $1" >&2
        usage >&2
        exit 2
      fi
      TARGET_DIR="$1"
      ;;
  esac
  shift
done

case "$PROFILE" in
  all) pattern="sj-*" ;;
  core) pattern="sj-core-*" ;;
  product) pattern="sj-product-*" ;;
  ive) pattern="sj-ive-*" ;;
  story) pattern="sj-story-*" ;;
  people) pattern="sj-people-*" ;;
  strategy) pattern="sj-strategy-*" ;;
  learning) pattern="sj-learning-*" ;;
  anti|anti-patterns) pattern="sj-anti-*" ;;
  *)
    echo "Unknown profile: $PROFILE" >&2
    usage >&2
    exit 2
    ;;
esac

if [ "$MODE" = "copy" ]; then
  "$ROOT/scripts/copy-skills.sh" "$TARGET_DIR" "$pattern"
else
  "$ROOT/scripts/link-skills.sh" "$TARGET_DIR" "$pattern"
fi

echo "Installed profile '$PROFILE' ($pattern) into $TARGET_DIR using $MODE mode"
