---
type: source
title: "What is CI, and why should you care about it"
created: 2026-05-07
updated: 2026-05-07
tags: [ci, dbt, data-engineering, continuous-integration]
related: [dbt-slim-ci, ci-cd-for-data-pipelines, shift-left-data-quality, dbt-cloud-environments, dbt-ci-pipeline-anatomy]
sources: ["What is CI, and why should you care about it.md"]
authors: [Gleb Mezhanskiy]
year: 2023
url: "https://www.datafold.com/blog/why-you-should-care-about-ci/"
venue: "Datafold Blog"
---
# What is CI, and why should you care about it

This article by [[Gleb Mezhanskiy]] argues that implementing Continuous Integration (CI) for dbt projects is one of the highest-ROI improvements a data team can make. It introduces the "dbt Hierarchy of Needs" pyramid, placing CI above foundational elements like models, tests, documentation, and materializations.

The article describes a three-environment model (Production, Development, Staging) and provides a five-step CI pipeline anatomy: compile, build, test, lint, and data diff. It includes practical setup instructions for both [[dbt-cloud]] (using PR-triggered jobs and [[dbt-slim-ci]]) and [[dbt-core]] (using GitHub Actions). The author emphasizes that without CI, code reviews rely on human eyeballs, leading to bad deployments, broken downstream dashboards, and team burnout.

The source promotes Datafold's data diff tool as a bonus CI step, which should be noted as vendor-specific content.
