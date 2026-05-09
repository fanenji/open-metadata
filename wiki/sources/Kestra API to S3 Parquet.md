---
type: source
title: Kestra API to S3 Parquet
created: 2026-04-29
updated: 2026-04-29
tags: [kestra, ingestion, parquet, s3, api, workflow]
related: [kestra, kestra-api-to-parquet-pattern, kestra-ion-format, elt-pattern, push-vs-pull-ingestion, data-ingestion-architectural-patterns]
sources: ["Kestra API to S3 Parquet.txt"]
---
# Kestra API to S3 Parquet

A minimal, working Kestra workflow template for ingesting data from an HTTP API and storing it as Parquet in S3. The workflow demonstrates a four-step pipeline: HTTP download, JSON-to-Ion conversion, Ion-to-Parquet conversion with an explicit Avro schema, and S3 upload with date-partitioned keys.

## Key Points

- **Pull ingestion pattern**: Kestra actively fetches data from the API, following the [[push-vs-pull-ingestion]] pull model.
- **ELT pattern**: The workflow extracts and loads raw data as Parquet, deferring transformation to later stages ([[elt-pattern]]).
- **Intermediate Ion format**: Kestra uses its internal Ion serialization format as an intermediate step between JSON and Parquet ([[kestra-ion-format]]).
- **Schema declaration**: An explicit Avro schema is required for the `IonToParquet` task to define column types, highlighting Parquet's schema-on-write requirement.
- **Date-partitioned S3 keys**: Uses `{{ now() | date('yyyy/MM/dd') }}` for daily partitioning of raw data in the data lake.
- **Secret injection**: Credentials are referenced via `{{ secret() }}` for security best practices.

## Limitations

This is a **template**, not a production configuration. It lacks:
- Error handling and retry logic
- Data quality checks and validation
- Schema evolution management
- Monitoring and alerting
- Performance optimization for large payloads

## Connections

- [[kestra]] — The orchestration tool executing this workflow.
- [[kestra-api-to-parquet-pattern]] — Documented reference pattern for API ingestion via Kestra.
- [[data-ingestion-architectural-patterns]] — This workflow is an instance of the ELT pattern within that framework.