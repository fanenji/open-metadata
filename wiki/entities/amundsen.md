---
type: entity
title: Amundsen
created: 2026-04-29
updated: 2026-05-08
tags: [data-catalog, open-source, lyft, deprecated, metadata-platform, data-mesh, catalog]
related: [datahub, openmetadata, data-catalog-tool-comparison, elasticsearch, neo4j, data-mesh, data-mesh-maturity-assessment, data-mesh-kpis, data-product-definition]
sources: ["Data Observability is Key A Hands-on Comparison of Open Source Data Catalog Tools.md", "research-data-mesh-organizational-maturity-assessment-2026-05-08.md"]
---
# Amundsen

Amundsen is an open-source data catalog tool originally developed by [[Lyft]] and released in 2019. It is one of the three major open-source data catalog tools, alongside [[DataHub]] and [[OpenMetadata]]. As of 2023, Amundsen is effectively in **maintenance mode** (see [[#Status|Status]]). In the context of [[data-mesh]], Amundsen is referenced in the [[data-mesh-maturity-assessment]] as a tool for publishing and discovering [[data-product-definition|data products]] and as a key indicator of data accessibility/discoverability maturity.

## Status

As of 2023, Amundsen is effectively in **maintenance mode**. According to a maintainer statement in the project's Slack, Lyft is not actively developing features for the OSS system and only supports community contributions. The project is not recommended for new deployments.

## Architecture

Amundsen has the simplest architecture among the compared tools:

- **Prerequisites**: [[Elasticsearch]] (search engine) and [[Neo4J]] (graph index) — [[Apache Atlas]] can be used as an alternative to Neo4J
- **Backend**: Two services — metadata service and search service
- **Frontend**: Single service communicating via REST APIs
- **Ingestion**: The `amundsen-databuilder` library extracts metadata from source systems

## Data Mesh Context

In the [[data-mesh-maturity-assessment]], Amundsen is referenced as:
- A tool for publishing and discovering [[data-product-definition|data products]]
- A key indicator of data accessibility/discoverability maturity

Amundsen is one of several data catalog tools (alongside [[DataHub]] and [[OpenMetadata]]) that serve as maturity indicators in the [[data-mesh-kpis]].

## Why It Was Excluded

The authors attempted to deploy Amundsen on Kubernetes but encountered significant issues:

- The public Helm chart uses outdated sources
- The Neo4J version in the chart is incompatible with the databuilder library
- Documentation is sparse
- The project is in maintenance mode with no active feature development

## Historical Significance

Amundsen was a pioneering open-source data catalog that influenced the design of later tools. Its core concepts — metadata extraction, search, and graph-based relationships — are now standard features in [[DataHub]] and [[OpenMetadata]].