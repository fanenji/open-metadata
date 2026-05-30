---
type: source
title: Ingest Glossary from dbt | Official Documentation
created: 2026-05-14
updated: 2026-05-14
tags: [dbt, glossary, ingestion, metadata]
related: [dbt-integration, dbt-artifacts, glossary-terms, how-to-add-glossary-terms, dbt-glossary-ingestion]
sources: ["ingest-glossary-from-dbt-official-documentation----20260514.md"]
---

# Ingest Glossary from dbt | Official Documentation

This source is the official OpenMetadata documentation page for ingesting glossary terms from dbt. It provides a step-by-step walkthrough for associating table-level and column-level glossary terms with dbt models using the `meta.openmetadata.glossary` configuration in `schema.yml` files. The glossary term FQNs are embedded in the dbt `manifest.json` artifact and ingested by OpenMetadata.

Key points covered:
- Glossary terms must be pre-created in OpenMetadata before dbt ingestion.
- Glossary term FQNs follow the format `Glossary_Name.term_name` (e.g., `Test_Glossary.term_one`), with nested terms using dot notation (e.g., `Test_Glossary.term_two.nested_term.more_nested_term`).
- Table-level glossary terms are configured under `model->name->meta->openmetadata->glossary` as a list of FQN strings.
- Column-level glossary terms are configured under `model->name->columns->column_name->meta->openmetadata->glossary`.
- The `manifest.json` file carries the glossary FQNs under `node_name->meta->openmetadata->glossary` for tables and `node_name->columns->column_name->meta->openmetadata->glossary` for columns.
- The source includes concrete examples using `Test_Glossary.term_one`, `Test_Glossary.term_two.nested_term.more_nested_term`, and `Test_Glossary.term_two.nested_term`.

This source is additive and consistent with existing wiki content. It extends the [[dbt-integration]] page by adding glossary as an explicit metadata category, and complements the manual UI workflow described in [[how-to-add-glossary-terms]].