---
type: concept
title: dbt Testing Workflow
created: 2026-04-04
updated: 2026-04-04
tags: [dbt, testing, workflow, development]
related: [dbt-testing-patterns, dbt-testing-motivation, dbt-unit-testing-challenges, dbt-smoke-testing, dbt-mocking-patterns, CI-CD-for-data-pipelines]
sources: ["State of testing in dbt - In-Depth Discussions.md"]
---
# dbt Testing Workflow

The testing workflow in dbt encompasses when and how tests are written and executed during the software development lifecycle. The post suggests mapping out the current development-time testing workflow and designing an improved workflow as a product initiative.

## Current Workflow

Based on community research, the current development-time testing workflow in dbt has these characteristics:

- **Primitive tests only**: Schema tests and data tests are the only built-in options.
- **Deployment-time focus**: Most testing occurs at deployment time (smoke tests in CI/CD), not during development.
- **Ad-hoc development testing**: Developers who want to test during development must build custom solutions (fixed datasets, external frameworks, macro-based mocking).
- **High barrier to entry**: Achieving advanced testing requires expert-level dbt knowledge or significant individual time investment.

## Improved Workflow (Suggested)

The post suggests designing an improved workflow that would:

- **Enable development-time testing**: Allow developers to test models during development, not just at deployment.
- **Provide first-class mocking**: Make mocking a dbt model and source a well-designed construct.
- **Reduce iteration time**: Address the long pipeline execution times that make TDD impractical.
- **Standardize best practices**: Document what a well-tested model looks like and when tests should be run.

## Testing Points in the Lifecycle

- **Development-time**: Unit tests, mocking, fixed dataset testing (currently difficult).
- **Continuous Integration**: Non-regression tests, integration tests (partially supported via `--defer`).
- **Continuous Deployment**: Smoke tests in blue/green deployment (successfully demonstrated by Claus).

## Connections

The testing workflow connects to [[CI-CD-for-data-pipelines]] (where testing fits in the pipeline), [[shift-left-data-quality]] (moving testing earlier), and the specific testing patterns documented in [[dbt-testing-patterns]], [[dbt-smoke-testing]], [[dbt-unit-testing-challenges]], and [[dbt-mocking-patterns]].
