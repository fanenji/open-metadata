---
type: source
title: "Are You Using Elementary for DBT?"
created: 2026-05-06
updated: 2026-05-06
tags: [dbt, observability, data-engineering]
related: ["elementary", "dbt-lifecycle", "data-observability", "metadata-mart", "anomaly-detection", "dbt-best-practices"]
authors: [Leo Godin]
year: 2023
url: "https://leo-godin.medium.com/are-you-using-elementary-for-dbt-f9a56ecbef42"
venue: "Medium"
sources: ["Are You Using Elementary for DBT?.md", "Are You Using Elementary for DBT?-20260506.md"]
---
# Are You Using Elementary for DBT?

An article by Leo Godin (Senior Data Engineer at Shopify) discussing the utility of the [[elementary]] package and CLI for dbt observability.

The author highlights how [[elementary]] provides "infrastructure-in-a-box" for dbt users, including a [[metadata-mart]] that stores dbt artifacts such as models, tests, runs, and exposures. This allows for advanced [[anomaly-detection]] (e.g., monitoring model execution time variance) using standard SQL.

Key features discussed:
- **Metadata Mart**: Automated maintenance of dimension tables for dbt artifacts.
- **Dashboarding**: Simple, intuitive dashboards for monitoring test results and pipeline health.
- **Slack Integration**: Context-rich, test-level alerting that includes failing rows and links to dashboards.
- **Reporting**: The ability to generate shareable reports via the `edr report` command.

The author notes that while the dashboard might initially seem rudimentary, its operational value for both engineers and non-technical stakeholders (like VPs) is immense.