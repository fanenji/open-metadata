---
type: concept
title: Engineering-Led Data Quality
created: 2026-04-29
updated: 2026-04-29
tags: [data-quality, governance, engineering, platform]
related: [data-quality-dimensions, data-quality-score, shift-left-data-quality, data-quality-certification-vs-usability-certification, dbt-data-contract-implementation, great-expectations-for-data-contracts]
sources: ["Defining Data Quality The Foundation of Modern Data Architecture.md"]
---
# Engineering-Led Data Quality

A decision framework for Data Quality (DQ) ownership, contrasting programmatic enforcement by pipeline engineers with investment in dedicated DQ platforms and Data Steward roles.

## Engineering-Led Enforcement (Default)

Most DQ dimensions can be enforced programmatically by pipeline engineers:

- **Timeliness**: Via pipeline orchestration and SLA monitoring.
- **Completeness**: Via schema/row checks and record count comparisons.
- **Uniqueness**: Via constraints and deduplication logic.
- **Validity & Consistency**: Via embedded business rules and standardization.

DQ validations are treated as part of integration and deployment testing — analogous to unit tests in software engineering.

## Dedicated DQ Platform (When Justified)

A centralized DQ platform and Data Steward roles are justified only when the cost of building and maintaining enterprise-wide dashboards, compliance reporting, or cross-domain oversight is outweighed by governance benefits or regulatory requirements.

## Data Stewardship in Context

Like automated testing replaced manual QA in software engineering, data engineering can embed quality directly in pipelines. Dedicated Data Stewards become necessary only for:

- Non-automatable business rule validation
- Regulatory reporting
- Enterprise-wide visibility

Otherwise, stewardship should be distributed among domain data product teams.

## Relationship to Existing Wiki Concepts

This framework supports the [[dbt-data-contract-implementation]] pattern, where contracts are enforced programmatically within dbt pipelines. It also connects to [[great-expectations-for-data-contracts]] as an enforcement engine. The decision framework is context-dependent — teams with compliance requirements may still need dedicated platforms despite engineering-led capabilities.

## Open Questions

- At what scale or governance maturity does a dedicated DQ platform become cost-justified?
- How does this framework apply in regulated industries (finance, healthcare) where audit trails require centralized oversight?