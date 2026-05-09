---
type: concept
title: Iceberg Hidden Partitioning
created: 2026-04-04
updated: 2026-04-04
tags: [iceberg, partitioning, data-lakehouse]
related: [apache-iceberg, iceberg-partition-evolution, data-lakehouse]
sources: ["Open Source and the Data Lakehouse Iceberg and Project Nessie.md"]
---
# Iceberg Hidden Partitioning

Hidden partitioning is a feature of [[Apache Iceberg]] that provides the benefits of partitioning without exposing the complexity to end users. Instead of requiring users to create derived columns for partitioning (e.g., a `month` column), Iceberg allows defining partitioning patterns as transformed values of an existing column.

Engines can partition by month, day, hour, truncated value, or a set number of buckets — all without introducing complexity in how the end user queries the table. The engine handles partition pruning automatically, simplifying query authoring and improving performance transparently.

This is a key differentiator from traditional partitioning schemes where users must be aware of partition columns to write efficient queries.