# Behavior Contract

This contract defines user-visible proof for the Steve Jobs plugin independently of its implementation.

## Interface Under Test

- A compatible harness can install or link the plugin and discover 91 `sj-*` skills.
- `$sj-core-catalog` is the only implicitly invokable skill.
- Every leaf skill remains available through explicit `$sj-*` invocation.
- Native Codex plugin invocation uses `$steve-jobs:sj-*`; loose-skill invocation uses `$sj-*`.
- A skill follows its declared workflow, returns its declared output fields, and respects its guardrails.

## Required Behaviors

1. Inventory surfaces agree on exactly 91 skills in eight groups.
2. Every skill has two dataset cases: one representative positive case and one missing-evidence boundary case.
3. Every case names one claim ID, all declared output fields, and all declared forbidden behaviors.
4. The catalog routes every ambiguous router case to the declared primary skill and may sequence only declared or clearly justified follow-ups.
5. Missing evidence produces explicit assumptions or requests for the artifact, never invented facts or quotations.
6. No response imitates Steve Jobs or Jony Ive as a persona.
7. Read-only live tests do not modify the fixture project.
8. Source IDs resolve locally without exposing the private source corpus.

## Failure Cases

- A generic workflow or output contract is duplicated across differently named leaf skills.
- More than one skill is implicitly invokable.
- UI metadata contains a generic default prompt or drifts from the skill's example prompt.
- A source, claim, skill, manifest, catalog, or behavior case is missing or duplicated.
- A promised output field exists only in documentation and not in the executable skill.
- Installation succeeds from source but the installed cache differs or fails validation.

## Proof Procedure

1. Run `./scripts/validate.sh` for structural, semantic, provenance, metadata, inventory, and dataset checks.
2. Run `./scripts/check-install.sh --refresh` for source-to-cache parity.
3. Run `./scripts/check-install.sh --live` for a read-only explicit leaf-skill smoke test.
4. Run the router live suite documented in `docs/BEHAVIOR_TESTING.md` when a compatible CLI is available.
5. Run local autoreview, verify accepted findings, rerun the affected checks, and record blocked harnesses separately from failures.

The behavior pass must use this contract and the user-visible commands above without inspecting implementation details to invent a passing explanation.
