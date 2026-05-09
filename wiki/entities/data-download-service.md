---
type: entity
title: Data Download Service
created: 2026-04-29
updated: 2026-04-29
tags: [data-platform, download, architecture, opendata]
related: [frictionless-data-package, metadata-fields-definition, data-ingestion-architectural-patterns, elt-pattern, dbt-artifacts]
sources: ["DOWNLOAD.md"]
---
# Data Download Service

The Data Download Service is a subsystem of the Data Platform responsible for preparing, packaging, and serving data to consumers. It is designed with a **synchronous-first** philosophy: data is prepared in all available formats and served immediately. Asynchronous mode is reserved for exceptional cases, such as dynamic format conversion (e.g., Parquet → CSV), flagged by a FLAG.

## Core Functions

- **Controls**: Access control, rate limiting, and validation.
- **Caching**: Storage of prepared data to reduce repeated computation.
- **URL Provisioning**: Generation of download URLs for consumers.
- **Notifications**: Alerts to consumers when async downloads are ready.
- **Logging**: Audit trail of all download requests and completions.
- **Async Request Handling**: Queue management for long-running format conversions.

## Metadata Attachment

Every download includes a metadata bundle containing:
- **Description**: Human-readable explanation of the dataset.
- **Schema**: Column names, types, and constraints.
- **Lineage**: Provenance information tracing the data's origin and transformations.

The [[frictionless-data-package]] standard is proposed as the packaging format for this metadata.

## Design Tensions

- **Sync vs Async**: Synchronous mode simplifies the system but limits format flexibility. Dynamic conversion (e.g., Parquet → CSV) may require async mode, creating a trade-off between simplicity and flexibility.
- **Credential Storage**: User/password credentials for source connections can be stored in a database (centralized, auditable) or configuration file (simpler, less secure). This is an unresolved architectural decision.

## Connections to Existing Wiki

- [[metadata-fields-definition]] — The metadata attachment requirement aligns with the existing metadata governance fields.
- [[data-ingestion-architectural-patterns]] — Download is the inverse of ingestion; similar architectural patterns apply (push vs pull, sync vs async).
- [[elt-pattern]] — The download function is a consumer-facing output of the ELT pipeline.
- [[dbt-artifacts]] — Lineage metadata could be sourced from dbt artifacts.