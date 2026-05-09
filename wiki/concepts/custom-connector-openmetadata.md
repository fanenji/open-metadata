---
type: concept
title: Custom Connector (OpenMetadata)
created: 2026-01-10
updated: 2026-01-10
tags: [openmetadata, custom-connector, metadata-ingestion, integration]
related: [openmetadata, openmetadata-dremio-connector, data-catalog-tool-comparison]
sources: ["Dremio Connector.md"]
---
# Custom Connector (OpenMetadata)

A user-built integration that ingests metadata from a data source not natively supported by [[openmetadata]]. Custom connectors follow a documented pattern and can be developed for any system that exposes schema, lineage, or other metadata.

## Pattern

OpenMetadata provides a framework for building custom connectors, including example code in the [openmetadata-demo repository](https://github.com/open-metadata/openmetadata-demo/tree/main/custom-connector) and [official documentation](https://docs.open-metadata.org/latest/connectors/custom-connectors). The pattern involves:

1. Implementing a connector class that interfaces with the target system's API or query engine.
2. Defining the metadata schema to be ingested (tables, columns, relationships).
3. Configuring the connector within OpenMetadata's ingestion framework.

## Example

The [[openmetadata-dremio-connector]] by [[tiki-institut]] is a concrete implementation of this pattern, enabling metadata ingestion from [[dremio]] into OpenMetadata.

## Relevance

Custom connectors extend OpenMetadata's reach to any data platform, making it a more flexible metadata management solution. This is particularly important for organizations using niche or legacy systems alongside mainstream platforms.