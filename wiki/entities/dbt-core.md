---
type: entity
title: dbt Core
created: 2026-04-29
updated: 2026-05-07
tags: [dbt, open-source, data-transformation, cli, analytics-engineering]
related: [dbt-cloud, dbt-labs, elt-pattern, dbt-profiles-yml, dbt-adapters, dbt-project-scaffolding, jinja, dbt-core-vs-platform, dbt-duckdb-adapter, dbt-dremio-adapter, dbt-project-structure, dbt-macros, dbt-testing-patterns]
sources: ["How to get started with dbt.md", "Report dettagliato su dbt software.md"]
---
# dbt Core

dbt Core is an open-source framework developed by [[dbt Labs]] (formerly Fishtown Analytics) that helps organize data warehouse SQL transformations. It is the command-line tool that provides the `dbt` command for running transformations, tests, and documentation generation. At the heart of the dbt ecosystem, it is a Python application that compiles and executes analytical code, transforming SQL SELECT statements into materialized tables and views within the target data platform. dbt Core only performs the T in ELT — it passes SQL through to the underlying warehouse compute without any processing within dbt itself. It is not a scheduler and requires external orchestration for scheduled execution.

## Key Characteristics

- **Free and open-source:** No licensing costs; hosted on GitHub. Users are responsible for infrastructure and orchestration.
- **CLI-based:** Development happens in a local IDE with command-line execution.
- **ELT responsibility:** Only performs the transformation step; leverages the warehouse for compute.
- **Adapter-dependent:** Requires a [[dbt-adapters|dbt adapter]] plugin to connect to a specific data platform.
- **Profile configuration:** Uses a [[dbt-profiles-yml|profiles.yml]] file for warehouse credentials.
- **Project initialization:** Projects are scaffolded with `dbt init`.
- **Manual orchestration:** External schedulers (cron, Airflow, Dagster) are needed for job scheduling.
- **Self-managed CI/CD:** Users configure their own CI/CD pipelines in tools like GitHub Actions or Jenkins.
- **Documentation:** Self‑hosted — documentation files are generated locally and require separate hosting (e.g., S3, GitHub Pages). The community considers dbt’s documentation to be exceptional.
- **Full control:** Users manage installation, updates, and maintenance of the environment.

## Installation

dbt Core is installed via pip, typically within a Python virtual environment:

```bash
pip install dbt-core dbt-duckdb dbt-dremio
```

Replace `dbt-duckdb` and `dbt-dremio` with the adapter(s) required for your target data platform.

## Adapter Architecture

dbt Core uses a plugin-based adapter architecture to connect to different data platforms. Each adapter is a separate Python package (e.g., `dbt-duckdb`, `dbt-dremio`, `dbt-snowflake`, `dbt-bigquery`, `dbt-redshift`, `dbt-databricks`). This design makes dbt platform-agnostic, supporting many data warehouses and query engines.

## Relationship to dbt Platform

dbt Core is the foundation upon which [[dbt-cloud|dbt Platform (Cloud)]] is built. The Platform is a managed SaaS offering that provides an integrated web IDE, scheduler, CI/CD, documentation hosting, and monitoring on top of dbt Core. The choice between Core and Platform is a foundational architectural decision impacting operational model, costs, and team skills. While dbt Core is self‑managed and requires users to handle infrastructure and scheduling, dbt Cloud abstracts these concerns for a more integrated experience.