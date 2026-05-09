---
type: entity
title: Stripe
created: 2026-04-04
updated: 2026-05-07
tags: [company, apache-iceberg, enterprise-adoption, saas, data-source, payments]
related: [apache-iceberg, iceberg-enterprise-adoption-signals, salesforce, zendesk, hubspot, fivetran, airbyte]
sources:
  - "Is Apache Iceberg Melting?.md"
  - "understanding-the-modern-data-stack.md"
---
# Stripe

Stripe is a payment processing SaaS platform that serves as a common data source in the [[modern-data-stack-overview|Modern Data Stack]]. Billing and subscription data from Stripe is typically extracted and loaded into cloud data warehouses via [[elt-pattern|ELT]] tools like [[fivetran]] or [[airbyte]]. Additionally, Stripe is an enterprise adopter of [[apache-iceberg]]. During Trino Fest, Stripe shared that they use Iceberg tables extensively and have replaced legacy Hive tables, describing operational friction points around reading Iceberg metadata from S3 and building internal tooling.