---
name: sj-product-speed-as-feature
description: "Choose speed or responsiveness as a product rule. Use when performance, latency, waiting, loading, build speed, or workflow drag may be the defining product experience."
---

# Speed as feature

## Core Move

Choose speed or responsiveness as a product rule.

## Workflow

1. Identify the repeated moments where waiting changes user behavior or confidence.
2. Measure or estimate current latency, variability, and perceived delay at each moment.
3. Set an explicit response-time budget tied to the intended feeling.
4. Remove work, precompute, stream, cache, defer, or redesign rather than only adding loading polish.
5. Define a repeatable measurement and the product tradeoff accepted to meet the budget.

## Read References

- Read `references/sj-product-craft.md` when this skill needs source grounding or deeper examples.
- Read `references/sj-anti-patterns.md` when this skill needs source grounding or deeper examples.

## Source Grounding

- Claim: `SJ-P10`
- Sources: `S03`, `S07`, `S09`
- Evidence level: `synthesized`
- Resolve IDs in `references/sj-source-map.md` and the claim row in `references/sj-evidence-map.md`.

## Output

Return a compact result with:

- Critical wait moments
- Current latency and variance
- Speed budget
- Structural speed move
- Measurement and tradeoff

## Guardrails

- Optimize the user's wait, not an irrelevant benchmark.
- Preserve correctness, safety, and trust boundaries.
- Do not use long quotations from the source material.
- Treat perceived speed and actual speed as separate evidence.

## Example Prompt

Use $sj-product-speed-as-feature to find the Safari-speed rule for this product.
