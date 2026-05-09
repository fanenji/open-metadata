---
type: concept
title: dbt Artifact Upload Macro
created: 2026-04-29
updated: 2026-04-29
tags: [dbt, artifacts, macro, observability, snowflake]
related: [dbt-artifacts, dbt-observability-implementation, dbt-query-comment-pattern, dbt-domain-tag-alerting, dbt-artifact-publishing, on-run-end-hook]
sources: ["How to add observability to your dbt deployment - Show and Tell.md"]
---
# dbt Artifact Upload Macro

A custom dbt macro pattern for uploading dbt artifacts (run_results.json, manifest.json) to a Snowflake stage, even when the dbt pipeline fails. This is a core component of the [[dbt-observability-implementation]] described in [[How to add observability to your dbt deployment - Show and Tell]].

## Pattern

The macro uses three SQL operations:
1. **PUT** — Uploads the artifact file from the Airflow worker's local disk to a Snowflake stage with auto-compression
2. **COPY** — Copies the file from the stage into the target table
3. **REMOVE** — Cleans up the staged file

## Failure Resilience

The critical design decision is running the macro even on pipeline failure, using a shell pattern:
```bash
dbt run -m tag:hourly; ret=$?;
dbt run-operation upload_dbt_artifacts --args 'run_results'; exit $ret
```
This ensures artifacts are uploaded regardless of dbt's exit code, preserving metadata for debugging failed runs.

## Context

This pattern predates the [[tails-com-dbt-artifacts]] package and represents a "build your own" approach to artifact management. It is Snowflake-specific but the concept of failure-resilient artifact capture is portable.