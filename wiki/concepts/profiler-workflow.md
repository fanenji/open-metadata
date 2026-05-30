---
type: concept
title: Profiler Workflow
created: 2026-05-14
updated: 2026-05-15
tags: [openmetadata, data-profiling, ingestion, workflow, profiler, metrics]
related: [data-profiling, spark-engine-profiling, data-quality, auto-classification, metadata-agent, ingestion-scheduling, profiler-metrics, system-metrics]
sources: ["data-profiler-openmetadata-data-profiling-guide----20260514.md", "metrics-openmetadata-profiler-metrics-guide---open-20260514.md"]
---
# Profiler Workflow

The Profiler Workflow is the operational mechanism within OpenMetadata for configuring and running [[data-profiling]] on connected data sources. It is a specialized type of [[metadata-agent]] that binds a set of [[profiler-metrics]] to a Table and executes them, extracting profiling statistics (descriptive statistics, null counts, uniqueness, distributions) from database tables and ingesting them into OpenMetadata. It serves as the operational layer that connects metric definitions to actual data sources.

Unlike the general metadata ingestion workflow, which focuses on schema and metadata extraction, the Profiler Workflow is dedicated to profiling and runs as a scheduled pipeline to capture table usage statistics over time, enabling data observability and validation of data assumptions.

## Core Concepts

- **Metric** — A computation on a Table or Column returning a value. Defined generically via SQLAlchemy.
- **Profiler** — The binding between a set of metrics and the external world. Contains the Table and Session information and is responsible for executing the metrics.

## Workflow Steps

The profiler workflow follows these steps:

1. **Metric Selection** — Choose which Table, Column, and System metrics to run.
2. **Profiler Configuration** — Configure the Profiler with the target Table and database Session.
3. **Execution** — The Profiler executes each metric against the Table using SQLAlchemy expressions.
4. **Result Collection** — Metric results are collected and stored as part of the table profile.
5. **Data Quality Integration** — Profile results can be used as inputs for [[data-quality]] tests.

## Key Capabilities

- **Scheduled Profiling:** Runs on a recurring schedule (hourly, daily, weekly, etc.) to capture trends over time.
- **Column-Level Statistics:** Computes descriptive statistics for each column, including null counts, distinct counts, min/max values, and distribution patterns.
- **Validation:** Enables checking for null values in non-null columns, duplicates in unique columns, and other data quality assumptions.
- **Integration with Data Quality:** Profiling data feeds into [[data-quality]] tests, providing baseline statistics for test configuration.

## Configuration

The Profiler Workflow is configured through the OpenMetadata UI or API. Key configuration parameters include:

- **Target Tables:** Which tables to profile (can use [[filter-patterns]]).
- **Metrics:** Which profiling metrics to compute (see [[profiler-metrics]]).
- **Schedule:** How often to run profiling (see [[ingestion-scheduling]]).
- **Engine:** Standard profiler or [[spark-engine-profiling]] for large datasets.
- **Auto PII Tagging:** Enable automatic detection and tagging of sensitive data during profiling (see [[auto-classification]]).

## Relationship to Other Concepts

- **[[data-profiling]]:** The conceptual foundation; the Profiler Workflow is the operational implementation.
- **[[profiler-metrics]]:** Catalog of all supported metrics executed by the workflow.
- **[[data-quality]]:** Profiling provides the statistical basis for data quality tests.
- **[[auto-classification]]:** Auto PII Tagging can be enabled within the workflow.
- **[[metadata-agent]]:** The Profiler Workflow is a specialized metadata agent.
- **[[ingestion-scheduling]]:** Controls the frequency of profiling runs.
- **[[spark-engine-profiling]]:** Alternative engine for profiling large datasets.
- **[[system-metrics]]:** DML operation metrics for freshness monitoring (related to profiling).