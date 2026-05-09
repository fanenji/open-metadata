---
type: concept
title: Parameter Tables for Business Rules
created: 2026-04-29
updated: 2026-04-29
tags: [data-engineering, business-rules, parameterization, data-driven]
related: [functional-data-engineering, conditional-logic-for-changing-business-rules, pure-task]
sources: ["Functional Data Engineering — a modern paradigm for batch data processing.md"]
---
# Parameter Tables for Business Rules

Parameter tables for business rules is a practice in [[functional-data-engineering]] that stores changing business rules as data in database tables with effective dates, rather than hard-coding them in conditional blocks of code.

## Principle

When business rules change over time, it is often better to express those changes as data rather than code. A "parameter table" stores the rule values and their effective periods. Task logic then joins to this table and applies the appropriate parameters for the facts being processed.

## Example

Instead of hard-coding tax rates in conditional blocks:
```sql
CASE WHEN event_date < '2018-01-01' THEN rate * 0.08
     WHEN event_date < '2019-01-01' THEN rate * 0.085
     ELSE rate * 0.09
END
```

Use a parameter table:
```sql
SELECT f.*, t.rate
FROM facts f
JOIN tax_rates t
  ON f.event_date BETWEEN t.effective_date AND t.expiry_date
```

## Benefits

- **Data-driven**: Rule changes become data operations, not code changes.
- **Auditability**: The history of rule changes is captured in the data.
- **Flexibility**: New rules can be added without modifying task code.
- **Reproducibility**: The same task logic applied to different time periods uses the correct rules automatically.