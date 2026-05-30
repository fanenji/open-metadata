---
type: concept
title: Glossary Term FQN (Fully Qualified Name)
created: 2026-05-14
updated: 2026-05-14
tags: [glossary, fqn, metadata, dbt]
related: [glossary-terms, dbt-glossary-ingestion, dbt-integration]
sources: ["ingest-glossary-from-dbt-official-documentation----20260514.md"]
---

# Glossary Term FQN (Fully Qualified Name)

A Glossary Term FQN (Fully Qualified Name) is the unique identifier for a glossary term in OpenMetadata. It follows the format `Glossary_Name.term_name` and is used to reference glossary terms in dbt's `meta.openmetadata.glossary` configuration.

## Format

```
Glossary_Name.term_name
```

For nested glossary terms, use dot notation:

```
Glossary_Name.parent_term.child_term.grandchild_term
```

## Examples

- `Test_Glossary.term_one` — a top-level term.
- `Test_Glossary.term_two.nested_term.more_nested_term` — a deeply nested term.

## Discovery

To find the FQN of a glossary term:
1. Navigate to the term in the OpenMetadata UI: Govern → Glossary → Glossary_Name → Term_Name.
2. Look at the URL in your browser. The FQN appears after `/glossary/` in the URL path.

For example, if the URL is `https://localhost:8585/glossary/Test_Glossary.term_two.nested_term.more_nested_term`, the FQN is `Test_Glossary.term_two.nested_term.more_nested_term`.

## Usage in dbt

The FQN is used in dbt's `schema.yml` file under `meta.openmetadata.glossary` as a list of strings. This is the bridge between dbt models and OpenMetadata glossary terms. See [[dbt-glossary-ingestion]] for the full workflow.