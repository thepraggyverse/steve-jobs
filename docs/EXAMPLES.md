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
| MVP bloat | `Use $sj-product-simplify-to-one to find the one thing this MVP should do.` | Identifies the primary outcome, competing priorities, one organizing priority, cuts, and end-to-end proof. |
| UI needs a walkthrough | `Use $sj-product-speaks-for-itself to audit this onboarding flow.` | Names the unassisted task, explanation dependencies, root causes, replacements, and novice retest. |
| Technical product feels cold | `Use $sj-product-liberal-arts-technology to add the humanities layer to this product.` | Connects technical capability to a human situation, missing meaning, a change, and a meaningful-use prototype. |
| Hidden quality risk | `Use $sj-product-back-of-cabinet-quality to audit the unseen craft in this project.` | Reviews the hidden surface, quality standard, craftsmanship debt, user consequence, and verification. |
| Usability gap | `Use $sj-product-telegraph-to-telephone to make this tool feel like a telephone, not a telegraph.` | Maps the expert workflow to ordinary intent, absorbed complexity, progressive path, and novice proof. |

## Jony Ive Design Studio Examples

| Situation | Prompt | What Good Output Looks Like |
|---|---|---|
| Technical product feels cold | `Use $sj-ive-humanize-technology to make this interface feel less cold and more approachable.` | Finds cold points, desired human feeling, copy changes, interaction changes, and a next prototype. |
| First moment matters | `Use $sj-ive-first-touch-moment to review the first moment someone experiences this product.` | Reviews the first sequence, immediate trust signals, withdrawals, and a more generous first encounter. |
| Design debate is abstract | `Use $sj-ive-prototype-volume to turn this design debate into a prototype selection loop.` | Defines the smallest comparable prototype, variants, and selection criteria. |
| Object or UI feels careless | `Use $sj-ive-care-is-felt to find where this product feels cared for or careless.` | Separates functional correctness from felt quality and names high-leverage details. |
| Redesign risks betrayal | `Use $sj-ive-future-without-betrayal to modernize this product without betraying what people love about it.` | Separates enduring soul from nostalgia and defines continuity signals plus transition proof. |

## Story And Selling Examples

| Situation | Prompt | What Good Output Looks Like |
|---|---|---|
| Feature list is dull | `Use $sj-story-sell-the-improvement to rewrite this feature list.` | Produces a feature-to-outcome map, chosen improvement, before and after, proof, and transformation pitch. |
| Launch lacks structure | `Use $sj-story-three-act-launch to structure this product announcement.` | Produces three explicit acts, proof beats, and a timed run of show. |
| Metrics need clarity | `Use $sj-story-number-context to explain these benchmark numbers.` | Verifies numbers, baselines, denominators, human context, and limits. |
| New category is hard to explain | `Use $sj-story-historical-analogy to position this AI product.` | Maps a structural historical parallel, its breakpoints, and plain-language positioning. |
| Demo is rough | `Use $sj-story-demo-rehearsal-loop to tighten this demo.` | Produces timed beats, a failure/fallback map, revisions, and a cold-run verdict. |

## People And Leadership Examples

| Situation | Prompt | What Good Output Looks Like |
|---|---|---|
| Candidate review | `Use $sj-people-a-player-bar to evaluate this candidate.` | Defines the role bar, evidence matrix, work-sample signal, risks, and decision with counterargument. |
| Mission fit | `Use $sj-people-missionaries-not-mercenaries to rewrite this hiring screen.` | Filters for ownership, purpose, and taste. |
| Decision committee mess | `Use $sj-people-one-owner-no-committees to fix this decision process.` | Defines the decision, accountable owner, input and veto map, protocol, and review. |
| Founder is insulated | `Use $sj-people-truth-to-founder to create a truth channel.` | Designs protected channels, an evidence brief, founder response protocol, and effectiveness measure. |
| Hard persuasion | `Use $sj-people-ed-catmull-patience to plan this hard persuasion.` | Maps disagreement, shared ground, an evidence sequence, decision horizon, and stop call. |

## Strategy Examples

| Situation | Prompt | What Good Output Looks Like |
|---|---|---|
| Too many products | `Use $sj-strategy-focus-matrix to simplify this product portfolio.` | Inventories the portfolio, chooses decision axes, makes explicit portfolio calls, and reallocates resources. |
| Commodity risk | `Use $sj-strategy-differentiation-or-death to test this startup idea.` | Tests alternatives, choice criteria, defensibility, and evidence that the difference changes a choice. |
| Failed launch | `Use $sj-strategy-failure-apprenticeship to autopsy this failed launch.` | Reconstructs the timeline, causes, missed signal, causal lessons, and changed operating tests. |
| Negotiation | `Use $sj-strategy-do-not-overplay-hand to review this negotiation plan.` | Inventories leverage, checks bluff and assumptions, and defines a proportionate proposal and exit rules. |
| Pivot needed | `Use $sj-strategy-pivot-to-core to find our WebObjects pivot.` | Separates story from capability, chooses a candidate core, plans retirement, and defines narrow validation. |

## Learning And Anti-Pattern Examples

| Situation | Prompt | What Good Output Looks Like |
|---|---|---|
| Turn reading into skill material | `Use $sj-learning-progressive-summarization to process this book into skill material.` | Produces a bounded ledger, atomic notes, claim map, reusable compression, and coverage audit. |
| Major life/work decision | `Use $sj-learning-regret-vs-mistake to evaluate this decision.` | Assesses process versus outcome, classifies regret, and defines repair or release plus a future rule. |
| Ambition feels costly | `Use $sj-learning-balanced-builder-audit to audit the life cost of this plan.` | Maps life costs, sustainability baselines, redesign, and stop conditions. |
| Ego strategy | `Use $sj-anti-revenge-motive-check to test my motive here.` | Runs a rival-free value test, compares a neutral alternative, and removes punitive elements. |
| Too much funding | `Use $sj-anti-too-much-money-check to audit this funding plan.` | Maps capital, discipline risks, lower-capital paths, evidence gates, and stop-loss governance. |

## Chaining Skills

A useful chain for a messy product idea:

```text
Use $sj-core-catalog to route this idea.
Then use $sj-product-customer-backwards.
Then use $sj-product-simplify-to-one.
Then use $sj-story-sell-the-improvement.
Then use $sj-core-compound-learning to capture what we learned.
```

A useful chain for product craft and tactile design:

```text
Use $sj-product-customer-backwards to define the user experience.
Then use $sj-product-simplify-to-one to cut to the core job.
Then use $sj-ive-design-story to find the design story.
Then use $sj-ive-prototype-volume to compare concrete variants.
Then use $sj-ive-care-is-felt to inspect the chosen artifact.
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
