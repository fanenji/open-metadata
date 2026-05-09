---
type: concept
title: YAML Data Contract Format
created: 2026-04-04
updated: 2026-04-04
tags: [data-contract, YAML, schema, data-quality]
related: [data-contract, data-contract-platform, data-contract-versioning-strategy, CI-CD-for-data-pipelines]
sources: ["Data Contracts Implementation Guide.md"]
---
# YAML Data Contract Format

The YAML data contract format is a machine-readable way to define a [[data-contract]]. It encapsulates the schema, metadata, and validation rules for a [[data-product-definition]].

## Example Structure

```yaml
table_name: customer_bookings
version: 1.1
owner: jack_dawson
schema:
  - column_name: tx_date
    type: timestamp
    constraints:
      not_null: true
      no_future_dates: true
  - column_name: customer_email
    type: string
    constraints:
      not_null: true
      check_pii: true
  - column_name: sales_amt
    type: decimal
    constraints:
      not_negative: true
  - column_name: revenue_amt
    type: decimal
    constraints:
      not_negative: true
  - column_name: booking_type
    type: string
    constraints:
      enum: [air, hotel, train]
```

## Key Elements

- **table_name**: The name of the table or dataset
- **version**: Semantic version of the contract
- **owner**: The data engineer or team responsible
- **schema**: List of columns with their types and constraints
- **constraints**: Rules such as `not_null`, `no_future_dates`, `check_pii`, `not_negative`, `enum`

## Enforcement

The YAML file is enforced through [[CI-CD-for-data-pipelines]] using Git-based workflows. The CI pipeline performs YAML linting, schema validation (using tools like `yamale` or `jsonschema`), and unit tests.