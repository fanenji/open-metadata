---
type: entity
title: Zendesk
created: 2026-05-07
updated: 2026-05-07
tags: [saas, data-source, support]
related: [stripe, salesforce, hubspot, fivetran, airbyte, hightouch, census]
sources: ["understanding-the-modern-data-stack.md"]
---
# Zendesk

A customer support SaaS platform that serves as a common data source and destination in the [[modern-data-stack-overview|Modern Data Stack]]. Support ticket data from Zendesk is extracted via [[elt-pattern|ELT]] tools, and enriched data can be synced back via [[reverse-etl-pattern|reverse ETL]] tools like [[hightouch]] and [[census]].