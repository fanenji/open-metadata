---
type: concept
title: dbt profiles.yml
created: 2026-04-29
updated: 2026-04-29
tags: [dbt, configuration, credentials]
related: [dbt-core, dbt-adapters, dbt-project-scaffolding]
sources: ["How to get started with dbt.md"]
---
# dbt profiles.yml

The `profiles.yml` file contains the credentials required to connect a [[dbt Core]] project to a data warehouse. By default, this file is located in the `$HOME/.dbt/` directory. Users can specify a custom location using the `--profiles-dir` CLI option.

The file defines one or more profiles, each containing connection details for a specific target environment (e.g., dev, prod). A connection to a warehouse requires a [[dbt-adapters|dbt adapter]] to be installed. The profiles.yml file is a critical configuration artifact that must be properly set up before any dbt commands can execute against a warehouse.