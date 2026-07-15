# Behavior Testing

The behavior system turns each skill's prose into a checkable contract.

## Coverage

| Dataset | Count | What it proves |
|---|---|---|
| `tests/behavior-cases.json` | 182 | One representative and one missing-evidence boundary case for each of 91 skills. |
| `tests/router-cases.json` | 18 | Ambiguous prompts have an expected primary route and optional follow-ups. |
| `tests/BEHAVIOR_CONTRACT.md` | 1 contract | User-visible pass, failure, read-only, provenance, and anti-imitation rules. |

Every per-skill case stores the stable claim ID, exact output fields, and exact forbidden behaviors from `SKILL.md`.
`scripts/build-behavior-cases.py --check` fails when any generated case drifts.
`scripts/check-skill-quality.py` independently checks counts, modes, claim links, output links, and guardrail links.

## Local Proof

```bash
./scripts/validate.sh
./scripts/check-install.sh --refresh
./scripts/check-install.sh --live
./scripts/check-router-live.sh
git diff --check
```

The first command covers all 182 deterministic contracts and all 18 router declarations.
The live command exercises a leaf skill through the installed Codex cache in a temporary read-only project.
It uses the native plugin namespace `$steve-jobs:sj-*` and fails unless the response explicitly confirms both skill loading and no file modification.
The router script removes expected answers from the fixture shown to Codex, exercises all 18 prompts through the installed namespaced catalog, and compares the returned primary routes with the hidden expected values.

## Router Live Suite

When Codex CLI is available, run `./scripts/check-router-live.sh`.
It asks `$steve-jobs:sj-core-catalog` to choose one primary route for every case.
For a manual spot check, ask the catalog to return only:

```text
Selected skill sequence
Why this sequence
First action
References to inspect
```

The primary route must match `expected_primary`.
An extra follow-up is acceptable only when it is declared or justified by a new fact in the fixture.

## Source-Blind Review

For final behavior validation, give the reviewer `tests/BEHAVIOR_CONTRACT.md` and the user-visible install and validation commands.
Do not explain the implementation or point the reviewer toward expected source-code branches.
Classify each requirement as pass, fail, blocked, or out of scope.
Missing harness executables are blocked coverage, not a passing claim and not a plugin failure.

## Adding Or Changing A Skill

1. Write a distinct workflow, output, and at least three guardrails.
2. Add or update source grounding.
3. Synchronize metadata and behavior cases.
4. Add an ambiguous router case when routing overlap is materially new.
5. Run validation, install proof, live proof, and autoreview.
