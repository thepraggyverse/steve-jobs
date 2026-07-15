---
name: sj-product-design-is-how-it-works
description: "Judge design by behavior, not surface styling. Use when reviewing UI, UX, product design, service design, or architecture where function and experience matter more than decoration."
---

# Design is how it works

## Core Move

Judge design by behavior, not surface styling.

## Workflow

1. Trace the user-visible behavior from intent through success, failure, and recovery.
2. Identify where visual styling promises behavior the system does not deliver.
3. Inspect affordance, feedback, state, latency, defaults, and error handling.
4. Rewrite the interaction rule so form and behavior express the same idea.
5. Define a task-based test that proves the design works without explanation.

## Read References

- Read `references/sj-product-craft.md` when this skill needs source grounding or deeper examples.
- Read `references/sj-anti-patterns.md` when this skill needs source grounding or deeper examples.

## Source Grounding

- Claim: `SJ-P06`
- Sources: `S02`, `S03`, `S07`
- Evidence level: `synthesized`
- Resolve IDs in `references/sj-source-map.md` and the claim row in `references/sj-evidence-map.md`.

## Output

Return a compact result with:

- User intent
- Behavior trace
- Promise-behavior mismatch
- Revised interaction rule
- Task-based proof

## Guardrails

- Do not grade a functional design from static appearance alone.
- Include failure and recovery states in the design.
- Do not use long quotations from the source material.
- Prefer observed behavior over design rationale.

## Example Prompt

Use $sj-product-design-is-how-it-works to review this dashboard.
