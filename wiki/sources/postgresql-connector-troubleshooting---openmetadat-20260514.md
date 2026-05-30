---
type: source
title: "PostgreSQL Connector Troubleshooting - OpenMetadata Documentation"
created: 2026-05-14
updated: 2026-05-14
tags: [postgresql, connector, troubleshooting, ingestion, lineage, pg-stat-statements]
related: [postgresql-connector, pg-stat-statements, ingestion-pipeline-troubleshooting, workflow-deployment-error, postgresql-iam-authentication, stored-procedure-lineage]
sources: ["postgresql-connector-troubleshooting---openmetadat-20260514.md"]
---

# PostgreSQL Connector Troubleshooting - OpenMetadata Documentation

This source is the official troubleshooting guide for the PostgreSQL connector in OpenMetadata v1.12.x. It covers common errors and their resolutions, including Workflow Deployment Error, debug logging, permission issues, `pg_stat_statements` relation does not exist, incomplete or missing lineage/usage data, unsupported PostgreSQL version errors, network connectivity errors (`no pg_hba.conf entry for host`), and IAM authentication failures (`PAM authentication failed`).

The document provides detailed diagnostic steps, error messages, and configuration solutions for each scenario. It is a critical reference for operators and administrators managing PostgreSQL metadata ingestion pipelines.

Key topics include:
- **Workflow Deployment Error**: A recoverable partial failure where the Ingestion Pipeline Entity is created but no workflow runs; resolved by editing and re-deploying the pipeline.
- **Debug Logging**: Procedure to enable verbose logs for any ingestion workflow via the UI.
- **pg_stat_statements**: The root cause of three distinct issues (extension not enabled, fixed-size eviction, server restart clearing entries) with three mitigation strategies (increase `pg_stat_statements.max`, run ingestion every 1-2 hours, use custom query source).
- **Unsupported PostgreSQL Version**: The `column "relispartition" does not exist` error indicates a version below the minimum supported.
- **Network Connectivity**: `no pg_hba.conf entry for host` error resolved by IP whitelisting, SSL mode adjustment, and Azure firewall rules.
- **IAM Authentication**: `PAM authentication failed` error requires three conditions: RDS IAM DB authentication enabled, user with `rds_iam` grant, and AWS role with `rds-db:connect` permission.
