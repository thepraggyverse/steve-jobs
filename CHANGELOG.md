# Changelog

## Unreleased

- Nothing yet.

## 0.3.0 - 2026-07-15

- Replaced shared family templates with 91 distinct workflow and output contracts.
- Added stable claim IDs, 15 source IDs, evidence levels, a complete evidence map, and self-contained local provenance files for every skill.
- Made `$sj-core-catalog` the only implicitly invokable skill while keeping all 90 leaf skills explicitly invokable.
- Replaced generic UI prompts with each skill's concrete example prompt and enforced 25-64 character metadata descriptions.
- Added 182 generated behavior cases, 18 ambiguous router cases, a source-blind behavior contract, and strict semantic validation.
- Added source, metadata, and behavior synchronization tools with drift checks in `scripts/validate.sh`.
- Corrected native Codex examples to use the `$steve-jobs:sj-*` plugin namespace and made live install proof fail closed when a skill does not load.
- Added a source-blind live router checker that evaluates all 18 ambiguous routing fixtures against hidden expected primaries.
- Completed the Claude plugin manifest with version, description, author, homepage, repository, and license metadata.
- Expanded installation, architecture, development, audit, behavior-testing, and handoff documentation for the deeper runtime contract.

## 0.2.0 - 2026-06-30

- Bumped the Codex plugin version to `0.2.0`.
- Added `scripts/list-skills.sh`, `scripts/install-profile.sh`, `scripts/unlink-skills.sh`, and `scripts/check-inventory.sh`.
- Added `docs/WHEN_TO_USE_WHAT.md` for choosing between product, Ive, story, people, strategy, learning, and anti-pattern skills.
- Hardened CI with shell syntax validation and optional ShellCheck.
- Added `scripts/check-install.sh` for source validation, local plugin visibility, installed-cache validation, optional refresh, and optional live smoke testing.
- Added `docs/PLAYBOOKS.md` with practical skill chains and profile install guidance.
- Added a README start-here flow for using the pack as a router-driven operating system.
- Added 10 `sj-ive-*` skills for Jony Ive design studio practice: design story, humanizing technology, first-touch moments, prototype volume, material honesty, manufacturing as design, care, novelty discipline, fragile idea protection, and future-without-betrayal transitions.
- Added `references/sj-ive-design-studio.md`, expanded the source map with the Jony Ive notes, and connected the new skills through the README, skill reference, catalogs, manifests, installer docs, validator, and handoff checklist.
- Added the SJ memory and logging system, including durable learning guidance, a learning template, and `$sj-core-learning-refresh`.
- Upgraded `$sj-core-compound-learning` with approval, duplicate-checking, source-safety, and durable learning rules.
- Added closeout documentation for installed-plugin validation, live `codex exec` proof, autoreview, and handoff.

## 0.1.0

- Created 80 `sj-*` operating skills across core, product, story, people, strategy, learning, and anti-pattern groups.
- Added Codex plugin metadata, repo marketplace metadata, local install scripts, symlink install support, copy install support, and validation.
- Added public-safe reference notes derived from Steve Jobs books, interviews, and podcast notes without including source texts or long excerpts.
- Added cross-harness documentation, skill-local references, and compatibility manifests for loose skill installs.
