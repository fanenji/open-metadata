---
type: concept
title: dbt Core Monitoring Guide
created: 2026-05-07
updated: 2026-05-07
tags: [dbt, monitoring, core, artifacts]
related: [dbt-artifacts, dbt-observability-implementation, dbt-monitoring-best-practices, dbt-cloud, mykola-bohdan-vynnytskyi]
sources: ["Understanding dbt. Monitoring.md"]
---
# dbt Core Monitoring Guide

A practical approach to monitoring dbt Core projects using logs and artifacts, without the built-in UI of dbt Cloud. This guide covers parsing `run_results.json`, `manifest.json`, and `dbt.log` for custom dashboards, alerts, and performance tracking.

## Key Artifacts

- **run_results.json**: Contains details about what ran, status (success, error, skipped), and execution time for each model.
- **manifest.json**: Contains metadata about the project, models, dependencies, tags, and configurations.
- **dbt.log**: Full log output of the run, including detailed tracebacks for errors.

## Common Use Cases

- **Quick checks**: Open `run_results.json` to see which models ran, their durations, and status.
- **Troubleshooting**: Use `dbt.log` for detailed error tracebacks.
- **Performance analysis**: Sort `run_results.json` by execution time to identify slow models.
- **Alerts**: Write a script to parse `run_results.json` and trigger Slack messages for failed models.

## Building Custom Dashboards

Parse `run_results.json` regularly, store results in a database, and visualize:
- Run durations over time
- Failure rate per model
- Which models fail most often

Tools: Google Data Studio, Tableau, Streamlit, Flask, or even a Notion page.

## DIY Slack Alerts

A script (Python, Airflow, GitHub Actions) that:
1. Parses `run_results.json` after every run
2. Checks for failed models
3. Sends a Slack message with model name, error details, and duration

## Related

- [[dbt-observability-implementation]] — A more structured, dbt-native approach using Jinja variables and on-run-end hooks.
- [[dbt-artifacts]] — General documentation of dbt artifact files and their structure.
- [[dbt-monitoring-best-practices]] — Best practices for monitoring dbt projects.