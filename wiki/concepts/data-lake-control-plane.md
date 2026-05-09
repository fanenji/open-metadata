---
type: concept
title: Data Lake Control Plane
created: 2026-05-07
updated: 2026-05-07
tags: [data-lake, governance, maintenance, orchestration]
related: [iceberg-table-maintenance, iceberg-retention-policies, iceberg-snapshot-tags, lakeops, data-lakehouse, data-lakehouse-versioning-strategies, data-catalog-tool-comparison, data-observability-definition]
sources: ["Why Every Data Lake Needs a Control Plane Lessons from Apache Iceberg.md"]
---
# Data Lake Control Plane

A centralized governance layer that orchestrates and enforces table maintenance policies across catalogs, query engines, and teams in a data lake environment. The control plane addresses the operational gap created by technologies like Apache Iceberg, which deliver performance gains but require disciplined maintenance procedures that diverge without central coordination.

## Key Functions

- **Policy Enforcement**: Ensures consistent retention defaults (snapshot age, minimum snapshots, reference age) across all tables and engines.
- **Cross-Engine Coordination**: Orchestrates maintenance across Spark, Trino/Starburst, Athena, and other query engines that may have different default behaviors.
- **Maintenance Orchestration**: Schedules and coordinates the correct sequence of procedures: compaction → snapshot expiration → orphan cleanup → Puffin file refresh.
- **Tag Lifecycle Management**: Tracks snapshot tags for DR and compliance, enforcing retention periods so tags don't become "immortal" references that block cleanup.
- **Visibility and Reporting**: Provides dashboards showing storage savings, metadata bloat, and compliance status across the entire lake.

## Relationship to Existing Concepts

The control plane concept is related to but distinct from [[data-catalog-tool-comparison]] (which focuses on metadata discovery) and [[data-observability-definition]] (which focuses on monitoring). A control plane is an **active governance** layer that enforces policies, not just observes or catalogs them. It can be implemented as a separate product (e.g., [[LakeOps]]) or potentially built with existing tools like dbt, Airflow, and OpenMetadata.

## Open Questions

- Is a control plane a separate product category, or can it be implemented with existing orchestration and governance tools?
- How does the control plane interact with [[nessie-catalog-versioning]] and [[lakefs-file-versioning]]?
- What are the concrete cost savings from snapshot expiration? The article claims savings but provides no quantitative benchmarks.