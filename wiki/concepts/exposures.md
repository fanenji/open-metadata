---
type: concept
title: Exposures
created: 2026-04-29
updated: 2026-04-29
tags: [dbt, cross-project, data-mesh, lineage]
related: [dbt-mesh, dbt-project-organization-strategies, dbt-packages, data-mesh]
sources: ["How to manage and schedule dbt.md"]
---
# Exposures

A dbt feature that allows projects to define downstream usage of their models. Exposures serve as a cross-project interface mechanism, enabling one dbt project to declare which models are consumed by external systems or other dbt projects.

## Usage in Multi-Project Architectures

In a multi-project setup, exposures in one project can be used to automatically generate source definitions in another project. For example:
- **Ops project** defines exposures for models that Marketing should be aware of.
- **Marketing project** uses automation to generate source definitions from Ops exposures.

## Comparison with Packages

| Aspect | Exposures | Packages |
|--------|-----------|----------|
| Dependency direction | Producer declares what's exposed | Consumer installs producer as dependency |
| Complexity | Lower — automation generates sources | Higher — dependency management, potential duplicate execution |
| Recommended for | Multi-project, data mesh architectures | Simple cross-project sharing |

## Relationship to Data Mesh

Exposures are a key enabler for [[data-mesh]] architectures in dbt, allowing domain teams to define clear interfaces between their data products and consumers. The GoDataDriven talk "dbt & data mesh: the perfect pair (?)" at Coalesce provides implementation guidance.