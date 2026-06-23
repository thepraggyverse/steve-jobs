#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd -P)"
PLUGIN_ID="${PLUGIN_ID:-steve-jobs@personal}"
CODEX_HOME_DIR="${CODEX_HOME:-$HOME/.codex}"
RUN_REFRESH=0
RUN_LIVE=0

usage() {
  cat <<'EOF'
Usage: scripts/check-install.sh [--refresh] [--live]

Checks the Steve Jobs plugin source tree, local Codex install, installed cache,
and optional live skill loading.

Options:
  --refresh  Run install-local.sh, remove the old local plugin cache, and add it again.
  --live     Run a read-only codex exec smoke test against a temporary project.
  -h, --help Show this help.
EOF
}

while [ "$#" -gt 0 ]; do
  case "$1" in
    --refresh)
      RUN_REFRESH=1
      ;;
    --live)
      RUN_LIVE=1
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Unknown argument: $1" >&2
      usage >&2
      exit 2
      ;;
  esac
  shift
done

version="$(python3 - "$ROOT/.codex-plugin/plugin.json" <<'PY'
import json
import sys
from pathlib import Path

print(json.loads(Path(sys.argv[1]).read_text())["version"])
PY
)"
cache_path="$CODEX_HOME_DIR/plugins/cache/personal/steve-jobs/$version"

echo "== Source validation =="
"$ROOT/scripts/validate.sh"

source_skills="$(find "$ROOT/skills" -mindepth 1 -maxdepth 1 -type d -name 'sj-*' | wc -l | tr -d ' ')"
source_refs="$(find "$ROOT/references" -maxdepth 1 -type f -name 'sj-*.md' | wc -l | tr -d ' ')"
echo "source skills: $source_skills"
echo "source root references: $source_refs"

if [ "$RUN_REFRESH" -eq 1 ]; then
  echo
  echo "== Refreshing local plugin install =="
  "$ROOT/scripts/install-local.sh"
  codex plugin remove "$PLUGIN_ID" --json >/dev/null 2>&1 || true
  codex plugin add "$PLUGIN_ID" --json
fi

echo
echo "== Plugin list =="
plugin_list="$(codex plugin list)"
printf '%s\n' "$plugin_list" | rg 'steve-jobs@personal|PLUGIN|Marketplace `personal`' -C 2 || true
if ! printf '%s\n' "$plugin_list" | awk -v plugin_id="$PLUGIN_ID" '
  $1 == plugin_id && $2 == "installed," && $3 == "enabled" { found = 1 }
  END { exit found ? 0 : 1 }
'; then
  echo "ERROR: $PLUGIN_ID is not installed and enabled in codex plugin list." >&2
  echo "Try: $ROOT/scripts/check-install.sh --refresh" >&2
  exit 1
fi

echo
echo "== Installed cache validation =="
if [ ! -d "$cache_path" ]; then
  echo "ERROR: expected installed cache missing: $cache_path" >&2
  echo "Try: $ROOT/scripts/check-install.sh --refresh" >&2
  exit 1
fi

"$cache_path/scripts/validate.sh"
cache_skills="$(find "$cache_path/skills" -mindepth 1 -maxdepth 1 -type d -name 'sj-*' | wc -l | tr -d ' ')"
cache_refs="$(find "$cache_path/references" -maxdepth 1 -type f -name 'sj-*.md' | wc -l | tr -d ' ')"
echo "cache path: $cache_path"
echo "cache skills: $cache_skills"
echo "cache root references: $cache_refs"

if [ "$cache_skills" != "$source_skills" ]; then
  echo "ERROR: source/cache skill count mismatch: source=$source_skills cache=$cache_skills" >&2
  exit 1
fi

if [ "$cache_refs" != "$source_refs" ]; then
  echo "ERROR: source/cache reference count mismatch: source=$source_refs cache=$cache_refs" >&2
  exit 1
fi

if [ ! -f "$cache_path/skills/sj-ive-humanize-technology/SKILL.md" ]; then
  echo "ERROR: installed cache is missing sj-ive-humanize-technology." >&2
  exit 1
fi

if [ "$RUN_LIVE" -eq 1 ]; then
  echo
  echo "== Live read-only smoke test =="
  tmp_dir="$(mktemp -d /tmp/steve-jobs-check-install.XXXXXX)"
  output_path="$tmp_dir/output.txt"
  printf '# Live smoke test\n\nAn AI settings page feels cold, dense, and full of jargon.\n' > "$tmp_dir/README.md"
  codex exec --ephemeral --skip-git-repo-check \
    -C "$tmp_dir" \
    -s read-only \
    -o "$output_path" \
    'Use $sj-ive-humanize-technology. Clean install smoke test. Do not modify files. Review README.md and return: skill loaded, artifact reviewed, cold points, human feeling, suggested changes, and no files modified.'
  sed -n '1,220p' "$output_path"
fi

echo
echo "Install check passed"
