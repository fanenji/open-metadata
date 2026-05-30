---
type: entity
title: Metrics
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, metrics, data-governance]
related: [metric-lineage, data-lineage, glossary-terms, classification-tags, openmetadata-features, data-quality]
sources: ["metrics-for-openmetadata---openmetadata-documentat-20260514.md"]
---

# Metrics

The **Metrics** entity in [[OpenMetadata]] allows users to define, track, and manage key business and operational metrics. Metrics are a first-class governance entity, categorized under the Governance section (Govern > Metrics), and are distinct from [[data-quality]] tests. They help organizations maintain consistency, traceability, and accuracy in data-driven decision-making.

## Key Properties

| Property | Description | Example Value |
|---|---|---|
| Name | Unique identifier, following camelCase naming conventions | `customerRetentionRate` |
| Display Name | Human-readable name | Customer Retention Rate |
| Description | Detailed explanation of what the metric represents | Percentage of retained users |
| Expression/Formula | Formula or SQL query used to calculate the metric | `COUNT(returning_customers) / COUNT(total_customers) * 100` |
| Granularity | Time scale (daily, weekly, monthly) | Monthly |
| Metric Type | Type of calculation (count, average, ratio, percentage) | Percentage |
| Unit of Measurement | Unit for interpreting values (count, dollars, percentage) | Percentage |
| SQL Query | Optional SQL query defining the metric | `SELECT COUNT(*) FROM customer_activity WHERE status='active'` |
| Owner | Individual or team responsible for maintaining the metric | Data Governance Team |

## JSON Schema Example

```json
{
  "id": "123e4567-e89b-12d3-a456-426614174000",
  "name": "customerRetentionRate",
  "displayName": "Customer Retention Rate",
  "description": "Percentage of customers retained over a given period.",
  "formula": "COUNT(returning_customers) / COUNT(total_customers) * 100",
  "sql": "SELECT COUNT(*) FROM customer_activity WHERE status='active'",
  "granularity": "Monthly",
  "metricType": "Percentage",
  "unit": "Percentage",
  "owner": "Data Governance Team",
  "tags": ["Customer", "KPI", "Retention"]
}
```

## UI Creation Workflow

1. **Navigate** to Govern > Metrics in the OpenMetadata UI.
2. **Add a New Metric** by clicking Add Metric.
3. **Enter Metric Details**: Name, Description, Granularity, Metric Type, and Computation Code (SQL, Python, or Java — though only SQL and formula are confirmed in the JSON schema).
4. **Create** the metric by clicking Create.
5. **View** the created metric on the Metrics page.

## Management Capabilities

- **Versioning**: Each update creates a new version, maintaining historical changes.
- **Linking**: Metrics can be linked to [[glossary-terms]], tables, dashboards, and pipelines for enriched context.
- **Monitoring**: Metrics can be monitored for value changes, enabling trend analysis over time.

## Best Practices

- **Consistent Naming**: Use camelCase for metric names.
- **Clear Definitions**: Provide comprehensive descriptions and units.
- **Lineage Tracking**: Always associate metrics with source tables and pipelines for traceability.
- **Ownership**: Assign metric owners for accountability and maintenance.

## Relationship to Other Entities

- [[metric-lineage]] — Metrics participate in lineage as nodes (Database Table → Metric → Pipeline → Dashboard).
- [[glossary-terms]] — Metrics can be linked to glossary terms.
- [[classification-tags]] — Tags can be applied to metrics (shown in JSON schema).
- [[data-lineage]] — Metric lineage extends the general lineage concept.
- [[openmetadata-features]] — Metrics are listed under the Data Governance feature category.