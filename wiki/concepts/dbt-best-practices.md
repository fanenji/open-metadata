---
type: concept
title: dbt Best Practices
created: 2026-04-07
updated: 2026-05-07
tags: [dbt, engineering-excellence, analytics-engineering, data-engineering, optimization]
related: [dbt, slim-ci, data-quality-dimensions, software-defined-assets, dbt-labs, dbt-modeling-layers, dbt-slim-ci-strategy]
sources: ["Best Practices for Workstreams A Guide to Effective dbt Use.md", "Complex geospatial analytics with dbt - Summary.md", "best-abilities-for-workflows-a-guide-to-effective-dbt-use.md"]
---
# dbt Best Practices

A collection of patterns and workflows designed to ensure the maintainability, scalability, and reliability of dbt projects, covering industry-standard practices for managing large-scale datasets and development workflows.

## Development Workflow & Environment

### Version Control
- **Git Flow**: Utilize branches and Pull Requests (PRs) for all changes to ensure peer review and code quality.

### Environment Isolation
- **Environment Separation**: Maintain separate `dev` and `prod` targets in `profiles. .yml` to ensure developers work in isolated schemas. This prevents development testing from impacting production datasets or causing accidental production writes.
- **Zero-Copy Cloning**: (Snowflake-specific) Use metadata-only clones to instantly reset development schemas to a production state.

### CI/CD
- **Slim CI**: Implement the `state:modified` strategy to run only the models that have changed, significantly reducing compute costs and CI/CD duration.

### Development Optimization
- **Dev Target Filtering & Optimization**: Use Jinja to inject `LIMIT` clauses or filters in `dev` environments (e.g., `{% if target.name == 'dev' %} LIMIT 1000 {% endif %}`) to enable much faster iteration.
    - **⚠️ Caution**: While this speeds up development, it can mask bugs related to data volume or specific edge cases that only appear in larger datasets.

## Modeling Standards & Architecture

### Core Principles
- **The `ref()` Function**: Always use `{{ ref('model_name') }}` instead of hardcoded relations to maintain the integrity of the Directed Acyclic Graph (DAG).
- **Source Abstraction**: Use `{{ source('source_name', 'table_name') }}` to reference raw data. This provides a single point of truth for upstream schema changes.
- **Modularization**: Avoid "Spaghetti SQL" by breaking down large, complex models with multiple CTEs into smaller, independent intermediate models.
- **Layered Architecture**:
    - **Staging Layer**: Source-centric models focused on renaming, recasting, and cleaning.
    - **Intermediate Layer**: Business logic and complex transformations.
    - **Mart/Analytics Layer**: Business-centric models optimized for end-user consumption.
- **Rename and Recast Pattern**: Use the initial staging layer to standardize field names (e.g., `usr_name` $\rightarrow$ `user_name`) and data types (e.g., converting all timestamps to UTC).

### Large-Scale Data Patterns
- **Incremental Materialization**: The default choice for large datasets. It processes only new data since the last run using a high-watermark column (e.g., `loaded_at`).
- **Insert by Period**: An advanced pattern (via `dbt_utils`) for time-partitioned datasets. It chunks data into periods to avoid resource exhaustion during massive backfills.
- **Manual Clustering Keys**: For very large tables with predictable query patterns, defining clustering keys (e.g., `cluster_by=['date', 'region']`) can significantly improve partition pruning and reduce scan costs.

## Data Quality & Governance
- **Automated Testing**: Every model should include tests for `unique` and `not_null` on primary keys.
- **Source Freshness**: Implement freshness checks to monitor data latency and prevent downstream models from running on stale data.
- **Automated Permissions**: Use `post-hooks` in `dbt_project.yml` to automate `GRANT SELECT` statements, ensuring that newly created tables are immediately accessible to authorized roles.

## Operational Pro-Tips
- **Model Selection**: Use model selection syntax (e.g., `dbt run -m +model_name`) to run only the specific model and its downstream dependencies during local development.
- **Whitespace Management**: Use Jinja whitespace control (`{%-` and `-%}`) to keep compiled SQL clean and readable.