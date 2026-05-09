---
type: entity
title: Snowflake Zero-Copy Clone
created: 2026-05-07
updated: 2026-05-07
tags: [snowflake, development-workflow, dbt, cloning]
related: [geospatial-analytics-with-dbt, dbt-insert-by-period, snowflake-manual-clustering]
sources: ["Complex geospatial analytics with dbt - Summary-20260507.md"]
---
# Snowflake Zero-Copy Clone

Snowflake Zero-Copy Cloning is a feature that creates metadata-only schema copies without duplicating underlying data. Nexar uses this as a key development workflow optimization for dbt.

## Usage in dbt Workflow

At the start of a new feature branch, developers run a dbt operation that:
1. Creates the dev schema if it doesn't exist (or drops and recreates it)
2. Clones the full production schema using Zero-Copy Cloning

```sql
CREATE OR REPLACE SCHEMA {{ target.schema }}
  CLONE production.public;
```

This takes approximately 5 minutes and copies only metadata (no actual data movement), giving developers a full, isolated copy of production to work against safely.