type: concept
title: Software-Defined Assets
created: 2024-03-13
updated: 2024-03-13
tags: [orchestration, dagster, data-engineering]
related: [dagster, dbt]
sources: ["Airflow vs Dagster vs Kestra.md"]
---
# Software-Defined Assets

**Software-Defined Assets (SDA)** is an orchestration paradigm popularized by **Dagster**. 

Instead of focusing on a graph of tasks (the "how"), the focus is placed on the data objects (the "what") that are produced or consumed by the pipeline. An **asset** is any object in persistent storage, such as a database table, a file, or a machine learning model.

This approach allows for:
- **Data Freshness Tracking**: Monitoring when an asset was last updated.
- **Upstream Dependency Management**: Automatically triggering updates to downstream assets when an upstream asset changes.
- **Improved Observability**: Viewing the state of the data platform through the lens of the data itself rather than the execution of scripts.