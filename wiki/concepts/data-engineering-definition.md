---
type: concept
title: Data Engineering Definition
created: 2026-05-07
updated: 2026-05-07
tags: [data-engineering, role-definition, discipline, manifesto]
related: [maxime-beauchemin, code-over-drag-and-drop-etl, modern-data-modeling-shifts, data-engineer-as-librarian, data-engineer-as-center-of-excellence, data-warehouse-as-public-institution, saas-data-integration-challenges, elt-pattern, context-architect-role]
sources: ["The Rise of the Data Engineer.md"]
---
# Data Engineering Definition

Data engineering is a distinct discipline that emerged from the evolution of business intelligence and data warehousing, incorporating elements from software engineering and specialization in "big data" distributed systems. This definition was formalized in Maxime Beauchemin's 2017 manifesto "The Rise of the Data Engineer."

## Core Characteristics

- **Superset of BI and data warehousing** — incorporates traditional analytical data management with modern software engineering practices.
- **Closer to software engineering than data science** — data engineers build tools, infrastructure, frameworks, and services, not just reports and dashboards.
- **Code-over-drag-and-drop** — programmatic ETL using tools like Airflow and Luigi replaces traditional GUI-based ETL tools.
- **Big data specialization** — expertise in distributed systems (Hadoop, Spark, Hive) and stream processing.
- **Higher-level abstractions** — building frameworks for A/B testing, anomaly detection, metrics computation, and metadata management.

## Evolution

The role evolved from business intelligence engineer (focused on reports and dashboards) to data engineer (focused on infrastructure, pipelines, and services). This shift was driven by:

1. Better self-service tooling allowing analysts and data scientists to consume data autonomously.
2. The obsolescence of traditional drag-and-drop ETL tools.
3. The rise of big data distributed systems requiring specialized operational knowledge.
4. The need for higher-level abstractions beyond basic ETL primitives.

## Relationship to Other Roles

- **Data Science:** Both write code and are analytical, but data engineers focus on infrastructure and tools rather than modeling and experimentation.
- **Software Engineering:** Data engineering is arguably closer to software engineering, sharing practices like version control, testing, and CI/CD.
- **Data Infrastructure:** In larger organizations, data infrastructure teams handle platform operations while data engineers build on top of those platforms.

## Connections

- [[maxime-beauchemin]] — Author of the defining manifesto
- [[code-over-drag-and-drop-etl]] — Core methodological argument
- [[modern-data-modeling-shifts]] — Related changes in data modeling
- [[data-engineer-as-librarian]] — Metadata management aspect
- [[data-engineer-as-center-of-excellence]] — Standards and education aspect
- [[data-warehouse-as-public-institution]] — Governance model
- [[saas-data-integration-challenges]] — Ongoing challenge
- [[elt-pattern]] — Modern ETL paradigm
- [[context-architect-role]] — Later evolution of the role toward meaning and context