---
type: concept
title: Kestra Ion Format
created: 2026-04-29
updated: 2026-04-29
tags: [kestra, serialization, ion, format]
related: [kestra, kestra-api-to-parquet-pattern, elt-pattern]
sources: ["Kestra API to S3 Parquet.txt"]
---
# Kestra Ion Format

Kestra's internal serialization format used as an intermediate representation between tasks in a workflow. Ion is a type-rich, self-describing data format developed by Amazon that preserves type information (integers, strings, timestamps, etc.) during serialization, enabling safe conversion between different data formats like JSON and Parquet.

## Role in Kestra Workflows

In the [[kestra-api-to-parquet-pattern]], the Ion format serves as the bridge between JSON (from the HTTP API) and Parquet (for S3 storage). The workflow converts JSON to Ion, then Ion to Parquet. This two-step conversion is necessary because:

- **JSON** is text-based and lacks native type information (all numbers are floats, no date types).
- **Ion** preserves type information from the JSON parsing step.
- **Parquet** requires explicit schema and type information for columnar storage.

## Usage

- `io.kestra.plugin.serdes.json.JsonToIon` — Converts JSON to Ion.
- `io.kestra.plugin.serdes.parquet.IonToParquet` — Converts Ion to Parquet, requiring an explicit Avro schema.

## Limitations

- The Ion format is internal to Kestra and not intended for direct consumption by external systems.
- The conversion step adds processing overhead.
- Schema must be declared explicitly for the Ion-to-Parquet conversion, creating a maintenance burden if the source schema changes.