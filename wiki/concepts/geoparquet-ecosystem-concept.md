---
type: concept
title: GeoParquet Ecosystem
created: 2026-05-07
updated: 2026-05-07
tags: [geoparquet, ecosystem, cloud-native, geospatial]
related: [geoparquet-ecosystem, geoarrow, source-cooperative, cloud-native-geospatial-workflow, formati-e-standard]
sources: ["The GeoParquet Ecosystem at 1.0.0.md"]
---
# GeoParquet Ecosystem

The GeoParquet Ecosystem refers to the collection of libraries, tools, data providers, and community infrastructure that support the GeoParquet 1.0.0 specification. It represents the practical realization of cloud-native geospatial data processing.

## Components

- **Libraries**: Multi-language support (Python, R, Go, Rust, JavaScript, Julia, .NET, C++)
- **Tools**: CLI, desktop, web, converters, frameworks
- **Data Providers**: Organizations publishing GeoParquet datasets
- **Hosting**: [[Source Cooperative]] as central repository
- **Community**: Slack, bi-weekly meetings, OGC grants

## Significance

The ecosystem's robustness is a key indicator of GeoParquet's viability as a standard format. The presence of multiple independent implementations and a growing body of data providers demonstrates real-world adoption beyond the specification itself.

## Gaps

- No native Java library
- DuckDB lacks direct GeoParquet support
- QGIS Mac installer requires workaround

## Relevance to Project

Understanding the GeoParquet ecosystem is essential for evaluating whether to adopt GeoParquet as a standard format for geospatial data exchange within the project's data platform.