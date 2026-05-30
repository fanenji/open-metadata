---
type: concept
title: "Dbt Custom Properties Ingestion"
created: 2026-05-30
updated: 2026-05-30
tags: []
related: []
---

type: concept
title: Custom Property Ingestion from dbt
created: 2026-05-14
updated: 2026-05-14
tags: [dbt, custom-properties, metadata-ingestion, openmetadata]
related: [custom-properties, dbt-integration, dbt-artifacts, dbt-lineage-ingestion, dbt-artifact-storage, dbt]
sources: ["ingest-custom-properties-from-dbt-openmetadata-cus-20260514.md"]
---

# Custom Property Ingestion from dbt

The process of reading custom property values from dbt's `schema.yml` (via `meta.openmetadata.customProperties`) and applying them to Table entities in OpenMetadata. This extends the standard metadata model with organization-specific attributes without requiring manual entry.

## Pre-definition Requirement

Custom properties must be defined on the Table entity type in OpenMetadata *before* ingestion. If a custom property is not defined, a warning is logged and that property is skipped. This creates a critical workflow ordering constraint: define properties in Settings > Custom Properties > Tables first, then run the dbt ingestion pipeline.

## Schema.yml Syntax

Custom properties are declared in dbt's `schema.yml` under the model's `meta.openmetadata.customProperties` key:

```yaml
models:
  - name: customers
    meta:
      openmetadata:
        customProperties:
          sla_hours: 24
          data_steward: "John Doe"
          refresh_frequency: "daily"
```

## Supported Custom Property Types

OpenMetadata supports 14 custom property types for dbt ingestion:

| Type | Description | Example Value |
|------|-------------|---------------|
| string | Plain text | `"value"` |
| integer | Whole number | `42` |
| number | Decimal number | `3.14` |
| markdown | Markdown formatted text | `"# Header\nContent"` |
| sqlQuery | SQL query string | `"SELECT * FROM table"` |
| email | Valid email address | `"user@example.com"` |
| date-cp | Date string | `"2024-01-15"` |
| dateTime-cp | DateTime string | `"2024-01-15T10:30:00"` |
| time-cp | Time string | `"10:30:00"` |
| timestamp | Milliseconds since epoch | `1705315200000` |
| duration | ISO 8601 duration | `"P23DT23H"` |
| enum | Single or multi-select | `"High"` or `["High", "Critical"]` |
| entityReference | Reference to another entity | See advanced examples |
| entityReferenceList | List of entity references | See advanced examples |
| timeInterval | Time interval with start/end | See advanced examples |
| table-cp | Tabular data with rows | See advanced examples |

## Advanced Examples

### Entity Reference

```yaml
customProperties:
  data_owner:
    type: "user"
    fqn: "john.doe"
  related_dashboard:
    type: "dashboard"
    fqn: "service.dashboard_name"
```

### Entity Reference List

```yaml
customProperties:
  stakeholders:
    - type: "user"
      fqn: "john.doe"
    - type: "user"
      fqn: "jane.smith"
```

### Time Interval

```yaml
customProperties:
  valid_period:
    start: 1705315200000
    end: 1705401600000
```

### Table Custom Property

```yaml
customProperties:
  data_quality_rules:
    - rule_name: "not_null_check"
      threshold: 99.5
      severity: "high"
    - rule_name: "unique_check"
      threshold: 100
      severity: "critical"
```

## Manifest.json Structure

After running the dbt workflow, custom properties appear in `manifest.json` under `node_name -> config -> meta -> openmetadata -> customProperties`:

```json
"model.jaffle_shop.customers": {
  "config": {
    "meta": {
      "openmetadata": {
        "customProperties": {
          "sla_hours": 24,
          "data_steward": "John Doe",
          "refresh_frequency": "daily"
        }
      }
    }
  }
}
```

## Validation and Error Handling

The ingestion process validates custom property values against their defined types with graceful degradation:

| Scenario | Behavior |
|----------|----------|
| Custom property not defined on Table entity | Warning logged, property skipped |
| Invalid value for property type | Warning logged with details, property skipped |
| Invalid enum value (single-select) | Warning logged, property skipped |
| Invalid enum value (multi-select) | Invalid values filtered out, valid values applied with warning |
| Missing required fields for complex types | Warning logged, property skipped |

## Viewing Custom Properties

Ingested custom properties appear on the table details page under the Custom Properties section in the OpenMetadata UI.

## Complete Example

```yaml
version: 2
models:
  - name: customers
    description: "Customer master data table"
    meta:
      openmetadata:
        domain: "Sales"
        tier: "Tier.Tier2"
        customProperties:
          sla_hours: 24
          data_classification: "Confidential"
          refresh_frequency: "hourly"
          last_certified: "2024-01-15"
          data_owner:
            type: "user"
            fqn: "john.doe"
          data_quality_rules:
            - rule_name: "completeness"
              threshold: 99.9
              severity: "high"
```

## Relationship to Other dbt Features

This ingestion pathway shares the same artifact-based pattern as [[dbt-lineage-ingestion]] and requires [[dbt-artifact-storage]] configuration for dbt Core deployments. It extends the [[dbt-integration]] by adding custom properties to the list of metadata categories ingested from dbt artifacts.