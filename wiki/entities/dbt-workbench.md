---
type: entity
title: dbt-Workbench
created: 2026-04-04
updated: 2026-04-04
tags: [dbt, ui, open-source, observability]
related: [dbt, dbt-best-practices, data-sosovereignty-strategy, data-lakehouse-on-premise-architecture]
sources: ["Building a dbt-UI I Wish Existed.md"]
---
# dbt-Workbench

**dbt-Workbench** is a self-hosted, open-source user interface for dbt projects. It is designed as an alternative to dbt Cloud for engineers working in environments where cloud connectivity is restricted or where local/on-premise control is a priority.

## Key Features
- **Artifact-Driven**: Uses standard dbt artifacts (`manifest.json`, `run_results.json`, `catalog.json`) to power the UI, requiring no extra metadata or remote services.
- **Lineage Visualization**: Provides clear visibility into model dependencies.
- **SQL Workspace**: Allows users to view compiled SQL side-by-side with the original model code.
- **Multi-Project Support**: Enables managing and switching between different dbt projects within a single interface with logical isolation.
- **Plugin-Friendly**: Features an architecture that allows for extensions and custom plugins.

## Use Cases
- **Air-Gapped/Restricted Environments**: Ideal for high-security sectors (government, finance) where internet access is limited.
- **On-Premise Deployments**: Serves as a lightweight exploration layer for the [[data-lakehouse-on-premise-architecture]].
- **Local Development**: Reduces context-switching friction for engineers working on local setups.

## Technical Implementation
The tool can be run locally using **Docker**, aligning with the broader [[infrastructure-architecture]] of the platform.
