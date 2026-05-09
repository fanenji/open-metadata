---
type: concept
title: dbt Metadata and Discovery
created: 2026-04-04
updated: 2026-04-04
tags: [dbt, data-governance, documentation]
related: [data-governance, dbt]
sources: ["10 Game-Changing dbt Tips I Wish I Knew Before My First Production Model.md"]
---
# dbt Metadata and Discovery

Effective data discovery relies on embedding metadata directly within the dbt project via YAML configuration files.

## Key Components

- **Descriptions**: Providing clear, human-readable explanations for models and columns.
- **Ownership**: Using the `meta` field to assign owners (e.g., `meta: {owner: email@company.com}`) to ensure accountability.
- **Tags**: Using tags to organize models by business domain (e.g., `finance`, `marketing`) or deployment priority.
- **dbt Docs**: Generating and hosting `dbt docs` allows stakeholders to explore the data lineage, schema, and test results, promoting transparency and self-service analytics.

By treating documentation as code, the data platform becomes more discoverable and easier to govern.

---END EXAMINE ---

---FILE: wiki/concepts/dbt-testing-best-practices.md---
---
type: concept
title: dbt Testing Best Practices
created: 2026-04-04
updated: 2026-04-04
tags: [dbt, data-quality, testing]
related: [data-observability, dbt]
sources: ["10 Game-Changing dbt Tips I Wish I Knew Before My First Production Model.md"]
---
# dbt Testing Best Practices

Automated testing is a cornerstone of [[data-observability]]. Implementing tests within dbt helps catch data bugs before they reach downstream production models.

## Types of Tests

### 1. Built-in Tests
dbt provides four standard tests that should be applied to critical columns:
- `unique`: Ensures no duplicate values exist in a column.
- `not_null`: Ensures no null values are present.

- `accepted_values`: Validates that a column only contains a predefined list of values.
- `relationships`: Validates referential integrity between models.

### 2. Custom Tests
For more complex business logic, custom singular or generic tests can be written:
- **Range Checks**: Ensuring values (like prices or quantities) are not negative.
- **Foreign Key Mismatches**: Verifying that keys in a child table exist in a parent table.
- **Business Logic Validation**: Custom SQL queries that fail if specific conditions are met.
