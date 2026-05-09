---
type: concept
title: Data Observability
created: 2026-04-29
updated: 2026-04-29
tags: [data-observability, data-governance, data-quality, data-lineage]
related: [data-catalog-tool-comparison, data-catalog-critique, data-contract-observability, data-mesh, datahub, openmetadata]
sources: ["Data Observability is Key A Hands-on Comparison of Open Source Data Catalog Tools.md"]
---
# Data Observability

Data observability is the ability to understand the health, quality, and state of data across an organization. It is a foundational capability for data-driven decision-making and is enabled by [[data-catalog-tool-comparison|data catalog tools]].

## Seven Dimensions of Data Observability

Based on the source article, data observability addresses the following dimensions:

1. **Data Freshness**: How up-to-date is the data?
2. **Data Security/Governance**: Who has access? Does the data contain sensitive information (PII)?
3. **Data Redundancy**: Is the data already available from another team?
4. **Data Discrepancy**: How can data be integrated across the organization with consistent standards?
5. **Data Documentation**: What does an attribute mean? What is the purpose of a dataset?
6. **Data Quality**: What checks are performed? How does quality evolve over time?
7. **Data Lineage**: Who uses which data? Who will be affected by schema changes?

## Relationship to Data Catalogs

Data catalogs serve as the foundation for data observability by providing a single source of truth for metadata. They enable:

- Discovery of available data assets
- Governance through access control and PII detection
- Quality monitoring through profiling and testing
- Impact analysis through lineage tracking

## Connection to Existing Wiki

Data observability is closely related to [[data-contract-observability]], which focuses on monitoring data contract violations. While data contracts provide the agreement between producers and consumers, data observability provides the broader monitoring infrastructure. The [[data-catalog-critique]] argues that traditional catalogs fail to deliver on observability promises, but modern tools like [[DataHub]] and [[OpenMetadata]] address many of these concerns through integrated ingestion, profiling, and governance features.
