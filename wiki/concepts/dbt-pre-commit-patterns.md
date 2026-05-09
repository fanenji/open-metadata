---
type: concept
title: dbt pre-commit Patterns
created: 2026-04-04
updated: 2026-04-04
tags: [dbt, pre-commit, ci-cd, governance, automation]
related: [dbt-osmosis, dbt-schema-synchronization, dbt-project-scaffolding, dbt-data-contract-implementation]
sources: ["dbt-osmosis Automation for Schema and Documentation Management in dbt.md"]
---
# dbt pre-commit Patterns

Pre-commit integration for dbt enforces YAML consistency, documentation standards, and schema governance as automated repo policies rather than manual best practice suggestions.

## dbt-osmosis pre-commit Hook

[[dbt-osmosis]] provides a pre-commit hook (`dbt-osmosis-yaml`) that validates and corrects YAML files on every commit:

```yaml
repos:
  - repo: https://github.com/z3z1ma/dbt-osmosis
    rev: v0.15.0
    hooks:
      - id: dbt-osmosis-yaml
```

## Benefits

- Every commit validates and corrects YAML automatically.
- No PR introduces inconsistent schemas.
- Documentation quality becomes a repo policy, not a suggestion.
- Reduces manual PR review burden for schema changes.

## Use Cases

- **Large teams**: Guarantees order without endless PR reviews.
- **Governance and compliance**: Regulated industries can enforce documentation standards automatically.
- **CI/CD pipelines**: Blocks inconsistent code before it reaches production.

## Relationship to Other dbt Practices

Pre-commit patterns complement [[dbt-project-scaffolding]] by adding an enforcement layer to project structure conventions. They also work alongside [[dbt-data-contract-implementation]] to ensure YAML files remain consistent before contract validation runs.
