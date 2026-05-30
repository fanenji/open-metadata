---
type: concept
title: Soft Deletion (Mark Deleted Tables)
created: 2026-05-14
updated: 2026-05-14
tags: [metadata-ingestion, data-governance, lineage, deletion]
related: [metadata-agent, filter-patterns, data-lineage, glossary-tags]
sources: ["how-to-ingest-metadata-official-documentation---op-20260514.md"]
---

# Soft Deletion (Mark Deleted Tables)

An ingestion option that marks tables as deleted in OpenMetadata when they are no longer present in the source system, rather than permanently removing them and their associated metadata. Controlled by the **Mark Deleted Tables** toggle on the [[metadata-agent|Metadata Agent]] configuration.

## Purpose

Soft deletion preserves:
- **Data lineage**: Historical lineage relationships remain intact even after source tables are dropped
- **Governance records**: Tags, classifications, and ownership assignments are retained for audit purposes
- **Impact analysis**: Downstream dependencies can still be traced to understand the impact of removed assets

## Behavior

When enabled:
- Tables present in the source are ingested normally
- Tables previously ingested but now absent from the source are marked with a "deleted" status in OpenMetadata
- Deleted tables remain visible in the UI with their historical metadata intact
- Deleted tables are excluded from active search results by default

When disabled:
- Tables absent from the source are permanently removed from OpenMetadata
- All associated metadata (lineage, tags, ownership) is lost

## Comparison with Service Deletion

Soft deletion is distinct from deleting a [[service-connection|Service Connection]]:
- **Soft deletion**: Operates at the table level, preserves metadata, reversible
- **Service deletion**: Removes the entire service and all its metadata permanently

## Best Practices

- Enable soft deletion in production environments to maintain data lineage integrity
- Periodically review and purge long-deleted assets if storage or clutter becomes a concern
- Combine with [[filter-patterns|Filter Patterns]] to ensure only intentionally tracked assets are ingested in the first place