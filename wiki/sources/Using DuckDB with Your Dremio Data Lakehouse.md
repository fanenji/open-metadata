---
type: source
title: Using DuckDB with Your Dremio Data Lakehouse
created: 2026-04-08
updated: 2026-04-08
tags: [dremio, duckdb, lakehouse, arrow-flight, integration]
related: [dremio, duckdb, dremio-duckdb-integration, data-lakehouse, apache-arrow-flight, local-offloading-strategy, dremio-simple-query]
sources: ["Using DuckDB with Your Dremio Data Lakehouse.md"]
authors: [Alex Merced]
year: 2023
url: "https://www.dremio.com/blog/using-duckdb-with-your-dremio-data-lakehouse/"
venue: Dremio Blog
---
# Using DuckDB with Your Dremio Data Lakehouse

This article by [[Alex Merced]] (Dremio employee) presents a cost-optimization architecture combining [[dremio]] as a massively parallel lakehouse query engine with [[duckdb]] as a local in-process analytical database. The core thesis is that by using Dremio as a data unification and governance layer, users can pull filtered subsets of data via [[apache-arrow-flight]] and perform ad hoc analytics locally on DuckDB, avoiding cloud compute costs.

The article demonstrates three implementation approaches:
1. **Manual pyArrow + DuckDB**: Using `pyarrow.flight.FlightClient` to query Dremio, convert the `FlightStreamReader` to an Arrow table, then to an Arrow dataset, and finally to a DuckDB relation via `duckdb.arrow()`.
2. **Simplified via `dremio-simple-query`**: Using the `DremioConnection.toDuckDB()` method to directly return a DuckDB relation from a Dremio query.
3. **Arrow table reference in DuckDB**: Using `DremioConnection.toArrow()` to get a stream, converting to an Arrow table, and referencing it directly in DuckDB SQL queries.

The example query joins an Iceberg table (from Dremio Arctic Catalog), a Snowflake table, and a Delta Lake table — demonstrating Dremio's data unification capability across heterogeneous sources.

The article positions this pattern as a solution to vendor lock-in, runaway data copies, and escalating storage/compute costs in traditional data warehouses. It emphasizes that Dremio handles governance and authorization, while DuckDB handles local processing of filtered subsets.

**Key caveats**: The article does not provide performance benchmarks, cost comparison data, or discuss data volume limits, network transfer costs, or security implications of moving data outside Dremio's governance boundary.