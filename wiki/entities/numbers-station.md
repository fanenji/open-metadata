---
type: entity
title: Numbers Station
created: 2026-04-29
updated: 2026-04-29
tags: [organization, text2sql, ai, synthetic-data]
related: [duckdb-nsql-7b, synthetic-sql-training-data, text2sql-patterns]
sources: ["Introducing DuckDB-NSQL-7B, A LLM for DuckDB SQL.md"]
---
# Numbers Station

Numbers Station is an organization that collaborated with [[MotherDuck]] to develop and release [[DuckDB-NSQL-7B]], a fine-tuned 7B-parameter language model for DuckDB-specific Text2SQL generation. They contributed the NSText2SQL dataset, containing over 250k general Text2SQL questions, which was used alongside 200k synthetically generated DuckDB SQL queries to train the model.

Numbers Station also published a companion blog post detailing the creation and evaluation methodology for DuckDB-NSQL-7B. Their work focuses on advancing text-to-SQL capabilities, particularly for domain-specific SQL dialects.