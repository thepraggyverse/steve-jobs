# Handoff And Live Test

Use this document when preparing a release, passing the repo to another agent, or proving that the installed plugin works in a fresh harness.

## Current Package Contract

| Surface | Expected state |
|---|---|
| Skill count | 91 `sj-*` runtime skills |
| Root references | 9 `references/sj-*.md` maintainer files |
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
git diff --check
codex plugin list | rg 'steve-jobs@personal|PLUGIN|Marketplace `personal`' -C 2
```

For a local Codex plugin install:

```bash
./scripts/install-local.sh
codex plugin add steve-jobs@personal --json
"$HOME/.codex/plugins/cache/personal/steve-jobs/0.1.0/scripts/validate.sh"
```

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
  'Use $sj-core-learning-refresh. Clean plugin-only live install test. Do not modify files. Audit saved SJ learnings in the current project. Return a compact report with: Skill loaded, learning store path, files reviewed, findings, and next prompt.'
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
- installed cache validate: <result>
- live codex exec test: <result>
- autoreview: <result>

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
| `chatgpt-apps@openai-curated` not installed | Stale external plugin/cache state. | Ignore for SJ validation unless it blocks Codex startup. |
| `compound-engineering` marketplace path warning | External marketplace metadata issue. | Ignore for SJ validation unless testing that plugin. |
| Cloudflare MCP `Auth required` | External MCP credential issue. | Ignore for SJ validation unless testing Cloudflare tools. |
| `TERM=dumb` in `codex doctor` | Non-interactive shell lacks terminal capabilities. | Ignore for non-interactive validation. |

If `steve-jobs@personal` is not `installed, enabled`, or the installed cache validator fails, treat that as a package/install issue and fix before handoff.
