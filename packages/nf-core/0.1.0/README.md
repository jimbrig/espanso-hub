# nf-core related commands for espanso

## What is nf-core?

[nf-core](https://nf-co.re/) is a community effort for building high-quality, reproducible bioinformatics pipelines with Nextflow.  
It provides:

- Standardized pipeline structure
- Automated linting and CI checks
- Consistent documentation and release practices
- Shared best practices across many pipelines

## What this espanso package is for

This package adds quick text expansions for frequent nf-core comments used in:

- GitHub pull request reviews
- GitHub issues
- Slack support and collaboration

The goal is to make repeated feedback faster, clearer, and more consistent.

## What the commands expand to

The shortcuts are designed for common review themes, such as:

- ✅ Positive feedback (thanks, approval, encouragement)
- 🧹 Style and formatting suggestions
- 🧪 Testing and reproducibility reminders
- 📚 Documentation requests
- 🧱 Pipeline structure and nf-core guideline checks
- 🔁 Requests for follow-up changes

Each trigger inserts a longer, ready-to-send comment so routine responses can be posted with minimal typing.

## Typical usage

1. Type a configured trigger in GitHub or Slack.
2. Let espanso expand it into the full comment.
3. Adjust project-specific details before sending.

## Notes

- Keep expansions short, respectful, and actionable.
- Prefer links to nf-core docs when suggesting standards.
- Update triggers regularly as team conventions evolve.