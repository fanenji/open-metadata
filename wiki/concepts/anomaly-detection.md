---
type: concept
title: Anomaly Detection
created: 2026-04-04
updated: 2026-04-04
tags: [statistics, observability, monitoring]
related: [metadata-mart, elementary, data-observability]
sources: ["Are You Using Elementary for DBT?.md"]
---
# Anomaly Detection

**Anomaly Detection** in data engineering refers to the use of statistical methods to identify significant deviations in pipeline metrics, such as model execution duration, row counts, or schema changes.

## Implementation via Metadata

When implemented using a **Metadata Mart** (as seen in [[elementary]]), anomaly detection can be achieved through standard SQL. A common approach involves calculating the standard deviation from the mean for a specific metric:

$$Z = \frac{x - \mu}{\sigma}$$

Where:
- $x$ is the current metric value.
- $\mu$ is the historical mean.
- $\sigma$ is the standard deviation.

A high Z-score indicates a potential anomaly that may require investigation by the data engineering team.