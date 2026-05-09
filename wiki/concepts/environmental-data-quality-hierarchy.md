---
type: concept
title: Environmental Data Quality Hierarchy
created: 2026-02-13
updated: 2026-02-13
tags: [data-quality, environmental-monitoring, validation, hierarchy]
related: [bus-media-giornaliera, media-gg-macro, bus-valori-prep, dbt-testing-patterns]
sources: ["dbt YAML schema for daily media calculations.md"]
---
# Environmental Data Quality Hierarchy

A three-tier data quality validation pattern for environmental monitoring data, where measurements are classified into progressively stricter validation levels. This pattern enables tracking data quality through progressive validation stages.

## The Three Tiers

### 1. VAL — Raw Valid Values
- **Filter**: `COD_VALID = '0'`
- **Meaning**: Basic validity check — the measurement instrument reported a value within expected operational parameters.
- **Use case**: Preliminary analysis, operational monitoring.

### 2. VAL_COR — Corrected Valid Values
- **Filter**: `COD_VALID = '0' AND COD_VALIDAZ = 'V'`
- **Meaning**: The value has passed both basic validity and a secondary validation process (e.g., automated correction algorithms).
- **Use case**: Standard reporting, trend analysis.

### 3. CERT — Certified Values
- **Filter**: `COD_VALIDAZ_REG = 'V'`
- **Meaning**: The value has received regional certification, the highest level of quality assurance.
- **Use case**: Regulatory reporting, official statistics, legal compliance.

## Implementation

In the [[bus-media-giornaliera]] model, the [[media-gg-macro]] is called three times with different filter conditions to compute daily averages for each tier. The results are joined on the four key grouping columns (DATA, COD_UBIC, COD_CONF, SIGLA_PARAM) to produce a single output row per day per station/parameter combination.

## Benefits

- **Progressive quality tracking**: Data consumers can see how quality improves through validation stages.
- **Auditability**: Each tier preserves the original data while adding validation context.
- **Flexibility**: Different use cases can consume different quality tiers.
- **Transparency**: The filter criteria are explicit and documented in the model logic.

## Connections

- Implemented in [[bus-media-giornaliera]] using the [[media-gg-macro]].
- Depends on [[bus-valori-prep]] for the validation codes.
- Related to [[dbt-testing-patterns]] as a domain-specific data quality pattern.