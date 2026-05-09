---
type: concept
title: Pure Task
created: 2026-04-29
updated: 2026-04-29
tags: [data-engineering, functional-programming, idempotence, determinism]
related: [functional-data-engineering, table-partitions-as-immutable-objects, apache-airflow]
sources: ["Functional Data Engineering — a modern paradigm for batch data processing.md"]
---
# Pure Task

A pure task is a deterministic, idempotent data processing unit that produces the same output given the same input, with no side effects. It is the core operational unit of [[functional-data-engineering]].

## Characteristics

- **Deterministic**: Given the same input parameters, the task always produces the same output.
- **Idempotent**: Re-running the task produces the same result as the first run. This makes re-execution safe and prevents double-counting or bad state.
- **Single output**: A pure task targets a single output (typically a table partition), analogous to a pure function returning a single object.
- **No side effects**: The task does not mutate any state outside its defined output scope.
- **Insulated transitional states**: Any temporary tables or dataframes used within the task are scoped so that multiple instances cannot interfere with one another.

## Implementation

In a SQL ELT context, a pure task typically overwrites a portion of a table (a partition). The output is akin to the immutable object that a pure function would return. The task should always fully overwrite its target partition.

## Benefits

- **Operability**: Failed tasks can be safely re-run without needing full context of previous executions.
- **Reproducibility**: The warehouse state can be recomputed from scratch.
- **Parallelization**: Independent task instances can run concurrently without interference.
- **Clarity**: Each task instance maps directly to a specific partition, making lineage and debugging straightforward.

## Relationship to Orchestration

[[Apache Airflow]] was designed with pure tasks in mind. In Airflow, each task corresponds to a table, and each task instance corresponds to a partition. This mapping makes it easy to track lineage and re-run specific partitions.