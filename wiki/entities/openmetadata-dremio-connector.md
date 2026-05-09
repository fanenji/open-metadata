---
type: entity
title: OpenMetadata Dremio Connector
created: 2026-01-10
updated: 2026-01-10
tags: [openmetadata, dremio, custom-connector, metadata-ingestion]
related: [openmetadata, dremio, tiki-institut, data-catalog-tool-comparison]
sources: ["Dremio Connector.md"]
---
# OpenMetadata Dremio Connector

A custom OpenMetadata connector for [[dremio]], developed and maintained by [[tiki-institut]]. This connector enables metadata ingestion from Dremio into [[openmetadata]], which does not natively support Dremio as a data source.

## Purpose

The connector allows organizations using Dremio as their data lakehouse query engine to catalog schemas, tables, views, and lineage within OpenMetadata. This fills a gap in the OpenMetadata ecosystem and enables unified metadata management across heterogeneous data platforms.

## Installation and Configuration

Refer to the [official repository](https://github.com/TIKI-Institut/openmetadata-dremio-connector) for installation instructions, configuration parameters, and usage examples. The connector follows the [[openmetadata]] custom connector pattern documented in the [OpenMetadata Custom Connectors Guide](https://docs.open-metadata.org/latest/connectors/custom-connectors).

## Status

The connector is hosted on GitHub by TIKI-Institut. Its production readiness and maintenance cadence are not documented in the source material. Users should evaluate the repository for recent commits, issue tracking, and community activity before deploying in production.