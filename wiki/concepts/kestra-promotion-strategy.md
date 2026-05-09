---
type: concept
title: Kestra Promotion Strategy
created: 2026-05-22
updated: 2026-05-22
tags: [ci-cd, orchestration, kestra, automation]
related: [kestra, environment-promotion-workflow, infrastructure-architecture]
sources: ["CI-CD GIT FLOW v2.0.md"]
---
# Kestra Promotion Strategy

The **Kestra Promotion Strategy** is a specialized CI/CD mechanism designed to move orchestration logic (flows) across different environments while maintaining strict namespace isolation and version control.

## Core Principle: Unified Repository Pattern
Instead of maintaining a separate repository for Kestra flows, all flow definitions are co-located within the `/flows/` directory of the respective dbt project repository. This ensures that orchestration logic and transformation logic are versioned, tested, and promoted together.

## Promotion Lifecycle

### 1. Dev $\rightarrow$ Test (The "Pull-Transform-Push" Cycle)
This is the most complex stage of the promotion. When a Merge Request (MR) is opened from `dev` to `test`, GitLab CI/CD performs the following:
1. **Fetch**: Retrieves the current flow YAML from the Kestra `dev` namespace via `curl (GET)`.
2. **Sync to Git**: Saves the retrieved YAML into the `/flows/` directory of the `dev` branch.
3. **Transform**: Renames the flow identifier to match the `test` namespace (e.g., `dev.project.flow` $\rightarrow$ `test.project.flow`).
4. **Update Git**: Saves the transformed YAML into the `test` branch.
5. **Push to Kestra**: Deploys the updated flow to the Kestra `test` namespace via `curl (POST)`.

### 2. Test $\rightarrow$ Stage/Prod (Cluster Migration)
Promotion from `test` to `stage` (and subsequently to `prod`) involves moving between different Kubernetes clusters/namespaces (from `Kestra_sviluppo` to `Kestra_esercizio`).
- The CI/CD pipeline handles the renaming of namespaces (e.g., `test` $\rightarrow$ `stage`) and the deployment of the updated YAML to the target Kestra instance.

## Namespace Isolation
The strategy relies on strict namespace separation within Kestra to prevent cross-environment interference:
- **Kestra_sviluppo**: Manages `dev` and `test` namespaces.
- **Kestra_esercizio**: Manages `stage` and `prod` namespaces.