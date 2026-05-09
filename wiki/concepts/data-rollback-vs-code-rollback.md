type: concept
title: Data Rollback vs. Code Rollback
created: 2026-05-07
updated: 2026-05-07
tags: [versioning, disaster-recovery, data-governance]
related: [nessie-catalog-versioning, dbt-git-branching-strategies, data-lakehouse-versioning-strategies]
sources: ["The Importance of Versioning in Modern Data Platforms Catalog Versioning with Nessie vs. Code Versioning with dbt.md"]
---
# Data Rollback vs. Code Rollback

Data rollback and code rollback are two distinct recovery mechanisms that address different failure modes in data platforms.

## Data Rollback

Data rollback reverts the state of the data catalog (metadata, schema, partitioning, format) to a previous point in time. This is achieved through catalog versioning systems like [[nessie-catalog-versioning]]. Data rollback is essential for:

- Recovering from data corruption or unwanted changes.
- Restoring data to a known good state after a bad data ingestion.
- Meeting auditing and compliance requirements by accessing historical data states.

## Code Rollback

Code rollback reverts the transformation logic (SQL models, dbt code) to a previous version. This is achieved through Git-based version control. Code rollback is essential for:

- Reverting buggy or incorrect transformations.
- Undoing changes that introduced errors in downstream datasets.
- Restoring a known working version of the data pipeline.

## Why Both Are Needed

Rolling back code does not affect the underlying data, and rolling back data does not fix bad transformation logic. Having both capabilities provides comprehensive recovery options:

- **Bad code in production**: Roll back the code to a previous Git commit, then re-run the transformations on the current data.
- **Data corruption**: Roll back the catalog to a point before the corruption occurred, preserving the transformation logic.
- **Combined failure**: If bad code corrupts data, roll back both code (Git) and data (catalog) to restore a clean state.

## Related Concepts

- [[nessie-catalog-versioning]] — The mechanism for data rollback.
- [[dbt-git-branching-strategies]] — The mechanism for code rollback.
- [[data-lakehouse-versioning-strategies]] — Broader framework for versioning approaches.