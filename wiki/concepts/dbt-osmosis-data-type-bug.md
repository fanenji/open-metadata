---
type: concept
title: dbt-osmosis data_type Bug (v1.14)
created: 2026-02-17
updated: 2026-02-17
tags: [dbt, dbt-osmosis, bug]
related: [dbt-osmosis]
sources: ["DBT-OSMOSIS.md"]
---
# dbt-osmosis data_type Bug (v1.14)

A known bug in [[dbt-osmosis]] version 1.14 where column data types are not populated in the generated YAML schema files.

## Symptoms

- After running `dbt-osmosis yaml refactor`, the `data_type` field for columns is missing or empty.
- The YAML schema files are otherwise correctly generated, but lack type information.

## Cause

The bug was introduced in version 1.14 of dbt-osmosis. The exact root cause is in the `src/dbt_osmosis/core/osmosis.py` module.

## Fix

A fix is available in the internal GitLab repository at `https://10.11.9.20/data-platform/dbt/models/dbt-osmosis` (branch `fix/data_type`). The fix modifies the `osmosis.py` file to correctly populate the `data_type` field.

## Workaround

Until the fix is applied, users must manually add `data_type` fields to their YAML schema files, or apply the patch from the internal repository.

## Related

- [[dbt-osmosis]] — Central tool affected by this bug