---
type: entity
title: OpenMetadata Architecture
created: 2026-04-05
updated: 2026-04-05
tags: [openmetadata, architecture, deployment]
related: [openmetadata, openmetadata-ingestion-framework, openmetadata-python-sdk, elasticsearch, mysql]
sources: ["OpenMetadata - The Complete Guide Every Data Engineer Needs to Read.md"]
---
# OpenMetadata Architecture

OpenMetadata is built on four main components:

1. **OpenMetadata Server** — The core service exposing the REST API, storing metadata, handling search, and running the UI.
2. **Metadata Store** — Built on MySQL (or compatible databases). Stores all entities (tables, pipelines, dashboards, users, tags, lineage) in a structured, versioned schema.
3. **Elasticsearch / OpenSearch** — Powers search and discovery. When you search for a table name or filter by tag, it hits Elasticsearch under the hood.
4. **Ingestion Framework** — A Python-based framework that connects to data sources and pulls metadata into the server. Runs as standalone scripts, Airflow DAGs, or scheduled jobs.

## Deployment Options

- **Docker Compose** — Fastest way to get started locally. Download the `docker-compose.yml` from GitHub releases and run `docker compose up -d`. Accessible at `http://localhost:8585` with default credentials `admin/admin`.
- **Kubernetes / Helm** — For production deployments. Install via Helm charts with dependencies (Airflow, MySQL, Elasticsearch).
- **Bare Metal / VM** — Manual installation of all components.

## Key Design Principles

- **Unified Metadata Model** — An open standard schema for all metadata entities.
- **Open API Standard** — Every operation is exposed via a full REST API.
- **Versioned Metadata** — Every change to every asset is tracked and versioned.