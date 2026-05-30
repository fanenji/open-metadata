---
type: source
title: "Source: data-contracts-openmetadata-data-contracts---openm-20260514.md"
created: 2026-05-15
updated: 2026-05-15
sources: ["data-contracts-openmetadata-data-contracts---openm-20260514.md"]
tags: []
related: []
---

# Source: data-contracts-openmetadata-data-contracts---openm-20260514.md

## Analysis of: Data Contracts | OpenMetadata Data Contracts - OpenMetadata Documentation

### Key Entities

- **OpenMetadata** (Platform) — Central entity; the active metadata repository where data contracts are created and managed.
- **Data Contract** (Entity/Feature) — Central concept; a formal agreement between data producers and consumers specifying schema, semantics, data quality, and SLAs for tables.
- **Table** (Data Asset) — The only asset type currently supported for data contracts.
- **DataContract entity** (JSON Schema Entity) — The underlying schema definition for the Data Contract; likely already exists in the wiki as part of the schema-first approach.

### Key Concepts

- **Data Contract** — A formal, enforceable agreement specifying expected schema structure, semantic requirements (description, owner), data quality tests, and execution history for a data asset. Matters because it bridges the gap between data producers and consumers in a data mesh architecture.
- **Data Mesh Architecture** — Organizational pattern where data domains are owned by cross-functional teams; data contracts are a key enabler for this model.
- **Schema Validation** — Automated checks ensuring the actual schema of a table matches the contract's expected schema.
- **Semantic Validation** — Automated checks ensuring metadata requirements (description, owner) are met.
- **Data Quality Validation** — Automated checks using assigned data quality tests as part of the contract.
- **Execution History** — Tracking of contract validation results over time for audit and compliance.

### Main Arguments & Findings

- **Core Claim:** Data contracts in OpenMetadata enable automated schema, semantic, and data quality validations that enforce data quality and SLAs across departments and domains.
- **Evidence:** The documentation describes the feature's purpose and capabilities but provides no empirical evidence or case studies. The evidence is purely descriptive/functional.
- **Strength:** Low — this is a feature overview, not a research paper. No quantitative data, no user studies, no comparison with alternatives.

### Connections to Existing Wiki

- **Directly related to:** [[data-quality]], [[data-profiling]], [[data-lineage]], [[schema-first-approach]], [[glossary-terms]], [[data-asset-ownership]], [[classification-tags]]
- **Extends:** The existing data quality and governance framework by adding a formal contract layer that ties together schema expectations, semantic requirements, and quality tests.
- **New concept:** Data Contracts as a distinct entity type with its own JSON Schema definition and UI workflow.

### Contradictions & Tensions

- **No contradictions** with existing wiki content.
- **Internal tension:** The documentation mentions "automated schema, semantic, and data quality validations" but does not explain how conflicts between contract requirements and actual data are resolved (e.g., automatic blocking vs. alerting).
- **Caveat:** Contracts are currentl
