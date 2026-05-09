---
type: entity
title: OpenMetadata Data Quality Tests
created: 2026-04-05
updated: 2026-04-05
tags: [openmetadata, data-quality, testing, observability]
related: [openmetadata, openmetadata-data-quality, openmetadata-observability-alerting, data-quality-dimensions, great-expectations-for-data-contracts, dbt-expectations]
sources: ["OpenMetadata - The Complete Guide Every Data Engineer Needs to Read.md"]
---
# OpenMetadata Data Quality Tests

OpenMetadata has a built-in data quality testing engine with no-code setup, SQL-based custom tests, and test suites.

## Table-Level Tests

- Row count is between N and M
- Row count equals a specific number
- A column exists
- Column names match a set
- No duplicate rows
- Table is fresh (data inserted within X hours)
- Compare two tables for differences

## Column-Level Tests

- Values not null
- Values unique
- Values between min and max
- Values in a predefined set
- String matches a regex pattern
- No duplicate values
- Mean, median, standard deviation within expected range
- Null proportion below threshold

## No-Code Test Setup

1. Navigate to any table.
2. Click the **Data Observability** tab.
3. Click **Add Test**.
4. Select table-level or column-level.
5. Pick the test type, fill in parameters, done.

## SQL-Based Custom Tests

```sql
-- Custom test: no orders should have negative amount
SELECT COUNT(*) as failed_rows
FROM orders
WHERE amount < 0
```

If this returns anything > 0, the test fails.

## Test Suites

Group related tests into **Test Suites** to run all quality checks for a dataset together and get a consolidated pass/fail report.

## Quality Propagation Through Lineage

One of OpenMetadata's most powerful features: quality test results propagate through the lineage graph. If `raw_orders` fails a freshness test, every downstream asset (`fct_orders`, `customer_ltv`, the Looker dashboard) is marked as potentially affected.