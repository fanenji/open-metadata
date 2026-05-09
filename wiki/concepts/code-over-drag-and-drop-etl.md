---
type: concept
title: Code-over-Drag-and-Drop ETL
created: 2026-05-07
updated: 2026-05-07
tags: [etl, code, abstraction, data-engineering, methodology]
related: [data-engineering-definition, elt-pattern, maxime-beauchemin, modern-data-modeling-shifts, airflow]
sources: ["The Rise of the Data Engineer.md"]
---
# Code-over-Drag-and-Drop ETL

The principle that ETL (Extract, Transform, Load) logic should be expressed in code rather than through graphical drag-and-drop interfaces. This is a core argument of Maxime Beauchemin's 2017 data engineering manifesto.

## Rationale

Code is argued to be the best abstraction for software, including ETL, because:

- **Arbitrary levels of abstraction** — code can express complex logic that drag-and-drop interfaces cannot.
- **Familiar logical operations** — all standard programming constructs are available.
- **Source control integration** — code integrates naturally with version control systems.
- **Easy versioning and collaboration** — standard software engineering practices apply.
- **Higher-level abstractions** — code enables building frameworks for A/B testing, anomaly detection, metrics computation, and other complex workflows that cannot be expressed in traditional ETL primitives.

## Obsolescence of Traditional ETL Tools

Traditional ETL tools (Informatica, IBM Datastage, Cognos, AbInitio, Microsoft SSIS) are considered largely obsolete because:

1. Logic cannot be expressed using code.
2. The abstractions needed (e.g., experiment configuration for A/B testing) cannot be expressed intuitively.
3. The shift forces the discipline to rebuild itself with a new stack, new tools, and new constraints.

## Modern Alternatives

Programmatic or configuration-driven platforms like Apache Airflow, Oozie, Azkaban, and Luigi replace traditional ETL tools. It is also common for engineers to develop and manage their own job orchestrators.

## Connections

- [[data-engineering-definition]] — Core methodological principle
- [[elt-pattern]] — Modern ETL paradigm that embodies this principle
- [[maxime-beauchemin]] — Author of the argument
- [[modern-data-modeling-shifts]] — Related changes in modeling
- [[airflow]] — Key tool embodying this principle