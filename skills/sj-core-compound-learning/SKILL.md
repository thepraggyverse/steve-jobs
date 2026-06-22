---
name: sj-core-compound-learning
description: "Capture 1-3 approved Jobs-derived lessons into a durable project learning store. Use after a product review, launch, hiring decision, strategy session, failure autopsy, or skill chain produced reusable operating knowledge."
---

# Compound Jobs learning

## Core Move

Turn a completed SJ skill run into a small, approved, reusable learning that future agents can find.

## Workflow

1. Identify the completed artifact, decision, review, or failure that created the learning.
2. Draft 1-3 candidate lessons only. Skip capture when the session produced no reusable lesson.
3. Classify each candidate as `product-taste`, `story`, `people`, `strategy`, `failure`, `learning`, `anti-pattern`, or `prompt-pattern`.
4. Mark the source as `run-derived`, `source-derived`, or `mixed`.
5. Search `docs/steve-jobs/learnings/` for similar titles, tags, and key phrases. If the directory is missing, say there are no saved SJ learnings yet.
6. Show the candidates and duplicate check to the user. Ask for approval before writing durable files.
7. Save each approved lesson to `docs/steve-jobs/learnings/<slug>.md` in the user's current project, creating the directory if needed.
8. Use `/tmp/steve-jobs/sj-core-compound-learning/<run-id>/` only for temporary working notes or comparison artifacts.

## Learning Format

Use this shape for each saved file:

```markdown
---
type: product-taste
domain: product
skills: [sj-product-simplify-to-one, sj-story-sell-the-improvement]
confidence: medium
created: YYYY-MM-DD
source: run-derived
tags: [onboarding, simplification, launch]
---

# Short Learning Title

## Lesson

Two to four sentences explaining what is now known.

## Context

What artifact, decision, review, launch, failure, or skill chain produced it.

## Reuse When

When a future agent should retrieve this lesson.

## Next Application

The next concrete artifact, prompt, checklist, or decision this should improve.
```

Use `templates/sj-learning.md` from this repository as the authoring template when it is available.

## Read References

- Read `references/sj-source-map.md` when this skill needs source grounding or deeper examples.
- Read `references/sj-skill-catalog.md` when this skill needs source grounding or deeper examples.

## Output

Before saving, return:

- Candidate lessons
- Type, domain, source, confidence, and tags
- Duplicate or stale-learning check
- Exact proposed file paths
- Approval request

After saving, return:

- Saved paths
- Tags that should retrieve each lesson
- When to reuse the lesson
- Any skipped candidate and why

## Guardrails

- Keep Jobs as a source of operating patterns, not as an imitation costume.
- Prefer concrete artifacts, decisions, tradeoffs, and next actions.
- Do not use long quotations from the source material.
- Do not save full transcripts, private notes, secrets, local absolute source paths, or copyrighted excerpts.
- Do not write durable learnings without user approval.
- Do not overwrite an existing learning unless the user explicitly chooses update or merge.
- If evidence is missing, ask for the artifact or state the assumption.

## Example Prompt

Use $sj-core-compound-learning to extract reusable Jobs lessons from this session.
