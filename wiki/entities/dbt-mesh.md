---
type: entity
title: dbt Mesh
created: 2026-05-07
updated: 2026-05-07
tags: [dbt, mesh, governance, data-products]
related: [data-mesh, dbt-cloud, dbt-catalog, dbt-cloud-environments]
sources: ["dbt Certified Architect Path beta - dbt Learn.md"]
---
# dbt Mesh

dbt Mesh is dbt Labs' implementation of the [[data-mesh]] architectural pattern within dbt Cloud. It enables organizations to manage cross-project dependencies, allowing different teams to own and develop their own dbt projects while consuming data products from other projects in a governed manner.

## Key Capabilities

- **Cross-project references**: Models in one project can reference models in another project via the `ref()` function.
- **Governance at scale**: Domain teams maintain ownership of their data products while the platform enforces access controls and dependency contracts.
- **Development speed**: Teams can develop and deploy independently without blocking on a monolithic project.
- **Reliability**: Contract enforcement between projects ensures upstream changes don't break downstream consumers.

## Relationship to Data Mesh

While [[data-mesh]] is a broad architectural paradigm with four principles (domain ownership, data as a product, self-serve platform, federated governance), dbt Mesh is a concrete product implementation that operationalizes these principles within the dbt Cloud ecosystem. It is a key topic in the [[dbt-cloud-architect-certification]] learning path (Milestone #4: Governance and Discovery).