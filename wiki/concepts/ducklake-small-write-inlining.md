type: concept
title: DuckLake Small Write Inlining
created: 2026-04-29
updated: 2026-04-29
tags: [ducklake, small-files-problem, streaming, cdc]
related: [ducklake, apache-iceberg, delta-lake, data-lakehouse]
sources: ["iceberg-built-a-maze-ducklake-just-handed-you-a-map.md"]
---
# DuckLake Small Write Inlining

A design-level solution to the small-files problem in lakehouse architectures, introduced by DuckLake. For writes below a configurable threshold, DuckLake can inline data directly into the catalog database, bypassing the write-to-Parquet step entirely. When enough inlined changes accumulate, they flush to Parquet as automatic micro-batching with zero extra infrastructure.

## Motivation

One of the genuine weaknesses of Iceberg for streaming or CDC workloads is that every small append produces new metadata files. A thousand small transactions per minute produce a thousand new manifest files per minute, creating the small-files problem that requires ongoing compaction.

## How It Works

- Configurable threshold determines when writes are inlined vs. written to Parquet
- Small writes go directly into the catalog database as metadata
- Accumulated inlined changes are flushed to Parquet automatically
- No separate compaction infrastructure needed

## Significance

This addresses the small-files problem at the architectural level rather than with operational band-aids like compaction jobs. It is particularly relevant for streaming and CDC workloads where small, frequent writes are common.