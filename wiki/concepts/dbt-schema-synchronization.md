---
type: concept
title: dbt Schema Synchronization
created: 2026-04-04
updated: 2026-04-04
tags: [dbt, schema-management, automation, yaml]
related: [dbt-osmosis, dbt-pre-commit-patterns, dbt-data-contract-implementation, dbt-project-scaffolding]
sources: ["dbt-osmosis Automation for Schema and Documentation Management in dbt.md"]
---
# dbt Schema Synchronization

Schema synchronization is the automated process of keeping dbt YAML schema files in sync with the actual warehouse schema. It addresses the common problem of documentation drift where YAML files become outdated as models evolve.

## How It Works

Tools like [[dbt-osmosis]] inspect actual models and sources in the warehouse, then:

1. Create or update YAML column entries for new columns.
2. Remove column entries that no longer exist in the model.
3. Reorganize files based on team-defined rules (alphabetical ordering, etc.).

## Example

When a developer adds `device_type` to a SQL model, running `dbt-osmosis yaml refactor` automatically updates the corresponding YAML file with the new column entry. If the column is later removed, the YAML is cleaned up automatically.

## Benefits

- Eliminates manual YAML maintenance for large projects.
- Prevents documentation debt from accumulating.
- Ensures schema files remain trustworthy references.
- Reduces PR clutter from YAML diffs.

## Relationship to Contract Enforcement

Schema synchronization complements but can potentially conflict with [[dbt-data-contract-implementation]]. While contracts validate YAML against model definitions, synchronization tools modify YAMLs automatically. Teams using both approaches should establish clear workflows to avoid conflicting modifications.
