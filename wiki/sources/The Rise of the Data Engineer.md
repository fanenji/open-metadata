---
type: source
title: The Rise of the Data Engineer
created: 2026-05-07
updated: 2026-05-07
tags: [data-engineering, manifesto, role-definition, etl, data-modeling]
related: [maxime-beauchemin, data-engineering-definition, code-over-drag-and-drop-etl, modern-data-modeling-shifts, data-engineer-as-librarian, data-engineer-as-center-of-excellence, data-warehouse-as-public-institution, saas-data-integration-challenges, elt-pattern, data-catalog-critique, data-mesh, data-quality-certification-vs-usability-certification]
sources: ["The Rise of the Data Engineer.md"]
---
# The Rise of the Data Engineer

**Author:** Maxime Beauchemin  
**Published:** 2017-01-21  
**Source:** freeCodeCamp  
**URL:** https://www.freecodecamp.org/news/the-rise-of-the-data-engineer-91be18f1e603/

## Summary

This foundational manifesto defines data engineering as a distinct discipline, superseding traditional business intelligence and data warehousing roles. Drawing on the author's experience at Facebook, Airbnb, and Yahoo!, the article argues that data engineering is closer to software engineering than data science, emphasizing code over drag-and-drop ETL tools, evolving data modeling practices, and the data engineer's role as librarian, center of excellence, and builder of higher-level abstractions.

## Key Arguments

1. **Data engineering is a distinct discipline** — evolved from BI engineering, incorporating software engineering and big data systems expertise.
2. **Traditional ETL tools are obsolete** — code is the best abstraction; drag-and-drop interfaces cannot express needed abstractions (e.g., A/B testing frameworks).
3. **Data modeling is shifting** — denormalization, blobs, dynamic schemas, snapshotting dimensions, and relaxed conformance are replacing rigid star schema approaches.
4. **Data warehouse as public institution** — open participation by data scientists, analysts, and software engineers, with data engineers owning certified core schemas.
5. **Data integration is a growing challenge** — SaaS proliferation creates unaccounted integration work with poorly designed APIs.

## Relevance

This article is a historical landmark (2017) that defined the data engineering role. It predates many modern concepts in this wiki (data contracts, dbt, Iceberg, data mesh) and should be treated as foundational context rather than current best practice. Its emphasis on "big data" distributed systems (Hadoop, Spark) contrasts with the wiki's focus on lightweight tools (DuckDB, dbt, Dremio).

## Connections

- [[data-engineering-definition]] — The article's central thesis
- [[code-over-drag-and-drop-etl]] — Core argument for programmatic ETL
- [[modern-data-modeling-shifts]] — The five observed shifts in modeling
- [[data-engineer-as-librarian]] — Metadata management role
- [[data-engineer-as-center-of-excellence]] — Standards and education role
- [[data-warehouse-as-public-institution]] — Open participation model
- [[saas-data-integration-challenges]] — SaaS API integration problems
- [[elt-pattern]] — Historical context for the ETL-to-ELT shift
- [[data-catalog-critique]] — Complementary "librarian" perspective
- [[data-mesh]] — Precursor to federated governance concepts
- [[data-quality-certification-vs-usability-certification]] — "Certified core schemas" concept