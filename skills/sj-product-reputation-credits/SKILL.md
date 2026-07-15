---
name: sj-product-reputation-credits
description: "Treat each interaction as adding or withdrawing trust. Use when auditing quality, support, onboarding, performance, reliability, messaging, or any customer contact point."
---

# Reputation credits

## Core Move

Treat each interaction as adding or withdrawing trust.

## Workflow

1. Enumerate the interactions where the product makes or breaks a promise.
2. Assign each interaction a trust deposit, neutral effect, or withdrawal with evidence.
3. Identify repeated small withdrawals and rare catastrophic ones.
4. Choose the repair that restores the most trust without making a new promise the system cannot keep.
5. Define a behavioral or operational signal that shows reputation is recovering.

## Read References

- Read `references/sj-product-craft.md` when this skill needs source grounding or deeper examples.
- Read `references/sj-anti-patterns.md` when this skill needs source grounding or deeper examples.

## Source Grounding

- Claim: `SJ-P19`
- Sources: `S04`, `S05`, `S07`
- Evidence level: `synthesized`
- Resolve IDs in `references/sj-source-map.md` and the claim row in `references/sj-evidence-map.md`.

## Output

Return a compact result with:

- Promise under review
- Trust ledger
- Cumulative withdrawals
- Reputation repair
- Recovery signal

## Guardrails

- Do not treat branding as a substitute for reliable behavior.
- Weight broken high-stakes promises more than cosmetic defects.
- Do not use long quotations from the source material.
- Avoid promising recovery before the repair is proven.

## Example Prompt

Use $sj-product-reputation-credits to find trust deposits and withdrawals in this flow.
