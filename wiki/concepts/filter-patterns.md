---
type: concept
title: Filter Patterns
created: 2026-05-14
updated: 2026-05-14
tags: [metadata-ingestion, filtering, configuration, performance]
related: [metadata-agent, metadata-ingestion-workflow, service-connection]
sources: ["how-to-ingest-metadata-official-documentation---op-20260514.md"]
---

# Filter Patterns

Inclusion and exclusion rules applied during metadata ingestion to control which assets are pulled from a source system into OpenMetadata. Filter patterns operate at three levels — databases, schemas, and tables — and are critical for both ingestion performance and metadata relevance.

## Pattern Levels

| Level | Scope | Purpose |
|-------|-------|---------|
| **Database Filter Pattern** | Databases within a service connection | Limit ingestion to specific databases when a service contains many |
| **Schema Filter Pattern** | Schemas within selected databases | Exclude internal or temporary schemas from ingestion |
| **Table Filter Pattern** | Tables within selected schemas | Focus ingestion on business-relevant tables, excluding test or staging data |

## Filtering Modes

### Simple Name Filtering
By default, patterns match against simple object names (e.g., `sales_db`, `public`). This is sufficient for most use cases where object names are unique within their scope.

### FQN (Fully Qualified Name) Filtering
When the **Use FQN For Filtering** toggle is enabled on the [[metadata-agent|Metadata Agent]], patterns are matched against fully qualified names (e.g., `sales_db.public.orders`). This provides more precise control in environments where object names may collide across different hierarchies.

## Pattern Syntax

Patterns support inclusion and exclusion rules. The exact syntax depends on the connector, but typically supports:
- Exact name matches
- Wildcard patterns (e.g., `sales_*`)
- Exclusion prefixes (e.g., `!test_*` to exclude test databases)

## Best Practices

- **Start broad, then narrow**: Begin with inclusive patterns and refine based on observed metadata volume
- **Exclude system schemas**: Always exclude internal/system schemas (e.g., `information_schema`, `pg_catalog`) to reduce noise
- **Use FQN filtering for complex hierarchies**: When multiple databases share schema or table names, FQN filtering prevents ambiguity
- **Review periodically**: As source systems evolve, filter patterns may need updates to capture new assets or exclude deprecated ones