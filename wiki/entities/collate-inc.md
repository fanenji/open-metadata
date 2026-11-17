---
sources: [OpenMetadata Community Meeting Oct 2023 Release 1 2 0 datamesh openmetadata.md, Announcing OpenMetadata 1.12 1.md]
tags: [organization, openmetadata, saas, collate, enterprise, managed-service]
related: [openmetadata, cost-analysis, knowledge-center, auto-classification, agentic-ai]
type: entity
title: Collate, Inc.
created: 2026-05-14
updated: 2026-07-07
---
# Collate, Inc.

**Collate, Inc.** is the company behind the [[openmetadata|OpenMetadata]] open-source project. It provides commercial support, drives the project's development roadmap, and offers a SaaS version of the platform called **Collate Cloud** (available at `https://cloud.getcollate.io/`). Collate extends OpenMetadata with enterprise-grade features, support, and hosting.

## Open-Core Model

Collate maintains an open-core model where the core metadata management platform is fully open-source, while certain advanced operational and enterprise features are exclusive to the Collate Cloud SaaS offering.

## Collate 1.12 Features

Released alongside OpenMetadata 1.12 (Feb 2026), Collate 1.12 introduces:

### AI & Automation
- **AI Studio**: Visibility and control over platform agents with customizable prompts and restore-to-defaults capability. Foundation for custom agent creation in 2.0
- **Custom Auto Classification**: ML-powered recognizers for any classification type (not just PII), with feedback loops for continuous improvement
- **AskCollate Enhancements**: Expanded entity support (metrics, knowledge center, dashboard data models), company context-awareness from glossary, MS Teams integration, enhanced thinking transparency, automatic chart generation

### Data Operations
- **Data Diff Column/Row Analysis**: Granular visual comparison of source vs. target table differences at column, row, and character level
- **GitHub Metadata Sink (beta)**: Metadata under version control — code review workflows, CI/CD integration, treating metadata with the same governance rigor as application code

### Platform Extensions
- **SQL Studio Extensions**: Postgres and Redshift support alongside existing Snowflake, Trino, BigQuery; secrets manager and hybrid deployment options
- **Metadata Exporter — Entity History**: Export complete change tracking to Snowflake, BigQuery, or Databricks for custom BI dashboarding
- **Learning Resources**: Contextual tutorials and videos throughout the UI with admin customization
- **New Connectors**: Microsoft Fabric (beta), Dremio, MuleSoft

## Earlier Collate-Exclusive Features

Features announced as SaaS-only in the 1.2.0 release include:

- **[[cost-analysis|Cost Analysis]]**: Used vs. unused asset tracking with size and storage cost estimation.
- **[[knowledge-center|Knowledge Center]]**: Full-page article creation and documentation system.

## Community Engagement

The company drives community engagement through regular community meetings, webinars, and the OpenMetadata Slack community.

## See Also

- [[openmetadata]] — Open-source platform
- [[auto-classification]] — Auto Classification capabilities
- [[collate-vs-openmetadata-comparison]] — Upgrading from OpenMetadata to Collate
