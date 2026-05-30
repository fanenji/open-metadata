---
type: entity
title: Spark Engine Profiling
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, data-profiling, spark, scalability]
related: [data-profiling, profiler-workflow, data-quality]
sources: ["data-profiler-openmetadata-data-profiling-guide----20260514.md"]
---
# Spark Engine Profiling

The Spark Engine is an integration within OpenMetadata's [[data-profiling]] system that enables distributed processing for large-scale data profiling. It uses Apache Spark to handle profiling workloads that exceed the capacity of the standard in-memory profiler, addressing performance and scalability concerns for large datasets.

## Overview

When profiling very large tables, the standard profiler may encounter memory or performance limitations. The Spark Engine integration allows profiling to be distributed across a Spark cluster, enabling efficient processing of terabytes of data. This is configured as part of the [[profiler-workflow]].

## Key Features

- **Distributed Processing:** Leverages Apache Spark's distributed computing model to parallelize profiling computations across multiple nodes.
- **Scalability:** Handles datasets that are too large for the standard single-node profiler.
- **Integration:** Configured within the Profiler Workflow as an alternative processing engine.

## Configuration

The Spark Engine is configured within the Profiler Workflow settings. Users specify the Spark connection details (e.g., Spark master URL, deployment mode) and the profiler automatically distributes the workload. The exact configuration parameters and requirements are detailed in the official documentation.

## Use Cases

- Profiling large fact tables in data warehouses.
- Running profiling on datasets exceeding available memory on the OpenMetadata server.
- Batch profiling of multiple large tables in a single workflow.

## Relationship to Other Features

- Works in conjunction with [[data-quality]] tests, which can also be executed via Spark for large-scale validation.
- Complements [[auto-classification]] by enabling PII detection on large datasets.
- Outputs the same profiling metrics as the standard profiler, ensuring consistency.

## Limitations

- Requires a running Spark cluster (standalone, YARN, or Kubernetes).
- Additional configuration overhead compared to the standard profiler.
- May not be suitable for real-time or ad-hoc profiling due to cluster startup time.