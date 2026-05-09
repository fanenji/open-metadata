---
type: concept
title: dbt Hierarchy of Needs
created: 2026-05-07
updated: 2026-05-07
tags: [dbt, data-engineering, maturity-model]
related: [dbt-ci-pipeline-anatomy, ci-cd-for-data-pipelines, dbt-slim-ci]
sources: ["What is CI, and why should you care about it.md"]
---
# dbt Hierarchy of Needs

The dbt Hierarchy of Needs is a pyramid model that visualizes the maturity progression of a dbt project. The foundational layers include models, tests, documentation, and materializations. Above these sits Continuous Integration (CI), representing the next level of maturity for data teams.

The model argues that once a team has mastered the basics of dbt (building models, writing tests, documenting, and configuring materializations), implementing CI is the highest-ROI improvement available. CI enables automated validation of code changes, enforces standards, and reduces the risk of bad deployments.

This framework is introduced by [[Gleb Mezhanskiy]] in the article "What is CI, and why should you care about it" and is not yet widely adopted across the dbt community. It serves as a useful conceptual tool for prioritizing data engineering investments.
