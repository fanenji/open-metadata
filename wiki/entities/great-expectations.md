---
type: entity
title: Great Expectations
created: 2026-04-04
updated: 2026-05-07
tags: [data-quality, testing, python, open-source, tool]
related: [ai-driven-data-quality, data-observability, monte-carlo, dbt-expectations, data-observability-definition, data-quality-dimensions, great-expectations-for-data-contracts]
sources: ["Automate Data Quality Checks with AI Agents.md", "understanding-the-modern-data-stack.md"]
---
# Great Expectations

**Great Expectations** is an open-source Python library for validating, documenting, and profiling data. It allows data engineers to define "expectations" (assertions) about their data, which are automatically checked against incoming datasets to ensure compliance with defined quality dimensions.

In the [[modern-data-stack-overview|modern data stack]], Great Expectations serves as a core data testing and observability tool, commonly used alongside [[monte-carlo]] for data governance and monitoring. The project also plays a key role in [[great-expectations-for-data-contracts|data contract enforcement]] and has been ported to dbt via the [[dbt-expectations]] package.