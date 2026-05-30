---
type: entity
title: orm-profiler
created: 2026-05-14
updated: 2026-05-14
tags: [auto-classification, ingestion-framework, processor, profiling, pii]
related: [auto-classification, auto-classification-external-workflow, pii-processor, ingestion-framework, data-profiling]
sources: ["external-auto-classification-workflow---openmetada-20260514.md"]
---
# orm-profiler

The `orm-profiler` is a processor type within the OpenMetadata ingestion framework used by the Auto Classification workflow to profile data and detect sensitive columns. It is specified in the workflow YAML configuration under `processor.type`.

## Role in Auto Classification

When the Auto Classification workflow executes, it uses the `orm-profiler` processor to:
1. Sample data from configured tables.
2. Apply pattern recognition and predefined criteria to identify columns potentially containing sensitive information (PII).
3. Assign classification tags based on the configured `confidence` threshold.

The processor is not specific to classification — it is the same profiling engine used for general [[data-profiling]] tasks, repurposed here for automated sensitive data detection.

## Configuration

In the workflow YAML, the processor is configured as:

```yaml
processor:
  type: "orm-profiler"
  config:
    tableConfig:
      - fullyQualifiedName: <fqn>
        profileSample: 85
        partitionConfig:
          partitionQueryDuration: 180
        columnConfig:
          excludeColumns:
            - column_a
            - column_b
```

Key parameters:
- **profileSample**: Number of rows to sample for profiling.
- **partitionConfig**: Partitioning settings for large tables.
- **columnConfig.excludeColumns**: Columns to skip during profiling.