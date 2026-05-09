---
type: concept
title: Reactive Notebook
created: 2026-05-06
updated: 2026-05-06
tags: [notebook, reactive, python, execution-model]
related: [marimo, git-friendly-reproducible-python]
sources: ["Marimo - next-generation Python notebook.md"]
---
# Reactive Notebook

A reactive notebook is a computational notebook where cells automatically re-execute when their dependent values or code change. This is in contrast to traditional notebooks (e.g., Jupyter) where cells must be manually re-run in order, leading to potential inconsistencies between displayed outputs and actual state.

## Key Characteristics

- **Automatic Re-execution:** Changing a variable or cell triggers re-execution of all downstream cells that depend on it.
- **Consistency Guarantee:** Outputs always reflect the current state of the code and data.
- **No Manual Ordering:** Users do not need to manage cell execution order; the system handles dependency tracking.

## Relevance to Data Platform

Reactive notebooks like [[marimo]] can improve data exploration and prototyping workflows by eliminating stale outputs and reducing manual re-runs. This is particularly valuable in ad-hoc analysis, data quality checks, and interactive documentation.

## Related Concepts

- [[git-friendly-reproducible-python]] — Marimo's approach to storing notebooks as plain Python files for version control.