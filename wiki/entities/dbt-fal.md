---
type: entity
title: dbt-fal
created: 2026-05-06
updated: 2026-05-06
tags: [dbt, deprecated, tool]
related: [dbt-python-models-support]
sources: ["Conintori dbt e Python.md"]
---
# dbt-fal

A now **deprecated** dbt adapter that acted as a "sidecar" or wrapper. It allowed users to run Python scripts by pulling data from databases like Postgres or Redshift into a local/intermediate environment, processing it via Pandas, and writing it back. It is no longer maintained and should be avoided in production.