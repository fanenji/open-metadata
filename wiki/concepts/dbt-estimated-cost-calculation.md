---
type: concept
title: dbt Estimated Cost Calculation
created: 2026-04-29
updated: 2026-04-29
tags: [dbt, cost, snowflake, observability]
related: [dbt-observability-implementation, dbt-query-comment-pattern]
sources: ["How to add observability to your dbt deployment - Show and Tell.md"]
---
# dbt Estimated Cost Calculation

A method for estimating the Snowflake cost of each dbt model run by mapping warehouse size to credits per hour, multiplying by elapsed time, and applying the contract rate.

## Formula

1. Map warehouse size to credits/hour (XSMALL=1, SMALL=2, MEDIUM=4, LARGE=8, XLARGE=16, XXLARGE=32, XXXLARGE=64, XXXXLARGE=128)
2. Calculate estimated credits used: `total_elapsed_time_mins * warehouse_credits_hourly / 60`
3. Calculate estimated cost: `snowflake_contract_rate * est_credits_used`

## Context

This calculation was part of the [[dbt-observability-implementation]] at Snapcommerce, enabled by joining dbt artifacts to Snowflake query history via the [[dbt-query-comment-pattern]]. It provides cost visibility at the model and pipeline level.