---
type: concept
title: Domain Inheritance
created: 2026-05-14
updated: 2026-05-14
tags: [data-mesh, domains, hierarchy]
related: [domains, data-mesh-openmetadata]
sources: ["OpenMetadata Community Meeting Oct 2023 Release 1 2 0 datamesh openmetadata.md"]
---
# Domain Inheritance

Domain inheritance is a propagation mechanism in [[OpenMetadata]]'s [[data-mesh-openmetadata|data mesh]] implementation where a [[domains|domain]] assignment at a higher hierarchical level automatically applies to all child entities.

## How It Works

When a domain is set on a database, the assignment propagates downward through the hierarchy:
- **Database** → **Schemas** → **Tables** → **Stored Procedures**

This eliminates the need to tag each individual asset with its domain. Setting the domain once at the database level is sufficient to classify all contained entities.

## Benefits

- **Reduced tagging burden**: Administrators and data owners don't need to manually assign domains to hundreds or thousands of individual tables.
- **Consistency**: Ensures all assets within a database hierarchy share the same domain classification.
- **Simplified onboarding**: New assets created within a domain-assigned database automatically inherit the correct domain.

## Relationship to Domain-Only View

Domain inheritance ensures that the [[domain-only-view]] filter works correctly — all assets that should belong to a domain are properly classified, even if only the top-level database was explicitly tagged.