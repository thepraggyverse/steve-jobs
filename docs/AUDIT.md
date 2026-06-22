# Reference Audit

This repo was audited against the current public shape of these projects and docs:

| Source | What it contributed |
|---|---|
| [Every compound engineering guide](https://every.to/guides/compound-engineering) | The loop idea: ideate, plan, work, review, polish, compound, and make the system remember useful lessons. |
| [EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin) | Multi-harness manifests, `AGENTS.md` as canonical repo instructions, strict validation, install/update docs, and self-contained skill references. |
| [mattpocock/skills](https://github.com/mattpocock/skills) | Small composable skills, clear invocation thinking, bucketed skill lists, and simple link scripts. |
| [EveryInc/compound-knowledge-plugin](https://github.com/EveryInc/compound-knowledge-plugin) | Knowledge-work loop docs, README/AGENTS/SECURITY/PRIVACY coverage, and the brainstorm -> plan -> review -> learn pattern. |
| [steipete/agent-scripts skills](https://github.com/steipete/agent-scripts/tree/main/skills) | Global setup thinking, skill validation, symlink workflows, and broad harness hygiene. |

## Gaps Found In This Repo

| Gap | Fix |
|---|---|
| README led with `unofficial Codex plugin`, which hid what the package does. | Rewrote the lead around 80 operating skills and moved affiliation language to the disclaimer. |
| No `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, or `CONTEXT.md`. | Added canonical repo instructions, compatibility shims, and a vocabulary file. |
| Runtime skills referenced root `../../references/*` files. | Copied needed references into each skill's own `references/` folder and changed skill instructions to local paths. |
| Install docs were Codex-heavy. | Added a harness matrix, Claude loose-skill instructions, copy mode, skills.sh manifest notes, and update guidance. |
| No copy script for harnesses that do not follow symlinks. | Added `scripts/copy-skills.sh`. |
| No one-command local update flow. | Added `scripts/update-local.sh`. |
| No Claude-style manifest or skills.sh-style catalog. | Added `.claude-plugin/plugin.json` and `skills.sh.json`. |
| Validation did not catch non-local runtime references or missing public repo files. | Expanded `scripts/validate.sh` checks. |
| No privacy/security/changelog docs. | Added `PRIVACY.md`, `SECURITY.md`, and `CHANGELOG.md`. |

## What Was Intentionally Not Added

| Not added | Reason |
|---|---|
| Dozens of specialist subagents | This package is an operating-skill pack, not a full engineering automation system. The useful unit is the `sj-*` skill. |
| A native manifest for every harness | Native plugin schemas differ and can drift. The repo ships portable skill folders plus currently useful manifests instead of guessing unstable formats. |
| Source books, transcripts, or long excerpts | Public safety and copyright boundaries. The repo keeps paraphrased operating references only. |
| Automatic shell actions inside skills | The SJ skills are judgment workflows; they should inspect artifacts and produce useful outputs without relying on harness-specific script execution. |

## Current Shape

| Surface | Count or status |
|---|---|
| Runtime skills | 80 |
| Root maintainer references | 8 |
| Skill-local reference copies | Created for every referenced runtime file |
| Native Codex manifest | `.codex-plugin/plugin.json` |
| Claude-style manifest | `.claude-plugin/plugin.json` |
| Grouped catalog | `skills.sh.json` |
| Local marketplace | `.agents/plugins/marketplace.json` |
| Install scripts | `install-local.sh`, `link-skills.sh`, `copy-skills.sh`, `update-local.sh` |
| Validation | `scripts/validate.sh` plus optional Codex authoring validators |
