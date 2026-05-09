type: entity
title: Dremio Dataset Promotion
created: 2026-05-07
updated: 2026-05-07
tags: [dremio, dataset, promotion, metadata]
related: [dremio, dremio-semantic-layer-ci-cd, iceberg-table-versioning]
sources: ["semantic-layer-ci-cd-with-dremio-and-dbt.pdf"]
---
# Dremio Dataset Promotion

Dataset promotion is Dremio's metadata collection process that enables reading file-based tables from object storage sources. For Dremio to read file-based tables, it must collect metadata in a process called "dataset promotion."

## Implementation in dbt

Dataset promotion can be combined with view creation in a single dbt model using a pre-hook:

```sql
{{ config(
    pre_hook='ALTER TABLE Samples."samples.dremio.com"."NYC-taxi-trips"
               REFRESH METADATA AUTO PROMOTION'
) }}
SELECT *
FROM Samples."samples.dremio.com"."NYC-taxi-trips"
```

This generates two SQL statements:
1. `ALTER TABLE ... REFRESH METADATA AUTO PROMOTION` — promotes the dataset
2. `CREATE OR REPLACE VIEW ...` — creates the semantic layer view

## Best Practices

- Maintain a 1-to-1 mapping between physical tables and virtual datasets in the Preparation/Staging layer
- Combine dataset promotion and view creation into a single dbt model
- Use `AUTO PROMOTION` to automatically promote datasets after metadata refresh
- Configure additional formatting properties as needed for different file types
