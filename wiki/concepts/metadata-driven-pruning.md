---
type: concept
title: Metadata-Driven Pruning
created: 2026-04-04
updated: 2026-04-04
tags: [apache-iceberg, performance, metadata, scan-planning]
related: [apache-iceberg, hidden-partitioning, iceberg-maintenance-operations]
sources: ["Is Apache Iceberg Melting?.md"]
---
# Metadata-Driven Pruning

Iceberg's approach to efficient scan planning using a metadata hierarchy (snapshots, manifest lists, manifests, data files). Operations should use O(1) remote calls to plan a scan, not O(n) calls that grow with table size.

## Performance Impact

- AWS published test results showing Athena scanned 50% or less data for queries on Iceberg tables compared to original data before conversion
- An enterprise case study reported nearly 50% reduction in I/O costs and 40-50% reduction in query latency for complex aggregations

## Caveats

- Results vary based on file sizing, partitioning, column stats, and the engine
- The mechanism is real: richer metadata enables better pruning and better planning
