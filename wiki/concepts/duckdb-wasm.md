---
type: concept
title: DuckDB WebAssembly (WASM)
created: 2026-04-04
updated: 2026-04-04
tags: [duckdb, wasm, webassembly, analytics, browser]
related: [duckdb, one-point-five-tier-architecture, duckdb-enterprise-use-cases]
sources: ["The Enterprise Case for DuckDB 5 Key Categories and Why Use It.md"]
---
# DuckDB WebAssembly (WASM)

DuckDB compiled to WebAssembly, enabling the full analytical database engine to run inside a web browser. This is a key enabler for the 1.5-tier architecture and interactive data applications.

## Capabilities

- Runs a full OLAP query engine within the browser environment.
- Provides local file system access for reading and writing data.
- Works on mobile devices, including Android phones.
- Eliminates network latency for data processing by keeping compute co-located with the user.

## Use Cases

- **Interactive dashboards**: Tools like Rill Developer, Evidence, and Observable Framework use DuckDB WASM for responsive data exploration.
- **Browser-based analytics**: Users can analyze datasets (e.g., NYC taxi data with 1.5 billion rows) directly in the browser.
- **Edge computing**: Process data on the client side without sending it to a server.

## Relationship to 1.5-Tier Architecture

DuckDB WASM is the client-side component of MotherDuck's 1.5-tier architecture. The same DuckDB engine runs in the browser (via WASM) and in the cloud, enabling seamless compute distribution.