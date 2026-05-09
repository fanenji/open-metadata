---
type: entity
title: bus_VALORI_PREP
created: 2026-02-13
updated: 2026-02-13
tags: [dbt, model, environmental-monitoring, prepared-data]
related: [bus-media-giornaliera, media-gg-macro, environmental-data-quality-hierarchy]
sources: ["dbt YAML schema for daily media calculations.md"]
---
# bus_VALORI_PREP

A dbt model that provides prepared hourly values for environmental monitoring calculations. It is the upstream dependency of `bus_MEDIA_GIORNALIERA` and belongs to the Business schema layer (`bus_` prefix).

## Role

The model serves as the input source for daily average computations. It contains hourly measurement data with validation codes that enable the multi-tier quality filtering used by downstream models.

## Key Columns (inferred)

- `DATA_DA` — start date/time of the measurement period
- `VAL` — raw measured value
- `VAL_COR` — corrected value
- `CERT` — certified value
- `COD_VALID` — validity code
- `COD_VALIDAZ` — validation code
- `COD_VALIDAZ_REG` — regional validation code
- `COD_UBIC` — station/measurement location code
- `COD_CONF` — instrument configuration code
- `SIGLA_PARAM` — environmental parameter code

## Connections

- Provides input data to [[bus-media-giornaliera]] for daily average computation.
- Used by the [[media-gg-macro]] for filtering and aggregation.
- Supports the [[environmental-data-quality-hierarchy]] by providing validation codes.