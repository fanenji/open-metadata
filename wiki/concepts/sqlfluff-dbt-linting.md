---
type: concept
title: SQLFluff Linting for dbt
created: 2026-04-29
updated: 2026-04-29
tags: [sqlfluff, linting, dbt, code-quality]
related: [dbt-ci-cd-github-actions, sqlfluff, dbt-pre-commit-patterns, implementing-cicd-for-dbt-first-steps]
sources: ["Implementing CICD for dbt First Steps.md"]
---
# SQLFluff Linting for dbt

The practice of using [[SQLFluff]] to enforce SQL code quality and consistency in [[dbt]] projects. SQLFluff is configured with a dbt templater to correctly parse dbt's Jinja syntax and supports custom rule sets for organization-specific standards.

## Configuration

A `.sqlfluff` file in the project root specifies the templater and SQL dialect:

```ini
[sqlfluff]
templater = dbt
dialect = snowflake
```

A `.sqlfluffignore` file excludes folders from linting:

```
analysis/
macros/
dbt_packages/
target/
```

## Custom Rules

SQLFluff supports custom rules for indentation, capitalization, and other style preferences:

```ini
[sqlfluff:indentation]
indented_joins = False
indented_using_on = True
template_blocks_indent = False

[sqlfluff:rules:capitalisation]
keywords = lower
```

## Integration with CI/CD

SQLFluff is typically run as a job in a [[GitHub Actions]] workflow on every pull request to ensure code quality before merging.