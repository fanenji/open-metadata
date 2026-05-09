---
type: concept
title: dbt Business Logic Testing
created: 2026-04-04
updated: 2026-04-04
tags: [dbt, testing, data-quality, best-practices]
related: [dbt-anti-patterns, dbt-testing-patterns, data-quality-dimensions, shift-left-data-quality, data-quality-resolution-workflow]
sources: ["Top 5 Advanced dbt Anti-Patterns That Nearly Killed Our Analytics Team.md"]
---
# dbt Business Logic Testing

A testing approach that goes beyond schema validation (unique, not_null, accepted_range) to validate the actual business meaning and reasonableness of data. This catches real data quality issues that schema-only testing misses.

## The "Testing Theatre" Anti-Pattern

Having 400+ schema tests that pass every day while data is completely wrong. Schema tests catch structural violations but miss:
- Incremental model drift (slowly degrading accuracy)
- Logic errors (e.g., 847% retention rate for single-order customers)
- Data freshness (models running on 5-day-old data)
- Cross-model consistency (mismatched counts between related models)

## Three Categories of Business Logic Tests

### 1. Reasonableness Tests
Validate that metrics fall within expected historical ranges:

```sql
-- Check average LTV is within expected range
WITH ltv_analysis AS (
  SELECT AVG(predicted_ltv) as avg_ltv
  FROM {{ ref('customer_ltv') }}
)
SELECT 'Average LTV outside expected range' as error_message
FROM ltv_analysis
WHERE avg_ltv NOT BETWEEN 150 AND 800
```

### 2. Data Freshness Tests
Alert when data is older than a threshold:

```sql
SELECT 'Customer LTV data is more than 2 days old' as error_message
FROM {{ ref('customer_ltv') }}
WHERE DATE_DIFF('day', MAX(last_updated), CURRENT_DATE) > 2
```

### 3. Cross-Model Consistency Tests
Detect drift between related models:

```sql
WITH customer_counts AS (
  SELECT 'ltv_table' as source, COUNT(DISTINCT customer_id) as count
  FROM {{ ref('customer_ltv') }}
  UNION ALL
  SELECT 'dim_table' as source, COUNT(DISTINCT customer_id) as count
  FROM {{ ref('dim_customers') }}
  WHERE is_active = true
)
SELECT 'Customer count mismatch' as error_message
FROM customer_counts
HAVING COUNT(DISTINCT count) > 1
```

## Results

- Actual data quality issues caught: 0/week → 3-4/week
- Business logic failures caught before affecting decisions
- Upstream pipeline delays identified immediately
- Executive trust restored: "Our tests caught a data issue" vs. "I found a data issue"