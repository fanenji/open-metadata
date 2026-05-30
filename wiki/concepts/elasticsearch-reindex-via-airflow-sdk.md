---
type: concept
title: Elasticsearch Reindex via Airflow SDK
created: 2026-05-14
updated: 2026-05-14
tags: [elasticsearch, reindex, airflow, sdk, automation, metadata-workflow]
related: [reindexing-search, cli-ingestion-with-basic-auth, metadata-cli, ingestion-framework, personal-access-token, metadata-workflow]
sources: ["run-elasticsearch-reindex-using-airflow-sdk---open-20260514.md"]
---
# Elasticsearch Reindex via Airflow SDK

The Elasticsearch Reindex via Airflow SDK is a programmatic method to rebuild the OpenMetadata search index using a Python DAG in Apache Airflow. It serves as an alternative to the UI-based reindex procedure documented in [[reindexing-search]], enabling automation, scheduling, and integration with existing Airflow-based ingestion pipelines.

## Workflow

1. **Define a YAML configuration** specifying the source (`MetadataES`), sink (Elasticsearch), and workflow settings (including the `recreate_indexes` flag and JWT authentication).
2. **Create a Python DAG** in Airflow that uses the `MetadataWorkflow` class from the OpenMetadata SDK (`metadata.workflow.metadata`) to execute the reindex operation.
3. **Schedule the DAG** as needed (e.g., after major ingestion runs, daily, or weekly).

## Key Components

- **MetadataWorkflow** — The same SDK workflow class used for metadata ingestion pipelines; handles the reindex operation when configured with the `MetadataES` source type.
- **YAML Config** — A configuration block defining source, sink, and workflow parameters, following the same pattern as metadata ingestion workflows.
- **JWT Token** — Authentication mechanism for headless/automated execution; embedded in the YAML config under `securityConfig`.
- **recreate_indexes** — A boolean flag that controls whether existing Elasticsearch indexes are dropped and recreated. Setting this to `true` is a destructive operation.

## When to Use

- Users who already run Airflow for metadata ingestion pipelines and want a unified orchestration approach.
- Environments requiring scheduled, automated reindexing (e.g., after nightly ingestion runs).
- Teams that need to integrate reindexing into CI/CD pipelines or other automated workflows.

## Important Considerations

- The `recreate_indexes: true` flag is destructive — it drops existing indexes before rebuilding. Use `false` for incremental updates if supported.
- The JWT token must be generated from the OpenMetadata server and have appropriate permissions (typically Admin or a bot account).
- The Airflow environment must have the OpenMetadata SDK installed (`openmetadata-ingestion` package).
- The sample DAG uses a `schedule_interval` of every 5 minutes, which is likely too frequent for production. A daily or weekly schedule is more appropriate.

## Relationship to UI-Based Reindex

The UI-based procedure ([[reindexing-search]]) exposes nine configurable parameters (e.g., `batchSize`, `recreateSubTopicIndexes`, `searchIndexMappingLanguage`) that are not covered in the Airflow SDK documentation. It is unclear whether the Airflow SDK method supports these same parameters. The UI method is recommended for ad-hoc reindexing or when fine-grained control is needed.