---
type: concept
title: MetadataWorkflow
created: 2026-05-14
updated: 2026-05-14
tags: [sdk, workflow, ingestion, reindex, python]
related: [ingestion-framework, elasticsearch-reindex-via-airflow-sdk, reindexing-search, cli-ingestion-with-basic-auth]
sources: ["run-elasticsearch-reindex-using-airflow-sdk---open-20260514.md"]
---
# MetadataWorkflow

`MetadataWorkflow` is a core Python class from the OpenMetadata SDK (`metadata.workflow.metadata`) that executes metadata ingestion and reindex pipelines. It is the programmatic entry point for running workflows defined by YAML configuration.

## Usage

The workflow is created from a YAML config dictionary using `MetadataWorkflow.create(workflow_config)`, then executed with `.execute()`. After execution, `.raise_from_status()` checks for errors, and `.stop()` performs cleanup.

## Common Use Cases

- **Metadata ingestion** — Extracting metadata from source systems (databases, dashboards, etc.) into OpenMetadata.
- **Elasticsearch reindex** — Rebuilding the search index from the metadata store, using the `MetadataES` source type (see [[elasticsearch-reindex-via-airflow-sdk]]).

## Relationship to Other Components

- The class is part of the [[ingestion-framework]] and is used by both the CLI (`metadata ingest` command via [[metadata-cli]]) and the Airflow SDK.
- It follows the same YAML config-driven pattern as all OpenMetadata ingestion workflows.