---
type: concept
title: dbt MCP Server Tools Reference
created: 2026-05-07
updated: 2026-05-07
tags: [dbt, mcp, tools, reference]
related: [dbt-mcp-server, dbt-mcp-server-deployment-modes, dbt-semantic-layer, dbt-fusion]
sources: ["the-dbt-mcp-server-how-ai-finally-gets-to-talk-to-your-data-the-right-way.md"]
---
# dbt MCP Server Tools Reference

The [[dbt-mcp-server]] exposes a rich set of tools across seven categories. This page documents each category with availability (local vs. remote).

## 1. dbt CLI Tools (Local Only)

Full command-line interface to dbt operations:
- `run` — Execute dbt models
- `test` — Run data tests
- `build` — Run + test in sequence
- `compile` — Compile Jinja/SQL without executing
- `docs` — Generate documentation
- `show` — Preview model output
- `list` — List resources
- `parse` — Parse project

## 2. Semantic Layer Tools (Local + Remote)

Access to governed business metrics:
- `list_metrics` — Discover available metrics
- `query_metrics` — Query metrics with dimensions and time grains
- Metric definitions with business logic

## 3. Discovery Tools (Local + Remote)

Metadata exploration:
- Model definitions and descriptions
- Source freshness and health
- Upstream/downstream lineage traversal
- Health signals

## 4. SQL Tools (Local + Remote)

Query execution:
- `text_to_sql` — Convert natural language to SQL using project context (consumes Copilot credits)
- `execute_sql` — Run SQL against the warehouse

## 5. Codegen Tools (Local Only)

Code generation:
- `generate_staging_model` — Scaffold staging model SQL
- `generate_model_yaml` — Create YAML documentation with column inheritance
- `generate_source_yaml` — Create source YAML definitions

## 6. Administrative API Tools (Local Only)

Platform management:
- `trigger_job_run` — Trigger dbt Cloud jobs
- Environment management
- Job status monitoring

## 7. Fusion Tools (Local + Remote)

Advanced lineage:
- `fusion.get_column_lineage` — Column-level lineage tracing via [[dbt-fusion]] engine
- Full DAG traversal at column granularity