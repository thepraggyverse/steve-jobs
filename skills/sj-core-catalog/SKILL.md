---
name: sj-core-catalog
description: "Choose the right Steve Jobs operating skill and sequence. Use when the user asks for a Jobs lens, Ive design studio lens, simplification, product craft, launch thinking, hiring bar, failure review, or does not know which sj skill to use."
---

# Catalog and router

## Core Move

Choose the right Steve Jobs operating skill and sequence.

## Workflow

1. Identify the user request and the operating domain.
2. Select the smallest useful set of sj skills.
3. Explain the order and why each selected skill applies.
4. Run the selected sequence when the user asked for action.
5. Record any reusable lesson only when it would improve future use.

## Read References

- Read `references/sj-source-map.md` when this skill needs source grounding or deeper examples.
- Read `references/sj-skill-catalog.md` when this skill needs source grounding or deeper examples.

## Routing Notes

- Use `sj-product-*` skills for product direction, simplification, quality bar, usability, and artifact review.
- Use `sj-ive-*` skills for design story, care, first touch, material, prototype selection, manufacturing reality, and modernization without loss of soul.
- Use `sj-story-*`, `sj-people-*`, `sj-strategy-*`, `sj-learning-*`, and `sj-anti-*` when those domains are the main constraint.

## Source Grounding

- Claim: `SJ-C01`
- Sources: `S02`, `S03`, `S04`, `S06`, `S07`, `S08`, `S09`, `S10`, `S13`, `S14`
- Evidence level: `synthesized`
- Resolve IDs in `references/sj-source-map.md` and the claim row in `references/sj-evidence-map.md`.

## Output

Return a compact result with:

- Selected skill sequence
- Why this sequence
- First action
- References to inspect

## Guardrails

- Keep Jobs as a source of operating patterns, not as an imitation costume.
- Prefer concrete artifacts, decisions, tradeoffs, and next actions.
- Do not use long quotations from the source material.
- If evidence is missing, ask for the artifact or state the assumption.

## Example Prompt

Use $sj-core-catalog to choose the best Steve Jobs skill sequence for this product decision.
