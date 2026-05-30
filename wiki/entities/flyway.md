---
type: entity
title: Flyway
created: 2026-05-14
updated: 2026-05-14
tags: [database, migration, tooling, openmetadata]
related: [openmetadata, openmetadata-code-layout, mysql, postgres]
sources: ["understand-code-layout---openmetadata-documentatio-20260514.md"]
---
# Flyway

Flyway is the database migration tool used by OpenMetadata to manage versioned changes to the metadata catalog schema. It ensures that the MySQL or Postgres database schema stays in sync with the application code across upgrades.

## Role in OpenMetadata

- **Version Management**: Flyway tracks and applies database migrations in a controlled, repeatable manner.
- **Bootstrap Integration**: The initial database tables are created via `bootstrap/openmetadata-ops.sh`, with Flyway managing subsequent schema evolution.
- **Supported Databases**: Works with both MySQL and Postgres, the two supported metadata catalog backends.

## Why Flyway Matters

In a schema-first architecture like OpenMetadata's, the database schema must precisely reflect the JSON Schema entity definitions. Flyway ensures that when entity models evolve, the database schema is updated reliably, preventing drift between the [[schema-first-approach|schema definitions]] and the physical data store.

Flyway is a peripheral tool in the [[openmetadata-code-layout|codebase]] but critical for production operations and upgrades.