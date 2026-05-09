---
type: concept
title: Slim CI
created: 2026-04-22
updated: 2026-04-22
tags: [ci-cd, data-engineering, efficiency]
related: [dbt, data-observability]
sources: ["5-dbt-slim-ci-tactics-for-large-repos.md"]
---
# Slim CI

**Slim CI** is a Continuous Integration strategy designed for large-scale data transformation projects (specifically dbt). Instead of running the entire repository on every Pull Request—which becomes unsustainable as the project grows—Slim CI focuses on running only the "blast radius" of a change.

### Core Principles
- **Impact Analysis**: Identifying changed models and their immediate upstream/downlag dependencies.
- **Efficiency**: Reducing compute costs and developer wait times by avoiding unnecessary re-materialization.
- **Tiered Testing**: Separating fast, schema-focused tests (run during PR) from heavy, end-to-end tests (run nightly).

### Key Techniques
- **State-Aware Selection**: Using metadata to identify modified nodes.
- **Smart Deferral**: Referencing production data to complete the DAG without rebuilding it.