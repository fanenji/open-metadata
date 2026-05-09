---
type: concept
title: Metadata Fields Definition
created: 2026-04-29
updated: 2026-04-29
tags: [metadata, governance, data-platform, schema]
related: [data-domain-governance, data-catalog-critique, kestra, data-observability-definition, federated-computational-governance, dbt-osmosis]
sources: ["DEFINIZIONE METADATI.md"]
---
# Metadata Fields Definition

A minimal, structured set of metadata fields required to govern the Data Platform. This schema defines the core attributes that should be tracked for every dataset or project within the platform.

## Fields

| Field | Description | Type | Required |
|-------|-------------|------|----------|
| Project Managers | People responsible for the data platform project | Person (1..n) | Yes |
| Data Stewards | People responsible for specific datasets | Person (1..n) | Yes |
| Update Frequency | Cron pattern for data refresh schedules | String (cron) | Yes |
| Last Update Date | Timestamp of the most recent data update | DateTime | Yes |
| Last Update Status | Whether the last data refresh succeeded or failed | Enum (success/failed) | Yes |
| Project Development Status | Lifecycle stage of the project | Enum (dev/staging/prod/deprecated) | Yes |
| Data Accessibility Level | Classification of data access permissions | Enum (public/internal/restricted/confidential) | Yes |

## Usage

These fields should be populated for every dataset and project in the Data Platform. They can be managed through:

- **Manual entry** via a governance interface
- **Automated population** via [[dbt-osmosis]] schema synchronization
- **Post-run hooks** in [[kestra]] to update status fields after each execution

## Connections

- Strengthens [[data-domain-governance]] by providing concrete metadata fields for governance tracking.
- Extends [[data-catalog-critique]] by offering a minimal catalog schema that could be embedded in the platform.
- The **Update Frequency** and **Last Update Status** fields enable [[data-observability-definition]] freshness monitoring.
- The **Data Accessibility Level** field directly supports [[federated-computational-governance]].

## Open Questions

- What are the exact enum values for **Data Accessibility Level**? (e.g., public, internal, restricted, confidential)
- What are the exact enum values for **Project Development Status**? (e.g., dev, staging, prod, deprecated)
- How are these fields populated — manually, via dbt-osmosis, or via Kestra post-run hooks?
- Is there a relationship between **Data Stewards** and existing domain owners in [[data-domain-governance]]?