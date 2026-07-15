---
name: sj-learning-progressive-summarization
description: "Turn books, podcasts, and notes into reusable knowledge. Use when processing reading, transcripts, podcast notes, highlights, or source material into durable summaries and skills."
---

# Progressive summarization

## Core Move

Turn books, podcasts, and notes into reusable knowledge.

## Workflow

1. Bound the source set, record provenance, and state the decision or capability the synthesis should support.
2. Extract atomic observations with enough context to preserve meaning and mark direct evidence versus interpretation.
3. Group observations into recurring claims, contradictions, examples, and open questions while retaining source IDs.
4. Compress only the highest-leverage claims into reusable principles, tests, or skill steps.
5. Run a coverage audit against the source ledger and save the synthesis separately from raw copyrighted material.

## Read References

- Read `references/sj-learning-practice.md` when this skill needs source grounding or deeper examples.
- Read `references/sj-source-map.md` when this skill needs source grounding or deeper examples.

## Source Grounding

- Claim: `SJ-L07`
- Sources: `S02`, `S07`, `S08`
- Evidence level: `synthesized`
- Resolve IDs in `references/sj-source-map.md` and the claim row in `references/sj-evidence-map.md`.

## Output

Return a compact result with:

- Bounded source ledger
- Atomic evidence notes
- Claim and contradiction map
- Reusable compression
- Coverage and provenance audit

## Guardrails

- Do not summarize from highlights alone when full coverage is promised.
- Compression must preserve uncertainty and disagreement.
- Never publish private transcripts, secrets, or long copyrighted excerpts.

## Example Prompt

Use $sj-learning-progressive-summarization to process this book into skill material.
