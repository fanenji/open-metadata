---
type: source
title: How to Create a Custom Property for a Data Asset - OpenMetadata Documentation
created: 2026-05-14
updated: 2026-05-14
tags: [custom-properties, data-assets, metadata-extension, schema-first]
related: [custom-properties, custom-property-types, custom-property-naming-conventions, schema-first-approach, openmetadata-administration]
sources: ["how-to-create-a-custom-property-for-a-data-asset---20260514.md"]
---

# How to Create a Custom Property for a Data Asset

Official OpenMetadata v1.12.x documentation for creating custom properties on data assets. This guide covers the schema-first approach that enables custom property support, the 18 supported data types, the step-by-step creation workflow, value assignment, and deletion procedures.

## Key Content

- **Schema-First Approach**: Custom properties extend the JSON Schema-based metadata models for all data asset types.
- **18 Supported Types**: Date, DateTime, Duration, Email, Entity Reference, Entity Reference List, Enum, Integer, Markdown, Number, SQL Query, String, Table, Time, Time Interval, Timestamp.
- **Creation Workflow**: Settings → Custom Properties → Select asset type → Add Property → Name/Type/Description → Create.
- **Naming Convention**: Must start with lowercase letter, use camelCase; no spaces, underscores, or dots.
- **Value Assignment**: From the Custom Property tab in the data asset's detailed view.
- **Deletion**: Settings → Custom Properties → Select asset type → Delete Property.

## Relevance

This source provides the detailed procedural workflow missing from the existing [[custom-properties]] concept page. It extends the [[schema-first-approach]] concept with a practical application and is related to [[openmetadata-administration]] as a key administrative capability.