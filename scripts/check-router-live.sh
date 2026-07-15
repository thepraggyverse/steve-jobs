#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd -P)"
tmp_dir="$(mktemp -d /tmp/steve-jobs-router-live.XXXXXX)"
output_path="$tmp_dir/output.txt"
trap 'rm -rf "$tmp_dir"' EXIT

python3 - "$ROOT/tests/router-cases.json" "$tmp_dir/router-prompts.json" <<'PY'
import json
import sys
from pathlib import Path

source = json.loads(Path(sys.argv[1]).read_text())
prompts = [{"id": case["id"], "prompt": case["prompt"]} for case in source["cases"]]
Path(sys.argv[2]).write_text(json.dumps(prompts, indent=2) + "\n")
PY

# shellcheck disable=SC2016 # The namespaced skill token is a literal invocation.
prompt='Use $steve-jobs:sj-core-catalog. This is a read-only router behavior test. Read router-prompts.json. For every case, choose the single best primary skill. Return exactly one plain line per case in the form case-id=sj-skill-name, with no bullets, table, dollar sign, namespace, explanation, or extra line. Do not modify files.'

codex exec --ephemeral --skip-git-repo-check \
  -C "$tmp_dir" \
  -s read-only \
  -o "$output_path" \
  "$prompt"

python3 - "$ROOT/tests/router-cases.json" "$output_path" <<'PY'
import json
import re
import sys
from pathlib import Path

expected_data = json.loads(Path(sys.argv[1]).read_text())
expected = {case["id"]: case["expected_primary"] for case in expected_data["cases"]}
actual = {}
errors = []
for line in Path(sys.argv[2]).read_text().splitlines():
    value = line.strip()
    if not value:
        errors.append("unexpected blank output line")
        continue
    match = re.fullmatch(r"([a-z0-9-]+)=(sj-[a-z0-9-]+)", value)
    if not match:
        errors.append(f"unexpected output line: {value}")
        continue
    case_id, skill = match.groups()
    if case_id in actual:
        errors.append(f"duplicate route: {case_id}")
        continue
    actual[case_id] = skill

if len(actual) != len(expected):
    errors.append(f"route count mismatch: expected {len(expected)}, got {len(actual)}")
for case_id, skill in expected.items():
    if case_id not in actual:
        errors.append(f"missing route: {case_id}")
    elif actual[case_id] != skill:
        errors.append(f"{case_id}: expected {skill}, got {actual[case_id]}")
for case_id in actual:
    if case_id not in expected:
        errors.append(f"unexpected route: {case_id}")

if errors:
    print("Router live check failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print(f"Router live check passed: {len(expected)} cases")
PY
