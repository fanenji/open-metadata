---
type: concept
title: dbt Monitoring Best Practices
created: 2026-05-07
updated: 2026-05-07
tags: [dbt, monitoring, best-practices]
related: [dbt-cloud, dbt-artifacts, dbt-observability-implementation, dbt-core-monitoring-guide, data-observability-definition]
sources: ["Understanding dbt. Monitoring.md"]
---
# dbt Monitoring Best Practices

A set of recommended practices for monitoring dbt projects, applicable to both dbt Cloud and dbt Core environments. These practices help teams catch failures early, track performance, and build trust in data pipelines.

## Best Practices

### Track Every Run
Always log runs — whether using dbt Cloud's Job History or saving `run_results.json` and `dbt.log` in dbt Core. Set up retention or export logic to analyze trends over time.

### Monitor Model Performance
Keep an eye on:
- Which models take the longest to run
- Models that frequently fail
- Downstream impacts of failed runs

This helps prioritize refactoring and optimization.

### Build Custom Checks
Add quality checks as part of the run:
- Use dbt tests (not null, unique, relationships)
- Create custom tests for business logic
- Parse `run_results.json` to track test failures over time

### Set Up Notifications
- **dbt Cloud**: Configure email or Slack notifications for failed jobs.
- **dbt Core**: Hook up scheduler or scripts to alert when things go wrong.

### Share Visibility with the Team
Build a small dashboard or document where others can check the latest run status, broken models, or upcoming changes.

## Related Concepts

- [[data-observability-definition]] — The broader framework of data observability dimensions.
- [[dbt-observability-implementation]] — A structured, dbt-native approach to monitoring.
- [[dbt-core-monitoring-guide]] — Practical guide for dbt Core users.