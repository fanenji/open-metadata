---
type: entity
title: Lakekeeper Catalog
created: 2026-05-07
updated: 2026-05-07
tags: [iceberg, catalog, rest-catalog]
related: [duckdb-iceberg-write-support, local-iceberg-development-stack, duckdb-iceberg-extension]
sources: ["Writing Iceberg Tables with DuckDB 1.4.0 A Practical Starter Guide.md"]
---
# Lakekeeper Catalog

A REST catalog server for Apache Iceberg metadata management, used in the local Iceberg development stack. Lakekeeper implements the Iceberg REST Catalog Protocol, allowing clients like DuckDB to connect and manage Iceberg tables via a standardized HTTP API. In the practical guide, it runs as a Docker container and is accessed by DuckDB through the `ATTACH` statement with an endpoint URL.