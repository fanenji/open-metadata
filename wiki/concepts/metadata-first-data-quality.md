---
type: concept
title: Metadata-First Data Quality
created: 2026-04-08
updated: 2026-04-08
tags: [data-quality, metadata, architecture, openmetadata]
related: [openmetadata-data-quality, no-code-data-quality, data-quality-resolution-workflow, data-catalog-critique, embedded-metadata]
sources: ["Simple, Easy, and Efficient Data Quality with OpenMetadata.md"]
---
# Metadata-First Data Quality

Metadata-first data quality is an architectural approach where data quality validation is built on top of a centralized metadata standard, rather than being implemented as a standalone tool or service. This is the core design philosophy behind [[OpenMetadata]]'s data quality module.

## Key Principles

1. **Metadata as Foundation**: All data quality tests, results, and context are stored in a centralized metadata repository, eliminating siloed duplicate tests and providing unified visibility.

2. **Reuse Existing Connections**: Data quality tests reuse metadata and data source connections already established by the metadata platform, reducing setup time from hours to minutes.

3. **Complete Context for Debugging**: When a test fails, the metadata platform provides lineage, schema changes, ownership, and versioning information in one place, eliminating the need to jump between tools.

4. **Unified Governance**: Data quality becomes part of the broader metadata governance framework, enabling organizational-level health dashboards and resolution workflows.

## Contrast with Standalone DQ Tools

| Aspect | Metadata-First | Standalone Tools (Great Expectations, Soda) |
|--------|---------------|---------------------------------------------|
| Setup | Reuses existing metadata/connections | Requires separate connection setup and metadata duplication |
| Context | Lineage, schema, ownership available natively | Limited to test results only |
| Collaboration | Built-in conversations, ownership, resolution workflows | Requires external tools |
| Visibility | Organizational health dashboard | Per-project dashboards |
| User Base | No-code UI for business users + extensibility for power users | Primarily technical users (Python/YAML) |

## Relationship to Other Concepts

- [[embedded-metadata]]: Both concepts argue for capturing metadata within the data creation/management workflow rather than in a separate system.
- [[data-catalog-critique]]: Metadata-first DQ addresses the critique that catalogs are disconnected from data work by making DQ a native feature of the catalog.
- [[no-code-data-quality]]: The metadata-first approach enables no-code DQ by providing a UI layer on top of the centralized metadata store.

## Open Questions

- Does the metadata-first approach scale to very large organizations with thousands of tables and millions of tests?
- How does it compare to dbt-native testing ([[dbt-testing-patterns]], [[dbt-expectations]]) in practice?
- Is the "no-code" approach actually adopted by business users, or does it remain a technical tool with a friendlier UI?