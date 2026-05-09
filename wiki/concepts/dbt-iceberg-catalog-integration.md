---
type: concept
title: dbt Iceberg Catalog Integration
created: 2026-05-07
updated: 2026-05-07
tags: [dbt, iceberg, catalog, table-format, lakehouse]
related: [iceberg-table-versioning, dbt-dremio-adapter, dbt-project-structure, data-lakehouse, nessie-catalog-versioning]
sources: ["Report dettagliato su dbt software.md"]
---
# dbt Iceberg Catalog Integration

dbt supports native materialization of models as Iceberg tables, a key capability for building a reliable data lakehouse. There are two approaches to configuration.

## Legacy Approach

Use the `table_format = 'iceberg'` configuration field directly in the model file:

```sql
{{
  config(
    materialized = "table",
    table_format = "iceberg",
    external_volume = "s3_iceberg_snow"
  )
}}

select * from {{ ref('raw_orders') }}
```

## Modern Approach (Recommended)

Use **catalog integration**, which centralizes catalog configuration and makes it more maintainable. This approach is more recent and robust.

The **Catalog** is the heart of Iceberg — a service that tracks table metadata (schema, partitions, snapshots). dbt interacts with the catalog through the query engine's adapter. For example, when using dbt with Snowflake, dbt can be configured to create Iceberg tables whose metadata is managed by Snowflake's internal catalog or an external catalog like AWS Glue, Polaris, or Nessie.

## Key Benefits of Catalog Integration

- **Centralized configuration:** Catalog settings are managed in one place rather than scattered across model files.
- **Automatic base_location management:** dbt automatically handles the `base_location` parameter to organize data within the volume, preventing disorder and technical debt.
- **Improved maintainability:** Changes to catalog configuration don't require modifying individual model files.
- **Future-proof:** Aligns with the evolving Iceberg ecosystem and catalog standards.

## Example

When using dbt with Snowflake and an external volume pointing to an S3 bucket, dbt instructs Snowflake to create an Iceberg table, writing data files to the specified volume. dbt automatically manages the `base_location` parameter to organize data within the volume.