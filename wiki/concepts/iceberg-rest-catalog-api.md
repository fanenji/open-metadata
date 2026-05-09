---
type: concept
title: Iceberg REST Catalog API
created: 2026-04-04
updated: 2026-04-04
tags: [apache-iceberg, catalog, api, interoperability]
related: [apache-iceberg, apache-polaris, snowflake-open-catalog, iceberg-query-engine-comparison]
sources: ["Is Apache Iceberg Melting?.md"]
---
# Iceberg REST Catalog API

A standardized REST-based catalog protocol defined by the Iceberg specification with an OpenAPI spec. It enables multi-engine interoperability by providing a common interface for catalog operations.

## Ecosystem Adoption

- AWS Glue documents an Iceberg REST endpoint for connecting engines to a REST catalog hosted in the Data Catalog
- Apache Polaris (incubating) implements Iceberg's REST API for multi-engine interoperability
- Snowflake Open Catalog is a managed service for Apache Polaris built on the Iceberg REST protocol

## Strategic Importance

For organizations pursuing a multi-engine, multi-platform long-term strategy, REST catalog compatibility should be treated as a first-class requirement. If starting from Hive Metastore or Glue, those can be initial options, but the REST catalog direction is the long-term standard.
