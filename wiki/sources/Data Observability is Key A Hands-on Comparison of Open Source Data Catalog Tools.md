---
type: source
title: "Data Observability is Key: A Hands-on Comparison of Open Source Data Catalog Tools"
created: 2026-04-29
updated: 2026-04-29
tags: [data-catalog, data-observability, comparison, open-source]
related: [datahub, openmetadata, amundsen, data-catalog-critique, data-mesh, data-observability-definition, data-catalog-tool-comparison, great-expectations-for-data-contracts]
sources: ["Data Observability is Key A Hands-on Comparison of Open Source Data Catalog Tools.md"]
authors: [David Schmidt, Tim Bossenmaier]
year: 2023
url: "https://www.inovex.de/de/blog/data-observability-is-key-a-hands-on-comparison-of-open-source-data-catalog-tools"
venue: "inovex blog"
---
# Data Observability is Key: A Hands-on Comparison of Open Source Data Catalog Tools

A practical, hands-on comparison of three open-source data catalog tools — [[DataHub]], [[OpenMetadata]], and [[Amundsen]] — deployed on Google Kubernetes Engine (GKE) with BigQuery as an ingestion source. The authors argue that data catalogs are foundational for [[data-observability-definition|data observability]], enabling discovery, governance, and quality management across the organization.

## Key Findings

- **Amundsen** is effectively in maintenance mode and not recommended for new deployments. Outdated dependencies and sparse documentation made deployment impractical.
- **OpenMetadata** excels in governance features (task assignment, approval workflows, PII detection), UX, and ease of ingestion configuration via the UI. Its architecture is simpler than DataHub's, requiring only Elasticsearch, a database, and Airflow.
- **DataHub** offers superior extensibility and engineering flexibility due to its event-based architecture (Kafka, multiple services). It integrates with [[great-expectations-for-data-contracts|Great Expectations]] for testing and supports file-based lineage definition.
- Both tools are viable, with the choice depending on organizational priorities: governance and UX (OpenMetadata) vs. flexibility and community-driven development (DataHub).

## Architecture Notes

- OpenMetadata uses a two-service architecture (ingestion + server) with Airflow for orchestration.
- DataHub uses a complex event-driven architecture with Kafka, Elasticsearch, a database, and multiple consumer services.
- Both tools support YAML/CLI-based ingestion as an alternative to UI configuration.

## Concerns

The authors express a "gut feeling" that OpenMetadata's OSS future may be deprioritized in favor of its SaaS offering (Collate), while DataHub's community-driven model appears more sustainable.

## Connection to Existing Wiki

This source extends the [[data-catalog-critique]] by showing that modern catalogs (OpenMetadata, DataHub) integrate ingestion, profiling, and governance into a unified platform, partially addressing the critique's concerns about disconnectedness. It also strengthens the [[data-mesh]] concept by explicitly stating that catalogs are essential for preventing data silos in mesh architectures.
