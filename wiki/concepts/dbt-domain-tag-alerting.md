---
type: concept
title: dbt Domain Tag Alerting
created: 2026-04-29
updated: 2026-04-29
tags: [dbt, alerting, tagging, observability, slack]
related: [dbt-observability-implementation, dbt-artifact-upload-macro, dbt-query-comment-pattern, data-incident-management]
sources: ["How to add observability to your dbt deployment - Show and Tell.md"]
---
# dbt Domain Tag Alerting

A pattern for routing dbt failure alerts to the correct owners using domain tags on models. Every model is tagged with exactly one domain (e.g., finance, growth, product), and Looker alerts fire to corresponding Slack user groups.

## Implementation

1. **Tagging** — Every model in the dbt project has a single domain tag: `tag:finance`, `tag:growth`, `tag:product`
2. **Dashboard** — A Looker chart shows the most recent run status for every model in a domain
3. **Alert** — A Looker alert runs every 15 minutes; if a failure is detected, it sends a notification to the #data-alerts Slack channel, tagging the domain's Slack user group (e.g., @finance-domain)
4. **Response** — A domain member investigates using the dashboard, fetches compiled SQL, and debugs

## Coverage

The pattern extends beyond model runs to include:
- Test failures
- Snapshot failures
- Source freshness failures

## Context

This pattern was part of the [[dbt-observability-implementation]] at Snapcommerce. It requires disciplined tagging but provides targeted, actionable alerts that reach the right people without noise.