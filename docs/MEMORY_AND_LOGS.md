# Memory And Logs

SJ skills should make the next run easier without turning private chats or source books into repo data.

## Storage Policy

| Store | Path | Purpose | Persistence |
|---|---|---|---|
| Durable learnings | `docs/steve-jobs/learnings/` | Approved reusable lessons from SJ skill runs. | Git-track when the user wants project knowledge committed. |
| Temporary artifacts | `/tmp/steve-jobs/<skill-name>/<run-id>/` | Scratch notes, comparison outputs, duplicate checks, and local review artifacts. | Disposable. Do not rely on this across machines. |
| Repo-bound context | `.context/steve-jobs/<workflow>/` | Optional project-specific context that is inseparable from the repo and branch. | Use only when explicitly useful and user-curated. |

The plugin repo ships the workflow and template. User projects own their `docs/steve-jobs/learnings/` notes.

## Durable Learning Rules

- Save only 1-3 lessons after a meaningful run.
- Ask the user before writing durable files.
- Search existing learning notes before creating a new one.
- Prefer update or merge when a new lesson improves an old one.
- Use `templates/sj-learning.md` as the shape for new notes.
- Mark every note as `run-derived`, `source-derived`, or `mixed`.
- Use concrete tags that future searches would actually use.

## Temporary Artifact Rules

Use `/tmp/steve-jobs/<skill-name>/<run-id>/` for:

- candidate learning drafts
- duplicate search snippets
- refresh reports
- temporary comparisons between old and new notes

Do not put durable decisions only in `/tmp`. If a lesson matters later, save it under `docs/steve-jobs/learnings/`.

## What To Avoid

Never save:

- source books or podcast transcripts
- long quotations or copyrighted excerpts
- private notes the user did not approve
- secrets, credentials, browser/session data, or API keys
- local absolute paths to source files unless the project itself uses that path
- raw chat transcripts as learning notes

## Refresh Loop

Use `$sj-core-learning-refresh` to audit `docs/steve-jobs/learnings/`.

It should flag:

- stale notes
- duplicates
- contradictions
- weak generic lessons
- low-confidence notes
- malformed frontmatter
- notes that future agents could not retrieve from tags or reuse triggers

The refresh skill recommends `keep`, `update`, `merge`, or `archive`; it does not delete automatically.

## Lifecycle Cleanup

CE-style install manifests and legacy cleanup are not needed while skill names remain stable. Add lifecycle cleanup only if `sj-*` skills are renamed, removed, or moved in a way that would leave stale loose-skill installs behind.
