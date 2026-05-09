---
type: concept
title: Database Snapshotting Pattern
created: 2026-04-29
updated: 2026-04-29
tags: [data-ingestion, databases, dataflow, snapshot]
related: [elt-pattern, data-ingestion-architectural-patterns, blablacar, reverse-etl-pattern]
sources: ["Data Pipelines Architecture at BlaBlaCar.md"]
---
# Database Snapshotting Pattern

Database snapshotting is a data ingestion pattern where production databases are periodically replicated to a data warehouse by taking full or incremental snapshots of specified tables. This pattern is commonly used in [[elt-pattern]] architectures to bring operational data into analytical systems.

## BlaBlaCar Implementation

At [[BlaBlaCar]], database snapshotting is managed by Google Dataflow using custom templates. Key characteristics:

- **Custom Dataflow templates**: Built to handle various use cases including encrypted PII data
- **Airflow orchestration**: Dataflow jobs are triggered by Airflow
- **Configurable snapshotting**: Data teams define table configurations and schedules in Airflow DAGs
- **Python library**: A library is provided for use in Airflow to simplify configuration

## Configuration Example

```python
SNAPSHOTTED_TABLES = [
  {
    'cluster_name': 'communication',
    'destination': {
      'bq_project_id': 'prod-bbc',
      'bq_dataset_id': 'snapshot',
    },
    'databases': [
      {
        'db_name': 'communication',
        'tables': [
          {
            'table_name': 'notifications',
            'primary_key': 'id',
          },
        ],
      },
    ],
  },
]
```

## Supported Databases

- MariaDB
- PostgreSQL
- Oracle
- BigTable (non-relational)

## Alternative Approaches

BlaBlaCar explored Airbyte (self-hosted) in 2022 but found its performance insufficient. The main challenge for adopting alternative tools is integrating custom features like handling encrypted PII data.