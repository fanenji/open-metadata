---
type: concept
title: Data Lineage
created: 2024-05-24
updated: 2024-05-24
tags: [openmetadata, data-lineage, data-governance]
related: [openmetadata, ingestion-framework]
sources: ["sources.md"]
---

# Data Lineage

Data lineage in OpenMetadata tracks the origin and transformation of data as it moves through various systems and pipelines. It provides a visual representation of how data flows from source to destination, enabling impact analysis and governance.

## Purpose

Lineage is critical for understanding data dependencies, troubleshooting issues, and ensuring compliance with data governance policies.

## Implementation

Lineage information is captured by the [[Ingestion Framework]] during metadata extraction and is stored and visualized in the [[OpenMetadata]] UI.