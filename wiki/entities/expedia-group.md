---
type: entity
title: Expedia Group
created: 2026-05-22
updated: 2026-05-07
tags: [organization, case-study, company, apache-iceberg, enterprise-adoption]
related: [write-audit-publish-pattern, apache-iceberg, iceberg-enterprise-adoption-signals]
sources: ["Chill Your Data with Iceberg Write Audit Publish.md", "Is Apache Iceberg Melting?.md"]
---
# Expedia Group

**Expedia Group** is a major travel technology company and an enterprise adopter of **Apache Iceberg**. The company's engineering blog describes a data lake on Amazon S3 backed by Hive Metastore and the complexity that created, framing table formats including Iceberg as an alternative built to take advantage of the cloud and provide ACID transactions, time travel, and partition spec evolution. Expedia Group serves as a primary case study for the effectiveness of the **Write-Audit-Publish (WAP)** pattern using Apache Iceberg.

## Case Study: WAP Implementation

Expedia transitioned from a traditional UAT (User Acceptance Testing) model—which required duplicating production tables and re-running ETL pipelines—to an Iceberg-based branching model.

### Results
*   **Storage Savings**: Achieved approximately a **30% reduction in storage consumption** by replacing physical UAT tables with temporary Iceberg branches.
*   **Cost Reduction**: Achieved up to a **99% reduction in release costs** by eliminating the need to execute the same ETL pipelines twice (once for testing and once for production).
*   **Operational Efficiency**: Enabled faster, safer deployments with a traceable audit history and nearly instantaneous publishing via metadata updates.