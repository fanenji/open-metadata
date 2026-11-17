---
type: entity
title: Great Expectations
created: 2026-07-15
updated: 2026-07-15
tags: [data-quality, testing, open-source, python]
related: [data-quality, data-quality-as-code]
sources: ["https://blog.open-metadata.org/how-to-get-started-with-data-quality-as-code-in-your-pipelines-122af5b93d7f"]
---

# Great Expectations

An open-source Python library for data validation and testing. Great Expectations provides a large library of built-in **Expectations** (test types) for validating data in pipelines, commonly used for data quality checks in ETL/ELT workflows.

## Comparison with OpenMetadata

OpenMetadata's [[data-quality-as-code]] is positioned as a more complete solution compared to Great Expectations:

- **More individual test types** in Great Expectations, but without platform integration
- **No incident management** in Great Expectations — tests run in isolation
- **No unified metadata integration** — Great Expectations lacks automatic linking to data lineage, ownership, and glossary
- **Primarily code-driven** — lacks the dual UI+SDK approach of OpenMetadata

## Relevance to OpenMetadata

Great Expectations serves as the primary competitive reference point for OpenMetadata's Data Quality as Code feature, with OpenMetadata differentiating through platform integration rather than test-type quantity.