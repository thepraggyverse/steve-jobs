---
name: sj-story-number-context
description: "Make numbers vivid and meaningful. Use when metrics, specs, performance claims, market sizes, pricing, or comparisons need context people can feel."
---

# Number context

## Core Move

Make numbers vivid and meaningful.

## Workflow

1. List every number, its unit, period, population, source, and comparison baseline.
2. Choose the human-scale denominator or familiar reference that makes magnitude interpretable.
3. Explain what changed, why it matters, and what the number cannot establish.
4. Remove vanity metrics, mixed denominators, cherry-picked windows, and false precision.
5. Write one sentence per surviving number and verify it against the underlying source.

## Read References

- Read `references/sj-story-selling.md` when this skill needs source grounding or deeper examples.
- Read `references/sj-product-craft.md` when this skill needs source grounding or deeper examples.

## Source Grounding

- Claim: `SJ-ST04`
- Sources: `S06`, `S07`
- Evidence level: `synthesized`
- Resolve IDs in `references/sj-source-map.md` and the claim row in `references/sj-evidence-map.md`.

## Output

Return a compact result with:

- Verified numbers
- Baselines and denominators
- Human-scale context
- Limits
- Final number story

## Guardrails

- Never compare values with different units or time windows without saying so.
- Do not turn correlation into causation.
- A large number without a decision-relevant baseline should be removed.

## Example Prompt

Use $sj-story-number-context to explain these benchmark numbers.
