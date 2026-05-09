---
type: entity
title: Apache Arrow Flight
created: 2026-04-08
updated: 2026-04-08
tags: [apache-arrow, protocol, data-transfer, dremio, duckdb]
related: [dremio, duckdb, dremio-duckdb-integration, alex-merced, dremio-simple-query]
sources: ["Using DuckDB with Your Dremio Data Lakehouse.md"]
---
# Apache Arrow Flight

Apache Arrow Flight is a high-performance data transfer protocol built on top of [[apache-arrow]] and gRPC. It enables efficient, low-latency transfer of large columnar datasets between systems.

In the context of the [[dremio-duckdb-integration-pattern]], Arrow Flight is the mechanism by which data is transferred from [[dremio]] to local clients. Dremio exposes an Arrow Flight endpoint (typically `grpc+tls://data.dremio.cloud:443`) that clients can use to authenticate and execute queries, receiving results as a `FlightStreamReader`.

The protocol is central to the cost-optimization strategy described by [[Alex Merced]]: users query Dremio via Arrow Flight, pull down a filtered subset of data, and then process it locally with [[duckdb]], avoiding cloud compute costs for ad hoc analytics.

Key features:
- Columnar data transfer (no row-by-row serialization)
- Parallel streaming via gRPC
- Authentication via bearer tokens
- Integration with pyArrow's `flight` module