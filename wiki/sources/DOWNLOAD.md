---
type: source
title: Data Platform Download Service Design Notes
created: 2026-01-15
updated: 2026-04-29
tags: [data-platform, opendata, download, architecture]
related: [data-download-service, frictionless-data-package, metadata-fields-definition, data-ingestion-architectural-patterns, elt-pattern, dbt-artifacts]
sources: ["DOWNLOAD.md"]
---
# Data Platform Download Service Design Notes

This document captures early-stage design notes for the Data Platform's download subsystem. It outlines the core functions (controls, caching, URL provisioning, notifications, logging, and async request handling), the preferred synchronous download mode, and the conditions under which asynchronous mode is required (dynamic format conversion flagged by a FLAG). The document also specifies metadata attachment requirements (description, schema, lineage) and suggests the Frictionless Data standard as a potential packaging format. A schema section defines source types (SQL, FILE, S3) with connection parameters, and raises an open question about credential storage (database vs configuration file).

## Key Design Decisions

- **Synchronous download as default**: Data is prepared and served immediately in all available formats, simplifying system design.
- **Asynchronous download as exception**: Reserved for cases flagged by a FLAG, primarily dynamic format conversion (e.g., Parquet → CSV).
- **Metadata attachment**: Every download should bundle description, schema, and lineage metadata. Frictionless Data is proposed as the packaging standard.
- **Credential management**: Open question — whether user/password credentials should be stored in a database (centralized, auditable) or configuration file (simpler, less secure).

## Open Questions

1. Can all downloads be served synchronously? What format conversions are required?
2. Which metadata packaging standard to adopt (Frictionless vs custom)?
3. What caching strategy (TTL, invalidation, storage backend)?
4. What notification mechanism (email, webhook, message queue)?
5. Credential storage: database or configuration file?