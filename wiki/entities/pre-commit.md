---
type: entity
title: pre-commit
created: 2026-04-07
updated: 2026-04-07
tags: [pre-commit, git, automation, quality]
related: [dbt-checkpoint, ci-cd-for-data-pipelines]
sources: ["dbt-checkpoint.md"]
---
# pre-commit

**pre-commit** is a framework for managing and maintaining multi-language pre-commit hooks. It is the execution framework used by [[dbt-checkpoint]] to run validation hooks before code is committed to version control.

## How It Works

1. A `.pre-commit-config.yaml` file defines which hooks to run
2. Hooks are installed as git hook scripts via `pre-commit install`
3. On `git commit`, hooks automatically run against staged files
4. If any hook fails, the commit is blocked until issues are resolved

## Key Features

- **Multi-language support**: Hooks can be written in Python, JavaScript, Ruby, Shell, and more
- **Repository-based**: Hooks are defined in external repositories and versioned
- **Lightweight**: Only runs on staged files by default
- **CI/CD compatible**: Can also run in CI pipelines via `pre-commit run --all-files`

## Relationship to dbt-checkpoint

[[dbt-checkpoint]] provides a repository of pre-commit hooks specifically for dbt projects. These hooks are configured in `.pre-commit-config.yaml` and run via the pre-commit framework. The combination enables automated quality validation at commit time for dbt projects.

## Related

- [[dbt-checkpoint]] — Pre-commit hooks for dbt projects
- [[ci-cd-for-data-pipelines]] — Broader CI/CD practices for data workflows