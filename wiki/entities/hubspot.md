---
type: entity
title: Hubspot
created: 2026-05-07
updated: 2026-05-07
tags: [saas, data-source, marketing]
related: [stripe, salesforce, zendesk, fivetran, airbyte, hightouch, census]
sources: ["understanding-the-modern-data-stack.md"]
---
# Hubspot

A marketing and sales SaaS platform that serves as a common data source and destination in the [[modern-data-stack-overview|Modern Data Stack]]. Marketing data from Hubspot is extracted via [[elt-pattern|ELT]] tools, and enriched data can be synced back via [[reverse-etl-pattern|reverse ETL]] tools like [[hightouch]] and [[census]].