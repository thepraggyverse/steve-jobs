---
name: sj-product-skepticism-hierarchy
description: "Sort objections by signal, source, and importance. Use when feedback conflicts, critics disagree, or a product team needs to know which objections matter."
---

# Skepticism hierarchy

## Core Move

Sort objections by signal, source, and importance.

## Workflow

1. Normalize each objection into a falsifiable claim about the artifact or outcome.
2. Record the source's proximity, expertise, incentives, evidence, and affected user segment.
3. Score signal strength, consequence if true, reversibility, and cost to test.
4. Rank objections as act now, test, monitor, or consciously ignore.
5. Assign one resolving artifact or experiment to every high-priority objection.

## Read References

- Read `references/sj-product-craft.md` when this skill needs source grounding or deeper examples.
- Read `references/sj-anti-patterns.md` when this skill needs source grounding or deeper examples.

## Source Grounding

- Claim: `SJ-P20`
- Sources: `S01`, `S03`, `S08`
- Evidence level: `synthesized`
- Resolve IDs in `references/sj-source-map.md` and the claim row in `references/sj-evidence-map.md`.

## Output

Return a compact result with:

- Normalized objections
- Source and evidence assessment
- Signal and consequence ranking
- Act, test, monitor, or ignore decision
- Resolving proof

## Guardrails

- Do not equate status, confidence, or volume with signal.
- Customer evidence can be important without being universal.
- Do not use long quotations from the source material.
- Preserve minority objections when their consequence is severe.

## Example Prompt

Use $sj-product-skepticism-hierarchy to triage this feedback.
