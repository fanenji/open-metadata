---
type: entity
title: Bitol Open Data Contract Standard (ODCS)
created: 2026-04-04
updated: 2026-04-04
tags: [data-contracts, standard, specification]
related: [jean-georges-perrin, ddl-to-data-contract-conversion, YAML-data-contract-format, data-contract-platform, data-contract-versioning-strategy]
sources: ["Experimenting with Data Contracts.md"]
---
# Bitol Open Data Contract Standard (ODCS)

An open standard specification for data contract YAML format, maintained by Bitol and used by the Bitol REST-based service. The specification defines the structure, schema, metadata, SLAs, and data quality rules for data contracts.

## Key Features

- **Version**: v3.0.2 (as referenced in the tutorial).
- **Format**: YAML-based with defined schema for tables, columns, types, and constraints.
- **Schema**: Supports logical and physical types, primary keys, required fields, and foreign key relationships.
- **Metadata**: Includes domain, tenant, team, description, purpose, and limitations.
- **SLAs**: Supports service-level agreement properties such as retention policies.
- **Data Quality**: Allows embedding quality rules (e.g., SQL-based checks) at the field level.
- **Semantic Versioning**: Enforces semver for contract versions.

## Usage

The ODCS specification is used by the Bitol service to validate and store data contracts. Contracts can be generated from DDL, enriched manually, and versioned via REST API.

## Related

- [[jean-georges-perrin]] — Author of the standard.
- [[ddl-to-data-contract-conversion]] — Pattern that produces ODCS-compliant contracts.
- [[YAML-data-contract-format]] — General YAML format for data contracts.
- [[data-contract-platform]] — Systems that implement the standard.