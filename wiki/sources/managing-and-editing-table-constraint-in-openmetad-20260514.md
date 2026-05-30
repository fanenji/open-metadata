---
type: source
title: "Managing and Editing Table Constraint in OpenMetadata - OpenMetadata Documentation"
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, data-discovery, table-constraints, foreign-keys, metadata-ingestion]
related: [table-constraints, data-discovery, data-lineage, metadata-ingestion-workflow, openmetadata-features]
sources: ["managing-and-editing-table-constraint-in-openmetad-20260514.md"]
authors: [OpenMetadata]
year: 2026
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/data-discovery/table-constraint"
venue: "OpenMetadata Documentation"
---

# Managing and Editing Table Constraint in OpenMetadata

This official OpenMetadata documentation page (v1.12.x) describes how table constraints — specifically foreign key relationships — are captured during metadata ingestion and how users can view and edit them through the OpenMetadata UI. It is categorized under the Data Discovery section of the documentation.

## Key Content

- **Table constraints** are integral to understanding relationships between tables, enhancing data discovery, and facilitating comprehensive data lineage tracking.
- By default, the ingestion process captures these constraints, allowing users to visualize and manage table relationships.
- **Viewing constraints:** After metadata ingestion, foreign key relationships can be explored on the Table Details Page, where constraints are displayed detailing relationships between the current table and related tables.
- **Editing constraints:** Requires appropriate edit permissions. Users navigate to the table's schema view to modify constraints. If editing options are unavailable, it may indicate insufficient permissions or that the feature is not supported in the current version.

## Limitations

- The document does not specify which connectors support table constraint ingestion.
- It does not indicate whether constraint ingestion is configurable (e.g., can be disabled).
- The types of constraints beyond foreign keys (e.g., primary keys, unique constraints, check constraints) are not enumerated.
- The specific permissions required to edit constraints are not detailed beyond "appropriate permissions."

## Relevance to Wiki

This source fills a gap in the wiki's coverage of data discovery features. It connects to [[data-lineage]] (foreign key constraints contribute to lineage visualization), [[data-discovery]] (constraints aid in discovering asset relationships), and [[metadata-ingestion-workflow]] (constraints are captured by default during ingestion).