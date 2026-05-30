---
type: concept
title: Custom Properties
created: 2026-05-14
updated: 2026-05-14
tags: ["administration", "metadata", "extensibility", "data-modeling", "custom-properties", "metadata-extension"]
related: ["openmetadata-administration", "glossary-tags", "jsonschemas", "custom-property-types", "custom-property-naming-conventions", "schema-first-approach", "data-asset-ownership"]
sources: ["admin-guide-openmetadata-administration-documentat-20260514.md", "how-to-create-a-custom-property-for-a-data-asset---20260514.md"]
---

# Custom Properties

Custom Properties are a mechanism in OpenMetadata that allows organizations to extend the metadata models of data assets with additional fields tailored to their specific needs. Built on the [[schema-first-approach]], custom properties enable capturing custom metadata beyond the default attributes.

## Supported Types

OpenMetadata supports 18 data types for custom properties. See [[custom-property-types]] for the complete list with descriptions and use cases.

## Naming Conventions

Custom property names must follow strict rules. See [[custom-property-naming-conventions]] for the full specification.

## Workflow

### Creating a Custom Property

1. Navigate to **Settings >> Custom Properties**.
2. Click on the type of data asset (e.g., Tables, Topics, Dashboards) you want to extend.
3. Click **Add Property**.
4. Enter the required details:
   - **Name**: Must follow camelCase naming conventions.
   - **Type**: Select from the 18 supported types.
   - **Description**: Provide context for your team.
5. Click **Create**.

### Assigning Values

Once a custom property is created for a data asset type, values can be added from the **Custom Property** tab in the detailed view of individual data assets.

### Deleting a Custom Property

1. Navigate to **Settings >> Custom Properties**.
2. Select the data asset type.
3. Click **Delete Property** on the target property.

## Related

- [[custom-property-types]] — Reference of all 18 supported data types.
- [[custom-property-naming-conventions]] — Detailed naming rules.
- [[schema-first-approach]] — The architectural principle enabling custom properties.
- [[openmetadata-administration]] — Custom Properties as an administrative capability.
- [[data-asset-ownership]] — Custom properties are per-asset extensions.