---
type: source
title: "Source: ingest-tiers-from-dbt-openmetadata-data-tiering-gu-20260514.md"
created: 2026-05-15
updated: 2026-05-15
sources: ["ingest-tiers-from-dbt-openmetadata-data-tiering-gu-20260514.md"]
tags: []
related: []
---

# Source: ingest-tiers-from-dbt-openmetadata-data-tiering-gu-20260514.md

## Analysis: Ingest Tiers from dbt | OpenMetadata Data Tiering Guide

### Key Entities

- **dbt (Data Build Tool)** — Central entity; the source system from which tier metadata is ingested. Already exists in wiki as [[dbt]] and [[dbt-integration]].
- **OpenMetadata** — Target platform receiving tier metadata. Already exists in wiki as [[openmetadata]].
- **Tiers** — Core concept being ingested; classification tags for data importance (Tier1-Tier5). Already exists in wiki as [[tiers]].
- **manifest.json** — dbt artifact file that carries tier metadata after dbt workflow execution. Already exists in wiki as [[dbt-artifacts]].
- **schema.yml** — dbt configuration file where tier metadata is manually defined by users. Not explicitly in wiki index.
- **Tier.Tier2** — Example tier value used in documentation; represents a specific tier FQN. Not a standalone entity.

### Key Concepts

- **dbt Tier Ingestion** — Process of extracting table-level tier classifications from dbt's `manifest.json` file and applying them to corresponding tables in OpenMetadata. Extends the existing [[dbt-integration]] with a specific metadata category.
- **Tier FQN (Fully Qualified Name)** — The format `Tier.Tier2` used to reference tiers in dbt meta configuration. Connects to [[tiers]] concept.
- **dbt meta field** — Extensible configuration block in `schema.yml` where OpenMetadata-specific metadata (including tiers) is defined. Not explicitly documented in wiki.

### Main Arguments & Findings

- **Core claim**: Tiers can be ingested from dbt by adding tier FQN under `model->name->meta->openmetadata->tier` in `schema.yml`, then running dbt workflow to generate `manifest.json`.
- **Prerequisite**: Tiers must already exist in OpenMetadata before ingestion — the dbt workflow does not create tiers, only assigns them.
- **Evidence**: Single worked example with `Tier.Tier2` on a `customers` model, showing both `schema.yml` configuration and resulting `manifest.json` structure.
- **Evidence strength**: Weak — single example, no troubleshooting, no edge cases, no validation steps.

### Connections to Existing Wiki

- **Strengthens**: [[dbt-integration]] — adds a specific metadata category (tiers) to the ten already documented categories.
- **Extends**: [[tiers]] — provides a practical ingestion method for applying tiers at scale via dbt, complementing the manual tagging workflow in [[how-to-classify-data-assets-official-documentation-20260514]].
- **Related**: [[dbt-artifacts]] — the `manifest.json` structure shown aligns with documented artifact format.
- **Related**: [[classification-tags]] — tiers are a specialized classification tag; this document shows automated assignment via dbt.

### Contradictions & Tensions

- **No contradictions** with existing wiki content.
- **Internal tension**: The document states tiers "must be created or present in OpenMetadata beforehand" but provides no guidance on how to create them if they don't exist — users must cross-reference [[tiers]] or [[h
