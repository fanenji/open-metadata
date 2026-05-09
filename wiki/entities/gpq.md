---
type: entity
title: GPQ
created: 2026-05-07
updated: 2026-05-07
tags: [geoparquet, go, cli, wasm, validation]
related: [geoparquet-ecosystem, gdal-ogr-geoparquet, cloud-native-geospatial-workflow]
sources: ["The GeoParquet Ecosystem at 1.0.0.md"]
---
# GPQ

GPQ is a Go library and command-line tool for working with GeoParquet, created by [[Tim Schaub]] and sponsored by [[Planet]]. It provides conversion, validation, and description capabilities for GeoParquet files.

## Features

- **Conversion**: Convert GeoJSON to/from GeoParquet
- **Validation**: Full accounting of each GeoParquet spec check
- **Description**: Detailed description of GeoParquet file contents
- **WASM distribution**: Enables browser-based GeoParquet processing (used by Scribble Maps, geoparquet.org converter)
- **Easy installation**: Go's distribution model makes it simple to install on any platform

## Usage

GPQ is the primary tool used by Chris Holmes for validation and working with non-GeoParquet Parquet data. It is also the engine behind the web-based GeoJSON converter at geoparquet.org.

## Relevance to Project

GPQ provides a lightweight, cross-platform tool for validating and converting GeoParquet files, useful for quality assurance in geospatial data pipelines.