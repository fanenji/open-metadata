---
type: entity
title: Nessie Spark Integration
created: 2026-05-07
updated: 2026-05-07
tags: [nessie, spark, iceberg, data-lakehouse, integration]
related: [nessie-catalog-versioning, iceberg-table-versioning, nessie-cli-commands]
sources: ["Dremio Open Source Explore Nessie.md"]
---
# Nessie Spark Integration

The Nessie Spark integration enables Apache Spark to use Nessie as a transactional catalog for Apache Iceberg tables. This allows Spark to leverage Nessie's Git-like branching, committing, and merging capabilities.

## Configuration

To configure Spark to use a Nessie catalog, the following configuration flags are passed:

```bash
spark-sql --packages org.apache.iceberg:iceberg-spark-runtime-3.2_2.12:0.14.0,org.projectnessie:nessie-spark-3.2-extensions:0.40.1 \
  --conf spark.sql.extensions="org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions,org.projectnessie.spark.extensions.NessieSpark32SessionExtensions" \
  --conf spark.sql.catalog.nessie.uri="http://nessie:19120/api/v1" \
  --conf spark.sql.catalog.nessie.ref=main \
  --conf spark.sql.catalog.nessie.authentication.type=NONE \
  --conf spark.sql.catalog.nessie.catalog-impl=org.apache.iceberg.nessie.NessieCatalog \
  --conf spark.sql.catalog.nessie=org.apache.iceberg.spark.SparkCatalog \
  --conf spark.sql.catalog.nessie.warehouse=$PWD/warehouse
```

### Configuration Details

- **Packages**: Ensures Spark uses the Nessie and Iceberg packages.
- **Extensions**: Enables the Nessie and Iceberg SQL extensions.
- **URI**: Sets the URL of the Nessie server.
- **Ref**: Sets the default branch for SQL commands.
- **Authentication**: Set to NONE for demo purposes; production requires proper authentication.
- **Catalog Implementation**: Creates a Spark catalog and sets it to a Nessie implementation.
- **Warehouse**: Identifies where the files will be stored.

## SQL Syntax

Once configured, Spark SQL can use Nessie-specific syntax:

- `CREATE BRANCH IF NOT EXISTS my_branch IN nessie;` — Create a new branch.
- `LIST REFERENCES IN nessie;` — List all branches.
- `INSERT INTO nessie.db.\`table@my_branch\` VALUES (...);` — Insert data on a specific branch.
- `SELECT * FROM nessie.db.\`table@my_branch\`;` — Query data from a specific branch.
- `MERGE BRANCH my_branch INTO main IN nessie;` — Merge a branch into main as a multi-table transaction.

## Docker Setup

A `docker-compose.yml` file with a Nessie server and a Spark-Iceberg container is used for local development:

```yaml
services:
  spark-iceberg:
    image: alexmerced/nessie-sandbox-072722
    ports:
      - "8080:8080"
      - "7077:7077"
      - "8081:8081"
  nessie:
    image: projectnessie/nessie
    ports:
      - "19120:19120"
```