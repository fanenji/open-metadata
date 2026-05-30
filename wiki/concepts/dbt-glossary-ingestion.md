---
type: concept
title: dbt Glossary Ingestion
created: 2026-05-14
updated: 2026-05-14
tags: [dbt, glossary, ingestion, metadata, fqn]
related: [dbt-integration, dbt-artifacts, glossary-terms, how-to-add-glossary-terms, dbt-lineage-ingestion, manifest-json]
sources: ["ingest-glossary-from-dbt-official-documentation----20260514.md"]
---

# dbt Glossary Ingestion

dbt Glossary Ingestion is the process of associating OpenMetadata glossary terms with dbt models and columns via the `meta.openmetadata.glossary` configuration in dbt's `schema.yml` file. The glossary term Fully Qualified Names (FQNs) are embedded in the generated `manifest.json` artifact and ingested by OpenMetadata during the dbt workflow.

## Prerequisites

Glossary terms **must be created or present in OpenMetadata beforehand** for data ingestion to work. The dbt workflow does not create glossary terms; it only associates existing ones with tables and columns. If a referenced FQN does not exist in OpenMetadata at ingestion time, the behavior (error vs. silent skip) is not documented.

## Glossary Term FQN Format

The Fully Qualified Name (FQN) for a glossary term follows the format:

```
Glossary_Name.term_name
```

For nested glossary terms, use dot notation:

```
Glossary_Name.parent_term.child_term.grandchild_term
```

For example:
- `Test_Glossary.term_one` — a top-level term.
- `Test_Glossary.term_two.nested_term.more_nested_term` — a deeply nested term.

To discover the FQN of a glossary term, navigate to the term in the OpenMetadata UI (Govern → Glossary → Glossary_Name → Term_Name) and look at the URL. The FQN appears after `/glossary/` in the URL path.

## Table-Level Glossary Association

To associate glossary terms with a specific table in your dbt model, add the FQNs under `model->name->meta->openmetadata->glossary` in your `schema.yml` file. The value must be a list of FQN strings.

Example:

```yaml
models:
  - name: customers
    meta:
      openmetadata:
        glossary: [
          'Test_Glossary.term_one',
          'Test_Glossary.term_two.nested_term.more_nested_term',
        ]
    description: This table has basic information about a customer
    columns:
      - name: customer_id
        description: This is a unique identifier for a customer
```

After running `dbt run`, the `manifest.json` will contain the glossary FQNs under `node_name->meta->openmetadata->glossary`.

## Column-Level Glossary Association

To associate glossary terms with a specific column, add the FQNs under `model->name->columns->column_name->meta->openmetadata->glossary`.

Example:

```yaml
models:
  - name: customers
    meta:
      openmetadata:
        glossary: [
          'Test_Glossary.term_one',
          'Test_Glossary.term_two.nested_term.more_nested_term',
        ]
    columns:
      - name: customer_id
        description: This is a unique identifier for a customer
        meta:
          openmetadata:
            glossary: [
              'Test_Glossary.term_two.nested_term'
            ]
```

After running `dbt run`, the `manifest.json` will contain the column-level glossary FQNs under `node_name->columns->column_name->meta->openmetadata->glossary`.

## Viewing Results

Table-level and column-level glossary terms ingested from dbt can be viewed on the respective nodes in the OpenMetadata UI.

## Relationship to Other dbt Ingestion Features

- [[dbt-lineage-ingestion]] — Both use `manifest.json` metadata for enrichment, but glossary ingestion uses `meta.openmetadata.glossary` while lineage uses `ref()`/`source()` dependencies.
- [[dbt-artifacts]] — The `manifest.json` artifact carries the glossary FQNs under the `meta` key.
- [[how-to-add-glossary-terms]] — This automated dbt-driven workflow complements the manual UI workflow for adding glossary terms.

## Open Questions

- What happens if a glossary term FQN in `schema.yml` does not match any existing term in OpenMetadata? Error or silent skip?
- Does the ingestion support updating or removing glossary associations when the dbt model changes, or is it additive only?
- Is there a limit on the number of glossary terms that can be associated with a single table or column?
- Does the ingestion handle glossary term renames in OpenMetadata (i.e., if the FQN changes, does the old association break)?