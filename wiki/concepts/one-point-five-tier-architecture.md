---
type: concept
title: 1.5-Tier Architecture
created: 2026-04-04
updated: 2026-04-04
tags: [architecture, duckdb, motherduck, analytics]
related: [duckdb, duckdb-enterprise-use-cases, duckdb-wasm, motherduck]
sources: ["The Enterprise Case for DuckDB 5 Key Categories and Why Use It.md"]
---
# 1.5-Tier Architecture

A data architecture pattern introduced by MotherDuck that sits between the traditional two-tier and three-tier architectures. In this model, the same DuckDB engine runs in both the user's web browser (or client) and the cloud, reducing the number of intermediate operations between the presentation layer and the data tier.

## How It Works

- The DuckDB engine is embedded in the browser via WebAssembly (WASM).
- The same engine runs in the cloud (MotherDuck).
- Data and compute can be moved closer to the user, minimizing network roundtrips.
- Queries can execute partially on the client and partially in the cloud, depending on data locality and performance requirements.

## Advantages Over Three-Tier Architecture

- **Reduced latency**: Fewer network roundtrips between client and server.
- **Improved UX**: Faster query response times for interactive analytics.
- **Simpler setup**: Easier to populate and synchronize new data.
- **Cost efficiency**: Avoids unnecessary cloud compute for operations that can run locally.

## Current Status

The 1.5-tier architecture is currently specific to MotherDuck's implementation. Vanilla DuckDB does not provide this capability natively. Enterprise BI tools (Tableau, Power BI) require MotherDuck to leverage this architecture, as they cannot work with vanilla DuckDB as a persistence layer.