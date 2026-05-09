---
type: concept
title: No-Code Data Quality
created: 2026-04-08
updated: 2026-04-08
tags: [data-quality, no-code, democratization, openmetadata]
related: [metadata-first-data-quality, openmetadata-data-quality, data-quality-dimensions]
sources: ["Simple, Easy, and Efficient Data Quality with OpenMetadata.md"]
---
# No-Code Data Quality

No-code data quality refers to the practice of writing data quality assertions (tests) through a graphical user interface (UI) rather than by writing code in Python, YAML, or SQL. This approach aims to democratize data quality by making it accessible to non-technical users such as business analysts, data scientists, and domain experts.

## Key Characteristics

1. **UI-Based Test Creation**: Users configure tests (e.g., "column X should not have null values") through dropdowns, forms, and point-and-click interfaces.

2. **Immediate Feedback**: Rich data profiling visualizations help users identify issues (e.g., unexpected nulls, negative values) and write targeted tests without writing code.

3. **Shared Responsibility**: By enabling business users to contribute tests, data quality becomes a shared organizational responsibility rather than the sole domain of data engineers.

4. **Centralized Repository**: All tests and results are stored in a central metadata repository, preventing siloed duplicate tests and reducing unnecessary compute costs.

## Example Workflow

1. A data scientist notices unexpected null values in a column during analysis.
2. They open the data quality UI, select the table and column, and configure a "column values not null" test with a few clicks.
3. The test runs automatically on the next scheduled validation.
4. If the test fails, the data scientist is alerted and can participate in the resolution workflow.

## Relationship to Other Concepts

- [[metadata-first-data-quality]]: No-code DQ is enabled by the metadata-first approach, which provides the underlying infrastructure for storing tests, results, and context.
- [[openmetadata-data-quality]]: OpenMetadata's native DQ module is the primary implementation of no-code DQ documented in this wiki.

## Open Questions

- Is the no-code approach actually adopted by business users in practice, or does it remain a technical tool with a friendlier UI?
- How does no-code DQ handle complex, multi-column, or cross-table validation logic?
- What is the learning curve for business users to adopt no-code DQ tools?