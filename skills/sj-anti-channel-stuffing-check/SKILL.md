---
name: sj-anti-channel-stuffing-check
description: "Separate real traction from fake comfort. Use when sales, usage, metrics, revenue, inventory, or pipeline might be inflated, pulled forward, or misread as demand."
---

# Channel stuffing check

## Core Move

Separate real traction from fake comfort.

## Workflow

1. Reconcile sell-in, sell-through, inventory, returns, discounts, receivables, and end-customer activation by period and channel.
2. Identify where incentives allow revenue or growth to be pulled forward without real demand.
3. Stress-test reported performance after normalizing shipment timing, partner inventory, cancellations, and collection risk.
4. Require owner explanations and independent evidence for anomalies before using the numbers in decisions.
5. Correct forecasts, disclosures, incentives, and channel practices, then monitor the next clean period.

## Read References

- Read `references/sj-anti-patterns.md` when this skill needs source grounding or deeper examples.
- Read `references/sj-strategy-failure.md` when this skill needs source grounding or deeper examples.

## Source Grounding

- Claim: `SJ-A02`
- Sources: `S04`, `S05`
- Evidence level: `counterexample`
- Resolve IDs in `references/sj-source-map.md` and the claim row in `references/sj-evidence-map.md`.

## Output

Return a compact result with:

- Channel reconciliation
- Incentive risks
- Normalized performance
- Anomaly evidence
- Corrections and monitoring

## Guardrails

- Treat this as an integrity and accounting risk, not merely a sales tactic.
- Escalate suspected fraud or disclosure failures to qualified legal and finance professionals.
- Do not accuse individuals without evidence and due process.

## Example Prompt

Use $sj-anti-channel-stuffing-check to audit these growth numbers.
