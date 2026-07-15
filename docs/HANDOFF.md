# Handoff And Live Test

Use this document when preparing a release, passing the repo to another agent, or proving that the installed plugin works in a fresh harness.

## Current Package Contract

| Surface | Expected state |
|---|---|
| Skill count | 91 `sj-*` runtime skills |
| Root references | 10 `references/sj-*.md` maintainer files |
| Skill contracts | 91 unique workflow/output pairs |
| Source traceability | 15 source IDs and 91 claim mappings |
| Invocation policy | `$sj-core-catalog` implicit; 90 leaf skills explicit |
| Behavior coverage | 182 skill cases and 18 ambiguous router cases |
| Native Codex plugin | `.codex-plugin/plugin.json` points at `./skills/` |
| Claude-style manifest | `.claude-plugin/plugin.json` lists every `./skills/sj-*` folder |
| skills.sh catalog | `skills.sh.json` lists every skill exactly once |
| Memory policy | `docs/MEMORY_AND_LOGS.md` and `templates/sj-learning.md` define durable learning capture |
| Local install | `scripts/install-local.sh` registers `steve-jobs@personal` |
| Loose skill install | `scripts/link-skills.sh` or `scripts/copy-skills.sh` installs portable skill folders |

## Closeout Checklist

Run these from the repository root:

```bash
./scripts/validate.sh
./scripts/check-inventory.sh
git diff --check
./scripts/check-install.sh --refresh
./scripts/check-router-live.sh
codex plugin list | rg 'steve-jobs@personal|PLUGIN|Marketplace `personal`' -C 2
```

For a local Codex plugin install:

```bash
./scripts/install-local.sh
codex plugin add steve-jobs@personal --json
"$HOME/.codex/plugins/cache/personal/steve-jobs/0.3.0/scripts/validate.sh"
```

For the current plugin version, prefer:

```bash
./scripts/check-install.sh --refresh --live
```

The full acceptance contract is in `tests/BEHAVIOR_CONTRACT.md`.
The deterministic behavior and routing checks run inside `./scripts/validate.sh`.

If the installed cache is stale after a same-version local change, refresh it:

```bash
codex plugin remove steve-jobs@personal --json
codex plugin add steve-jobs@personal --json
```

For a clean plugin-only live test, avoid writing output inside the test project:

```bash
rm -rf /tmp/steve-jobs-live-clean
mkdir -p /tmp/steve-jobs-live-clean
printf '# Clean live test project\n' > /tmp/steve-jobs-live-clean/README.md

codex exec --ephemeral --skip-git-repo-check \
  -C /tmp/steve-jobs-live-clean \
  -s read-only \
  -o /tmp/steve-jobs-live-clean-output.txt \
  'Use $steve-jobs:sj-core-learning-refresh. Clean plugin-only live install test. Do not modify files. Audit saved SJ learnings in the current project. Begin with exactly "Skill loaded: yes" and finish with exactly "No files modified."'
```

Expected result:

```text
Skill loaded: sj-core-learning-refresh
Learning store path: /tmp/steve-jobs-live-clean/docs/steve-jobs/learnings/
Files reviewed: README.md; no SJ learning files found.
Findings: learning store directory is missing, so no saved SJ learnings are available to audit.
No files modified.
```

## Autoreview

Run autoreview after non-trivial skill, manifest, script, or documentation changes:

```bash
$HOME/.agents/skills/autoreview/scripts/autoreview \
  --mode local \
  --parallel-tests './scripts/validate.sh'
```

If autoreview reports an actionable finding, verify it against the actual files, fix only in-scope issues, rerun validation, and rerun autoreview.

## Handoff Summary Template

Use this shape when another agent will continue the work:

```text
Repo: /path/to/steve-jobs
Branch: main
Goal:
- <what the user wanted>

Changed:
- <files or surfaces changed>

Installed:
- <plugin install status and cache path>

Verified:
- ./scripts/validate.sh: <result>
- ./scripts/check-inventory.sh: <result>
- installed cache validate: <result>
- live codex exec test: <result>
- live 18-case router test: <result>
- autoreview: <result>
- behavior contract: <result>

Known non-blocking environment warnings:
- <warnings from other plugins, global skill scans, auth, or terminal state>

Next:
- <commit, push, release, or follow-up>
```

## Environment Warning Triage

The following warnings can appear during live `codex exec` tests and are not, by themselves, Steve Jobs plugin failures:

| Warning | Meaning | Action |
|---|---|---|
| `skills scan truncated after 2000 directories` | The global skill directories are very large. | Prefer native plugin install over duplicate loose `sj-*` links. |
| Global implicit skill description budget exceeded | Too many unrelated plugins expose implicit skills. | The SJ plugin exposes only `$sj-core-catalog` implicitly; remove stale duplicate loose links if the warning persists. |
| `chatgpt-apps@openai-curated` not installed | Stale external plugin/cache state. | Ignore for SJ validation unless it blocks Codex startup. |
| `compound-engineering` marketplace path warning | External marketplace metadata issue. | Ignore for SJ validation unless testing that plugin. |
| Cloudflare MCP `Auth required` | External MCP credential issue. | Ignore for SJ validation unless testing Cloudflare tools. |
| `TERM=dumb` in `codex doctor` | Non-interactive shell lacks terminal capabilities. | Ignore for non-interactive validation. |

If `steve-jobs@personal` is not `installed, enabled`, or the installed cache validator fails, treat that as a package/install issue and fix before handoff.
