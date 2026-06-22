# Examples

These examples show how to use the plugin as an operating system rather than a quote generator.

## Router First

When you are unsure which skill applies, start here:

```text
Use $sj-core-catalog to choose the right Steve Jobs operating skill for this task:
We have a messy AI note-taking app idea with too many features and no launch story.
```

Expected shape:

| Section | What You Should Get |
|---|---|
| Selected skills | A small sequence such as `$sj-product-simplify-to-one`, `$sj-product-customer-backwards`, `$sj-story-sell-the-improvement` |
| Why this sequence | One sentence per skill |
| First action | A concrete next artifact, draft, or decision |
| References | One or two shared references to load if needed |

## Product Examples

| Situation | Prompt | What Good Output Looks Like |
|---|---|---|
| MVP bloat | `Use $sj-product-simplify-to-one to find the one thing this MVP should do.` | Names the core user job, cuts features, explains tradeoff, picks next demo. |
| UI needs a walkthrough | `Use $sj-product-speaks-for-itself to audit this onboarding flow.` | Finds where the interface depends on explanation and suggests self-evident changes. |
| Technical product feels cold | `Use $sj-product-liberal-arts-technology to add the humanities layer to this product.` | Connects the tool to human meaning, emotion, and craft. |
| Hidden quality risk | `Use $sj-product-back-of-cabinet-quality to audit the unseen craft in this project.` | Reviews internal details that shape trust even when users never see them. |
| Usability gap | `Use $sj-product-telegraph-to-telephone to make this tool feel like a telephone, not a telegraph.` | Turns expert workflow into ordinary-user flow. |

## Story And Selling Examples

| Situation | Prompt | What Good Output Looks Like |
|---|---|---|
| Feature list is dull | `Use $sj-story-sell-the-improvement to rewrite this feature list.` | Converts specs into customer transformation. |
| Launch lacks structure | `Use $sj-story-three-act-launch to structure this product announcement.` | Problem, meaning, solution, demo beats. |
| Metrics need clarity | `Use $sj-story-number-context to explain these benchmark numbers.` | Makes the number tangible and relevant. |
| New category is hard to explain | `Use $sj-story-historical-analogy to position this AI product.` | Uses a familiar transition to explain the new thing. |
| Demo is rough | `Use $sj-story-demo-rehearsal-loop to tighten this demo.` | Produces rehearsal passes, weak points, and next practice move. |

## People And Leadership Examples

| Situation | Prompt | What Good Output Looks Like |
|---|---|---|
| Candidate review | `Use $sj-people-a-player-bar to evaluate this candidate.` | Defines the bar, evidence, gaps, risks, and recommendation. |
| Mission fit | `Use $sj-people-missionaries-not-mercenaries to rewrite this hiring screen.` | Filters for ownership, purpose, and taste. |
| Decision committee mess | `Use $sj-people-one-owner-no-committees to fix this decision process.` | Assigns one owner and removes approval fog. |
| Founder is insulated | `Use $sj-people-truth-to-founder to create a truth channel.` | Designs a way for reality to reach authority. |
| Hard persuasion | `Use $sj-people-ed-catmull-patience to plan this hard persuasion.` | Uses facts, timing, and trust rather than ego escalation. |

## Strategy Examples

| Situation | Prompt | What Good Output Looks Like |
|---|---|---|
| Too many products | `Use $sj-strategy-focus-matrix to simplify this product portfolio.` | A compact grid with keep/cut/sequence logic. |
| Commodity risk | `Use $sj-strategy-differentiation-or-death to test this startup idea.` | Shows where differentiation is real or fake. |
| Failed launch | `Use $sj-strategy-failure-apprenticeship to autopsy this failed launch.` | Facts, false story, real lesson, discipline leak, next smaller move. |
| Negotiation | `Use $sj-strategy-do-not-overplay-hand to review this negotiation plan.` | Identifies leverage, trust risk, and restraint. |
| Pivot needed | `Use $sj-strategy-pivot-to-core to find our WebObjects pivot.` | Finds reusable capability after the initial business fails. |

## Learning And Anti-Pattern Examples

| Situation | Prompt | What Good Output Looks Like |
|---|---|---|
| Turn reading into skill material | `Use $sj-learning-progressive-summarization to process this book into skill material.` | Extracts principles, warnings, and reusable prompts. |
| Major life/work decision | `Use $sj-learning-regret-vs-mistake to evaluate this decision.` | Separates reversible mistakes from long-term regret. |
| Ambition feels costly | `Use $sj-learning-balanced-builder-audit to audit the life cost of this plan.` | Names health, family, sanity, and joy tradeoffs. |
| Ego strategy | `Use $sj-anti-revenge-motive-check to test my motive here.` | Separates product truth from revenge or status motive. |
| Too much funding | `Use $sj-anti-too-much-money-check to audit this funding plan.` | Finds where money is weakening focus or truth. |

## Chaining Skills

A useful chain for a messy product idea:

```text
Use $sj-core-catalog to route this idea.
Then use $sj-product-customer-backwards.
Then use $sj-product-simplify-to-one.
Then use $sj-story-sell-the-improvement.
Then use $sj-core-compound-learning to capture what we learned.
```

A useful chain for a failed project:

```text
Use $sj-strategy-failure-apprenticeship to autopsy this project.
Then use $sj-anti-revenge-motive-check to check our motives.
Then use $sj-strategy-pivot-to-core to find the reusable capability.
Then use $sj-core-compound-learning to save the lesson.
```

A useful chain for hiring:

```text
Use $sj-people-a-player-bar to define the bar.
Then use $sj-people-pushback-interview to design interview questions.
Then use $sj-people-missionaries-not-mercenaries to check mission fit.
```

## Compounding And Refresh

| Situation | Prompt | What Good Output Looks Like |
|---|---|---|
| A review produced a reusable principle | `Use $sj-core-compound-learning to save the lesson from this product review.` | 1-3 approved learning candidates, duplicate check, saved paths, and retrieval tags. |
| Old learnings may be stale | `Use $sj-core-learning-refresh to audit saved SJ learnings before we reuse them.` | Keep/update/merge/archive recommendations with exact file paths. |
