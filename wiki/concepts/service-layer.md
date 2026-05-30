---
type: concept
title: Service Layer
created: 2026-05-14
updated: 2026-05-14
tags: [data-lineage, service-layer, cross-platform, openmetadata]
related: [data-lineage, lineage-layers, openmetadata-connectors]
sources: ["explore-the-lineage-view-official-documentation----20260514.md"]
---
# Service Layer

The Service Layer is one of the five [[lineage-layers]] in the OpenMetadata lineage view. It visualizes how data flows across different platforms and services, such as Hive, Redshift, Power BI, and Tableau.

This layer connects ingestion, transformation, and consumption points, offering a system-level view of the end-to-end data journey. It helps users understand:
- Which source systems feed into which transformation tools.
- How data moves between storage (databases) and analytics (BI tools).
- The overall architecture of the data pipeline across the organization.

The Service Layer is particularly valuable for platform engineers and architects who need to manage cross-platform data dependencies and troubleshoot integration issues.