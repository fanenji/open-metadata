---
type: entity
title: Ingestion Framework
created: 2024-05-24
updated: 2024-05-24
tags: [openmetadata, ingestion, metadata-pipeline]
related: [openmetadata, data-profiling, data-lineage, data-quality, airflow]
sources: ["sources.md"]
---

# Ingestion Framework

The Ingestion Framework is the backbone of OpenMetadata, responsible for moving metadata from source systems into the OpenMetadata platform. It handles the extraction, transformation, and loading (ETL) of metadata from a wide variety of sources, including databases, data warehouses, dashboards, pipelines, and more.

## Role

The Ingestion Framework is the critical component for getting data into the system. It separates the concerns of extraction (handled by the framework) from storage and presentation (handled by the OpenMetadata Server and UI).

## Orchestration

Ingestion pipelines are typically orchestrated using tools like [[Airflow]], which schedule and monitor the execution of metadata extraction jobs.

## Key Capabilities

- Extracts metadata from diverse source systems.
- Supports data profiling and data quality tests during ingestion.
- Captures data lineage information.
- Can be configured to run on a schedule or on-demand.