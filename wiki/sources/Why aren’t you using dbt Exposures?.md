---
type: source
title: Why aren’t you using dbt Exposures?
created: 2026-04-04
updated: 2026-04-04
tags: [dbt, exposures, lineage, data-governance]
related: [dbt-exposures, dbt-catalog, dbt-observability-implementation, data-contract-observability, dbt-cloud, elementary-dbt-package]
sources: ["Why aren’t you using dbt Exposures?.md"]
authors: [Matthew Senick]
year: 2025
url: https://blog.dataengineerthings.org/why-arent-you-using-dbt-exposures-78b11e15be02
venue: Data Engineer Things
---
# Why aren’t you using dbt Exposures?

This article by [[Matthew Senick]] argues that [[dbt-exposures]] are an underutilized feature that solves real pain points around change management, lineage visibility, and stakeholder communication. The author presents four key benefits: making downstream connections explicit, extending the lineage graph to business-relevant assets, enabling proactive communication during changes, and facilitating model review sessions. The article provides a simple YAML example and discusses implementation options (manual, scripted via BI tool APIs, and dbt Cloud native integrations). The core claim is that exposures are a low-effort, high-impact governance practice that bridges the gap between data models and business value.