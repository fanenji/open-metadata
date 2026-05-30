---
type: source
title: "Source: auto-ingest-dbt-core---openmetadata-documentation-20260514.md"
created: 2026-05-15
updated: 2026-05-15
sources: ["auto-ingest-dbt-core---openmetadata-documentation-20260514.md"]
tags: []
related: []
---

# Source: auto-ingest-dbt-core---openmetadata-documentation-20260514.md

## Analysis: Auto Ingest dbt-core - OpenMetadata Documentation

### Key Entities

- **dbt-core**: Central entity. The data transformation tool whose artifacts are ingested. Already exists in wiki as [[dbt]].
- **OpenMetadata**: Central entity. The target platform receiving the ingested metadata. Already exists as [[openmetadata]].
- **metadata ingest-dbt CLI command**: Central tool. A new CLI command (`metadata ingest-dbt`) that reads configuration from `dbt_project.yml`. Does NOT exist in wiki.
- **dbt_project.yml**: Central configuration file. The source of truth for ingestion configuration, eliminating separate YAML files. Does NOT exist in wiki.
- **manifest.json**: Required artifact. Model definitions, relationships, metadata. Already exists as [[dbt-artifacts]].
- **catalog.json**: Optional artifact. Table/column statistics. Already exists as [[dbt-artifacts]].
- **run_results.json**: Optional artifact. Test results. Already exists as [[dbt-artifacts]].
- **JWT token**: Authentication mechanism. Already exists as [[personal-access-token]].
- **OpenMetadata ingestion package**: Peripheral. Python package (`openmetadata-ingestion[dbt]`). Does NOT exist in wiki.
- **CI/CD (GitHub Actions)**: Peripheral. Integration pattern for automation. Does NOT exist in wiki.

### Key Concepts

- **Auto Ingest dbt-core**: A simplified ingestion workflow where configuration is embedded directly in `dbt_project.yml` via `vars` section, eliminating the need for separate OpenMetadata YAML configuration files. This is a new, streamlined approach distinct from the existing [[dbt-integration]] workflow.
- **Environment Variable Substitution**: Three supported patterns (shell-style `${VAR}`, dbt-style `{{ env_var("VAR") }}`, dbt-style with default `{{ env_var("VAR", "default") }}`) for secure configuration. Does NOT exist in wiki.
- **Artifact Discovery**: Automatic detection of artifacts from the `target/` directory. Extends existing [[dbt-artifacts]] concept.
- **Filter Patterns**: Regex-based inclusion/exclusion for databases, schemas, and tables. Already exists as [[filter-patterns]].
- **CI/CD Integration**: Pattern for running ingestion as part of automated build pipelines. Does NOT exist in wiki.

### Main Arguments & Findings

- **Core Claim**: The `metadata ingest-dbt` command provides a simplified, configuration-free ingestion workflow by reading settings directly from `dbt_project.yml`.
- **Evidence**: The documentation provides a complete Quick Start (3 steps: configure `dbt_project.yml`, generate artifacts, run command), a complete example, and a CI/CD integration example.
- **Evidence Strength**: Strong. Official documentation with concrete, executable examples. The approach eliminates a separate configuration file, reducing friction.
- **Key Finding**: This is a significant simplification over the existing [[dbt-integration]] workflow which requires a separate YAML configuration file and the `metadata ingest` command.

### Connections to Existing Wik
