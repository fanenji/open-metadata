type: concept
title: Nessie Versioning Strategy
created: 2026-05-22
updated: 2026-05-22
tags: [data-governance, versioning, architecture]
related: [nessie, dbt-workflow]
sources: ["AMBIIT.md"]
---
# Nessie Versioning Strategy

A critical architectural decision for the platform is determining how to implement environment isolation and project management within the **Nessie** catalog. Two primary strategies are under consideration.

## Strategy 1: Folder-based Isolation
In this approach, environments are isolated using separate root-level folders within the Nessie catalog.
- **Pros**: High stability, lower complexity, easier to implement within standard **dbt** workflows.
- **Cons**: Less "Git-native" than branching; requires managing path conventions in `profiles.yml` (e.g., `dev.test_local_4`).

## Strategy 2: Branch-based Isolation
This approach leverages Nessie's native branching capabilities, creating a `main` branch for production and `project-xxx` branches for individual development tasks.
- **Pros**: Highly elegant and aligns with Git-based development workflows; allows for feature-based data isolation.
- **Cons**: High complexity; requires custom **dbt** macros for branch management; significant risk of data inconsistency if merges to `main` are not strictly controlled.

## Comparison Summary

| Feature | Folder-based | Branch-based |
| :--- | :--- | :--- |
| **Complexity** | Low | High |
| **Risk of Error** | Low | High (Accidental merges) |
| **dbt Integration** | Standard (Path-based) | Requires Custom Macros |
| **Isolation Level** | Logical (Path) | Logical (Branch) |
