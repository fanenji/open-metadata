---
type: source
title: "Understanding dbt: Monitoring"
created: 2026-05-07
updated: 2026-05-07
tags: [dbt, monitoring, tutorial]
related: [dbt-cloud, dbt-artifacts, dbt-observability-implementation, dbt-core-monitoring-guide, dbt-monitoring-best-practices, mykola-bohdan-vynnytskyi]
sources: ["Understanding dbt. Monitoring.md"]
authors: [Mykola-Bohdan Vynnytskyi]
year: 2025
url: "https://mbvyn.medium.com/understanding-dbt-monitoring-2844411093d2"
venue: Medium
---
# Understanding dbt: Monitoring

A beginner-friendly tutorial on monitoring dbt projects, covering both dbt Cloud's built-in features and dbt Core's artifact-based approach. The article explains how to track runs, monitor performance, set up alerts, and build custom dashboards using dbt artifacts like `run_results.json` and `manifest.json`.

## Key Topics

- **Why monitoring matters**: Catching failures early, tracking performance, building trust in data pipelines.
- **dbt Cloud monitoring**: Run History Dashboard, Slack/Email/Webhook alerts, CI/CD monitoring, and the dbt Cloud API.
- **dbt Core monitoring**: Parsing logs and artifacts (`run_results.json`, `manifest.json`, `dbt.log`) for custom monitoring.
- **Custom monitoring dashboards**: Building visualizations from parsed artifact data using tools like Google Data Studio, Tableau, or Streamlit.
- **DIY Slack alerts**: Script-based alerting from parsed `run_results.json`.
- **Best practices**: Track every run, monitor model performance, build custom checks, set up notifications, and share visibility with the team.

## Relevance

This source provides a practical, accessible introduction to dbt monitoring concepts. It reinforces and extends existing wiki content on [[dbt-observability-implementation]] and [[dbt-artifacts]] with concrete, beginner-friendly examples. It is a tutorial, not a definitive reference, but offers actionable patterns for teams using dbt Core.