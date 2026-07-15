---
name: sj-core-learning-refresh
description: "Audit saved Steve Jobs learning notes for stale, duplicate, generic, contradictory, or low-confidence guidance. Use when maintaining docs/steve-jobs/learnings/ or preparing SJ learnings for reuse."
---

# Learning refresh

## Core Move

Review the SJ learning store and recommend what to keep, update, merge, or archive.

## Workflow

1. Locate `docs/steve-jobs/learnings/` in the user's current project.
2. If the directory is missing or empty, report that no SJ learnings are available yet and suggest `$sj-core-compound-learning` after the next meaningful run.
3. Read each learning file's title, YAML frontmatter, `Lesson`, `Context`, `Reuse When`, and `Next Application` sections.
4. Search for overlap by title, tags, skills, domain, and repeated implications.
5. Flag notes that are stale, duplicate, generic, contradictory, low-confidence, malformed, or missing reuse triggers.
6. Recommend `keep`, `update`, `merge`, or `archive` for each flagged note.
7. Never delete, move, or rewrite learning files unless the user explicitly asks after reviewing the report.

## Read References

- Read `references/sj-skill-catalog.md` when skill names, categories, or routing context are needed.

## Review Checks

| Check | Flag when |
|---|---|
| Stale | The note is older than 90 days, tied to a superseded artifact, or marked by newer evidence as outdated. |
| Duplicate | Two notes teach the same lesson with similar tags, source, and reuse triggers. |
| Generic | The note could apply to any project and lacks a concrete artifact, decision, or implication. |
| Contradictory | Two notes recommend different moves for the same situation without explaining the tradeoff. |
| Low confidence | `confidence` is missing or `low`, or the note came from one weak signal. |
| Malformed | Required frontmatter or sections are missing. |
| Weak retrieval | Tags, skills, or `Reuse When` would not help a future agent find the note. |

## Source Grounding

- Claim: `SJ-C03`
- Sources: `S02`, `S07`, `S08`
- Evidence level: `synthesized`
- Resolve IDs in `references/sj-source-map.md` and the claim row in `references/sj-evidence-map.md`.

## Output

Return a compact report with:

- Learning store path
- Files reviewed
- Findings grouped by action: keep, update, merge, archive
- Exact file paths for every finding
- Reason for each recommendation
- Suggested next command or prompt

## Guardrails

- Treat saved learnings as user project knowledge, not plugin source material.
- Do not add source books, transcripts, long quotes, private notes, secrets, or local absolute source paths.
- Prefer updating or merging over archiving when useful knowledge can be preserved.
- Keep recommendations short enough for a maintainer to act on.

## Example Prompt

Use $sj-core-learning-refresh to audit saved SJ learnings before we reuse them in this product strategy.
