---
type: entity
title: Leo Godin
created: 2026-05-06
updated: 2026-05-07
tags: [person, data-engineer, dbt, data-engineering, author]
related: [elementary, dbt-macro-unit-testing, dbt-testing-patterns]
sources: ["Are You Using Elementary for DBT?-20260506.md", "Testing Dbt Macros.md"]
---
# Leo Godin

**Senior Data Engineer at Shopify**

Leo Godin is a Senior Data Engineer at Shopify and a practitioner in data engineering and observability. He contributes insights on the practical implementation of tools like [[elementary]] within production environments.

Godin is the author of the article *"Testing Dbt Macros"* published on the Data Engineer Things publication. In this article, he advocates for automated unit testing of dbt Jinja macros using a validation model pattern, arguing that dbt's built-in data quality tests are insufficient for ensuring pipeline reliability. His work provides a practical, reproducible methodology for macro testing that covers core functionality, path coverage, and boundary testing. The article includes a concrete example that caught a real bug — an ISO week start mismatch — demonstrating the value of the approach.

Godin maintains the `leogodin217/dbt_demos` GitHub repository containing code examples for his testing patterns.