# Playbooks

Use these playbooks when you want the whole skill pack to behave like an operating system instead of a list of prompts. Start with the closest situation, run the skills in order, and stop as soon as the artifact improves enough to inspect again.

## Universal Router

```text
Use $sj-core-catalog to choose the right SJ skill sequence for this task:
<describe the artifact, decision, or mess>
```

Use this when you are unsure. It should return a small sequence, why each skill applies, and the first action.

## Product Redesign

Use when a product is bloated, confusing, cold, or hard to explain.

```text
Use $sj-product-customer-backwards to define the user experience.
Then use $sj-product-simplify-to-one to cut to the core job.
Then use $sj-product-speaks-for-itself to remove explanation dependencies.
Then use $sj-ive-humanize-technology to make the interface feel approachable.
Then use $sj-ive-care-is-felt to inspect whether users can sense care.
```

Expected output:

- Primary user and organizing outcome
- Cuts, subordinations, and end-to-end proof
- Explanation dependencies, replacements, and novice retest
- Humanized language and interaction changes
- Care signals, withdrawals, and a high-leverage repair

## Jony Ive Design Studio Pass

Use when form, feel, first touch, material, prototype choice, or modernization is the main issue.

```text
Use $sj-ive-design-story to find the product's design story.
Then use $sj-ive-first-touch-moment to inspect the first encounter.
Then use $sj-ive-prototype-volume to turn taste debate into concrete variants.
Then use $sj-ive-material-honesty to review sensory and material truth.
Then use $sj-ive-manufacturing-as-design to test whether the concept survives implementation.
```

Expected output:

- Design story
- First-touch trust signals
- Prototype variants and selection criteria
- Sensory or material mismatches
- Implementation constraints that improve or threaten the idea

## Launch Story

Use when a launch, website, deck, or announcement sounds like features instead of meaning.

```text
Use $sj-story-sell-the-improvement to rewrite the feature list around the user improvement.
Then use $sj-story-one-message-marketing to reduce the launch to one promise.
Then use $sj-story-three-act-launch to structure the announcement.
Then use $sj-story-demo-rehearsal-loop to make the demo feel inevitable.
```

Expected output:

- Before-and-after customer transformation with proof
- One remembered launch message
- Three acts and proof beats
- Timed demo, fallback map, and cold-run verdict

## Founder Strategy Review

Use when a company, product line, or roadmap is drifting.

```text
Use $sj-strategy-focus-matrix to reduce priorities to a clear grid.
Then use $sj-strategy-differentiation-or-death to test whether the product is meaningfully different.
Then use $sj-strategy-company-as-invention to inspect whether the organization can make the product.
Then use $sj-people-truth-to-founder to create a reality channel.
```

Expected output:

- Evidence-based portfolio matrix and resource shift
- Defensible difference and choice-changing evidence
- Institutional mechanism and bounded organization prototype
- Protected truth channels and founder response protocol

## Hiring And Team Bar

Use when a role, candidate, or team shape needs a higher standard.

```text
Use $sj-people-a-player-bar to define the bar.
Then use $sj-people-missionaries-not-mercenaries to check purpose and ownership.
Then use $sj-people-pushback-interview to test independent thinking.
Then use $sj-people-small-a-team to simplify the team shape.
```

Expected output:

- Role bar, evidence matrix, and work-sample signal
- Mission commitment and principled-disagreement evidence
- Pushback scenarios and scored rubric
- Smallest complete outcome and named core team

## Failure Autopsy

Use when a project, launch, product, or decision failed and the team needs truth.

```text
Use $sj-strategy-failure-apprenticeship to autopsy the failure.
Then use $sj-anti-revenge-motive-check to remove ego from the next move.
Then use $sj-anti-channel-stuffing-check to separate real traction from fake comfort.
Then use $sj-strategy-pivot-to-core to find the reusable capability.
```

Expected output:

- Failure timeline, cause classification, and missed signal
- Rival-free motive test and neutral alternative
- Channel reconciliation and normalized performance
- Candidate core, retirement plan, and narrow validation

## Learning And Compounding

Use after a useful review or whenever reading should become reusable operating knowledge.

```text
Use $sj-core-compound-learning to extract reusable lessons from this session.
```

Later:

```text
Use $sj-core-learning-refresh to audit saved SJ learnings before we reuse them.
```

Expected output:

- 1-3 approved learning candidates
- Duplicate check
- Saved lesson path when approved
- Keep, update, merge, or archive recommendations during refresh

## Skill Profiles

Use profiles when a harness has too many global skills or when you want a smaller searchable set.

| Profile | Pattern | Best for |
|---|---|---|
| All | `sj-*` | Full plugin use |
| Product | `sj-product-*` | Product simplification and artifact review |
| Ive | `sj-ive-*` | Tactile design, care, materials, first touch |
| Story | `sj-story-*` | Launches, demos, positioning |
| People | `sj-people-*` | Hiring, leadership, team design |
| Strategy | `sj-strategy-*` | Focus, pivots, distribution, company design |
| Learning | `sj-learning-*` | Reading, practice, mortality, reflection |
| Anti-patterns | `sj-anti-*` | Ego, fake traction, overfunding |

Examples:

```bash
./scripts/list-skills.sh profiles
./scripts/install-profile.sh ive ~/.codex/skills
./scripts/install-profile.sh product ~/.claude/skills --copy
./scripts/unlink-skills.sh ~/.codex/skills 'sj-ive-*' --dry-run
```
