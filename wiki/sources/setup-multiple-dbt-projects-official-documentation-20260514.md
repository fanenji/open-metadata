---
type: source
title: "Source: setup-multiple-dbt-projects-official-documentation-20260514.md"
created: 2026-05-15
updated: 2026-05-15
sources: ["setup-multiple-dbt-projects-official-documentation-20260514.md"]
tags: []
related: []
---

# Source: setup-multiple-dbt-projects-official-documentation-20260514.md

## Analysis: Setup Multiple dbt Projects

### Key Entities

| Name | Type | Role | In Wiki? |
|------|------|------|----------|
| dbt | Tool/Product | Central — the subject of the document | Yes ([[dbt]], [[dbt-integration]], [[dbt-artifacts]], etc.) |
| S3 | Storage Service | Central — one of three supported storage backends | No (as a standalone entity; mentioned in [[dbt-artifact-storage]]) |
| GCS | Storage Service | Peripheral — supported but not detailed | No |
| Azure | Storage Service | Peripheral — supported but not detailed | No |
| manifest.json | File/Artifact | Central — required dbt artifact | Yes ([[dbt-artifacts]]) |
| catalog.json | File/Artifact | Central — required dbt artifact | Yes ([[dbt-artifacts]]) |
| run_results.json | File/Artifact | Central — required dbt artifact; supports multiple files with suffixes | Yes ([[dbt-artifacts]]) |
| dbt Bucket Name | Configuration Field | Central — input parameter in OpenMetadata UI | No |
| dbt Object Prefix | Configuration Field | Central — input parameter in OpenMetadata UI | No |

### Key Concepts

| Name | Definition | Why It Matters | In Wiki? |
|------|------------|----------------|----------|
| Multi-project dbt ingestion | Ingesting metadata from multiple dbt projects (each with its own artifacts) in a single workflow | Extends the single-project pattern; enables enterprise-scale dbt adoption | No |
| Directory-based project isolation | Organizing each dbt project's artifacts into separate directories under a common prefix | Required for the workflow to correctly identify and process each project | No |
| Multiple run_results.json support | Splitting dbt test results across multiple `run_results_*.json` files in the same directory as `manifest.json` | Accommodates dbt workflows where tests are run separately | No |
| Prefix-based bucket scanning | The workflow scans a specified prefix path in the bucket, traversing subdirectories to find dbt artifacts | Defines the discovery mechanism; empty prefix = scan entire bucket | No |

### Main Arguments & Findings

- **Core claim**: OpenMetadata supports ingesting metadata from multiple dbt projects in a single workflow, provided artifacts are organized in separate directories under a common prefix.
- **Supported backends**: S3, GCS, and Azure only (not local storage or HTTP).
- **File naming convention**: Each project directory must contain `manifest.json`, `catalog.json`, and `run_results.json` (or `run_results_*.json` for split test results).
- **Configuration**: Two UI fields — `dbt Bucket Name` (required) and `dbt Object Prefix` (optional; empty = scan entire bucket).
- **Evidence**: A worked example with three projects (`dbt_project_one`, `dbt_project_two`, `dbt_project_three`) in a bucket named `dbt_bucket` under prefix `bucket_home/dbt_files/`.
- **Evidence strength**: Moderate — official documentation with a concrete example, but no troubleshooting or edge cases discussed.

### Connections to Existing Wiki

- **Directly extend
