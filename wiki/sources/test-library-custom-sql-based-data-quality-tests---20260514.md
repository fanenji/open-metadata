---
type: source
title: "Test Library Custom Sql Based Data Quality Tests   20260514"
created: 2026-05-30
updated: 2026-05-30
tags: []
related: []
authors: []
year: 2026
url: ""
venue: ""
---

type: source
title: "Test Library | Custom SQL-Based Data Quality Tests - OpenMetadata Documentation"
created: 2026-05-14
updated: 2026-05-14
tags: [data-quality, test-library, sql, openmetadata]
related: [test-library, custom-sql-test-definitions, test-platforms, data-quality]
sources: ["test-library-custom-sql-based-data-quality-tests---20260514.md"]
---
# Test Library | Custom SQL-Based Data Quality Tests

This source is the official OpenMetadata v1.12.x documentation for the Test Library feature, which allows administrators to create reusable, parameterized SQL-based data quality test definitions. It covers the full workflow: accessing the Test Library, creating custom test definitions with SQL expressions, managing definitions (edit, enable/disable, delete), and using them to create test cases. Six worked examples demonstrate common patterns: column value threshold, range check, null check, row count, referential integrity, and date freshness. The document emphasizes the critical distinction between test platforms — only "OpenMetadata" triggers native execution; other platforms (dbt, Soda, GreatExpectations) are for external result tracking only. The fail-on-rows semantics (empty result = pass) is the core logic pattern for all custom tests.