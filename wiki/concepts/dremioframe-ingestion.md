---
type: concept
title: dremioframe Ingestion Patterns
created: 2026-04-04
updated: 2026-04-04
tags: [dremio, ingestion, api, pandas]
related: [dremioframe, dremio, data-ingestion-architectural-patterns]
sources: ["Introducing dremioframe - A Pythonic DataFrame Interface for Dremio.md"]
---

# dremioframe Ingestion Patterns

**dremioframe** provides two primary mechanisms for ingesting external data into [[dremio]]: REST API ingestion and Pandas DataFrame insertion. These patterns enable Python developers to bring data into Dremio's lakehouse without leaving the Python ecosystem.

## REST API Ingestion

The `.ingest_api()` method pulls data from a REST API endpoint and writes it directly into a Dremio table.

```python
client.ingest_api(
    url="https://jsonplaceholder.typicode.com/posts",
    table_name="sandbox.api_posts",
    mode="merge"
)
```

**Parameters:**
- `url`: The REST API endpoint URL.
- `table_name`: Target Dremio table (catalog.schema.table format).
- `mode`: Ingestion mode (e.g., "merge", "overwrite", "append").

## Pandas DataFrame Insertion

Existing Pandas DataFrames can be inserted into Dremio tables:

```python
client.table("sandbox.my_table").insert("sandbox.my_table", data=pd_df)
```

## Use Cases

- **API data ingestion**: Pulling data from external services (e.g., CRM, analytics, public APIs) directly into the data lakehouse.
- **Notebook workflows**: Loading processed DataFrames from Jupyter notebooks into Dremio for downstream consumption.
- **ETL pipelines**: Using Python as the transformation layer before persisting results in Dremio.

## Relationship to Other Patterns

This pattern complements the [[data-ingestion-architectural-patterns]] framework by providing a Python-centric, programmatic approach to data ingestion. It is particularly suited for:
- **Push ingestion**: The Python application pushes data to Dremio.
- **Stream processing**: When combined with the async client, can handle continuous data flows.
- **Reverse ETL**: Inserting processed results back into the lakehouse for consumption by other tools.

## Limitations

- REST API ingestion is synchronous by default.
- No built-in scheduling or retry logic (requires external orchestration).
- DataFrame insertion performance depends on data size and Dremio configuration.
- Alpha status means ingestion patterns may change.