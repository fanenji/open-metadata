---
type: concept
title: Table Constraints
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, data-discovery, foreign-keys, metadata-ingestion, data-lineage]
related: [data-discovery, data-lineage, metadata-ingestion-workflow, openmetadata-features, roles-and-policies]
sources: ["managing-and-editing-table-constraint-in-openmetad-20260514.md"]
---

# Table Constraints

In OpenMetadata, table constraints refer primarily to foreign key relationships between tables that are captured during metadata ingestion and displayed in the UI. They enhance data discovery by showing how tables relate to one another and facilitate comprehensive data lineage tracking.

## How Constraints Are Captured

By default, the metadata ingestion process captures table constraints from connected data sources. This means that when a connector ingests metadata from a database, foreign key relationships defined in that database are automatically extracted and stored in OpenMetadata's [[unified-metadata-graph]].

**Note:** The official documentation does not specify which connectors support constraint ingestion, whether it is configurable (e.g., can be disabled), or what constraint types beyond foreign keys are supported.

## Viewing Table Constraints

Once metadata ingestion is complete, users can view constraints by:

1. Navigating to the Table Details Page for the desired table.
2. Exploring the displayed constraints, which detail relationships between the current table and its related tables.

This visualization aids in understanding data dependencies and supports effective data governance.

## Editing Table Constraints

To modify table constraints:

1. **Ensure appropriate permissions:** The user must have the necessary edit permissions for the table. If editing options are unavailable, it may indicate insufficient permissions or that the feature is not supported in the current OpenMetadata version.
2. **Access the table's schema:** Navigate to the table's schema view within the OpenMetadata UI.
3. **Modify constraints:** Edit the table constraint as required.

If editing is unavailable, users should consider upgrading to the latest version or consulting their [[openmetadata-administration|administrator]].

## Relationship to Other Concepts

- **[[data-lineage]]:** Foreign key constraints directly support lineage tracking by showing table relationships.
- **[[data-discovery]]:** Constraints aid in discovering asset relationships and understanding data dependencies.
- **[[metadata-ingestion-workflow]]:** Constraints are captured during the ingestion process by default.
- **[[roles-and-policies]]:** Editing constraints requires appropriate permissions, linking to the RBAC system.
- **[[openmetadata-features]]:** Table constraints are a feature of the data discovery module.

## Open Questions

- Which connectors support table constraint ingestion?
- Is constraint ingestion configurable (e.g., can it be disabled)?
- What types of constraints beyond foreign keys are supported (e.g., primary keys, unique constraints, check constraints)?
- What specific permissions are required to edit constraints?