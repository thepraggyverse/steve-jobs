# Plugin Architecture

This package has four layers.

| Layer | Path | Purpose |
|---|---|---|
| Repo marketplace | `.agents/plugins/marketplace.json` | Lets the repository act as a plugin marketplace. |
| Plugin manifest | `.codex-plugin/plugin.json` | Makes the package installable as a Codex plugin. |
| Runtime skills | `skills/sj-*/SKILL.md` | Small procedural instructions that Codex can load when relevant. |
| Shared references | `references/sj-*.md` | Broader Jobs-derived context loaded only when useful. |

## Why Keep Skills Small?

Skills share the model context with the user's request, source files, tool output, and other triggered skills. Each `SKILL.md` therefore stays focused on the operating move: workflow, references, output format, and guardrails.

## Why Put Tables In Docs Instead?

Tables and examples are excellent for humans browsing a GitHub repo. They are less ideal inside every runtime skill because they inflate context. This repo keeps the rich explanations in `README.md`, `docs/EXAMPLES.md`, and `docs/SKILL_REFERENCE.md`, while runtime skills stay lean.

## How References Work

A skill links to one or two references, for example:

```text
../../references/sj-product-craft.md
../../references/sj-anti-patterns.md
```

The agent should read those only when deeper grounding is needed.

## Public-Safe Source Policy

The plugin is inspired by books, interviews, and podcast notes. The public repo contains operating patterns and paraphrased references, not source texts, full transcripts, or long copyrighted passages.
