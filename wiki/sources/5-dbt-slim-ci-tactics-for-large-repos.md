---
type: source
title: "5 dbt Slim CI Tactics for Large Repos"
created: 2026-04-22
updated: 2026-04-22
tags: [dbt, ci-cd, data-engineering, slim-ci]
related: [dbt, slim-ci, data-observability, data-governance]
sources: ["5-dbt-slim-ci-tactics-for-large-repos.md"]
authors: [Neurobyte]
year: 2025
url: "https://medium.com/@kaushalsinh73/5-dbt-slim-ci-tactics-for-large-repos-33c6a1789a22"
venue: "Medium"
---
# 5 dbt Slim CI Tactics for Large Repos

An article detailing five production-ready tactics for implementing "Slim CI" in large dbt projects to maintain fast, safe, and focused Pull Request builds.

Key tactics include:
- **State-Aware Selection**: Using `state:modified+` to capture the blast radius.
- **Smart Deferral**: Reusing production relations to avoid re-materializing the entire DAG.
- **Focused Testing**: Splitting tests into fast PR-time schema tests and deep nightly tests.
- **Partial Parsing**: Reducing planning time by reusing metadata.
- **Artifact Hygiene**: Managing `manifest.json` and `run_results.json` in cloud storage.