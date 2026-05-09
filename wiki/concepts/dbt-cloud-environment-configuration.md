type: concept
title: dbt Cloud Environment Configuration
created: 2026-04-29
updated: 2026-04-29
tags: [dbt, dbt-cloud, environments, configuration]
related: [dbt-cloud-environments, dbt-git-branching-strategies, direct-promotion, indirect-promotion, dbt-cloud]
sources: ["getting-started-with-git-branching-strategies-and-dbt.md"]
---
# dbt Cloud Environment Configuration

**dbt Cloud Environment Configuration** refers to the mapping of dbt Cloud environments (Development, CI, QA, Production) to specific git branches, databases, and schemas based on the chosen [[dbt-git-branching-strategies]].

## Direct Promotion Configuration

| Environment | Type | Base Branch | Database | Schema |
|---|---|---|---|---|
| Development | development | `main` | `development` | User-specified |
| Continuous Integration | deployment (General) | `main` | `development` | `dev_ci` (overridden) |
| Production | deployment (Production) | `main` | `production` | `analytics` |

## Indirect Promotion Configuration (1:1 Pattern)

| Environment | Type | Base Branch | Database | Schema |
|---|---|---|---|---|
| Development | development | `qa` | `development` | User-specified |
| Feature CI | deployment (General) | `qa` | `development` | `dev_ci` (overridden) |
| Quality Assurance | deployment (Staging) | `qa` | `qa` | `analytics` |
| Release CI | deployment (General) | `main` | `development` | Safe default |
| Production | deployment (Production) | `main` | `production` | `analytics` |

## Indirect Promotion Configuration (Workflow Initiative Pattern)

| Environment | Type | Base Branch | Database | Schema |
|---|---|---|---|---|
| Development | development | `qa` | `development` | User-specified |
| Feature CI | deployment (General) | `qa` | `qa` | `dev_ci` (overridden) |
| Quality Assurance | deployment (Staging) | `qa` | `qa` | `analytics` |
| Release CI | deployment (General) | `main` | `qa` | Safe default |
| Production | deployment (Production) | `main` | `production` | `analytics` |

## Key Principles

- A default database is set at the connection level; deployment environments can override this.
- CI schemas are typically overridden by the CI job to denote the unique PR (e.g., `dbt_cloud_pr_#`).
- The choice of database and schema organization should reflect the branching strategy and workflow needs.