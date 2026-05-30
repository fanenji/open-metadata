---
type: source
title: "OpenMetadata System Architecture | Developer Guide"
created: 2026-05-14
updated: 2026-05-14
tags: [architecture, developer-guide, openmetadata]
related: [openmetadata, openmetadata-system-architecture, dropwizard, schema-first-approach, external-dependencies-configuration, openmetadata-code-layout]
sources: ["openmetadata-system-architecture-developer-guide---20260514.md"]
authors: ["OpenMetadata Documentation Team"]
year: 2026
url: "https://docs.open-metadata.org/v1.12.x/developers/architecture"
venue: "OpenMetadata Official Documentation v1.12.x"
---

# OpenMetadata System Architecture | Developer Guide

This is the official developer-oriented architecture page from the OpenMetadata v1.12.x documentation. It provides a minimal, high-level overview of the platform's four core dependencies.

## Summary

OpenMetadata is described as an end-to-end metadata platform that includes data discovery, governance, data quality, observability, and people collaboration. The platform depends on the following components:

- **JsonSchemas** for defining Metadata Schemas
- **Dropwizard/Jetty** for REST APIs
- **MySQL 8.x** to store Metadata
- **ElasticSearch 7.x** to index Metadata and power search

The page directs readers to the "Design page" for a more comprehensive understanding of how everything fits together, and references the ML Model entity page as an example of schema design and API behavior.

## Key Takeaways

This source establishes the official, canonical list of core architectural dependencies. It is notably sparse and does not cover the ingestion framework, the unified metadata graph, or the Kubernetes-native orchestrator — topics documented elsewhere in the wiki. The explicit mention of ElasticSearch 7.x (rather than OpenSearch) reflects the version-specific nature of this documentation snapshot.