# Steve Jobs Codex Plugin

An unofficial Codex plugin with 80 `sj-*` skills for product craft, simplicity, storytelling, hiring, strategy, learning, and failure review.

The skills are inspired by Steve Jobs books, interviews, and podcast notes. This repository does not include the source books, transcripts, or long copyrighted excerpts. It contains compact operating patterns, skill workflows, and paraphrased reference notes.

## What Is Inside

```text
.codex-plugin/plugin.json      Codex plugin manifest
skills/                        80 sj-prefixed skills
references/                    8 shared reference files
assets/sj-skills.csv           machine-readable skill catalog
scripts/install-local.sh       install as a local Codex plugin
scripts/link-skills.sh         symlink skills into any harness
scripts/validate.sh            validate counts, metadata, and manifests
docs/INSTALL.md                detailed install and update guide
docs/SYMLINKS.md               symlink recipes for Codex, Claude, and others
docs/DEVELOPMENT.md            maintainer notes
```

## Quick Install For Codex

```bash
git clone https://github.com/thepraggyverse/steve-jobs.git ~/plugins/steve-jobs
cd ~/plugins/steve-jobs
./scripts/install-local.sh
codex plugin add steve-jobs@personal
```

Then start a new Codex thread and try:

```text
Use $sj-core-catalog to choose the right Steve Jobs operating skill for this task.
```

## Install As Loose Skills

For harnesses that read plain skill folders, symlink all skills:

```bash
git clone https://github.com/thepraggyverse/steve-jobs.git ~/Developer/steve-jobs
cd ~/Developer/steve-jobs
./scripts/link-skills.sh ~/.codex/skills
```

For Claude Code style skill folders:

```bash
./scripts/link-skills.sh ~/.claude/skills
```

For any other harness:

```bash
./scripts/link-skills.sh /path/to/your/skills-dir
```

You can also link only one group:

```bash
./scripts/link-skills.sh ~/.codex/skills 'sj-product-*'
./scripts/link-skills.sh ~/.codex/skills 'sj-story-*'
./scripts/link-skills.sh ~/.codex/skills 'sj-people-*'
```

## Skill Groups

- `sj-core-*`: routing, catalog, and knowledge capture
- `sj-product-*`: product craft, simplicity, taste, demos, hidden quality
- `sj-story-*`: launches, selling, narrative, PR, numbers, analogy
- `sj-people-*`: hiring, teams, leadership, feedback, trust
- `sj-strategy-*`: focus, differentiation, pivots, distribution, negotiation
- `sj-learning-*`: biographies, practice, mortality, tradeoffs, summarization
- `sj-anti-*`: failure modes, ego checks, fake traction, too much money

The full catalog lives in [`references/sj-skill-catalog.md`](references/sj-skill-catalog.md).

## Example Prompts

```text
Use $sj-product-simplify-to-one to find the one thing this MVP should do.
Use $sj-product-product-speaks-for-itself to audit this onboarding flow.
Use $sj-story-sell-the-improvement to rewrite this feature list.
Use $sj-people-a-player-bar to evaluate this candidate.
Use $sj-strategy-failure-apprenticeship to autopsy this failed launch.
Use $sj-learning-progressive-summarization to process this book into skill material.
Use $sj-anti-too-much-money-check to audit this funding plan.
```

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

## Updating

```bash
cd ~/plugins/steve-jobs
git pull
./scripts/install-local.sh
codex plugin add steve-jobs@personal
```

Start a new Codex thread after reinstalling so the updated skills are loaded.

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

## Disclaimer

This is an unofficial educational and productivity project. It is not affiliated with Apple, Steve Jobs, the Steve Jobs Archive, publishers, authors, or rights holders. "Steve Jobs" is used descriptively to identify the inspiration for the operating patterns.

## License

MIT. See [`LICENSE`](LICENSE).
