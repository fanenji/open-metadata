---
type: concept
title: Dremio Dataset Promotion
created: 2026-05-06
updated: 2026-05-06
tags: [dremio, dataset-promotion, metadata, object-storage]
related: [dremio, dremio-semantic-layer-ci-cd, dbt-dremio-adapter]
sources: ["Semantic Layer CI-CD with Dremio and dbt.md"]
---
# Dremio Dataset Promotion

Dataset promotion is Dremio's process of collecting metadata from file-based tables in object storage sources (like S3 or ADLS) to make them readable by the query engine. Depending on the file type, data formatting may require additional configuration properties to succeed.

## Integration with dbt

As part of Dremio's semantic layer best practices, a 1-to-1 mapping between physical tables and virtual datasets in the initial "Preparation" (or "Staging") layer is recommended. In dbt, this means combining the physical dataset promotion and the creation of the basic view into one dbt file using a pre-hook.

Example:
```sql
{{ config(
  pre_hook='ALTER TABLE Samples."samples.dremio.com"."NYC-taxi-trips" REFRESH METADATA AUTO PROMOTION'
) }}
SELECT * FROM Samples."samples.dremio.com"."NYC-taxi-trips"
```

This generates two queries: the metadata refresh/promotion, followed by the view creation.