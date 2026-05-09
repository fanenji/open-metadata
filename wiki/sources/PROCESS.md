---
type: source
title: Process Definition for dbt Workflows
created: 2026-01-15
updated: 2026-01-15
tags: [data-platform, dbt, workflow, orchestration]
related: [dbt-workflow-sql-only, dbt-workflow-sql-python-hybrid, dbt-orchestration-yaml-python, dbt-vscode-extensions-setup, altimate-dbt-power-user, dbt-project-scaffolding, dbt-dremio-adapter]
sources: ["PROCESS.md"]
---
# Process Definition for dbt Workflows

This document defines two core dbt workflow patterns for the data platform: a pure SQL workflow using dbt and Dremio, and a hybrid SQL+Python workflow where SQL models target Dremio and Python models target DuckDB. It also proposes a lightweight orchestration pattern using a YAML configuration file read by a Python script, and documents VS Code extension setup for dbt development.

## Key Workflows

- **Workflow DBT 1 (SQL):** Pure SQL transformation pipeline using dbt and Dremio for both ingestion and transformation. All data sources are configured on Dremio (relational databases, files on S3).
- **Workflow DBT 2 (SQL + Python):** Hybrid pipeline where SQL models target Dremio and Python models target DuckDB. Used when Python transformations are needed alongside SQL.

## Orchestration Proposal

A lightweight orchestration pattern is proposed: a YAML configuration file defines model dependencies and execution flow, and a Python script reads the YAML and runs the pipeline. This is an alternative to full orchestration tools like Airflow or Kestra.

## VS Code Extensions

The document documents the installation of two VS Code extensions for dbt development: Datamates and Power User for dbt. An Altimate account was created for the Power User features. A key configuration detail is that the `profiles.yaml` file must be placed in the project home directory for the extensions to detect it.

## Security Note

The document contains hardcoded credentials for the Altimate service, which should be replaced with environment variables or a secrets manager.