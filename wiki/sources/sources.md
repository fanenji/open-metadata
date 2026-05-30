---
type: source
title: OpenMetadata Architecture Overview
created: 2024-05-24
updated: 2024-05-24
tags: [openmetadata, architecture, metadata-management]
related: [openmetadata, ingestion-framework, data-profiling, data-lineage, data-quality, glossary-tags]
sources: ["sources.md"]
---

# OpenMetadata Architecture Overview

This source document provides a high-level overview of the OpenMetadata platform, its core architecture, and key features. It describes the three main components: the Ingestion Framework, the OpenMetadata Server, and the OpenMetadata UI, and explains how they work together to enable data discovery, lineage, data quality, observability, and governance.

## Key Points

- OpenMetadata is an open-source platform for end-to-end metadata management.
- The **Ingestion Framework** is the backbone for moving metadata from source systems into OpenMetadata.
- The **OpenMetadata Server** provides the core API and storage layer.
- The **OpenMetadata UI** is the user interface for interacting with the platform.
- Key features include data profiling, data lineage, data quality tests, and business glossary/tags.
- Common orchestrators like Airflow are used to run ingestion pipelines.
- Elasticsearch powers the search index, and MySQL/PostgreSQL serves as the metadata store.

## Relevance

This document serves as a foundational overview of the OpenMetadata system, defining the relationships between its core components and features. It is essential for understanding the platform's architecture and capabilities.