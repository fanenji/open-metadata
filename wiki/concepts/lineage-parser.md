---
type: concept
title: Lineage Parser
created: 2026-05-14
updated: 2026-05-14
tags: [lineage, parser, sql, dbt]
related: [dbt-lineage-ingestion, dbt-artifacts, data-lineage]
sources: ["ingest-lineage-from-dbt-official-documentation---o-20260514.md"]
---

# Lineage Parser

The Lineage Parser is an internal OpenMetadata component that parses SQL queries from the `compiled_code` or `compiled_sql` field in the dbt `manifest.json` artifact. It extracts source and target tables to create lineage edges.

## Behavior

- The parser reads the compiled SQL query for each dbt model node.
- It identifies referenced tables (sources) and the model's output table (target).
- Lineage is created based on this analysis.

## Limitations

- The parser may fail on complex or unsupported SQL syntax.
- If parsing fails, lineage is not created for that node.
- The documentation advises checking OpenMetadata logs for errors when lineage is missing.

## Relationship to `depends_on`

The Lineage Parser is a secondary mechanism. The primary, more reliable mechanism is the `depends_on` key, which provides direct node dependencies without SQL parsing. The parser is used when additional lineage detail beyond direct dependencies is needed.
