---
type: concept
title: Profiler Agent
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, data-profiling, ingestion, profiler]
related: [data-profiling, custom-metrics, metadata-agent, ingestion-framework, data-quality]
sources: ["custom-metrics---openmetadata-documentation-20260514.md"]
---
# Profiler Agent

The **Profiler Agent** is a scheduled pipeline in [[OpenMetadata]] that executes profiling workflows against connected data sources. It is the execution engine for [[data-profiling]] and is required to compute [[custom-metrics]] after they are defined.

## Role in the System

The Profiler Agent is a specialized type of [[metadata-agent]] responsible for:

- Running system-defined profiling metrics (null counts, distinct values, min/max, etc.).
- Executing user-defined [[custom-metrics]] SQL queries at both table and column levels.
- Populating Table Profile and Column Profile views with computed values.

## Workflow

1. A profiling workflow is configured for a database service (via UI or CLI).
2. The Profiler Agent runs on a schedule (or on-demand) against the connected source.
3. It computes all configured metrics, including custom metrics.
4. Results are stored and displayed in the OpenMetadata UI.

## Relationship to Custom Metrics

Custom metrics are defined in the UI but are not computed until the Profiler Agent runs. This means:

- After defining a custom metric, the user must trigger or wait for the next Profiler Agent run.
- The agent executes the SQL query against the target database and stores the result.
- The computed value appears in the profile view after the agent completes.

## Operational Considerations

- The Profiler Agent requires appropriate database permissions to execute SQL queries.
- Performance depends on the complexity of the SQL queries and the size of the target data.
- Scheduling should account for the frequency of custom metric updates needed.

## Related Pages

- [[data-profiling]] — Core profiling concepts and built-in metrics.
- [[custom-metrics]] — User-defined business metrics computed by the Profiler Agent.
- [[metadata-agent]] — General concept of configurable ingestion pipelines.
- [[ingestion-framework]] — The backbone for moving metadata into OpenMetadata.
- [[data-quality]] — Data quality testing and domain-specific checks.