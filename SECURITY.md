# Security

Please report security issues through GitHub issues or a private channel to the repository owner if public disclosure would expose user risk.

## Scope

This repo ships Markdown skills, JSON manifests, and small shell/Python validation scripts. It does not ship a server, background daemon, credential store, or networked runtime.

## Handling Secrets

Do not add API keys, tokens, private transcripts, proprietary notes, or local machine paths to this repository. If a skill needs user-specific context, keep that context in the user's local project files, not in this public plugin.

## Validation

Run:

```bash
./scripts/validate.sh
```

The validator checks manifest structure and makes sure runtime skills reference only local support files.
