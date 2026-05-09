---
type: concept
title: Smart Deferral
created: 2026-04-22
updated: 2026-04-22
tags: [dbt, efficiency, ci-cd]
related: [slim-ci, dbt]
sources: ["5-dbt-slim-ci-tactics-for-large-repos.md"]
---
# Smart Deferral

**Smart Deferral** is a technique used in dbt CI pipelines to allow a development or CI build to reference existing production relations instead of re-materializing the entire dependency graph.

### How it Works
By using the `--defer` flag and providing a `--state` pointing to a recent production `manifest.json`, dbt can:
1. Build only the models that have changed in the current branch.
2. For all upstream dependencies that haven't changed, "defer" to the existing tables/views in the production environment.

### Benefits
- **Reduced Compute Cost**: Avoids running expensive transformations for unchanged data.
- **Faster CI Cycles**: Drastically reduces the time required for a Pull Request to pass.
- **Smaller Footprint**: Minimly impacts the warehouse with ephemeral CI schemas.