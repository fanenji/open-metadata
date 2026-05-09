---
type: concept
title: dbt Smoke Testing
created: 2026-04-04
updated: 2026-04-04
tags: [dbt, testing, smoke-testing, deployment]
related: [dbt-testing-patterns, CI-CD-for-data-pipelines, dbt-testing-motivation, dbt-testing-workflow]
sources: ["State of testing in dbt - In-Depth Discussions.md"]
---
# dbt Smoke Testing

Smoke testing is a software testing technique adapted for dbt data pipelines. A smoke test confirms that the system under test looks and/or behaves a certain way. In dbt, smoke tests are used as a last-step check before production cutover, typically in a blue/green deployment pipeline.

## Definition

"Where there's smoke, there's fire." A smoke test is a lightweight check that verifies the system is functioning correctly. If the smoke test fails, the deployment pipeline fails, preventing broken data from reaching production.

## Community Implementation

Claus demonstrated running primitive dbt tests as smoke tests during a blue/green data deployment. The workflow:

1. Build the new data pipeline in a green environment.
2. Run dbt tests (schema tests and data tests) as smoke tests against the green environment.
3. If smoke tests pass, make the dbt output available for use (cutover to green).
4. If smoke tests fail, the deployment fails and the blue environment remains active.

## Characteristics

- **Deployment-time testing**: Smoke tests are run during continuous deployment, not during development.
- **Difficult at development-time**: Smoke tests require the entire production system to be functioning, making them impractical for individual developers.
- **Sign of maturity**: Smoke testing in deployment pipelines indicates a mature data engineering practice.
- **Complements development-time testing**: Smoke tests catch issues that are difficult to detect during development.

## Connections

Smoke testing is a key pattern in [[CI-CD-for-data-pipelines]] and complements [[dbt-unit-testing-challenges]] and [[dbt-mocking-patterns]] (which focus on development-time testing). It is part of the broader [[dbt-testing-patterns]] landscape.
