---
name: sj-product-concrete-artifact-review
description: "Force decisions around visible work rather than ideas. Use when the conversation is stuck in hypotheticals and needs a screen, draft, prototype, patch, diagram, or demo."
---

# Concrete artifact review

## Core Move

Force decisions around visible work rather than ideas.

## Workflow

1. Require the smallest real artifact that exposes the disputed decision.
2. Separate direct observations from interpretations and missing evidence.
3. Walk the artifact in the order a user, operator, or builder encounters it.
4. Make decisions against visible details, not imagined future quality.
5. Specify the changed artifact that must return for the next review.

## Read References

- Read `references/sj-product-craft.md` when this skill needs source grounding or deeper examples.
- Read `references/sj-anti-patterns.md` when this skill needs source grounding or deeper examples.

## Source Grounding

- Claim: `SJ-P23`
- Sources: `S03`, `S07`, `S14`
- Evidence level: `synthesized`
- Resolve IDs in `references/sj-source-map.md` and the claim row in `references/sj-evidence-map.md`.

## Output

Return a compact result with:

- Artifact inspected
- Direct observations
- Assumptions and gaps
- Decisions made
- Required next version

## Guardrails

- Do not accept a deck or description when the real artifact can be inspected.
- Do not turn preference into an observation.
- Do not use long quotations from the source material.
- End with a versioned artifact, not an open-ended discussion.

## Example Prompt

Use $sj-product-concrete-artifact-review to critique this artifact instead of the idea.
