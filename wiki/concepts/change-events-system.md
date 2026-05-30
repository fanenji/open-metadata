---
type: concept
title: Change Events System
created: 2026-05-14
updated: 2026-05-15
tags:
  - openmetadata
  - events
  - elasticsearch
  - architecture
  - notifications
  - activity-feeds
related:
  - openmetadata
  - openmetadata-code-layout
  - unified-metadata-graph
  - elasticsearch
  - openmetadata-collaboration
  - following-data-assets
  - data-asset-ownership
  - pull-based-ingestion-model
  - data-observability-alerts
sources:
  - understand-code-layout---openmetadata-documentatio-20260514.md
  - how-to-follow-a-data-asset-official-documentation--20260514.md
---

# Change Events System

OpenMetadata captures all changes to metadata entities as **change events**, which are dual-stored in the server database and indexed in Elasticsearch. This event-driven mechanism underpins activity feeds, search functionality, and data observability within the platform. When a metadata entity is created, updated, or deleted via the REST API, the Change Events System intercepts the response and generates a change event that is both persisted to the database for historical tracking and indexed in Elasticsearch for immediate searchability.

## Architecture

### Event Capture

Event handlers are defined under `openmetadata-service/src/main/java/org/openmetadata/service/events`. The `ContainerResponseFilter` (a JAX-RS filter) globally applies these event handlers to every outgoing API response, ensuring that no entity change goes unrecorded. This guarantees that every API mutation produces a corresponding event, maintaining integrity across the [[unified-metadata-graph]].

### Dual Storage

1. **Database**: Change events are persisted in the OpenMetadata server database (MySQL or Postgres) as the durable record, providing an audit trail for data governance and [[data-lineage]] tracking.
2. **Elasticsearch**: The `ElasticSearchEventPublisher` (`openmetadata-service/.../elasticsearch/ElasticSearchEventPublisher.java`) captures change events and updates Elasticsearch indices, making them searchable in real time.

### Index Creation

Elasticsearch indices are created when the `metadata_to_es.json` ingestion connector is run (located under `ingestion/pipelines/`).

## User-Facing Features

### Activity Feeds

The Activity Feeds tab displays updates for data assets that a user owns, follows, or is @mentioned in. This is the primary user-facing interface of the change events system and is documented further in [[openmetadata-collaboration]].

### Following Data Assets

The [[following-data-assets]] feature is a user-facing subscription mechanism built on top of the change events system. When a user follows a data asset, they receive notifications for all change events related to that asset. This is distinct from ownership-based automatic notifications.

### Data Observability Alerts

Fine-grained alerts for schema changes, pipeline failures, and data quality issues are also powered by the change events system. See [[data-observability-alerts]].

### Search Index Updates

The change events system ensures that the Elasticsearch search index is kept in sync with the transactional database, enabling real-time search results across metadata entities.

## Relationship to Other Concepts

- **[[pull-based-ingestion-model]]**: While ingestion pulls metadata on a schedule, the change events system captures changes made within OpenMetadata itself (e.g., user edits, tag assignments).
- **[[data-asset-ownership]]**: Owners receive automatic notifications for change events on their assets, supplementing the following mechanism.
- **[[openmetadata-collaboration]]**: The collaboration features (activity feeds, following, conversations) all depend on the change events system.

This system is a foundational internal component that makes OpenMetadata's real-time metadata management possible.