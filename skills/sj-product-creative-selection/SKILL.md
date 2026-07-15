---
name: sj-product-creative-selection
description: "Run a concrete demo-driven iteration loop. Use when a product, feature, interface, prototype, pitch, or design needs artifact-based review instead of abstract discussion."
---

# Creative selection

## Core Move

Run a concrete demo-driven iteration loop.

## Workflow

1. Name the decision that cannot be resolved through discussion alone.
2. Create or request contrasting variants that each test a distinct bet.
3. Define selection criteria tied to the user job, product story, and technical truth.
4. Compare variants side by side and record what each reveals.
5. Select, combine, or reject variants and set the next demo threshold.

## Read References

- Read `references/sj-product-craft.md` when this skill needs source grounding or deeper examples.
- Read `references/sj-anti-patterns.md` when this skill needs source grounding or deeper examples.

## Source Grounding

- Claim: `SJ-P22`
- Sources: `S03`, `S10`, `S14`
- Evidence level: `synthesized`
- Resolve IDs in `references/sj-source-map.md` and the claim row in `references/sj-evidence-map.md`.

## Output

Return a compact result with:

- Decision under review
- Variant set
- Selection criteria
- Comparison findings
- Selection and next demo

## Guardrails

- Each variant must test a meaningfully different choice.
- Do not let authorship determine selection.
- Do not use long quotations from the source material.
- Stop generating variants once the decision is visible.

## Example Prompt

Use $sj-product-creative-selection to run the next demo review for this prototype.
