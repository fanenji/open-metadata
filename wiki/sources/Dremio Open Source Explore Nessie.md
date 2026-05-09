---
type: source
title: "Dremio Open Source: Explore Nessie"
created: 2026-05-07
updated: 2026-05-07
tags: [nessie, iceberg, data-lakehouse, catalog-versioning, git-for-data]
related: [nessie-catalog-versioning, iceberg-table-versioning, data-lakehouse-versioning-strategies, nessie-cli-commands, nessie-spark-integration]
sources: ["Dremio Open Source Explore Nessie.md"]
authors: [Dremio]
year: 2023
url: "https://www.dremio.com/open-source/nessie/"
venue: Dremio Blog
---
# Dremio Open Source: Explore Nessie

This article introduces Project Nessie, a transactional catalog that brings Git-like workflows (branching, committing, merging) to data lakehouse catalogs. It provides a step-by-step Docker-based tutorial for setting up Nessie with Apache Iceberg and Apache Spark, demonstrating how to create branches, insert isolated data, and merge multi-table transactions.

## Key Points

- Nessie is a transactional metastore that tracks the state and changes of all tables in the catalog via commits and branches, analogous to Git for code.
- It provides just as much functionality as Hive or AWS Glue as a data catalog, with the added ability to create branches of the entire catalog.
- Nessie manages versions of the catalog (the list of tables and their metadata locations), not individual table data.
- The article demonstrates creating a branch, inserting data on the branch, querying the main vs. branch, and merging the branch as a multi-table transaction.
- The `table@branch` syntax allows querying specific branches.
- The `MERGE BRANCH` command enables atomic multi-table transactions.

## Caveats

- The demo uses `authentication.type=NONE` — production deployments require proper authentication configuration.
- The article oversimplifies the comparison between Nessie and Hive/Glue; Nessie is a transactional catalog, not a full replacement for all catalog functions.
- Performance implications of catalog-level versioning at scale are not discussed.

## Connections

- Strengthens [[nessie-catalog-versioning]] with concrete SQL syntax and CLI commands.
- Extends [[iceberg-table-versioning]] by showing how Nessie enables catalog-scale versioning.
- Adds practical implementation detail to [[data-lakehouse-versioning-strategies]].