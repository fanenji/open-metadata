---
type: concept
title: Column-Level Lineage
created: 2026-05-14
updated: 2026-05-14
tags: [data-lineage, column-lineage, field-level-lineage, openmetadata]
related: [data-lineage, lineage-layers, data-quality]
sources: ["explore-the-lineage-view-official-documentation----20260514.md"]
---
# Column-Level Lineage

Column-level lineage is the ability to trace the flow and transformation of individual fields (columns) across tables, pipelines, and dashboards. In OpenMetadata, this is explored through the **Column Layer** of the [[lineage-layers]] framework.

When clicking on a table in the lineage view, the UI displays the list of columns and their column-level lineage connections. This granularity helps data engineers and analysts understand data dependencies at the attribute level — for example, tracing how `customer_id` flows from a source table through a transformation pipeline into a target table.

Column-level lineage is automatically ingested for database views and can be manually added or edited. It is a critical feature for impact analysis, debugging data quality issues, and regulatory compliance (e.g., GDPR data flow mapping).