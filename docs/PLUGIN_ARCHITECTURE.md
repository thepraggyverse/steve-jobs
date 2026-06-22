# Plugin Architecture

This package has six layers.

| Layer | Path | Purpose |
|---|---|---|
| Repo instructions | `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `CONTEXT.md` | Authoring context for humans and agents changing this repo. |
| Repo marketplace | `.agents/plugins/marketplace.json` | Lets the repository act as a plugin marketplace. |
| Native plugin manifest | `.codex-plugin/plugin.json` | Makes the package installable as a Codex plugin. |
| Portable catalogs | `.claude-plugin/plugin.json`, `skills.sh.json` | Let other installers discover the same skill folders. |
| Runtime skills | `skills/sj-*/SKILL.md` | Small procedural instructions that agents can load when relevant. |
| Skill-local references | `skills/sj-*/references/sj-*.md` | Compact Jobs-derived context loaded only when useful. |
| Human docs | `README.md`, `docs/` | Tables, install instructions, examples, update guides, and audit notes. |

## Why Keep Skills Small?

Skills share model context with the user's request, source files, tool output, and other triggered skills. Each `SKILL.md` therefore stays focused on the operating move: workflow, references, output format, guardrails, and an example prompt.

## Why Put Tables In Docs Instead?

Tables and examples are excellent for humans browsing GitHub. They are less useful inside every runtime skill because they inflate context. This repo keeps rich explanations in `README.md`, `docs/EXAMPLES.md`, and `docs/SKILL_REFERENCE.md`, while runtime skills stay lean.

## How References Work

A skill links to one or two files inside its own directory, for example:

```text
references/sj-product-craft.md
references/sj-anti-patterns.md
```

The agent should read those only when deeper grounding is needed.

Root `references/` are maintainer copies. Runtime skills should not use `../../references/*` because converter-based and loose-skill installs may move each skill folder independently.

## Public-Safe Source Policy

The plugin is inspired by books, interviews, and podcast notes. The public repo contains operating patterns and paraphrased references, not source texts, full transcripts, or long copyrighted passages.

## Compound Workflow Fit

`docs/COMPOUNDING.md` describes how to use the skills as a loop: route, ground in an artifact, simplify, raise the bar, change the artifact, and capture the reusable lesson. This keeps the plugin useful as an operating system instead of a static list of prompts.
