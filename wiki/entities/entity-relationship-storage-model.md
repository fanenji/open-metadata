---
type: entity
title: Entity-Relationship Storage Model
created: 2026-05-15
updated: 2026-05-15
tags: [architecture, storage, mysql, design]
related: [openmetadata-system-architecture, mysql-8x, jsonschemas, unified-metadata-graph]
sources: ["research-capture-referenced-design-page-2026-05-15.md"]
---
# Entity-Relationship Storage Model

The Entity-Relationship Storage Model is a key architectural innovation in [[OpenMetadata]] that decouples the storage of entities and their relationships within [[mysql-8x|MySQL 8.x]]. This design enables independent lifecycle management of entities and their connections, and efficient graph traversal for the [[unified-metadata-graph]].

## Design

- **Entity Tables:** Each entity type (e.g., `table_entity`, `dashboard_entity`) stores the JSON definition of the entity's attributes plus system fields (`id`, `updatedAt`, `updatedBy`). Relationships are *not* embedded in this JSON.
- **Relationship Table:** A separate `entity_relationship` table stores connections as graph edges. Each edge is a labeled relationship (e.g., `contains`, `uses`, `owns`) between two entity nodes.

## Benefits

- **Decoupled Concerns:** Deleting a Dashboard does not directly cascade into the ownership relationship logic; the relationship is cleaned up independently.
- **Efficient Processing:** The system can process entities and relationships independently, validating at runtime what needs updating or retrieving.
- **Graph Traversal:** The relationship table enables efficient traversal of the [[unified-metadata-graph]] for [[data-lineage]] and impact analysis.

## Relationship Types

The `entity_relationship` table supports various relationship types including:
- `contains` — hierarchical containment (e.g., Database contains Schema contains Table)
- `uses` — dependency (e.g., Dashboard uses Table)
- `owns` — ownership (e.g., Team owns Table)
- `follows` — user follows an asset
- `reports` — reporting relationships

## Performance Considerations

For large-scale deployments, the `entity_relationship` table can grow significantly. Indexing on entity IDs and relationship types is critical for query performance. The decoupled design allows for independent scaling and optimization of entity and relationship storage.