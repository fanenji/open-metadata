---
type: source
title: "Oracle Connector | OpenMetadata Enterprise Database Guide"
created: 2026-05-14
updated: 2026-05-14
tags: [oracle, connector, ingestion, metadata, permissions]
related: [oracle-connector, openmetadata-connectors, service-connection, metadata-ingestion-workflow, data-profiling, data-quality, dbt-integration, data-lineage]
sources: ["Oracle Connector  OpenMetadata Enterprise Database Guide.md"]
authors: []
year: 2026
url: "https://docs.open-metadata.org/v1.12.x/connectors/database/oracle"
venue: "OpenMetadata Official Documentation"
---
# Oracle Connector | OpenMetadata Enterprise Database Guide

Official documentation for the Oracle connector in OpenMetadata v1.12.x. Covers supported Oracle versions (12c, 18c, 19c, 21c), the `python-oracledb` driver, minimum permission requirements for metadata ingestion (`CREATE SESSION` + `SELECT_CATALOG_ROLE`), additional `SELECT` grants needed for Profiler and Data Quality features, and the Oracle-specific limitation that no native schema-level `SELECT` grant exists. Provides SQL examples for both role-based and direct user permission models. References external guides for Usage, Lineage, Profiler, Data Quality, dbt integration, and troubleshooting workflows.