---
name: sj-product-customer-backwards
description: "Start from the user experience and work back to technology. Use when a proposal starts with technology, implementation, model choice, architecture, or features before naming the customer experience."
---

# Customer backwards

## Core Move

Start from the user experience and work back to technology.

## Workflow

1. Identify the specific user, moment, and progress they are trying to make.
2. Describe the ideal experience without naming implementation or technology.
3. Define the trust, speed, clarity, and emotional conditions that experience requires.
4. Work backward into capabilities, data, architecture, and operational constraints.
5. Sequence the smallest technology proof that can validate the experience.

## Read References

- Read `references/sj-product-craft.md` when this skill needs source grounding or deeper examples.
- Read `references/sj-anti-patterns.md` when this skill needs source grounding or deeper examples.

## Source Grounding

- Claim: `SJ-P02`
- Sources: `S01`, `S02`, `S07`
- Evidence level: `synthesized`
- Resolve IDs in `references/sj-source-map.md` and the claim row in `references/sj-evidence-map.md`.

## Output

Return a compact result with:

- User and moment
- Ideal experience
- Experience conditions
- Required capabilities
- First technology proof

## Guardrails

- Do not smuggle the preferred implementation into the experience statement.
- Distinguish a user request from the underlying progress they need.
- Do not use long quotations from the source material.
- Preserve feasibility constraints without letting them define the starting point.

## Example Prompt

Use $sj-product-customer-backwards to reframe this feature from the user experience back.
