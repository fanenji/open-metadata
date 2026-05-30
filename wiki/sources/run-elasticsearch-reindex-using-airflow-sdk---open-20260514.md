---
type: source
title: "Run Elasticsearch Reindex using Airflow SDK - OpenMetadata Documentation"
created: 2026-05-14
updated: 2026-05-14
tags: [elasticsearch, reindex, airflow, sdk, metadata-workflow, automation]
related: [reindexing-search, cli-ingestion-with-basic-auth, metadata-cli, ingestion-framework, data-insights-application-troubleshooting, airflow-storage-requirements, airflow-to-kubernetes-migration, personal-access-token]
sources: ["run-elasticsearch-reindex-using-airflow-sdk---open-20260514.md"]
authors: [OpenMetadata]
year: 2026
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/data-insights/elasticsearch-reindex"
venue: "OpenMetadata Documentation"
---
# Run Elasticsearch Reindex using Airflow SDK - OpenMetadata Documentation

This official OpenMetadata v1.12.x documentation page describes how to perform an Elasticsearch reindex operation programmatically using the Airflow SDK. It provides a complete YAML configuration template and a Python DAG that wraps the `MetadataWorkflow` class from the OpenMetadata SDK.

The workflow uses the `MetadataES` source type to read metadata from the OpenMetadata server, authenticating via a JWT token embedded in the YAML config. The sink is configured for Elasticsearch with a `recreate_indexes` flag that controls whether existing indexes are dropped and rebuilt.

This method provides an automation-friendly alternative to the UI-based reindex procedure documented in [[reindexing-search]], enabling scheduling and integration into existing Airflow-based workflows.