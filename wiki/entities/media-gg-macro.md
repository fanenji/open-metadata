---
type: entity
title: media_gg macro
created: 2026-02-13
updated: 2026-02-13
tags: [dbt, macro, daily-average, reusable-pattern]
related: [bus-media-giornaliera, bus-valori-prep, environmental-data-quality-hierarchy]
sources: ["dbt YAML schema for daily media calculations.md"]
---
# media_gg macro

A reusable dbt macro for computing daily averages (media giornaliera) from prepared hourly data. The macro accepts a column name and a filter condition, enabling flexible computation of daily averages with different validation criteria.

## Usage

The macro is called with two parameters:
1. **Column name** — the value column to average (e.g., `VAL`, `VAL_COR`, `CERT`)
2. **Filter condition** — a SQL WHERE clause for data validation (e.g., `"COD_VALID = '0'"`)

## Example Calls

```sql
{{ media_gg ('VAL', "COD_VALID = '0'") }}
{{ media_gg ('VAL_COR', "COD_VALID = '0' AND COD_VALIDAZ = 'V'") }}
{{ media_gg ('CERT', "COD_VALIDAZ_REG = 'V'") }}
```

## Output

The macro produces a result set with:
- Grouping columns: DATA, COD_UBIC, COD_CONF, SIGLA_PARAM
- `MEDIA_GIORNALIERA_{column}` — the daily average
- `VALORI_VALIDI_GG_{column}` — count of valid values used

## Connections

- Used by [[bus-media-giornaliera]] to compute three tiers of daily averages.
- Implements the core computation logic for the [[environmental-data-quality-hierarchy]].
- Depends on [[bus-valori-prep]] for input data.