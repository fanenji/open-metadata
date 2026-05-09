---
type: source
title: "Writing Iceberg Tables with DuckDB 1.4.0: A Practical Starter Guide"
created: 2026-05-07
updated: 2026-05-07
tags: [duckdb, iceberg, lakehouse, tutorial]
related: [duckdb-iceberg-write-support, local-iceberg-development-stack, duckdb-iceberg-extension, data-lakehouse, dwicky-feri]
sources: ["Writing Iceberg Tables with DuckDB 1.4.0 A Practical Starter Guide.md"]
authors: [Dwicky Feri]
year: 2025
url: "https://dwickyferi.medium.com/writing-iceberg-tables-with-duckdb-1-4-0-a-practical-starter-guide-54d6da4c4bce"
venue: "Medium"
---
# Writing Iceberg Tables with DuckDB 1.4.0: A Practical Starter Guide

A practical walkthrough demonstrating how to write Apache Iceberg tables using DuckDB 1.4.0's new Iceberg write capability. The guide covers setting up a local Iceberg stack with Docker (Lakekeeper REST catalog and optional MinIO object store), configuring DuckDB to connect via the REST catalog protocol, and executing a simple SQL script to create, insert, and query an Iceberg table. The author emphasizes the approachability of the workflow — requiring only Docker and a small SQL script to produce production-grade open table formats locally. The guide positions DuckDB as a lightweight Iceberg authoring tool for prototyping before scaling to big data engines like Spark, Flink, and Trino.