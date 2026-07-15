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
| README led with `unofficial Codex plugin`, which hid what the package does. | Rewrote the lead around the operating skill pack and moved affiliation language to the disclaimer. |
| No `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, or `CONTEXT.md`. | Added canonical repo instructions, compatibility shims, and a vocabulary file. |
| Runtime skills referenced root `../../references/*` files. | Copied needed references into each skill's own `references/` folder and changed skill instructions to local paths. |
| Install docs were Codex-heavy. | Added a harness matrix, Claude loose-skill instructions, copy mode, skills.sh manifest notes, and update guidance. |
| No copy script for harnesses that do not follow symlinks. | Added `scripts/copy-skills.sh`. |
| No one-command local update flow. | Added `scripts/update-local.sh`. |
| No Claude-style manifest or skills.sh-style catalog. | Added `.claude-plugin/plugin.json` and `skills.sh.json`. |
| Validation did not catch non-local runtime references or missing public repo files. | Expanded `scripts/validate.sh` checks. |
| No privacy/security/changelog docs. | Added `PRIVACY.md`, `SECURITY.md`, and `CHANGELOG.md`. |
| `$sj-core-compound-learning` named compounding but did not define durable storage, approval, duplicate checks, or refresh. | Added `docs/MEMORY_AND_LOGS.md`, `templates/sj-learning.md`, upgraded capture rules, and `$sj-core-learning-refresh`. |
| No explicit closeout, live-test, autoreview, or handoff recipe. | Added `docs/HANDOFF.md` and made it part of validation. |
| The Jony Ive source notes were not represented as first-class runtime skills. | Added a connected `sj-ive-*` design studio layer and `references/sj-ive-design-studio.md`. |
| Most leaf skills in a family shared the same workflow and output labels. | Rewrote every leaf into a skill-specific procedure and added a validator requiring 91 unique workflow/output contracts. |
| All 91 skills were implicitly invokable, which inflated global skill context. | Kept only `$sj-core-catalog` implicit and made the 90 leaf skills explicit by name. |
| UI prompts were generic and did not demonstrate the skill. | Synchronized every `agents/openai.yaml` default prompt with the skill's concrete example prompt. |
| The source map listed titles but did not connect claims to skills. | Added 15 source IDs, 91 claim IDs, evidence levels, and a complete `sj-evidence-map.md`. |
| Validation proved structure but not behavioral contract depth. | Added 182 per-skill cases, 18 ambiguous router cases, a source-blind behavior contract, and semantic drift checks. |

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
| Runtime skills | 91 |
| Root maintainer references | 10 |
| Skill-local reference copies | Created for every referenced runtime file |
| Native Codex manifest | `.codex-plugin/plugin.json` |
| Claude-style manifest | `.claude-plugin/plugin.json` |
| Grouped catalog | `skills.sh.json` |
| Local marketplace | `.agents/plugins/marketplace.json` |
| Install scripts | `install-local.sh`, `link-skills.sh`, `copy-skills.sh`, `update-local.sh` |
| Closeout and handoff | `docs/HANDOFF.md` |
| Provenance | 15 sources, 91 claim mappings, and self-contained local evidence maps |
| Invocation policy | One implicit router and 90 explicit leaf skills |
| Behavior dataset | 182 skill cases and 18 router cases |
| Validation | Structural, semantic, provenance, metadata, dataset, inventory, and optional Codex authoring validators |
