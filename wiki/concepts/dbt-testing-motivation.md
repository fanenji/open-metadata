---
type: concept
title: dbt Testing Motivation
created: 2026-04-04
updated: 2026-04-04
tags: [dbt, testing, motivation, software-testing]
related: [dbt-testing-patterns, dbt-unit-testing-challenges, dbt-smoke-testing, dbt-mocking-patterns, dbt-testing-workflow, CI-CD-for-data-pipelines, shift-left-data-quality]
sources: ["State of testing in dbt - In-Depth Discussions.md"]
---
# dbt Testing Motivation

The "why" of testing in dbt, drawing from software engineering principles and community research. Testing in dbt serves the same fundamental purposes as testing in any software project: reducing unexpected outcomes, preventing regressions, inspiring confidence, and documenting behavior through edge-case illustration.

## Why Test in dbt?

With software tests, an engineer can:

- **Reduce likelihood of unexpected outcomes** or side-effects from code or system under test.
- **Reduce likelihood** that a current or future code change will introduce a system error.
- **Inspire confidence** in the test author and others that the code or system works as intended.
- **Document code and system behavior** by illustrating edge-cases.

## The Gap in dbt

dbt offers two primitive test types: schema tests (constraint enforcement) and data tests (arbitrary SQL assertions). While these are useful, they leave a gap for advanced testing needs. Community research documented in [[State of testing in dbt - In-Depth Discussions]] shows that:

- There is no tool for deterministic re-creation of conditions (Petyo Pahunchev).
- Long pipeline execution times make TDD impractical (Michael Kaminsky).
- SQL makes unit test assertions "unnatural" (MichelleArk).
- Successful approaches (fixed datasets, smoke testing) exist but are not easily reproducible or standardized.

## The Need for Advanced Testing

The community desires capabilities known in software testing: mocking, unit testing, test-driven development (TDD), and behavioral-driven development (BDD). These capabilities would enable development-time testing that catches issues before code reaches production, complementing deployment-time smoke testing.

## Connections

This concept provides the foundational motivation for [[dbt-testing-patterns]] and connects to [[CI-CD-for-data-pipelines]] (testing as a CI/CD practice) and [[shift-left-data-quality]] (moving testing earlier in the development lifecycle).
