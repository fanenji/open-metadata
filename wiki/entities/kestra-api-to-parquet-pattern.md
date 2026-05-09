---
type: entity
title: Kestra API to S3 Parquet Pattern
created: 2026-04-29
updated: 2026-04-29
tags: [kestra, ingestion, parquet, s3, api, workflow, pattern]
related: [kestra, kestra-ion-format, elt-pattern, push-vs-pull-ingestion, data-ingestion-architectural-patterns]
sources: ["Kestra API to S3 Parquet.txt"]
---
# Kestra API to S3 Parquet Pattern

A reference pattern for ingesting data from an HTTP API into S3 as Parquet using [[kestra]]. The pattern consists of four sequential tasks: HTTP download, JSON-to-Ion conversion, Ion-to-Parquet conversion with an explicit Avro schema, and S3 upload with date-partitioned keys.

## Workflow Steps

1. **HTTP Download** — Uses `io.kestra.plugin.core.http.Download` to fetch data from an API endpoint.
2. **JSON to Ion** — Converts the downloaded JSON to Kestra's internal [[kestra-ion-format]] using `io.kestra.plugin.serdes.json.JsonToIon`.
3. **Ion to Parquet** — Converts Ion to Parquet using `io.kestra.plugin.serdes.parquet.IonToParquet`, requiring an explicit Avro schema for column type definition.
4. **S3 Upload** — Uploads the Parquet file to S3 using `io.kestra.plugin.aws.s3.Upload` with a date-partitioned key pattern (`raw/data/yyyy/MM/dd/output.parquet`).

## Key Characteristics

- **Pull ingestion**: Kestra actively pulls data from the API ([[push-vs-pull-ingestion]]).
- **ELT pattern**: Extract and load raw data, transform later ([[elt-pattern]]).
- **Schema-on-write**: Parquet requires an explicit schema at write time, hardcoded in the workflow YAML.
- **Date partitioning**: Standard data lake organization pattern for raw ingestion layers.
- **Secret management**: Uses `{{ secret() }}` for credential injection.

## Production Considerations

This pattern is a minimal template. Production deployments should add:
- Error handling and retry logic
- Data quality validation (e.g., [[great-expectations-for-data-contracts]])
- Schema evolution management (e.g., schema registry integration)
- Monitoring and alerting (e.g., [[data-observability-definition]])
- Performance tuning for large payloads (chunking, parallelization)

## Open Questions

- How does Kestra handle schema evolution when the API response structure changes?
- What is the performance ceiling for this pattern (file size, record count)?
- Does Kestra support schema registry integration (e.g., Confluent Schema Registry) for the Parquet conversion?