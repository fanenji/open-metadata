---
type: concept
title: Post-Update Views
created: 2026-04-29
updated: 2026-04-29
tags: [gis, postgis, views, etl]
related: [airflow-geospatial-etl-pattern, legacy-geospatial-etl-pipeline]
sources: ["Geoscript in DAG Airflow_Kuberbetes .md"]
---
# Post-Update Views

Post-Update Views are materialized view recreations that run after the Oracle-to-PostGIS spatial cache refresh completes. They maintain downstream data products that depend on the cached spatial layers.

## Purpose

After new spatial data is imported into PostGIS, views that aggregate or transform this data must be refreshed to reflect the updated data. This ensures that downstream applications and services always query current data.

## Implementation

The post-update step executes a series of `CREATE OR REPLACE VIEW` statements. Examples from the pipeline:

1. **pgr_grandi_piccole_deriv_idr**: Union of water derivation points filtered by usage type and status
2. **pgr_v_sis_instab_pub**: Instability data filtered by specific type codes

## Best Practices

- Execute post-update as a separate Airflow task for better observability
- Log success/failure for each view recreation
- Consider using materialized views with concurrent refresh for large datasets
- Document view dependencies to understand impact of schema changes