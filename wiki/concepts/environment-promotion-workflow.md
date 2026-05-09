---
type: concept
title: Environment Promotion Workflow
created: 2026-05-22
updated: 2026-05-22
tags: [ci-cd, workflow, lifecycle]
related: [kestra-promotion-strategy, dbt-modeling-layers]
sources: ["CI-CD GIT FOR v2.0.md"]
---
# Environment Promotion Workflow

The **Environment Promotion Workflow** defines the sequential, branch-based lifecycle of data projects within the Data Platform. It ensures that all code (dbt) and orchestration (Kestra) undergo rigorous testing before reaching production.

## The Promotion Path
The workflow follows a linear progression:
**`dev` $\rightarrow$ `test` $\rightarrow$ `stage` $\rightarrow$ `prod`**

### Phase 0: Development (Dev)
- **Scope**: Local development and initial testing.
- **Infrastructure**: `Kestra_sviluppo` (namespace `dev`).
- **Action**: Developers use `dbt-creator` to bootstrap projects. All changes are pushed to the `dev` branch.

### Phase 1: Testing (Test)
- **Trigger**: Merge Request from `dev` $\rightarrow$ `test`.
- **Validation**: Includes `dbt-checkpoint` (pre-commit tests), metadata ingestion (Dremio/OpenMetadata), and Kestra pipeline execution.
- **Infrastructure**: `Kestra_svancuppo` (namespace `test`).

### Phase 2: Staging (Stage)
- **Trigger**: Merge Request from `test` $\rightarrow$ `stage`.
- **Infrastructure**: `Kestra_esercizio` (namespace `stage`).
- **Note**: This stage involves a transition between different Kubernetes clusters.

### Phase 3: Production (Prod)
- **Trigger**: Merge Request from `stage` $\rightarrow$ `prod`.
- **Infrastructure**: `Kestra_esercizio` (namespace `prod`).
- **Goal**: Final deployment of stable, audited code to the production environment.

## Key Governance Rules
- **Single Source of Truth**: While Kestra flows may initially be modified in the Kestra UI, they **must** be saved to the Git repository as the first operation of any Merge Request to prevent loss of state.
- **Automated Auditing**: The CI/CD pipeline provides automated links to Dremio datasets, OpenMetadata schemas, and Kestra/OpenSearch logs upon successful deployment.
