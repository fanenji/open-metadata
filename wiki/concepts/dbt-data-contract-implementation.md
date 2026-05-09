---
type: concept
title: dbt Data Contract Implementation
created: 2026-05-07
updated: 2026-05-07
tags: [dbt, data-contracts, data-quality, data-governance]
related: [dbt-preflight-validation, dbt-contract-artifact-integration, data-contract-platform, YAML-data-contract-format, data-contract-versioning-strategy, CI-CD-for-data-pipelines, dbt-testing-patterns]
sources: ["dbt and Data Contracts Enabling Reliable, API-Driven Analytics.md"]
---
# dbt Data Contract Implementation

A dbt data contract is a formal YAML specification enforced at build time that defines exact schema, data types, and constraints (NOT NULL, UNIQUE, CHECK) for a model. It is distinct from dbt tests: contracts enforce schema proactively before the model is materialized, while tests validate data values reactively after creation.

## Key Elements

- **YAML Definition:** Contracts are defined under the `config:` block in a model's YAML file with `contract: enforced: true` and a list of columns with `data_type` and optional `constraints`.
- **Preflight Validation:** dbt checks contract compliance before materializing the model; halts the build with a side-by-side diff on mismatch.
- **Supported Materializations:** Works with `table`, `view`, and `incremental` models (with certain `on_schema_change` configs).
- **Data Type Aliasing:** dbt auto-converts generic types (`string`, `int`) to warehouse-specific types; can be disabled with `alias_types: false`.
- **Model Versioning:** dbt v1.5+ enables safe additive changes and backward compatibility; consumers can pin to versions.

## Best Practices

- Combine contracts with granular data quality tests for comprehensive guarantees (schema + values).
- Enable contract checking in CI/CD using `dbt build --select state:modified`.
- Start with strategic data products and expand incrementally.
- Version every breaking change and communicate deprecation cycles.
- Surface contract metadata via dbt artifacts for API-driven consumption.

## Comparison with Other Approaches

dbt-native contracts are tightly integrated with the dbt workflow but may be less comprehensive than dedicated contract platforms like [[datacontract-com]], which offer broader functionality for heterogeneous environments.