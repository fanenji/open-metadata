---
type: entity
title: bus_MEDIA_GIORNALIERA
created: 2026-02-13
updated: 2026-02-13
tags: [dbt, model, environmental-monitoring, daily-average]
related: [media-gg-macro, bus-valori-prep, environmental-data-quality-hierarchy, dbt-data-contract-implementation]
sources: ["dbt YAML schema for daily media calculations.md"]
---
# bus_MEDIA_GIORNALIERA

A dbt model that computes daily averages (media giornaliera) from environmental monitoring data. It is materialized as a view and belongs to the Business schema layer (`bus_` prefix), consistent with data mesh domain organization.

## SQL Logic

The model:
1. Reads prepared hourly values from `bus_VALORI_PREP`, filtering out the first year of data (needed for 8-hour moving average calculations).
2. Uses the `media_gg` macro three times to compute daily averages with different validation criteria.
3. Joins the three result sets on the four key grouping columns: DATA, COD_UBIC, COD_CONF, SIGLA_PARAM.

## Multi-Tier Validation

The model produces three sets of daily averages:
- **VAL** — raw valid values (`COD_VALID = '0'`)
- **VAL_COR** — corrected valid values (`COD_VALID = '0' AND COD_VALIDAZ = 'V'`)
- **CERT** — certified values (`COD_VALIDAZ_REG = 'V'`)

## Columns

| Column | Description |
|--------|-------------|
| DATA | Reference date for the daily average |
| COD_UBIC | Station/measurement location code |
| COD_CONF | Instrument configuration code |
| SIGLA_PARAM | Environmental parameter code (e.g., PM10, NO2, O3) |
| MEDIA_GIORNALIERA_VAL | Daily average of raw valid values |
| VALORI_VALIDI_GG_VAL | Count of valid values used for VAL average |
| MEDIA_GIORNALIERA_VAL_COR | Daily average of corrected valid values |
| VALORI_VALIDI_GG_VAL_COR | Count of valid values used for VAL_COR average |
| MEDIA_GIORNALIERA_CERT | Daily average of certified values |
| VALORI_VALIDI_GG_CERT | Count of valid values used for CERT average |

## YAML Schema

The model's YAML schema documents all columns with Italian descriptions and applies `not_null` tests on the four key grouping columns.

## Connections

- Uses the [[media-gg-macro]] for daily average computation.
- Depends on [[bus-valori-prep]] for prepared hourly values.
- Implements the [[environmental-data-quality-hierarchy]] pattern.
- Follows [[dbt-data-contract-implementation]] practices for YAML schema documentation.