---
type: concept
title: dbt VS Code Extensions Setup
created: 2026-01-15
updated: 2026-01-15
tags: [dbt, vscode, extension, setup, datamates, altimate]
related: [datamates, altimate-dbt-power-user, dbt-project-scaffolding, dbt]
sources: ["PROCESS.md"]
---
# dbt VS Code Extensions Setup

This concept documents the setup of VS Code extensions for dbt development, as defined in the process document.

## Extensions Installed

- **Datamates:** A VS Code extension for dbt development.
- **Power User for dbt:** An extension provided by Altimate that enhances dbt development with lineage visualization, documentation generation, and query profiling.

## Configuration Issue

A key configuration detail is that VS Code extensions (both Datamates and Power User for dbt) fail to detect the `profiles.yaml` file unless it is placed in the project home directory. The workaround is to move `profiles.yaml` to the project root.

## Security Note

The original process document contains hardcoded credentials for the Altimate service. These should be replaced with environment variables or a secrets manager.