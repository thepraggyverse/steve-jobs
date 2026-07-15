---
name: sj-product-pixel-polish
description: "Review the artifact at detail level and improve finish. Use when a visual interface, presentation, landing page, demo, or artifact needs detailed polish and exactness."
---

# Pixel polish

## Core Move

Review the artifact at detail level and improve finish.

## Workflow

1. Inspect the rendered artifact at representative sizes, states, and content extremes.
2. Review hierarchy, spacing, type, alignment, color, motion, copy, affordance, and feedback.
3. Record exact defects with location, state, and user consequence.
4. Prioritize defects that break comprehension, coherence, accessibility, or perceived care.
5. Specify before-and-after fixes and the viewports or states to recheck.

## Read References

- Read `references/sj-product-craft.md` when this skill needs source grounding or deeper examples.
- Read `references/sj-anti-patterns.md` when this skill needs source grounding or deeper examples.

## Source Grounding

- Claim: `SJ-P14`
- Sources: `S03`, `S10`, `S15`
- Evidence level: `synthesized`
- Resolve IDs in `references/sj-source-map.md` and the claim row in `references/sj-evidence-map.md`.

## Output

Return a compact result with:

- Surfaces inspected
- Exact polish defects
- User consequence
- Prioritized fixes
- Reinspection matrix

## Guardrails

- Do not polish screenshots while interactive states remain broken.
- Accessibility defects outrank decorative refinements.
- Do not use long quotations from the source material.
- Use stable comparisons so subjective drift is visible.

## Example Prompt

Use $sj-product-pixel-polish to find rough edges in this UI.
