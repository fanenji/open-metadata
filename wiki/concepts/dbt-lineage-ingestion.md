---
type: concept
title: dbt Lineage Ingestion
created: 2026-05-14
updated: 2026-05-15
tags:
  - dbt
  - lineage
  - ingestion
  - compiled-code
  - metadata-ingestion
  - manifest
  - openmetadata
related:
  - dbt-integration
  - dbt-artifacts
  - data-lineage
  - unified-metadata-graph
  - dbt
  - dbt-artifact-storage
  - manifest-json
  - lineage-parser
sources:
  - dbt Workflow  OpenMetadata Data Build Tool Integration.md
  - dbt-workflow-openmetadata-data-build-tool-integrat-20260514.md
  - ingest-lineage-from-dbt-official-documentation---o-20260514.md
---
# dbt Lineage Ingestion

OpenMetadata extracts transformation lineage from dbt model dependencies — specifically `ref()` and `source()` calls — and displays it in OpenMetadata's lineage view. This lineage shows how data flows between dbt models and from source tables into models, enriching the [[data-lineage]] capabilities of the [[unified-metadata-graph]].

Lineage information is sourced from the dbt `manifest.json` artifact using two distinct mechanisms described in detail below.

## How Lineage Is Extracted

### 1. Lineage from the `depends_on` Key

The `depends_on` key in `manifest.json` lists upstream node dependencies directly. This is the primary, reliable mechanism — OpenMetadata reads the `nodes` array under `depends_on` to create lineage edges between dbt models.

For example:

```json
"model.jaffle_shop.customers": {
  "compiled": true,
  "resource_type": "model",
  "depends_on": {
    "macros": [],
    "nodes": [
      "model.jaffle_shop.stg_customers",
      "model.jaffle_shop.stg_orders",
      "model.jaffle_shop.stg_payments"
    ]
  }
}
```

This produces lineage showing `model.jaffle_shop.customers` depends on the three staging models.

### 2. Lineage from `compiled_code` / `compiled_sql` (Query Parsing)

The `compiled_code` (or `compiled_sql`) field contains the compiled SQL query for a dbt model. OpenMetadata’s lineage parser parses this SQL to extract source and target tables.

```json
"model.jaffle_shop.customers": {
  "compiled": true,
  "resource_type": "model",
  "compiled_code": "Query for the model"
}
```

**Important caveat:** The lineage parser may fail on complex or unsupported SQL syntax. If lineage is not created, check the OpenMetadata logs for errors. This mechanism is secondary to `depends_on` and less reliable.

## Lineage Capture and the `compiled_code` Field

For the query-parsing mechanism to work, the `compiled_code` (or `compiled_sql`) field **must** be present in `manifest.json`. If it is missing for a given node, lineage from that mechanism will not be captured for that node — and this failure is **silent** (no error is raised). The `depends_on` mechanism, however, does **not** rely on `compiled_code`; basic model‑to‑model lineage will still be created as long as `depends_on` entries are present.

To ensure `compiled_code` is populated for all models, run the following commands in your dbt project **before** generating artifacts:

```shell
dbt compile
dbt docs generate
```

The `dbt compile` step resolves all `ref()` and `source()` references into compiled SQL, populating the `compiled_code` field. `dbt docs generate` then produces the full `manifest.json` with the enriched metadata. For complete lineage coverage (including query‑level details), both commands are recommended.

## Viewing Lineage

Once lineage is ingested, the resulting graph can be viewed in the **Lineage** tab of the respective dbt model, source, or table entities in OpenMetadata.

## Reliability Comparison

| Mechanism | Reliability | Notes |
|-----------|-------------|-------|
| `depends_on` | High | Direct node dependencies; deterministic |
| `compiled_code` parsing | Medium | May fail on complex SQL; check logs |

## Troubleshooting Missing Lineage

If lineage does not appear after ingestion:

1. Verify that `compiled_code` exists in `manifest.json` for the affected models.
2. Confirm that the `depends_on` entries are present and correctly structured in the `manifest.json` for the models in question.
3. Re-run `dbt compile` followed by `dbt docs generate`.
4. Re-upload artifacts to storage (for dbt Core) or re-trigger the dbt Cloud job.
5. Re-run the OpenMetadata ingestion workflow.
6. For the query‑parsing mechanism, check OpenMetadata logs for SQL‑parsing errors that may indicate the code could not be parsed.

## Related

- [[dbt]] — The Data Build Tool entity.
- [[dbt-integration]] — Overall integration overview.
- [[dbt-artifacts]] — Detailed artifact file reference.
- [[dbt-artifact-storage]] — Storage configuration for dbt Core.
- [[data-lineage]] — Core lineage concepts.
- [[unified-metadata-graph]] — OpenMetadata’s graph model.
- [[manifest-json]] — Structure and fields of the dbt manifest.
- [[lineage-parser]] — How OpenMetadata parses SQL for lineage.