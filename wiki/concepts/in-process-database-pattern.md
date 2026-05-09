---
type: concept
title: In-Process Database Pattern
created: 2026-04-29
updated: 2026-04-29
tags: [architecture, database, pattern]
related: [duckdb, embedded-olap-database, sqlite, data-lakehouse]
sources: ["DuckDB — What’s the Hype About?.md"]
---
# In-Process Database Pattern

The in-process database pattern is an architectural approach where the database engine runs inside the same process as the application that uses it, rather than as a separate server process that communicates over a network.

## How It Works

- The database is linked as a library (e.g., a Python package, C library)
- Queries execute directly in the application's memory space
- No network round-trips between client and server
- No separate database server to install, configure, or maintain

## Benefits

- **Zero network latency**: Eliminates the primary bottleneck in client-server database communication
- **Simplified deployment**: `pip install` or equivalent is all that's needed
- **Portability**: Can run on laptops, cloud VMs, cloud functions, browsers
- **Low overhead**: No server process management, connection pooling, or authentication infrastructure

## Trade-offs

- **Single-process limitation**: Cannot handle concurrent writes from multiple processes
- **Resource sharing**: Database competes for CPU/memory with the host application
- **No built-in multi-tenancy**: Not designed for large-scale shared deployments
- **Limited scalability**: Cannot distribute queries across multiple nodes

## Examples

- **[[DuckDB]]**: In-process OLAP database for analytical workloads
- **SQLite**: In-process OLTP database for transactional workloads
- **RocksDB**: Embedded key-value store

## Relevance to Modern Data Stack

The in-process database pattern is gaining relevance in the context of [[data-lakehouse]] architectures and [[self-serve-data-platform]] initiatives, where lightweight, local query engines can complement centralized cloud warehouses for exploratory analysis and edge computing.
