---
type: entity
title: dlt (data load tool)
created: 2026-04-29
updated: 2026-04-29
tags: [open-source, python, elt, data-loading]
related: [dlthub-platform, python-native-elt, elt-pattern, duckdb, snowflake-zero-copy-clone]
sources: ["dltHub ELT as Python Code.md"]
---
# dlt (data load tool)

**dlt** (data load tool) is an open-source Python library for moving data from various sources into structured, live datasets. It is the most popular production-ready Python library for data movement, with 10M+ PyPI downloads, 8,000+ OSS companies in production, and 600+ Snowflake customers.

## Key Features

- **Python-native**: No backends or containers required — just `pip install dlt` and import into any Python environment (code editor, Jupyter Notebook).
- **Source flexibility**: Loads data from any source producing Python data structures, including APIs, files, databases, and more.
- **Schema inference**: Automatically infers and evolves schemas from incoming data.
- **Incremental loading**: Supports incremental data loading patterns.
- **Destination support**: Works with DuckDB, Snowflake, and other destinations.

## Architecture

dlt operates as a lightweight library that can be embedded in any Python application. It does not replace existing data platforms, deployments, or security models. The typical usage pattern is:

1. Define a data source (API, filesystem, database)
2. Configure a pipeline with a destination
3. Run the pipeline to extract and load data

## Example

```python
import dlt
from dlt.sources.filesystem import filesystem

resource = filesystem(
    bucket_url="s3://example-bucket",
    file_glob="*.csv"
)

pipeline = dlt.pipeline(
    pipeline_name="filesystem_example",
    destination="duckdb",
    dataset_name="filesystem_data",
)

pipeline.run(resource)
```

## Relationship to dltHub

dlt is the open-source core of the [[dlthub-platform]] vision. While dlt handles extraction and loading (EL), dltHub will extend into ELT, storage, and runtime as a SaaS platform.

## Connections

- Complements [[elt-pattern]] with a Python-native implementation
- Contrasts with YAML-heavy tools like [[dbt-cloud]] and DAG-based tools like [[kestra]]
- Relevant to [[python-native-elt]] as the primary example