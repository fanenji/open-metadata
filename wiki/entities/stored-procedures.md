---
type: entity
title: Stored Procedures
created: 2026-05-14
updated: 2026-05-14
tags: [entity-type, lineage, ingestion]
related: [data-lineage, unified-metadata-graph, search-indexes]
sources: ["OpenMetadata Community Meeting Oct 2023 Release 1 2 0 datamesh openmetadata.md"]
---
# Stored Procedures

Stored Procedures are a new entity type introduced in [[OpenMetadata]] 1.2.0, representing database stored procedures as ingestible metadata entities with lineage tracking and code display.

## Capabilities

- **Code display**: Shows the procedure definition — Python functions if defined in Python, SQL definitions if defined in SQL.
- **Lineage tracking**: Stored procedures appear as edges in [[data-lineage|lineage]] graphs when they transform data between tables (e.g., moving data from a silver to a gold database).
- **Edge details**: When viewing lineage, clicking on a stored procedure edge displays the procedure code, language, and the exact query that was executed.
- **Column-level lineage**: If the procedure performs transformations (e.g., `SELECT *`), column-level lineage is populated from source to target entities.

## Example Use Case

A stored procedure that transforms a `users` table from a silver database into a gold database will appear as an edge in the lineage graph. Users can inspect the procedure's code and understand exactly how data was transformed.