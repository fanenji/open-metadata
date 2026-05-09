type: concept
title: dbt Project Governance
created: 2026-04-04
updated: 2026-04-04
tags: [dbt, governance, data-mesh, project-management]
related: [data-mesh, dbt-scaling-patterns, blablacar, dbt-dag-generator]
sources: ["One Thousands and One dbt Models How BlaBlaCar Moved to dbt in 12 months - Summary.md"]
---
# dbt Project Governance

**dbt project governance** refers to the criteria and processes for deciding when to create a new dbt project vs. when to add a new folder within an existing project. This concept emerged from [[blablacar]]'s experience where a data mesh structure led to the creation of **50+ dbt projects** in 12 months.

## Problems with Project Proliferation

- **Cross-project `ref()` not supported natively**: Requires `source()` for cross-project references, losing lineage visibility
- **Version drift**: Different projects on different dbt versions
- **CI overhead**: 50 separate CI pipelines to maintain
- **Cross-project dependency management**: Harder to track and manage

## Governance Criteria

Define clear criteria for when a new project is warranted:

- **New project**: When the domain team has fully independent data products with no cross-references to other projects
- **New folder within existing project**: When models share dependencies, lineage, or need to `ref()` each other

## Key Lesson

Set **project creation governance early** — before teams start creating projects independently. The cost of consolidating projects later is much higher than establishing boundaries upfront.

## Related Concepts

- [[data-mesh]] — The architectural paradigm that encourages domain autonomy but requires governance guardrails
- [[dbt-scaling-patterns]] — Collection of practices for scaling dbt adoption
- [[dbt-dag-generator]] — The DAG generation pattern that makes multi-project management feasible