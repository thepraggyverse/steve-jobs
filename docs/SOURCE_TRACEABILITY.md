# Source Traceability

The plugin uses a bounded 15-source corpus without publishing the underlying books or transcripts.
Traceability has three layers.

| Layer | Handle | Location | Purpose |
|---|---|---|---|
| Source | `S01` through `S15` | `references/sj-source-map.md` | Identifies the source title, format, and primary contribution. |
| Claim | `SJ-C01`, `SJ-P01`, and related IDs | `references/sj-evidence-map.md` | Connects one operating claim to one skill and one or more sources. |
| Runtime | `Source Grounding` plus local map slices | `skills/sj-*/` | Carries the claim row, relevant source rows, and evidence level with the portable skill. |

## Evidence Levels

| Level | Meaning |
|---|---|
| `direct` | The source explicitly presents the operating idea or a close paraphrase. |
| `synthesized` | The skill combines multiple episodes or sources into a reusable method. |
| `counterexample` | The source mainly grounds a warning, limitation, or failure check. |

Most skills are deliberately marked `synthesized`.
They are operating methods derived from a corpus, not quotations or claims that Steve Jobs or Jony Ive used the exact five-step procedure.

## Update Procedure

1. Add or revise the source in `references/sj-source-map.md` without copying long source text.
2. Update the relevant mapping in `scripts/sync-source-grounding.py`.
3. Run `./scripts/sync-source-grounding.py` to regenerate the evidence map and portable local copies.
4. Run `./scripts/build-behavior-cases.py` if a claim or skill contract changed.
5. Run `./scripts/validate.sh`.

Use `./scripts/sync-source-grounding.py --check` in CI or review to prove that generated files are current.

## Interpretation Boundary

- A source ID proves bounded provenance, not the historical truth of every interpretation.
- A claim ID gives maintainers a stable review handle.
- Historical, legal, financial, medical, or safety-critical decisions still require primary-source and domain-expert verification.
- Public output should use concise paraphrase and identify uncertainty.
- Original source files, private notes, secrets, and long excerpts stay outside this repository.
