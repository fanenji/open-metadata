---
type: source
title: "dbt YAML schema for daily media calculations"
created: 2026-02-13
updated: 2026-02-13
tags: [dbt, yaml, schema, environmental-monitoring]
related: [bus-media-giornaliera, media-gg-macro, bus-valori-prep, environmental-data-quality-hierarchy, dbt-data-contract-implementation, dbt-testing-patterns]
sources: ["dbt YAML schema for daily media calculations.md"]
---
# dbt YAML schema for daily media calculations

A conversation output showing a dbt YAML schema file for the `bus_MEDIA_GIORNALIERA` model, which computes daily averages (media giornaliera) from environmental monitoring data. The model uses a reusable macro (`media_gg`) to compute three distinct daily averages with different validation criteria: raw values (VAL), corrected values (VAL_COR), and certified values (CERT).

## Key Content

- **Model**: `bus_MEDIA_GIORNALIERA` — a view materialization that computes daily averages from prepared data.
- **Upstream model**: `bus_VALORI_PREP` — provides prepared hourly values.
- **Macro**: `media_gg` — reusable macro for computing daily averages with configurable column and filter conditions.
- **Data source**: `progetto_pilota_aria` (object storage), database `space_progetto_pilota_aria`.

## Multi-Tier Validation

The model demonstrates a three-level data quality hierarchy:
1. **VAL** — raw valid values (`COD_VALID = '0'`)
2. **VAL_COR** — corrected valid values (`COD_VALID = '0' AND COD_VALIDAZ = 'V'`)
3. **CERT** — certified values (`COD_VALIDAZ_REG = 'V'`)

## YAML Schema

The YAML schema documents 10 columns with Italian descriptions and `not_null` tests on the four key grouping columns (DATA, COD_UBIC, COD_CONF, SIGLA_PARAM).

## Connections

- Related to [[dbt-data-contract-implementation]] — the YAML schema pattern aligns with dbt contract syntax.
- Related to [[YAML-data-contract-format]] — the YAML structure follows standard dbt schema conventions.
- Related to [[dbt-testing-patterns]] — the `not_null` tests are basic singular tests.