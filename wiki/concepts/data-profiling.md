---
type: concept
title: Data Profiling
created: 2024-05-24
updated: 2024-05-24
tags: [openmetadata, data-quality, data-profiling]
related: [openmetadata, data-quality, ingestion-framework]
sources: ["sources.md"]
---

# Data Profiling

Data profiling in OpenMetadata is the process of analyzing data to understand its structure, content, and quality. It is a key feature for data quality management and is typically executed as part of the ingestion pipeline.

## Purpose

Data profiling helps users understand the characteristics of their data assets, such as column distributions, null values, data types, and patterns. This information is essential for data governance, quality assessment, and discovery.

## Integration

Profiling is performed by the [[Ingestion Framework]] and the results are stored in the [[OpenMetadata]] server, where they can be viewed in the UI.