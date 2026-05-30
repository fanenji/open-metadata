---
type: concept
title: Custom Property Naming Conventions
created: 2026-05-14
updated: 2026-05-14
tags: [custom-properties, naming-conventions, metadata-extension]
related: [custom-properties, custom-property-types, schema-first-approach]
sources: ["how-to-create-a-custom-property-for-a-data-asset---20260514.md"]
---

# Custom Property Naming Conventions

OpenMetadata enforces specific naming rules for custom properties to ensure consistency and compatibility with the schema-first approach.

## Rules

- **Must start with a lowercase letter**: The first character must be a lowercase letter (a-z).
- **Use camelCase format**: Compound names should use camelCase (e.g., `dataSteward`, `retentionPeriod`).
- **Uppercase letters allowed**: Uppercase letters can be used within the name (e.g., `slaDeadline`).
- **Numbers allowed**: Digits can be included in the field name (e.g., `tier2Contact`).
- **No spaces**: Spaces are not supported.
- **No underscores**: Underscores are not supported.
- **No dots**: Dots are not supported.

## Examples

| Valid | Invalid |
|-------|---------|
| `dataSteward` | `data_steward` (underscore) |
| `retentionPeriod` | `retention period` (space) |
| `slaDeadline` | `sla.deadline` (dot) |
| `tier2Contact` | `2tierContact` (starts with number) |

## Rationale

The naming conventions align with the [[schema-first-approach]] where custom properties extend JSON Schema definitions. CamelCase without special characters ensures compatibility with code generation and API serialization.

## Related

- [[custom-properties]] — The overall mechanism for extending data models.
- [[custom-property-types]] — The 18 supported data types for custom properties.