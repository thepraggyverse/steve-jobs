# Steve Jobs Codex Plugin [![Validate](https://github.com/thepraggyverse/steve-jobs/actions/workflows/validate.yml/badge.svg)](https://github.com/thepraggyverse/steve-jobs/actions/workflows/validate.yml)

An unofficial Codex plugin with **80 `sj-*` skills** for product craft, simplicity, storytelling, hiring, strategy, learning, and failure review.

The goal is simple: make Steve Jobs-derived operating patterns easy to invoke inside Codex and other agent harnesses without stuffing an entire book summary into every prompt.

This repository does **not** include source books, full transcripts, or long copyrighted excerpts. It contains compact skill workflows, paraphrased references, source-title notes, install scripts, and examples.

## Philosophy

Each pass through a product, strategy, story, or team decision should make the next pass sharper.

A good Jobs-style review is not cosplay. It should produce leverage:

- clearer product intent
- fewer features fighting for attention
- a stronger user-facing story
- higher hiring and craft standards
- more honest failure review
- reusable lessons for the next agent session

## The Core Loop

| Step | Skill | What It Does | Output |
|---|---|---|---|
| 1 | `$sj-core-catalog` | Choose the right Jobs lens or sequence. | Skill route and order |
| 2 | One domain skill | Product, story, people, strategy, learning, or anti-pattern review. | Concrete critique or draft |
| 3 | Artifact pass | Apply the critique to the real product, plan, copy, decision, or demo. | Next artifact to inspect |
| 4 | `$sj-core-compound-learning` | Capture what should become reusable. | Future-facing lesson |

Typical prompt:

```text
Use $sj-core-catalog to choose the right Steve Jobs operating skill for this task.
```

Then follow the route it gives you, for example:

```text
Use $sj-product-simplify-to-one to find the one thing this MVP should do.
Use $sj-story-sell-the-improvement to rewrite this feature list.
Use $sj-strategy-failure-apprenticeship to autopsy this failed launch.
```

## Skill Groups

| Group | Count | When To Use | Example Skills |
|---|---:|---|---|
| Core | 2 | Route requests, choose a lens, and capture reusable lessons. | `$sj-core-catalog`, `$sj-core-compound-learning` |
| Product craft | 23 | Simplify products, inspect artifacts, improve taste, craft, speed, and UX. | `$sj-product-make-something-wonderful`, `$sj-product-customer-backwards`, `$sj-product-bicycle-for-the-mind` |
| Story and selling | 9 | Shape launches, demos, value propositions, analogies, and marketing. | `$sj-story-one-message-marketing`, `$sj-story-sell-the-improvement`, `$sj-story-three-act-launch` |
| People and leadership | 19 | Raise the talent bar, improve leadership, feedback, trust, and team design. | `$sj-people-a-player-bar`, `$sj-people-missionaries-not-mercenaries`, `$sj-people-pushback-interview` |
| Strategy | 15 | Focus the portfolio, handle pivots, negotiate, and review failure patterns. | `$sj-strategy-focus-matrix`, `$sj-strategy-differentiation-or-death`, `$sj-strategy-innovate-out` |
| Learning and practice | 9 | Turn books, practice, mortality, and reflection into reusable operating habits. | `$sj-learning-biographies-as-mentors`, `$sj-learning-regret-vs-mistake`, `$sj-learning-mortality-lens` |
| Anti-patterns | 3 | Catch ego, fake traction, overfunding, revenge, and other failure modes early. | `$sj-anti-revenge-motive-check`, `$sj-anti-channel-stuffing-check`, `$sj-anti-too-much-money-check` |

## Quick Examples

| Situation | Use | Example Prompt | Expected Shape |
|---|---|---|---|
| A product idea has too many features. | `$sj-product-simplify-to-one` | `Use $sj-product-simplify-to-one to find the one thing this MVP should do.` | One core job, cuts, tradeoff, next artifact |
| A UI needs explaining. | `$sj-product-speaks-for-itself` | `Use $sj-product-speaks-for-itself to audit this onboarding flow.` | Explanation dependencies and simplifications |
| A feature list sounds boring. | `$sj-story-sell-the-improvement` | `Use $sj-story-sell-the-improvement to rewrite this feature list.` | Customer improvement, proof, sharper copy |
| A launch needs structure. | `$sj-story-three-act-launch` | `Use $sj-story-three-act-launch to structure this product announcement.` | Problem, meaning, solution, demo beats |
| A candidate seems impressive but unclear. | `$sj-people-a-player-bar` | `Use $sj-people-a-player-bar to evaluate this candidate.` | Bar, evidence, risk, recommendation |
| A startup may be drifting. | `$sj-strategy-focus-matrix` | `Use $sj-strategy-focus-matrix to simplify this product portfolio.` | Focus grid, keep/cut choices, next test |
| A failure needs truth. | `$sj-strategy-failure-apprenticeship` | `Use $sj-strategy-failure-apprenticeship to autopsy this failed launch.` | Facts, false story, lesson, pivot |
| Success is distorting judgment. | `$sj-learning-all-glory-fleeting` | `Use $sj-learning-all-glory-fleeting to deflate this ego trap.` | Perspective, risk, grounding action |
| Funding is making the team soft. | `$sj-anti-too-much-money-check` | `Use $sj-anti-too-much-money-check to audit this funding plan.` | Failure pattern, evidence, correction |

More detailed examples live in [`docs/EXAMPLES.md`](docs/EXAMPLES.md).

## Full Skill Inventory

| Skill | Purpose |
|---|---|
| `$sj-core-catalog` | Choose the right Steve Jobs operating skill and sequence. |
| `$sj-core-compound-learning` | Capture reusable Jobs-derived lessons after each use. |
| `$sj-product-make-something-wonderful` | Raise ambition, care, usefulness, and emotional quality. |
| `$sj-product-customer-backwards` | Start from the user experience and work back to technology. |
| `$sj-product-bicycle-for-the-mind` | Frame tools as human leverage rather than machinery. |
| `$sj-product-liberal-arts-technology` | Connect engineering with taste, story, culture, and emotion. |
| `$sj-product-speaks-for-itself` | Remove design that requires explanation to make sense. |
| `$sj-product-design-is-how-it-works` | Judge design by behavior, not surface styling. |
| `$sj-product-simplify-to-one` | Reduce a product, path, message, or priority set to one clear thing. |
| `$sj-product-simple-stick` | Challenge undistilled, winding, or overcomplicated thinking. |
| `$sj-product-hack-away-unessential` | Remove anything that does not serve the core experience. |
| `$sj-product-speed-as-feature` | Choose speed or responsiveness as a product rule. |
| `$sj-product-apple-experience-audit` | Audit every touchpoint as a trust deposit or withdrawal. |
| `$sj-product-back-of-cabinet-quality` | Care about hidden quality even when users may not see it. |
| `$sj-product-taste-review` | Use judgment where metrics and committees are not enough. |
| `$sj-product-pixel-polish` | Review the artifact at detail level and improve finish. |
| `$sj-product-no-second-rate-products` | Identify mediocrity and force a higher standard. |
| `$sj-product-beautiful-object-standard` | Ask whether the thing deserves to exist as an object. |
| `$sj-product-telegraph-to-telephone` | Turn expert complexity into everyday usability. |
| `$sj-product-founder-workbench` | Demystify reality by making and inspecting things directly. |
| `$sj-product-reputation-credits` | Treat each interaction as adding or withdrawing trust. |
| `$sj-product-skepticism-hierarchy` | Sort objections by signal, source, and importance. |
| `$sj-product-raw-work-no-filters` | Get decision makers close to the actual artifact. |
| `$sj-product-creative-selection` | Run a concrete demo-driven iteration loop. |
| `$sj-product-concrete-artifact-review` | Force decisions around visible work rather than ideas. |
| `$sj-story-one-message-marketing` | Make one clear promise across copy, ads, and launch. |
| `$sj-story-sell-the-improvement` | Sell the better life, not the product feature. |
| `$sj-story-three-act-launch` | Build the problem, meaning, solution arc. |
| `$sj-story-number-context` | Make numbers vivid and meaningful. |
| `$sj-story-historical-analogy` | Use history to make the future understandable. |
| `$sj-story-demo-rehearsal-loop` | Practice until the demo feels inevitable. |
| `$sj-story-values-marketing` | Explain what the brand stands for. |
| `$sj-story-missionary-pr` | Use publicity to educate, not just hype. |
| `$sj-story-old-story-new-tool` | Put new technology inside enduring human stories. |
| `$sj-people-a-player-bar` | Apply an unusually high talent standard. |
| `$sj-people-missionaries-not-mercenaries` | Filter for purpose, ownership, and belief. |
| `$sj-people-pushback-interview` | Test independent thinking and intelligent disagreement. |
| `$sj-people-small-a-team` | Prefer a small excellent team over a large average one. |
| `$sj-people-one-owner-no-committees` | Assign clear ownership and remove committee drift. |
| `$sj-people-blunt-truth-review` | Say the direct thing clearly and usefully. |
| `$sj-people-no-seagull-management` | Avoid detached executive drive-by feedback. |
| `$sj-people-management-by-values` | Align destination and values, then allow flexible routes. |
| `$sj-people-ideas-from-anywhere` | Remove hierarchy from idea flow. |
| `$sj-people-founder-soul-guardian` | Protect the product or company soul. |
| `$sj-people-ceo-at-bottom` | Treat leadership as service to the builders. |
| `$sj-people-confidant-board` | Use trusted outsiders to organize thought. |
| `$sj-people-ask-for-help` | Ask serious builders directly and specifically. |
| `$sj-people-smart-people-can-leave` | Remember talented people are volunteers, not possessions. |
| `$sj-people-permanent-ensemble` | Build a recurring creative team with compounding trust. |
| `$sj-people-truth-to-founder` | Create channels for reality to reach the decision maker. |
| `$sj-people-ed-catmull-patience` | Use facts, trust, and time to change strong minds. |
| `$sj-people-andy-grove-correction` | Accept hard correction from a serious operator. |
| `$sj-people-bob-iger-trust` | Negotiate with transparency when trust matters. |
| `$sj-strategy-focus-matrix` | Reduce product lines, priorities, or bets to a clear grid. |
| `$sj-strategy-differentiation-or-death` | Check whether the product is meaningfully different. |
| `$sj-strategy-innovate-out` | Respond to commoditization with invention. |
| `$sj-strategy-direct-channel` | Build a direct relationship with customers. |
| `$sj-strategy-ambush-distribution` | Meet customers where attention and traffic already are. |
| `$sj-strategy-say-yes-then-learn` | Commit before full certainty when the risk is survivable. |
| `$sj-strategy-reality-is-malleable` | Challenge learned helplessness and false constraints. |
| `$sj-strategy-failure-apprenticeship` | Turn failure into operating wisdom without flattering it. |
| `$sj-strategy-startup-discipline` | Keep scarcity, focus, and truth inside the startup. |
| `$sj-strategy-pivot-to-core` | Find the real business after the first plan fails. |
| `$sj-strategy-synthesizer-strategy` | Combine separate technologies into one coherent product. |
| `$sj-strategy-do-not-overplay-hand` | Use leverage with restraint. |
| `$sj-strategy-build-for-yourself` | Build what the team deeply wants and understands. |
| `$sj-strategy-company-as-invention` | Treat the company as the machine that makes great products. |
| `$sj-strategy-web-as-community` | Use the web as relationship infrastructure. |
| `$sj-learning-biographies-as-mentors` | Use lives of builders as reusable mentorship. |
| `$sj-learning-regret-vs-mistake` | Separate reversible mistakes from life regrets. |
| `$sj-learning-mortality-lens` | Use finitude to clarify courage and priority. |
| `$sj-learning-avocation-to-vocation` | Turn deep curiosity into work. |
| `$sj-learning-endurance-loop` | Design the repeated effort needed for mastery. |
| `$sj-learning-fundamentals-practice` | Return to the basic reps that compound. |
| `$sj-learning-progressive-summarization` | Turn books, podcasts, and notes into reusable knowledge. |
| `$sj-learning-balanced-builder-audit` | Check ambition against health, family, joy, and sanity. |
| `$sj-learning-all-glory-fleeting` | Keep ego and success in perspective. |
| `$sj-anti-revenge-motive-check` | Detect when strategy is secretly ego or revenge. |
| `$sj-anti-channel-stuffing-check` | Separate real traction from fake comfort. |
| `$sj-anti-too-much-money-check` | Prevent abundant funding from killing discipline. |

For examples for every skill, see [`docs/SKILL_REFERENCE.md`](docs/SKILL_REFERENCE.md).

## Repository Layout

| Path | Purpose |
|---|---|
| `.agents/plugins/marketplace.json` | Repo-local marketplace entry for GitHub/custom marketplace installs |
| `.codex-plugin/plugin.json` | Codex plugin manifest |
| `skills/` | 80 runtime skill folders |
| `references/` | Shared Jobs-derived references loaded only when useful |
| `assets/sj-skills.csv` | Machine-readable skill catalog |
| `scripts/install-local.sh` | Local Codex plugin installer |
| `scripts/link-skills.sh` | Symlink skills into Codex, Claude, or another harness |
| `scripts/validate.sh` | Public validation script |
| `docs/INSTALL.md` | Detailed install and update guide |
| `docs/SYMLINKS.md` | Symlink recipes and collision policy |
| `docs/SKILL_REFERENCE.md` | Full skill table with examples |
| `docs/EXAMPLES.md` | Scenario-based usage examples |

## Install Matrix

| Target | Command | Notes |
|---|---|---|
| Codex App from GitHub | Add marketplace source `thepraggyverse/steve-jobs` | Git ref `main`, sparse paths blank |
| Codex CLI marketplace | `codex plugin marketplace add thepraggyverse/steve-jobs` | Then install `steve-jobs` from `/plugins` |
| Codex plugin, default local path | `git clone https://github.com/thepraggyverse/steve-jobs.git ~/plugins/steve-jobs && cd ~/plugins/steve-jobs && ./scripts/install-local.sh` | Then run `codex plugin add steve-jobs@personal` |
| Codex plugin, repo cloned elsewhere | `./scripts/install-local.sh` | Creates `~/plugins/steve-jobs` symlink to this checkout |
| Codex loose skills | `./scripts/link-skills.sh ~/.codex/skills` | Useful when you want direct skill folders |
| Claude Code loose skills | `./scripts/link-skills.sh ~/.claude/skills` | Symlinks all `sj-*` folders |
| Custom harness | `./scripts/link-skills.sh /path/to/skills` | Works for any directory-scanning harness |
| One skill group | `./scripts/link-skills.sh ~/.codex/skills 'sj-product-*'` | Also supports `sj-story-*`, `sj-people-*`, etc. |

Full installation details live in [`docs/INSTALL.md`](docs/INSTALL.md).

## Validate

```bash
./scripts/validate.sh
```

The validator checks:

- exactly 80 skill folders
- exactly 8 shared references
- each skill has `SKILL.md`
- each skill has `agents/openai.yaml`
- each skill frontmatter name matches its folder
- `agents/openai.yaml` default prompt mentions the skill
- plugin manifest parses as JSON
- local Codex validators, when available

## Update

```bash
cd ~/plugins/steve-jobs
git pull
./scripts/install-local.sh
codex plugin add steve-jobs@personal
```

Start a new Codex thread after reinstalling so the updated skills load.

## Design Notes

This package follows three constraints:

1. Every skill starts with `sj-` so search is easy.
2. Each `SKILL.md` stays small and procedural.
3. Shared references hold the broader Jobs-derived ideas so every skill does not duplicate the same context.

The structure was influenced by public skill/plugin repositories such as:

- <https://github.com/mattpocock/skills>
- <https://github.com/EveryInc/compound-engineering-plugin>
- <https://github.com/EveryInc/compound-knowledge-plugin>
- <https://github.com/steipete/agent-scripts/tree/main/skills>

## FAQ

### Is this official?

No. This is an unofficial educational and productivity project.

### Does this include the books or transcripts?

No. It intentionally avoids full books, full transcripts, and long copyrighted excerpts. The runtime material is compact, paraphrased, and operational.

### Why 80 skills instead of one big skill?

Small skills are easier to trigger, search, inspect, symlink, and compose. `$sj-core-catalog` is the router when you do not know which one to use.

### Can I use only a few skills?

Yes. Use `scripts/link-skills.sh` with a pattern such as `sj-product-*` or copy specific skill folders manually.

### Do I need the plugin wrapper?

No. The plugin wrapper is best for Codex plugin workflows. The `skills/` folders can also be used directly by any harness that reads skill directories.

## Disclaimer

This is an unofficial educational and productivity project. It is not affiliated with Apple, Steve Jobs, the Steve Jobs Archive, publishers, authors, or rights holders. "Steve Jobs" is used descriptively to identify the inspiration for the operating patterns.

## License

MIT. See [`LICENSE`](LICENSE).
