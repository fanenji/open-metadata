---
type: concept
title: Modern Data Stack Overview
created: 2026-05-07
updated: 2026-05-07
tags: [modern-data-stack, architecture, cloud-native]
related: [elt-pattern, reverse-etl-pattern, data-observability-definition, data-ingestion-architectural-patterns, data-lakehouse, data-mesh, data-contract-platform, fivetran, airbyte, snowflake, bigquery, redshift, databricks, dbt, monte-carlo, great-expectations, atlan, amundsen, datahub, metacat, hightouch, census, looker, tableau, mode, metabase, noteable, hex, portable, confluent, snowpipe, lookml, delta-live-tables, segment, snowplow, transform]
sources: ["understanding-the-modern-data-stack.md"]
---
# Modern Data Stack Overview

The Modern Data Stack refers to a suite of cloud-native products used for data integration and analysis by technology-forward companies. Key characteristics include lower setup barriers, easier scaling, and operational focus compared to legacy stacks.

## Components

The stack is typically broken down into six layers:

1. **Data Sources**: Databases (Postgres, MySQL, Mongo), SaaS products ([[stripe]], [[salesforce]], [[zendesk]], [[hubspot]]), and event streams ([[segment]], [[snowplow]]).
2. **Data Integration**: [[elt-pattern|ELT]] tools like [[fivetran]], [[airbyte]], and [[portable]]; streaming via [[confluent|Apache Kafka/Confluent]] or [[snowpipe]].
3. **Data Storage and Querying**: Cloud warehouses ([[snowflake]], [[bigquery]], [[redshift]]) and data lakes ([[databricks]]).
4. **Data Transformation**: [[dbt]], [[apache-airflow]], [[lookml]], [[delta-live-tables]].
5. **Data Governance and Monitoring**: Testing/observability ([[monte-carlo]], [[great-expectations]]), metrics layer ([[transform]]), cataloging ([[atlan]], [[amundsen]], [[datahub]], [[metacat]]), access control.
6. **Data Uses**: Analytics/collaboration ([[noteable]], [[hex]]), BI ([[looker]], [[tableau]], [[mode]], [[metabase]]), [[reverse-etl-pattern|reverse ETL]] ([[hightouch]], [[census]]).

## Relationship to Other Wiki Concepts

The Modern Data Stack provides the foundational architecture that more advanced patterns build upon. The [[data-lakehouse]] extends the storage layer with ACID/performance features. [[data-mesh]] reorganizes the stack around domain ownership and data products. [[data-contract-platform]] adds active governance to the monitoring layer. The [[elt-pattern]] is the core architectural pattern, while [[reverse-etl-pattern]] closes the loop by syncing data back to operational systems.

## Limitations

This overview (based on [[tanay-jaipuria|Tanay Jaipuria's]] 2022 article) is a 101-level description. It does not cover recent trends like data lakehouses, Apache Iceberg, or AI-driven data engineering. The wiki contains more critical perspectives on specific components, such as the [[data-catalog-critique]] and [[Data Engineering After AI]]'s ECL framework.