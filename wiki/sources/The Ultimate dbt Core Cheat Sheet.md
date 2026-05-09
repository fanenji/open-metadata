---
type: source
title: The Ultimate dbt Core Cheat Sheet
created: 2026-04-04
updated: 2026-04-04
tags: [dbt, cheat-sheet, reference, tutorial]
related: [dbt-core-cheat-sheet, dbt-command-reference, dbt-testing-patterns, dbt-macros, dbt-project-scaffolding, dbt-cloud-environments, dbt-slim-ci]
sources: ["The Ultimate dbt Core Cheat Sheet.md"]
authors: [Mihir Samant]
year: 2025
url: "https://towardsdev.com/the-ultimate-dbt-core-cheat-sheet-9a8bb7b99eb6"
venue: "Towards Dev"
---
# The Ultimate dbt Core Cheat Sheet

A practical reference guide for [[dbt Core]] covering project setup, essential commands, model organization patterns, SQL best practices, testing strategies, macros, environment management, and performance optimization. Authored by [[Mihir Samant]] and published on Towards Dev in August 2025.

## Key Topics

- **Project Setup**: `dbt init`, `dbt debug`, `dbt_project.yml` configuration
- **Essential Commands**: `dbt run`, `dbt test`, `dbt build`, `dbt compile`, `dbt retry`, `dbt seed`, `dbt docs generate`, `dbt docs serve`
- **Model Organization**: Staging → Intermediate → Marts folder structure with naming conventions (`stg_`, `int_`, `fct_`, `dim_`)
- **SQL Patterns**: CTE-based modular SQL, staging model templates, `{{ ref() }}` and `{{ source() }}` usage
- **Testing**: Built-in tests (unique, not_null, accepted_values, relationships), custom generic tests, singular tests
- **Macros**: Date spine macro, environment-specific logic with `target.name`, logging with `{{ log() }}`
- **Sources & Seeds**: Freshness thresholds, seed loading and refresh
- **Environment Management**: `profiles.yml` with dev/prod targets, `env_var()` for secrets
- **Performance**: Incremental models, materialization strategies, indexing, partitioning
- **Debugging**: `dbt compile` for SQL inspection, `dbt debug` for connection checks, `dbt clean` for cache clearing

## Relevance to Wiki

This source provides concrete, executable examples that complement the wiki's existing conceptual coverage of [[dbt-testing-patterns]], [[dbt-macros]], [[dbt-project-scaffolding]], [[dbt-cloud-environments]], and [[dbt-slim-ci]]. It introduces practical patterns not yet documented, such as `pre_hook`/`post_hook` for constraint enforcement, `dbt retry` for failed model recovery, and environment-specific logic using `target.name`.