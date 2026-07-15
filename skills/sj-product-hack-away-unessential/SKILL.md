---
name: sj-product-hack-away-unessential
description: "Remove anything that does not serve the core experience. Use when a feature list, workflow, roadmap, or design needs pruning, deferral, merging, or sharper tradeoffs."
---

# Hack away unessential

## Core Move

Remove anything that does not serve the core experience.

## Workflow

1. State the core promise and the minimum complete experience that fulfills it.
2. Inventory features, steps, words, states, dependencies, and owners.
3. Classify each item as essential, supporting, mergeable, deferrable, or removable.
4. Remove or merge the highest-cost nonessential items and state the lost option.
5. Re-run the core journey to prove the cuts preserved usefulness and coherence.

## Read References

- Read `references/sj-product-craft.md` when this skill needs source grounding or deeper examples.
- Read `references/sj-anti-patterns.md` when this skill needs source grounding or deeper examples.

## Source Grounding

- Claim: `SJ-P09`
- Sources: `S02`, `S07`, `S09`
- Evidence level: `synthesized`
- Resolve IDs in `references/sj-source-map.md` and the claim row in `references/sj-evidence-map.md`.

## Output

Return a compact result with:

- Core promise
- Essential set
- Merge, defer, and remove list
- Tradeoffs accepted
- Post-cut journey proof

## Guardrails

- Do not remove support that makes the core promise trustworthy.
- Treat maintenance and cognitive cost as real cost.
- Do not use long quotations from the source material.
- Simplicity is a coherent whole, not the smallest feature count.

## Example Prompt

Use $sj-product-hack-away-unessential to cut this roadmap down.
