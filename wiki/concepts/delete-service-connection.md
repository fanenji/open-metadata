---
type: concept
title: Delete Service Connection
created: 2026-05-14
updated: 2026-05-14
tags: [administration, service-connection, deletion, lifecycle]
related: [service-connection, openmetadata-administration, soft-deletion, metadata-ingestion-workflow, ingestion-pipeline-troubleshooting]
sources: ["how-to-delete-a-service-connection-official-docume-20260514.md"]
---
# Delete Service Connection

The administrative operation of permanently removing a configured [[service-connection|service connection]] — the link between OpenMetadata and an external data source. This is a destructive action that removes the connection configuration and requires explicit confirmation.

## Procedure

1. Navigate to the service page for the connection you wish to delete.
2. Click the vertical ellipsis (⋮) icon on the right side of the page.
3. Select **Delete** from the dropdown menu.
4. In the confirmation dialog, type the word `DELETE` and click **Confirm**.

The two-step confirmation (click Delete, then type DELETE) serves as a safeguard against accidental removal.

## Important Considerations

### Distinction from Database Deletion

The confirmation prompt in the UI uses the wording "permanently delete the database." This is misleading: the action deletes the **service connection configuration**, not the underlying database itself. The external data source remains intact; only the connection metadata within OpenMetadata is removed.

### Downstream Effects

The official documentation does not explicitly address what happens to previously ingested metadata when a service connection is deleted. Operators should consider:

- **Ingested metadata**: Tables, schemas, and other entities ingested through this connection may become orphaned or may be deleted depending on internal behavior. Verify before proceeding.
- **Ingestion pipelines**: Any [[metadata-agent|metadata agent]] pipelines associated with this service connection should be stopped or deleted first to prevent errors.
- **Lineage and data quality**: [[data-lineage|Lineage]] relationships and [[data-quality|data quality]] test results tied to entities from this service may be affected.
- **Reversibility**: Deletion is permanent. There is no undo. Compare with [[soft-deletion]], which marks entities as deleted while preserving historical metadata.

### Prerequisites

Before deleting a service connection:
1. Stop any active ingestion pipelines associated with the service.
2. Assess the impact on downstream consumers of the metadata.
3. Ensure you have backups or documentation of the connection configuration if it may need to be recreated.

## Related Administrative Tasks

- [[how-to-ingest-metadata-official-documentation---op-20260514|How to Ingest Metadata]] — creating service connections and ingestion pipelines.
- [[openmetadata-administration]] — overview of all administrative capabilities.
- [[service-connection]] — conceptual definition of service connections.