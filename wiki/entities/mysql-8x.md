---
type: entity
title: MySQL 8.x
created: 2026-05-14
updated: 2026-05-14
tags: [database, openmetadata, metadata-storage, infrastructure]
related: [openmetadata, openmetadata-system-architecture, external-dependencies-configuration, unified-metadata-graph]
sources: ["openmetadata-system-architecture-developer-guide---20260514.md"]
---

# MySQL 8.x

MySQL 8.x is the relational database management system used by OpenMetadata as its primary transactional metadata store. It is one of the four core architectural dependencies identified in the [[openmetadata-system-architecture]].

## Role in OpenMetadata

- Persists all metadata entities, relationships, tags, and system configuration
- Serves as the backing store for the [[unified-metadata-graph]]
- Managed via [[flyway]] for versioned database migrations

## Deployment Context

MySQL 8.x is an [[external-dependencies-configuration|external dependency]] that must be provisioned and configured when deploying OpenMetadata, whether on Kubernetes or bare metal. The platform requires a dedicated database with appropriate user permissions and schema.