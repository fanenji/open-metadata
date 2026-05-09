---
type: concept
title: Artifact-Driven UI
created: 2026-04-04
updated: 2026-04-04
tags: [ui, metadata, dbt]
related: [dbt-workbench, dbt]
sources: ["Building a dbt-UI I Wish Existed.md"]
---
# Artifact-Driven UI

An **Artifact-Driven UI** is a user interface paradigm where the application's state and visibility are derived from existing metadata files produced by a primary tool (in this case, [[dbt]]), rather than requiring a live connection to a running database or a remote orchestration service.

## Characteristics
- **Low Overhead**: Does not require a running database or a remote service to function.
- **High Performance**: Allows for rapid exploration of data lineage and model logic by parsing static JSON files.

- **Decoupled**: The UI is decoupled from the execution engine, making it highly suitable for [[data-sovereignty-strategy]] and air-gapped environments.

## Example
**dbt-Workbench** implements this concept by parsing `manifest.json`, `run_results.json`, and `catalog.json` to reconstruct the dbt project structure and lineage.
