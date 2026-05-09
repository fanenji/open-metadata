---
type: concept
title: dbt-osmosis Execution Order
created: 2026-02-17
updated: 2026-02-17
tags: [dbt, dbt-osmosis, workflow]
related: [dbt-osmosis, dbt-schema-synchronization]
sources: ["DBT-OSMOSIS.md"]
---
# dbt-osmosis Execution Order

The correct sequence of commands required for [[dbt-osmosis]] to properly synchronize YAML schema files and generate documentation after modifying SQL models.

## Required Sequence

```bash
dbt build
dbt docs generate
dbt-osmosis yaml refactor
```

Running `dbt-osmosis yaml refactor` alone after modifying SQL will **not** update documentation. The tool depends on the artifacts produced by `dbt docs generate` to detect schema changes.

## Why This Order Matters

1. **`dbt build`** — Executes models and tests, materializing the latest schema in the warehouse.
2. **`dbt docs generate`** — Produces the `catalog.json` and `manifest.json` artifacts that dbt-osmosis reads to understand the current schema.
3. **`dbt-osmosis yaml refactor`** — Reads the dbt artifacts and synchronizes the YAML schema files, optionally generating documentation via the LLM module.

## Related

- [[dbt-osmosis]] — Central tool
- [[dbt-schema-synchronization]] — Broader concept of schema YAML synchronization