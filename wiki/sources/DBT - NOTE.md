---
type: source
title: DBT - NOTE.md
created: 2026-02-17
updated: 2026-02-17
tags: [dbt, nessie, dremio, data-platform, metadata]
related: [dbt-nessie-branch-workaround, dbt-llm-documentation-generation, nessie-catalog-versioning, dremio-mcp-server, data-lakehouse-versioning-strategies, data-domain-governance, data-product-definition]
sources: ["DBT - NOTE.md"]
---
# DBT - NOTE.md

Internal project note documenting two practical techniques for the dbt-Dremio-Nessie stack:

1. **Nessie branch support via macro override** — A workaround for the dbt-dremio adapter's lack of native Nessie branch support. The note details overriding the `create_table_as` and `relation` macros, configuring `dbt dispatch` in `dbt_project.yml`, and injecting the branch name via dbt variables (`--vars`, `dbt_project.yml`, or environment variables). A `pre_hook` creates the branch if it does not exist, though the note flags this as a TODO to refactor into an ad-hoc macro.

2. **LLM-assisted YAML documentation generation** — Using a language model (ChatGPT) to auto-generate dbt YAML documentation from SQL model definitions. The note includes a test case for the `bus_MEDIA_GIORNALIERA` model, with Italian-language descriptions and a complete YAML output including column-level tests and a composite unique test.

The note also proposes a metadata schema for dbt models: owners (technical, analytics, business), domain, frequency, sensitivity, and PII.