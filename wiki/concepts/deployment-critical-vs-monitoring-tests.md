---
type: concept
title: Deployment-Critical vs. Non-Deployment-Critical Data Quality Tests
created: 2026-04-04
updated: 2026-04-04
tags: [data-quality, testing, ci-cd, deployment]
related: [data-ci-cd-principles, data-release-pipeline, data-quality-certification-vs-usability-certification, dbt-testing-patterns]
sources: ["How CI-CD should look for Data teams.md"]
---
# Deployment-Critical vs. Non-Deployment-Critical Data Quality Tests

A distinction between two categories of data quality tests in CI/CD pipelines, introduced by [[Hugo Lu]] in the context of [[data-ci-cd-principles]].

## Deployment-Critical Tests
Tests that block deployment if they fail. These tests should run in the staging environment before data is promoted to production. Examples include schema validation, null checks on key columns, and referential integrity constraints.

## Non-Deployment-Critical Tests
Tests that monitor data health post-deployment but do not block the release. These tests catch issues that arise from exogenous changes (e.g., third-party API schema changes) that could affect data quality in production. They fall under proactive system health monitoring.

## Rationale
The distinction is important because software can be affected by exogenous changes post-deployment (e.g., a third-party API changes its schema), but data in production should not be affected by such changes if proper staging validation is in place. If a test can ascertain data quality in production, it should live in the staging environment as a deployment-critical test.

## Relationship to Existing Wiki
This concept parallels the existing [[data-quality-certification-vs-usability-certification]] distinction, which separates "how good" data is from "how ready" it is. Both frameworks categorize quality assessments by their purpose and timing in the pipeline.