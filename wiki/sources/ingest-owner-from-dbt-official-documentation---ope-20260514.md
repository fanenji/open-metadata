---
type: source
title: "Source: ingest-owner-from-dbt-official-documentation---ope-20260514.md"
created: 2026-05-15
updated: 2026-05-15
sources: ["ingest-owner-from-dbt-official-documentation---ope-20260514.md"]
tags: []
related: []
---

# Source: ingest-owner-from-dbt-official-documentation---ope-20260514.md

## Key Entities

- **dbt (Data Build Tool)** — Central entity. Data transformation tool whose JSON artifacts (manifest.json, catalog.json) are the source of owner metadata.
- **OpenMetadata** — Central entity. The metadata platform that ingests owner information from dbt artifacts.
- **manifest.json** — Core artifact. Contains owner information under `node_name -> metadata -> owner`.
- **catalog.json** — Core artifact. Contains owner information under `node_name -> metadata -> owner`.
- **schema.yml** — Peripheral. dbt configuration file where multiple owners can be defined under `meta.openmetadata.owner`.
- **User** — Central entity type. One of the two possible owner types in OpenMetadata.
- **Team** — Central entity type. One of the two possible owner types in OpenMetadata.
- **dbtUpdateOwners** — Peripheral configuration parameter. Controls overwrite behavior for existing owners.

All entities likely already exist in the wiki (dbt, dbt-integration, dbt-artifacts, data-asset-ownership, teams-and-users).

## Key Concepts

- **Owner Ingestion from dbt** — Process of extracting owner information from dbt manifest.json or catalog.json and linking it to OpenMetadata entities. Matters because it establishes dbt as a single source of truth for ownership.
- **Multiple Owners** — Capability to define multiple users or teams as owners for a single dbt model via schema.yml. Extends the standard single-owner model.
- **Owner Resolution Order** — OpenMetadata first searches for a user matching the owner name; if not found, it searches for a team. Determines how ambiguous owner names are resolved.
- **Update Owners Toggle** — Configuration option controlling whether dbt owners overwrite existing owners or only apply to unowned assets. Critical for establishing dbt as the authoritative source.
- **Single Source of Truth** — Design principle: ownership should be maintained in one place (either OpenMetadata or dbt), not both. The Update Owners toggle enforces this.

All concepts likely already exist in the wiki (dbt-integration, data-asset-ownership, owner-propagation).

## Main Arguments & Findings

- **Core Claim**: OpenMetadata can ingest owner information from dbt manifest.json or catalog.json files, linking users or teams to tables/models.
- **Evidence**: Sample JSON nodes showing owner fields (`"owner": "openmetadata_team"` and `"owner": "openmetadata"`). Step-by-step UI procedures for creating users and teams.
- **Strength**: Moderate. Official documentation with concrete examples, but no empirical validation or edge-case analysis.

## Connections to Existing Wiki

- **Strengthens**: [[dbt-integration]] — Adds specific owner ingestion workflow to the existing dbt integration documentation.
- **Extends**: [[data-asset-ownership]] — Introduces dbt as an external source of ownership, with overwrite control.
- **Extends**: [[owner-propagation]] — The Update Owners toggle is a new mechanism for controlling ownership assignment.
- **Related**: [[dbt-artifacts
