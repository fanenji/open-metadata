---
type: concept
title: Conditional Logic for Changing Business Rules
created: 2026-04-29
updated: 2026-04-29
tags: [data-engineering, business-rules, versioning, reproducibility]
related: [functional-data-engineering, parameter-tables-for-business-rules, pure-task]
sources: ["Functional Data Engineering — a modern paradigm for batch data processing.md"]
---
# Conditional Logic for Changing Business Rules

Conditional logic for changing business rules is a practice in [[functional-data-engineering]] that captures time-varying business logic inside task logic with effective dates. This ensures that source control describes how to build the full state of the data warehouse across all time periods.

## Principle

Business rules change over time, sometimes retroactively and sometimes not. When a change is non-retroactive (e.g., a new tax calculation for 2018 that shouldn't apply to 2017), the task logic must capture this distinction. The solution is to apply conditional logic within the task with a certain effective date, so that depending on the slice of data being computed, the appropriate rule is applied.

## Example

If a new tax rule is introduced for 2018, the task should contain conditional logic that checks the effective date of the data being processed. When backfilling 2017 data, the old rule is applied; when processing 2018 data, the new rule is applied. This prevents accidentally applying the 2018 rule to 2017 data during unrelated backfills.

## Relationship to Parameter Tables

In many cases, business rules are best expressed as data rather than code. The companion concept [[parameter-tables-for-business-rules]] stores changing rules in database tables with effective dates, which the task logic joins to and applies as needed.