---
type: concept
title: dbt Meta Configuration
created: 2026-05-14
updated: 2026-05-14
tags: [dbt, configuration, metadata, schema-yml]
related: [dbt-glossary-ingestion, dbt-integration, dbt-artifacts]
sources: ["ingest-glossary-from-dbt-official-documentation----20260514.md"]
---

# dbt Meta Configuration

The dbt `meta` configuration is a mechanism in dbt's `schema.yml` file that allows users to attach arbitrary metadata to models and columns. OpenMetadata uses this mechanism to associate glossary terms with dbt models and columns via the `meta.openmetadata.glossary` key.

## Structure

The `meta` configuration is a YAML dictionary that can be placed at the model level or the column level within a `schema.yml` file.

### Model-Level (Table-Level)

```yaml
models:
  - name: customers
    meta:
      openmetadata:
        glossary: [
          'Test_Glossary.term_one',
          'Test_Glossary.term_two.nested_term.more_nested_term',
        ]
```

### Column-Level

```yaml
models:
  - name: customers
    columns:
      - name: customer_id
        meta:
          openmetadata:
            glossary: [
              'Test_Glossary.term_two.nested_term'
            ]
```

## How It Works

1. The glossary term FQNs are added under `meta.openmetadata.glossary` as a list of strings.
2. When `dbt run` is executed, the `manifest.json` artifact is generated with the glossary FQNs embedded under `node_name->meta->openmetadata->glossary` (for tables) and `node_name->columns->column_name->meta->openmetadata->glossary` (for columns).
3. OpenMetadata's dbt ingestion workflow reads the `manifest.json` and associates the glossary terms with the corresponding tables and columns.

## Relationship to Other dbt Features

- [[dbt-glossary-ingestion]] — The full workflow for ingesting glossary terms via dbt.
- [[dbt-artifacts]] — The `manifest.json` artifact carries the `meta` configuration.
- [[dbt-lineage-ingestion]] — Uses a different mechanism (`ref()`/`source()` dependencies) for lineage enrichment.