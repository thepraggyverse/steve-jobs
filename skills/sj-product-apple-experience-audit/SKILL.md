---
name: sj-product-apple-experience-audit
description: "Audit every touchpoint as a trust deposit or withdrawal. Use when reviewing customer support, onboarding, purchase, install, trial, docs, error states, packaging, retail, or any end-to-end experience."
---

# Apple Experience audit

## Core Move

Audit every touchpoint as a trust deposit or withdrawal.

## Workflow

1. Map the journey from discovery through purchase, setup, use, failure, support, and return.
2. Record the user's expectation and the product signal at each relevant touchpoint.
3. Mark trust deposits, trust withdrawals, broken handoffs, and contradictory promises.
4. Prioritize withdrawals by severity, frequency, and recoverability.
5. Assign one repair, owner, and observable proof for the highest-risk touchpoint.

## Read References

- Read `references/sj-product-craft.md` when this skill needs source grounding or deeper examples.
- Read `references/sj-anti-patterns.md` when this skill needs source grounding or deeper examples.

## Source Grounding

- Claim: `SJ-P11`
- Sources: `S02`, `S03`, `S07`
- Evidence level: `synthesized`
- Resolve IDs in `references/sj-source-map.md` and the claim row in `references/sj-evidence-map.md`.

## Output

Return a compact result with:

- Journey segment
- Trust deposits
- Trust withdrawals
- Broken handoffs
- Priority repair and proof

## Guardrails

- Review the whole journey, not only the polished happy path.
- Separate observed touchpoints from assumed ones.
- Do not use long quotations from the source material.
- Do not call delight a repair when reliability or clarity is broken.

## Example Prompt

Use $sj-product-apple-experience-audit to review this signup-to-first-value path.
