# Steve Jobs Operating Skills [![Validate](https://github.com/thepraggyverse/steve-jobs/actions/workflows/validate.yml/badge.svg)](https://github.com/thepraggyverse/steve-jobs/actions/workflows/validate.yml)

**91 `sj-*` skills for product craft, simplification, Jony Ive design studio practice, storytelling, hiring, strategy, learning, and failure review.**

These skills help an agent apply Steve Jobs-derived operating patterns and Jony Ive design studio lenses to a real artifact: a product idea, screen, object, launch story, hiring decision, strategy memo, failure review, or learning loop. They are not a personality simulator. The useful output is a clearer product, sharper story, higher bar, better decision, more human design, or reusable lesson.

The repo works as a Codex plugin and as plain `SKILL.md` folders for harnesses that scan a skills directory. Runtime skills are small and self-contained so individual folders can be symlinked, copied, or converted without breaking their references.

Only `$sj-core-catalog` is implicitly invokable.
The other 90 skills remain directly available through explicit `$sj-*` prompts.
This router-first policy keeps the complete pack searchable without loading 91 descriptions into every model turn.

This repository does not include source books, full transcripts, or long copyrighted excerpts.
It contains compact workflows, paraphrased reference notes, 15 stable source IDs, 91 claim-to-skill mappings, install scripts, behavior contracts, and examples.

## Start Here

Use the pack through the router first:

```text
Use $sj-core-catalog to choose the right SJ skill sequence for this task:
<describe the artifact, decision, product, story, team, strategy, or failure>
```

That is the portable loose-skill form.
In a native Codex plugin install, Codex namespaces plugin skills, so use:

```text
Use $steve-jobs:sj-core-catalog to choose the right SJ skill sequence for this task:
<describe the artifact, decision, product, story, team, strategy, or failure>
```

The same rule applies to leaves: `$sj-product-simplify-to-one` as a loose skill and `$steve-jobs:sj-product-simplify-to-one` through the native plugin.

Then run the recommended skills in order. If the session produces a reusable lesson, finish with:

```text
Use $sj-core-compound-learning to extract reusable lessons from this session.
```

Later, clean old saved lessons with:

```text
Use $sj-core-learning-refresh to audit saved SJ learnings before we reuse them.
```

For ready-made chains, use [`docs/PLAYBOOKS.md`](docs/PLAYBOOKS.md). When two skill families both seem plausible, use [`docs/WHEN_TO_USE_WHAT.md`](docs/WHEN_TO_USE_WHAT.md).

## What The Skills Do

| Group | Count | What it does | Example skills |
| --- | --- | --- | --- |
| Core | 3 | Route requests, choose the right lens, capture reusable lessons, and refresh saved learnings. | `$sj-core-catalog`, `$sj-core-compound-learning`, `$sj-core-learning-refresh` |
| Product craft | 23 | Simplify products, inspect artifacts, improve taste, craft, speed, and UX. | `$sj-product-simplify-to-one`, `$sj-product-customer-backwards`, `$sj-product-taste-review` |
| Jony Ive design studio | 10 | Make product decisions tactile through story, care, materials, first touch, prototypes, manufacturing, and modernization. | `$sj-ive-humanize-technology`, `$sj-ive-care-is-felt`, `$sj-ive-future-without-betrayal` |
| Story and selling | 9 | Shape launches, demos, value propositions, analogies, and marketing. | `$sj-story-one-message-marketing`, `$sj-story-sell-the-improvement`, `$sj-story-three-act-launch` |
| People and leadership | 19 | Raise the talent bar, improve leadership, feedback, trust, and team design. | `$sj-people-a-player-bar`, `$sj-people-missionaries-not-mercenaries`, `$sj-people-truth-to-founder` |
| Strategy | 15 | Focus the portfolio, handle pivots, negotiate, and review failure patterns. | `$sj-strategy-focus-matrix`, `$sj-strategy-differentiation-or-death`, `$sj-strategy-failure-apprenticeship` |
| Learning and practice | 9 | Turn books, practice, mortality, and reflection into reusable operating habits. | `$sj-learning-biographies-as-mentors`, `$sj-learning-progressive-summarization`, `$sj-learning-mortality-lens` |
| Anti-patterns | 3 | Catch ego, fake traction, overfunding, revenge, and other failure modes early. | `$sj-anti-revenge-motive-check`, `$sj-anti-channel-stuffing-check`, `$sj-anti-too-much-money-check` |

## The Core Loop

| Step | Skill | What happens | Output |
| --- | --- | --- | --- |
| 1 | `$sj-core-catalog` | Choose the right Jobs lens or sequence. | Skill route and order |
| 2 | A domain skill | Review the product, story, people, strategy, learning, or anti-pattern question. | Concrete critique or draft |
| 3 | Artifact pass | Apply the critique to the real screen, plan, copy, decision, demo, or memo. | Next artifact to inspect |
| 4 | `$sj-core-compound-learning` | Capture what should become reusable. | Future-facing lesson |

Typical prompt:

```text
Use $sj-core-catalog to choose the right Steve Jobs operating skill for this task.
```

Then follow the route it gives you, for example:

```text
Use $sj-product-simplify-to-one to find the one thing this MVP should do.
Use $sj-ive-humanize-technology to make this interface feel less cold and more approachable.
Use $sj-story-sell-the-improvement to rewrite this feature list.
Use $sj-strategy-failure-apprenticeship to autopsy this failed launch.
```

## Quick Examples

| Situation | Use | Example prompt | Expected shape |
| --- | --- | --- | --- |
| A product idea has too many features. | `$sj-product-simplify-to-one` | `Use $sj-product-simplify-to-one to find the one thing this MVP should do.` | Primary outcome, competing priorities, one organizing priority, cuts, end-to-end proof |
| A UI needs explaining. | `$sj-product-speaks-for-itself` | `Use $sj-product-speaks-for-itself to audit this onboarding flow.` | Explanation dependencies and simplifications |
| A technical product feels cold. | `$sj-ive-humanize-technology` | `Use $sj-ive-humanize-technology to make this interface feel less cold and more approachable.` | Cold points, human feeling, language and interaction changes |
| A redesign may lose what people love. | `$sj-ive-future-without-betrayal` | `Use $sj-ive-future-without-betrayal to modernize this product without betraying what people love about it.` | Enduring soul, false nostalgia, continuity signals, transition proof |
| A feature list sounds boring. | `$sj-story-sell-the-improvement` | `Use $sj-story-sell-the-improvement to rewrite this feature list.` | Customer improvement, proof, sharper copy |
| A launch needs structure. | `$sj-story-three-act-launch` | `Use $sj-story-three-act-launch to structure this product announcement.` | Problem, meaning, solution, demo beats |
| A candidate seems impressive but unclear. | `$sj-people-a-player-bar` | `Use $sj-people-a-player-bar to evaluate this candidate.` | Role bar, evidence matrix, work sample, risks, decision with counterargument |
| A startup may be drifting. | `$sj-strategy-focus-matrix` | `Use $sj-strategy-focus-matrix to simplify this product portfolio.` | Portfolio, decision axes, matrix, portfolio calls, resource shift |
| A failure needs truth. | `$sj-strategy-failure-apprenticeship` | `Use $sj-strategy-failure-apprenticeship to autopsy this failed launch.` | Failure timeline, cause classes, missed signal, causal lessons, changed tests |
| Success is distorting judgment. | `$sj-learning-all-glory-fleeting` | `Use $sj-learning-all-glory-fleeting to deflate this ego trap.` | Temporary glory, durable anchors, distortion risk, grounding action, review |
| Funding is making the team soft. | `$sj-anti-too-much-money-check` | `Use $sj-anti-too-much-money-check to audit this funding plan.` | Capital map, discipline risks, alternatives, evidence gates, stop-loss governance |

More detailed examples live in [`docs/EXAMPLES.md`](docs/EXAMPLES.md). Examples for every skill live in [`docs/SKILL_REFERENCE.md`](docs/SKILL_REFERENCE.md).

## Full Skill Inventory

| Skill | Purpose |
| --- | --- |
| `$sj-core-catalog` | Choose the right Steve Jobs operating skill and sequence. |
| `$sj-core-compound-learning` | Capture reusable Jobs-derived lessons after each use. |
| `$sj-core-learning-refresh` | Audit saved SJ learning notes for stale, duplicate, generic, contradictory, or low-confidence guidance. |
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
| `$sj-ive-design-story` | Find the product's design story before debating features. |
| `$sj-ive-humanize-technology` | Make technology feel approachable, friendly, touchable, and emotionally legible. |
| `$sj-ive-first-touch-moment` | Audit the first thing a user sees, opens, touches, hears, wears, or feels. |
| `$sj-ive-prototype-volume` | Replace argument with many concrete models and selection. |
| `$sj-ive-material-honesty` | Review material, finish, weight, color, sound, edge, and texture as part of the idea. |
| `$sj-ive-manufacturing-as-design` | Treat production, tooling, suppliers, and implementation constraints as part of design. |
| `$sj-ive-care-is-felt` | Audit whether users can sense care or carelessness in an artifact. |
| `$sj-ive-better-not-different` | Test whether novelty makes the product better, not merely different. |
| `$sj-ive-fragile-idea-protection` | Protect early promising ideas from premature committee, metric, or engineering flattening. |
| `$sj-ive-future-without-betrayal` | Move a beloved product, brand, or category into the future without losing its soul. |
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

## Repository Layout

| Path | Purpose |
| --- | --- |
| `AGENTS.md` | Canonical authoring instructions for this repository. |
| `CLAUDE.md`, `GEMINI.md` | Compatibility shims that point to `AGENTS.md`. |
| `CONTEXT.md` | Vocabulary for maintainers and agents working in this repo. |
| `.agents/plugins/marketplace.json` | Repo-local marketplace entry for GitHub/custom marketplace installs. |
| `.codex-plugin/plugin.json` | Native Codex plugin manifest. |
| `.claude-plugin/plugin.json` | Simple Claude-style skill manifest listing all skill folders. |
| `skills.sh.json` | Grouped skill catalog for skills.sh-style installers and audits. |
| `skills/sj-*` | 91 runtime skill folders. Each folder is self-contained. |
| `skills/sj-*/references/` | Skill-local thematic notes plus only the claim and source rows that skill needs. |
| `references/` | Root maintainer copies of the compact reference notes. |
| `references/sj-source-map.md` | Fifteen-source corpus index and evidence-level definitions. |
| `references/sj-evidence-map.md` | Complete claim-to-source-to-skill mapping. |
| `tests/behavior-cases.json` | 182 positive and boundary behavior contracts. |
| `tests/router-cases.json` | Ambiguous requests with expected catalog routing. |
| `tests/BEHAVIOR_CONTRACT.md` | Source-blind user-visible acceptance contract. |
| `docs/MEMORY_AND_LOGS.md` | Durable learning, temporary artifact, and refresh policy. |
| `docs/HANDOFF.md` | Closeout checklist, live install proof, autoreview, and handoff template. |
| `docs/PLAYBOOKS.md` | Practical chains for product, design, launch, hiring, strategy, failure, and learning workflows. |
| `docs/WHEN_TO_USE_WHAT.md` | Decision guide for choosing the right skill family. |
| `templates/sj-learning.md` | Template for approved project learning notes. |
| `assets/sj-skills.csv` | Machine-readable skill catalog. |
| `scripts/check-install.sh` | One-command source, installed-cache, and optional live smoke verification. |
| `scripts/check-inventory.sh` | Generated inventory drift check across catalogs and manifests. |
| `scripts/check-skill-quality.py` | Semantic uniqueness, provenance, metadata, docs, and dataset checks. |
| `scripts/check-router-live.sh` | Source-blind live routing proof across all 18 ambiguous cases. |
| `scripts/sync-source-grounding.py` | Synchronizes claim and source mappings into every portable skill. |
| `scripts/sync-openai-metadata.py` | Synchronizes prompts and router-only implicit invocation policy. |
| `scripts/build-behavior-cases.py` | Builds two behavior cases for every skill. |
| `scripts/list-skills.sh` | Grouped skill browser for the command line. |
| `scripts/install-profile.sh` | Profile installer for all, product, Ive, story, people, strategy, learning, or anti-pattern skills. |
| `scripts/unlink-skills.sh` | Safe loose-skill symlink remover. |
| `scripts/install-local.sh` | Local Codex plugin installer. |
| `scripts/link-skills.sh` | Symlink skills into Codex, Claude, or another harness. |
| `scripts/copy-skills.sh` | Copy skills into harnesses that do not follow symlinks. |
| `scripts/update-local.sh` | Pull, reinstall the local plugin pointer, and validate. |
| `scripts/validate.sh` | Public validation script. |
| `docs/` | Install, harness, update, audit, architecture, examples, and reference docs. |

## Install Matrix

| Target | Best path | Command or action |
| --- | --- | --- |
| Codex App | Native plugin marketplace | Add GitHub marketplace `thepraggyverse/steve-jobs`, install `steve-jobs`, restart Codex. |
| Codex CLI | Marketplace plus `/plugins` UI | `codex plugin marketplace add thepraggyverse/steve-jobs`, then install from `/plugins`. |
| Local Codex plugin | Local marketplace entry | `git clone https://github.com/thepraggyverse/steve-jobs.git ~/plugins/steve-jobs && cd ~/plugins/steve-jobs && ./scripts/install-local.sh` |
| Codex loose skills | Symlink or copy skill folders | `./scripts/link-skills.sh ~/.codex/skills` |
| Claude Code loose skills | Symlink or copy skill folders | `./scripts/link-skills.sh ~/.claude/skills` |
| Claude plugin-aware loaders | Use `.claude-plugin/plugin.json` | Import this checkout if your loader accepts a local Claude plugin manifest. |
| Cursor, OpenCode, Gemini, Qwen, Pi, Copilot-style harnesses | Plain `SKILL.md` folders | Use that harness skill directory with `scripts/link-skills.sh` or `scripts/copy-skills.sh`. |
| skills.sh-style catalogs | `skills.sh.json` | Use the grouped manifest to browse or install the `sj-*` skills. |

Full install details: [`docs/INSTALL.md`](docs/INSTALL.md). Harness notes: [`docs/HARNESSES.md`](docs/HARNESSES.md). Symlink and copy recipes: [`docs/SYMLINKS.md`](docs/SYMLINKS.md).

Native Codex plugin invocations use `$steve-jobs:sj-*`.
Loose-skill and most portable examples use `$sj-*`.

## Browse And Install Profiles

```bash
./scripts/list-skills.sh
./scripts/list-skills.sh profiles
./scripts/install-profile.sh ive ~/.codex/skills
./scripts/install-profile.sh product ~/.claude/skills --copy
./scripts/unlink-skills.sh ~/.codex/skills 'sj-ive-*' --dry-run
```

## Check Your Install

```bash
./scripts/check-install.sh --refresh
```

For a live read-only smoke test:

```bash
./scripts/check-install.sh --refresh --live
```

For the full 18-case live router suite:

```bash
./scripts/check-router-live.sh
```

## Update

```bash
cd ~/plugins/steve-jobs
./scripts/update-local.sh
```

For a loose symlink install, `git pull --ff-only` is enough because the harness points at this checkout. For copied skills, rerun `scripts/copy-skills.sh` with `SKILL_COPY_OVERWRITE=1`.

More detail: [`docs/UPDATE.md`](docs/UPDATE.md).

## Validate

```bash
./scripts/validate.sh
```

The validator checks exactly 91 skills, 10 root references, 91 unique workflow/output contracts, 91 source claims, 182 behavior cases, 18 router cases, router-only implicit invocation, required docs, manifests, portable local references, and Codex authoring validators when available.

Behavior and provenance details: [`docs/BEHAVIOR_TESTING.md`](docs/BEHAVIOR_TESTING.md) and [`docs/SOURCE_TRACEABILITY.md`](docs/SOURCE_TRACEABILITY.md).

For installed-plugin proof and handoff, use [`docs/HANDOFF.md`](docs/HANDOFF.md).

## Design Notes

This package follows five constraints:

1. Every skill starts with `sj-` so search is easy.
2. Each `SKILL.md` stays small and procedural.
3. Each runtime skill is self-contained, with local `references/` files.
4. Human-facing tables and examples live in docs, not every runtime skill.
5. The public repo contains operating patterns and paraphrase, not source texts.
6. One implicit router selects among 90 explicit leaf skills.
7. Generated checks make metadata, provenance, behavior, and documentation drift fail validation.

The structure was audited against:

- [Every's compound engineering guide](https://every.to/guides/compound-engineering)
- [EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin)
- [mattpocock/skills](https://github.com/mattpocock/skills)
- [EveryInc/compound-knowledge-plugin](https://github.com/EveryInc/compound-knowledge-plugin)
- [steipete/agent-scripts skills](https://github.com/steipete/agent-scripts/tree/main/skills)

See [`docs/AUDIT.md`](docs/AUDIT.md) for what was adopted and what was intentionally left out.

## FAQ

### Is this official?

No. It is an independent educational and productivity project. The useful part is the skill pack: compact operating workflows inspired by Steve Jobs-related public materials.

### Does this include the books or transcripts?

No. It intentionally avoids full books, full transcripts, and long copyrighted excerpts. The runtime material is compact, paraphrased, and operational.

### Why many skills instead of one big skill?

Small skills are easier to trigger, search, inspect, symlink, copy, validate, and compose. `sj-core-catalog` is the router when you do not know which one to use.

### Can I use only a few skills?

Yes. Use `scripts/link-skills.sh` or `scripts/copy-skills.sh` with a pattern such as `sj-product-*`, `sj-ive-*`, `sj-story-*`, or `sj-strategy-*`.

### Do I need the plugin wrapper?

No. The plugin wrapper is best for Codex native plugin workflows. The `skills/` folders can also be used directly by any harness that reads skill directories.

## Disclaimer

This is an independent educational and productivity project. It is not affiliated with Apple, Steve Jobs, Jony Ive, LoveFrom, the Steve Jobs Archive, publishers, authors, podcast hosts, or rights holders. "Steve Jobs" and "Jony Ive" are used descriptively to identify the inspiration for the operating patterns.

## License

MIT. See [`LICENSE`](LICENSE).
