---
type: entity
title: Salesforce
created: 2026-05-07
updated: 2026-05-07
tags: [saas, data-source, crm]
related: [stripe, zendesk, hubspot, fivetran, airbyte, hightouch, census]
sources: ["understanding-the-modern-data-stack.md"]
---
# Salesforce

A customer relationship management (CRM) SaaS platform that serves as a common data source and destination in the [[modern-data-stack-overview|Modern Data Stack]]. Customer data from Salesforce is extracted via [[elt-pattern|ELT]] tools, and enriched data can be synced back via [[reverse-etl-pattern|reverse ETL]] tools like [[hightouch]] and [[census]].