---
type: entity
title: dbt LLM Documentation Generation
created: 2026-02-17
updated: 2026-02-17
tags: [dbt, llm, documentation, yaml, chatgpt]
related: [dbt-testing-patterns, data-product-definition, data-domain-governance]
sources: ["DBT - NOTE.md"]
---
# dbt LLM Documentation Generation

A pattern for using large language models (LLMs) to auto-generate dbt YAML documentation from SQL model definitions. This technique accelerates documentation creation by having the LLM infer column descriptions, data types, and test suggestions directly from the SQL code.

## Test Case: `bus_MEDIA_GIORNALIERA`

The source note includes a complete example: a ChatGPT prompt requesting a dbt YAML file for the `bus_MEDIA_GIORNALIERA` model, with descriptions in Italian. The prompt included the full SQL definition, and the LLM returned a complete YAML with:

- Model description
- Column-level descriptions for all 8 columns (DATA, COD_UBIC, COD_CONF, SIGLA_PARAM, MEDIA_GIORNALIERA_VAL, VALORI_VALIDI_GG_VAL, MEDIA_GIORNALIERA_VAL_COR, VALORI_VALIDI_GG_VAL_COR, MEDIA_GIORNALIERA_CERT, VALORI_VALIDI_GG_CERT)
- `not_null` tests on key columns
- A composite `unique` test on the natural key (DATA, COD_UBIC, COD_CONF, SIGLA_PARAM)

## Metadata Schema

The note also proposes a metadata schema for dbt models:
- **owners** — technical, analytics, business
- **domain** — business domain
- **frequency** — update cadence
- **sensitivity** — data sensitivity classification
- **pii** — whether the model contains personally identifiable information

This schema aligns with [[data-domain-governance]] and [[data-product-definition]] concepts.