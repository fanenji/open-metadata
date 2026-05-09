---
type: source
title: "Principles of effective data delivery: How CI/CD should look for Data teams (Miniseries Part 3)"
created: 2026-04-04
updated: 2026-04-04
tags: [ci-cd, data-delivery, data-teams, accelerate]
related: [data-ci-cd-principles, data-release-pipeline, deployment-critical-vs-monitoring-tests, hugo-lu, CI-CD-for-data-pipelines, data-contract-observability, dbt-slim-ci, data-mesh]
sources: ["How CI-CD should look for Data teams.md"]
authors: [Hugo Lu]
year: 2023
url: "https://medium.com/orchestras-data-release-pipeline-blog/principles-of-effective-data-delivery-how-ci-cd-should-look-for-data-teams-miniseries-part-3-396deb5af97a"
venue: "Orchestra Blog (Medium)"
---
# Principles of effective data delivery: How CI/CD should look for Data teams (Miniseries Part 3)

This article argues that data teams have fundamentally different CI/CD needs than software or ML teams because they ship *data objects* (files/tables), not just code. It adapts the 24 characteristics from the book *Accelerate* for data teams and introduces a "Hierarchy of Data Needs" as a prioritization framework for tooling and process decisions.

Key contributions:
- Defines data teams' dual responsibility: deploying code for data pipelines AND managing the state of data objects in production.
- Adapts Accelerate's Continuous Delivery and Architecture capabilities for data, adding concepts like [[data-release-pipeline]], [[deployment-critical-vs-monitoring-tests]], and "flat cloning" data into production.
- Introduces the **Hierarchy of Data Needs**: Security → Functionality → Reliability → Cost/Time → Flexibility → Simplicity.
- Advocates for trunk-based development (fewer than 3 branches) for SQL repositories.
- Distinguishes between deployment-critical and non-deployment-critical data quality tests.
- Emphasizes "state availability" for downstream consumers.

The article is opinion-based and vendor-adjacent (Orchestra), with the author acknowledging "limited scientifically collated quantitative data."