type: concept
title: Hybrid Geospatial Systems
created: 2026-04-04
updated: 2026-04-04
tags: [geospatial, cloud-native, browser, architecture]
related: [kyle-barron, geoarrow, geoparquet, lonboard, geoarrow-rust, data-boundaries-problem, cloud-native-geospatial-workflow, duckdb, datafusion, polars]
sources: ["Interview with Kyle Barron on GeoArrow and GeoParquet, and the Future of Geospatial Data Analysis.md"]
---
# Hybrid Geospatial Systems

Hybrid geospatial systems are an architectural pattern where data processing spans local and remote (cloud) data stores, intelligently fetching only the portions of data required for a given query over the network. This concept is central to [[kyle-barron]]'s vision for the future of geospatial data analysis.

## Motivation

Network bandwidth is the primary bottleneck in modern geospatial workflows. Both local devices and cloud compute are getting more powerful, but internet connectivity is not improving proportionally fast. This creates a gulf between local on-device compute and cloud compute, making data movement minimization the key design challenge.

## Enabling Technologies

- **Hybrid analytical databases:** [[DuckDB]], [[DataFusion]], and [[Polars]] can work with data on the cloud in a hybrid approach, fetching only required portions.
- **In-memory formats:** [[geoarrow]] enables efficient binary-level data sharing between programs.
- **Cloud-native file formats:** [[geoparquet]] allows reading only relevant portions of files from cloud storage.
- **Browser-based processing:** [[geoarrow-rust]] provides WebAssembly bindings for browser-based geospatial data processing.

## Browser-Based Vision

[[kyle-barron]] envisions a future where non-technical users navigate to a website, connect to all their local and cloud-based data sources, and the system intelligently decides which data sources to download and materialize into the browser. This would connect to rendering technology like [[lonboard]] to efficiently display data on interactive maps.

## Current Progress

Kyle has demonstrated this concept by collaborating with Meta to access [[Overture Maps]] GeoParquet data directly from the browser, performing spatial queries of data from S3 without any server involved.