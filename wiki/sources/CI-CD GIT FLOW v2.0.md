---
type: source
title: CI-CD GIT FLOW v2.0
created: 2026-05-22
updated: 2026-05-22
tags: [ci-cd, kestra, git, dbt]
related: [kestra, dbt-modeling-layers, infrastructure-architecture]
authors: []
year: 2026
url: ""
venue: ""
---
# CI-CD GIT FLOW v2.0

This source document outlines the rules and workflow for promoting dbt projects and orchestration pipelines across various environments (Dev, Test, Stage, Prod) using GitLab CI/CD and Kestra.

Key components include the `dbt-creator` automation script, the unified repository pattern (co-locating Kestra flows within dbt projects), and the namespace-based isolation strategy.