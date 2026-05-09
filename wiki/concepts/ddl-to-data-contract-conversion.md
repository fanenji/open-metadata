---
type: concept
title: DDL-to-Data-Contract Conversion
created: 2026-04-04
updated: 2026-04-04
tags: [data-contracts, ddl, automation, conversion]
related: [bitol-open-data-contract-standard, jean-georges-perrin, data-contract-platform, YAML-data-contract-format, data-contract-versioning-strategy]
sources: ["Experimenting with Data Contracts.md"]
---
# DDL-to-Data-Contract Conversion

A pattern for automatically generating data contracts from SQL Data Definition Language (DDL) statements via REST API. This approach allows teams to bootstrap data contracts from existing database schemas without manual YAML writing.

## How It Works

1. **Input**: SQL DDL (e.g., `CREATE TABLE` statements) from a database schema.
2. **API Call**: The DDL is sent to a service (e.g., Bitol) with parameters for version, name, domain, and tenant.
3. **Output**: A validated data contract in ODCS YAML format, with schema, metadata, and team information.
4. **Enrichment**: The generated contract can be manually edited to add descriptions, business names, SLAs, and data quality rules.

## Advantages

- **Speed**: Rapidly creates contract skeletons from existing schemas.
- **Consistency**: Ensures contracts match the physical database structure.
- **Low Barrier**: No need to learn YAML contract syntax initially.

## Limitations

- **Not a Final Contract**: The author notes that "DDL is not a data contract" — the generated contract is a starting point that requires enrichment with business context, SLAs, and quality rules.
- **Physical Focus**: DDL captures physical schema, not business semantics or governance policies.

## Related

- [[bitol-open-data-contract-standard]] — The output format for the conversion.
- [[jean-georges-perrin]] — Creator of the Bitol service demonstrating this pattern.
- [[data-contract-platform]] — Systems that support this conversion pattern.
- [[YAML-data-contract-format]] — The target format for generated contracts.