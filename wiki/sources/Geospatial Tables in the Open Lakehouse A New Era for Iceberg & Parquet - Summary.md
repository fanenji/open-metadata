---
type: source
title: "Geospatial Tables in the Open Lakehouse: A New Era for Iceberg & Parquet — Summary"
created: 2026-04-04
updated: 2026-04-29
tags: [geospatial, iceberg, geoparquet, parquet, lakehouse, spatial]
related: [iceberg-v3-geo-types, geoparquet-origins, foursquare-geospatial-architecture, spatial-predicate-pushdown, iceberg-rest-catalog, geoparquet-vs-iceberg-metadata, iceberg-geospatial-support, duckdb-iceberg-extension, data-lakehouse]
sources: ["Geospatial Tables in the Open Lakehouse A New Era for Iceberg & Parquet - Summary.md"]
authors: [Jia Yu, Chris Holmes, Szehon Ho, Vikram Gundeti]
year: 2025
url: "https://www.youtube.com/watch?v=m5SvI2MjCmk"
venue: Wherobots Livestream
---
# Geospatial Tables in the Open Lakehouse: A New Era for Iceberg & Parquet — Summary

This source is a summary of a Wherobots livestream panel (May 8, 2025) featuring Jia Yu (Wherobots), Chris Holmes (Planet, creator of GeoParquet), Szehon Ho (Databricks, Iceberg PMC), and Vikram Gundeti (Foursquare, CTO). The panel discusses the evolution of geospatial data management in the open lakehouse ecosystem, focusing on GeoParquet's role in interoperability, the introduction of native geospatial types in Apache Iceberg V3, and the architectural implications for storage/compute separation and catalog standardization.

Key topics include: the origins and design of GeoParquet, the Iceberg V3 geo type specification (CRS + edge interpolation parameters, row-group-level bounding box statistics), the performance benefits of two-level spatial pruning, Foursquare's real-world architecture for billions of GPS pings, the comparison between Iceberg and Delta Lake for geospatial workloads, and the critical role of catalog standardization (Iceberg REST Catalog) for governance and observability.
