---
type: concept
title: dbt Query Comment Pattern
created: 2026-04-29
updated: 2026-04-29
tags: [dbt, query-comment, observability, snowflake, lineage]
related: [dbt-artifacts, dbt-observability-implementation, dbt-artifact-upload-macro, dbt-jinja-variables]
sources: ["How to add observability to your dbt deployment - Show and Tell.md"]
---
# dbt Query Comment Pattern

A dbt configuration pattern that injects metadata (node_id, invocation_id, model name, etc.) into every SQL query as a comment. This enables joining dbt artifact data to the data warehouse's query history for cost and performance analysis.

## Implementation

The pattern uses dbt's `query-comment` project configuration with a custom macro:

```yaml
query-comment:
  comment: "{{ query_comment(node) }}"
  append: true
```

The macro generates a JSON comment containing:
- `app`, `dbt_version`, `profile_name`, `target_name`
- `invocation_id` — unique identifier for the dbt run
- `node_id` — unique identifier for the model/test being executed
- `node_name`, `resource_type`, `package_name`
- Relation metadata (database, schema, identifier, materialization)

## Key Insight

The `node_id` and `invocation_id` fields are the critical integration point. They allow joining artifact instances (from run_results.json) to the actual SQL queries executed in Snowflake, enabling:
- Per-model cost estimation
- Query performance metrics (byte spillage, partitions scanned)
- Model-level runtime analysis

## Context

This pattern was central to the [[dbt-observability-implementation]] at Snapcommerce. It is Snowflake-specific in its documented form but the concept applies to any warehouse with a query history log.